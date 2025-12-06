# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models.amount import Amount
from yookassa.domain.models.currency import Currency
from yookassa.domain.models.invoice import LineItem
from yookassa.domain.models.invoice_data.request.delivery_method_self import DeliveryMethodSelf
from yookassa.domain.models.invoice_data.request.payment_data import PaymentData
from yookassa.domain.models.receipt import Receipt
from yookassa.domain.request.invoice_request import InvoiceRequest


class TestInvoiceRequest(unittest.TestCase):

    def test_request_cast(self):
        self.maxDiff = None
        request = InvoiceRequest()
        request.payment_data = PaymentData({
            "amount": {
                "value": "10.00",
                "currency": "RUB"
            },
            "capture": True,
            "description": "Заказ №137",
            "metadata": {
                "order_id": "137"
            }
        })
        request.cart = [
            LineItem({
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
            }),
            LineItem({
                "description": "Товар арт. 67890",
                "price": {
                    "value": "1.00",
                    "currency": "RUB"
                },
                "quantity": 3.000
            }),
        ]
        request.payment_data.receipt = Receipt({
            'email': 'example@email.com',
            'tax_system_code': 1,
            'items': [
                {
                    "description": "Товар арт. 12345",
                    "quantity": 1.0,
                    "amount": {
                        "value": 7.00,
                        "currency": Currency.RUB
                    },
                    "vat_code": 1,
                    "payment_mode": "full_payment",
                    "payment_subject": "commodity"
                },
                {
                    "description": "Товар арт. 67890",
                    "quantity": 3.0,
                    "amount": {
                        "value": 1.00,
                        "currency": Currency.RUB
                    },
                    "vat_code": 1,
                    "payment_mode": "full_payment",
                    "payment_subject": "commodity"
                }
            ]
        })
        request.delivery_method_data = DeliveryMethodSelf()
        request.expires_at = '2024-11-18T10:51:18.139Z'
        request.locale = 'ru_RU'
        request.description = "Счет на оплату заказа номер 137"
        request.metadata = {"order_id": "137"}

        self.assertEqual({
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
                            "quantity": "1.0",
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
                            "quantity": "3.0",
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
        }, dict(request))

    def test_request_setters(self):
        request = InvoiceRequest({
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
    })

        self.assertIsInstance(request.payment_data, PaymentData)
        self.assertIsInstance(request.cart, list)
        self.assertIsInstance(request.payment_data.receipt, Receipt)
        self.assertIsInstance(request.delivery_method_data, DeliveryMethodSelf)

        with self.assertRaises(TypeError):
            request.payment_data = 'invalid receipt'

        with self.assertRaises(TypeError):
            request.cart = 'invalid amount'

        with self.assertRaises(TypeError):
            request.delivery_method_data = 'invalid recipient'

        with self.assertRaises(ValueError):
            request.expires_at = None

        with self.assertRaises(ValueError):
            request.description = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                                  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def test_request_validate(self):
        request = InvoiceRequest()

        with self.assertRaises(ValueError):
            request.validate()

        request.payment_data = {
            "capture": True,
            "description": "Заказ №137",
            "metadata": {
                "order_id": "137"
            }
        }
        with self.assertRaises(ValueError):
            request.validate()

        request.payment_data.amount = Amount({'value': 0.0, 'currency': Currency.RUB})

        with self.assertRaises(ValueError):
            request.validate()

        request.payment_data.amount = Amount({'value': 1.0, 'currency': Currency.RUB})

        request.payment_data.receipt = {'phone': '79990000000', 'items': [
            {
                "description": "Product 1",
                "quantity": 2.0,
                "amount": {
                    "value": 250.0,
                    "currency": Currency.RUB
                },
            },
            {
                "description": "Product 2",
                "quantity": 1.0,
                "amount": {
                    "value": 100.0,
                    "currency": Currency.RUB
                },
            }
        ]}
        with self.assertRaises(ValueError):
            request.validate()

        request.receipt = {'tax_system_code': 1, 'items': [
            {
                "description": "Product 1",
                "quantity": 2.0,
                "amount": {
                    "value": 250.0,
                    "currency": Currency.RUB
                },
                "vat_code": 2
            },
            {
                "description": "Product 2",
                "quantity": 1.0,
                "amount": {
                    "value": 100.0,
                    "currency": Currency.RUB
                },
                "vat_code": 2
            }
        ]}
        with self.assertRaises(ValueError):
            request.validate()
