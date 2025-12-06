# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch

from yookassa import Invoice
from yookassa.domain.models.invoice_data.response.delivery_method_self import DeliveryMethodSelf
from yookassa.domain.response import InvoiceResponse
from yookassa.configuration import Configuration


class TestInvoice(unittest.TestCase):

    def setUp(self):
        Configuration.configure(account_id='test_account_id', secret_key='test_secret_key')

    def test_create(self):
        self.maxDiff = None
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "id" : "in-2eac7581-0000-0050-25bc-a4f9b1e406ce",
                "status": "pending",
                "cart": [{
                    "description": "Товар арт. 12345",
                    "price": {
                        "value": "9.00",
                        "currency": "RUB"
                    },
                    "discount_price": {
                        "value": "7.00",
                        "currency": "RUB"
                    },
                    "quantity": 1.000
                }, {
                    "description": "Товар арт. 67890",
                    "price": {
                        "value": "1.00",
                        "currency": "RUB"
                    },
                    "discount_price": {
                        "value": "1.00",
                        "currency": "RUB"
                    },
                    "quantity": 3.000
                }],
                "delivery_method": {
                    "type": "self",
                    "url": "https://front-main.cmssdk2.cloud.yookassa.ru/my/i/ZxphwoIIWw59/a"
                },
                "created_at": "2024-10-24T15:03:30.183Z",
                "expires_at": "2024-11-18T10:51:18.139Z",
                "description": "Счет на оплату заказа номер 137",
                "metadata": {
                    "order_id": "137"
                }
            }

            params = {
                "payment_data": {
                    "amount": {
                        "value": "10.00",
                        "currency": "RUB"
                    },
                    "capture": True,
                    "description": "Заказ №137",
                    "metadata": {
                        "order_id": "137"
                    },
                    "receipt": {
                        "customer": {
                            "email": "example@email.com"
                        },
                        "items": [
                            {
                                "description": "Товар арт. 12345",
                                "amount": {
                                    "value": "7.00",
                                    "currency": "RUB"
                                },
                                "quantity": 1.000,
                                "vat_code": 1,
                                "payment_mode": "full_payment",
                                "payment_subject": "commodity"
                            },
                            {
                                "description": "Товар арт. 67890",
                                "amount": {
                                    "value": "1.00",
                                    "currency": "RUB"
                                },
                                "quantity": 3.000,
                                "vat_code": 1,
                                "payment_mode": "full_payment",
                                "payment_subject": "commodity"
                            }
                        ],
                        "tax_system_code": 1
                    }
                },
                "cart": [
                    {
                        "description": "Товар арт. 12345",
                        "price": {
                            "value": "9.00",
                            "currency": "RUB"
                        },
                        "discount_price": {
                            "value": "7.00",
                            "currency": "RUB"
                        },
                        "quantity": 1.000
                    },
                    {
                        "description": "Товар арт. 67890",
                        "price": {
                            "value": "1.00",
                            "currency": "RUB"
                        },
                        "quantity": 3.000
                    }
                ],
                "delivery_method_data": {
                    "type": "self"
                },
                "locale": "ru_RU",
                "expires_at": "2024-11-18T10:51:18.139Z",
                "description": "Счет на оплату заказа номер 137",
                "metadata": {
                    "order_id": "137"
                }
            }
            rec = Invoice.create(params)

            self.assertIsInstance(rec, InvoiceResponse)
            self.assertEqual(rec.status, "pending")
            self.assertIsInstance(rec.delivery_method, DeliveryMethodSelf)


        with self.assertRaises(TypeError):
            Invoice.create('invalid data')

    def test_invoice_info(self):
        receipt_facade = Invoice()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "id" : "in-2eac7581-0000-0050-25bc-a4f9b1e406ce",
                "status": "pending",
                "cart": [{
                    "description": "Товар арт. 12345",
                    "price": {
                        "value": "9.00",
                        "currency": "RUB"
                    },
                    "discount_price": {
                        "value": "7.00",
                        "currency": "RUB"
                    },
                    "quantity": 1.000
                }, {
                    "description": "Товар арт. 67890",
                    "price": {
                        "value": "1.00",
                        "currency": "RUB"
                    },
                    "discount_price": {
                        "value": "1.00",
                        "currency": "RUB"
                    },
                    "quantity": 3.000
                }],
                "delivery_method": {
                    "type": "self",
                    "url": "https://front-main.cmssdk2.cloud.yookassa.ru/my/i/ZxphwoIIWw59/a"
                },
                "created_at": "2024-10-24T15:03:30.183Z",
                "expires_at": "2024-11-18T10:51:18.139Z",
                "description": "Счет на оплату заказа номер 137",
                "metadata": {
                    "order_id": "137"
                }
            }
            rec = receipt_facade.find_one('in-2eac7581-0000-0050-25bc-a4f9b1e406ce')

        self.assertIsInstance(rec, InvoiceResponse)
        self.assertEqual(rec.id, "in-2eac7581-0000-0050-25bc-a4f9b1e406ce")
        self.assertEqual(rec.status, "pending")
        self.assertIsInstance(rec.delivery_method, DeliveryMethodSelf)

    def test_invalid_data(self):
        with self.assertRaises(ValueError):
            Invoice().find_one('')

        with self.assertRaises(TypeError):
            Invoice().create('invalid params')
