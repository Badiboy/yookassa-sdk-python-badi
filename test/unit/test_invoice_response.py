# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models import CancellationDetails
from yookassa.domain.models.invoice_data.response.delivery_method_self import DeliveryMethodSelf
from yookassa.domain.models.invoice_data.response.delivery_method_unknown import DeliveryMethodUnknown
from yookassa.domain.response import InvoiceResponse


class TestInvoiceResponse(unittest.TestCase):

    def test_response_cast(self):
        self.maxDiff = None
        response = InvoiceResponse({
            "id": "in-e44e8088-bd73-43b1-959a-954f3a7d0c54",
            "status": "cancel",
            "cart": [
                {
                    "description": "Товар арт. 12345",
                    "price": {
                        "value": "10.00",
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
            "delivery_method": {
                "type": "self",
                "url": "https://yookassa.ru/my/i/Zqncq0lhxSqo/l"
            },
            "created_at": "2024-10-01T11:37:15.137Z",
            "expires_at": "2024-10-18T10:51:18.139Z",
            "description": "Счет на оплату заказа номер 37",
            "metadata": {
                "order_id": "37"
            },
            "cancellation_details": {
                "party": "merchant",
                "reason": "invoice_canceled"
            }
        })

        self.assertIsInstance(response.cart, list)
        self.assertIsInstance(response.delivery_method, DeliveryMethodSelf)
        self.assertIsInstance(response.metadata, dict)
        self.assertIsInstance(response.cancellation_details, CancellationDetails)
        self.assertEqual(response.created_at, "2024-10-01T11:37:15.137Z")
        self.assertEqual(response.expires_at, "2024-10-18T10:51:18.139Z")
        self.assertEqual(response.description, "Счет на оплату заказа номер 37")
        self.assertEqual(response.metadata, {
            "order_id": "37"
        })
        self.assertEqual(response.id, "in-e44e8088-bd73-43b1-959a-954f3a7d0c54")
        self.assertEqual(response.status, "cancel")
        self.assertEqual(response.cancellation_details.reason, "invoice_canceled")

    def test_response_unknown(self):
        self.maxDiff = None
        response = InvoiceResponse({
            "id": "in-e44e8088-bd73-43b1-959a-954f3a7d0c54",
            "status": "pending",
            "cart": [
                {
                    "description": "Товар арт. 12345",
                    "price": {
                        "value": "10.00",
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
            "delivery_method": {
                "type": "new_method",
                "url": "https://yookassa.ru/my/i/Zqncq0lhxSqo/l"
            },
            "created_at": "2024-10-01T11:37:15.137Z",
            "expires_at": "2024-10-18T10:51:18.139Z",
            "description": "Счет на оплату заказа номер 37",
            "metadata": {
                "order_id": "37"
            }
        })

        self.assertIsInstance(response.cart, list)
        self.assertIsInstance(response.delivery_method, DeliveryMethodUnknown)
        self.assertIsInstance(response.metadata, dict)
        self.assertEqual(response.created_at, "2024-10-01T11:37:15.137Z")
        self.assertEqual(response.expires_at, "2024-10-18T10:51:18.139Z")
        self.assertEqual(response.description, "Счет на оплату заказа номер 37")

        self.assertEqual(response.metadata, {
            "order_id": "37"
        })
        self.assertEqual(response.id, "in-e44e8088-bd73-43b1-959a-954f3a7d0c54")
        self.assertEqual(response.status, "pending")
