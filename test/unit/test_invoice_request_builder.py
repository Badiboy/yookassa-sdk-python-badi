# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models.invoice_data.request.delivery_method_self import DeliveryMethodSelf
from yookassa.domain.request.invoice_request_builder import InvoiceRequestBuilder


class TestInvoiceRequestBuilder(unittest.TestCase):

    def test_build_object(self):
        self.maxDiff = None
        request = None
        builder = InvoiceRequestBuilder()
        builder.set_payment_data({
            "amount": {
                "value": "10.00",
                "currency": "RUB"
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
            },
            "capture": True,
            "description": "Заказ №137",
            "metadata": {
                "order_id": "137"
            }
        }) \
            .set_cart([
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
        ]) \
            .set_delivery_method_data(DeliveryMethodSelf()) \
            .set_locale("ru_RU") \
            .set_expires_at("2024-11-18T10:51:18.139Z") \
            .set_description("Счет на оплату заказа номер 137") \
            .set_metadata({"order_id": "137"})

        request = builder.build()

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
