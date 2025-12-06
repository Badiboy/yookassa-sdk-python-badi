# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch

from yookassa import Receipt
from yookassa.domain.common import ReceiptType
from yookassa.domain.models import Amount, Currency, ReceiptCustomer, ReceiptItemSupplier
from yookassa.domain.models.settlement import SettlementType, Settlement
from yookassa.domain.request import ReceiptItemRequest, ReceiptRequest
from yookassa.domain.response import ReceiptListResponse, ReceiptResponse
from yookassa.configuration import Configuration


class TestReceipt(unittest.TestCase):

    def setUp(self):
        Configuration.configure(account_id='test_account_id', secret_key='test_secret_key')

    def test_list(self):
        self.maxDiff = None
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "type": "list",
                "items": [
                    {
                        "id": "rt_1da5c87d-0984-50e8-a7f3-8de646dd9ec9",
                        "type": "refund",
                        "refund_id": "215d8da0-000f-50be-b000-0003308c89be",
                        "fiscal_document_number": "3986",
                        "fiscal_storage_number": "9288000100115785",
                        "fiscal_attribute": "2617603921",
                        "registered_at": "2019-05-13T17:56:00.000+03:00",
                        "fiscal_provider_id": "fd9e9404-eaca-4000-8ec9-dc228ead2345",
                        "tax_system_code": 1,
                        "internet": True,
                        "timezone": 11,
                        "receipt_registration": 'succeeded',
                        "items": None,
                        "settlements": [
                            {
                                "type": "cashless",
                                "amount": {
                                    "value": "45.67",
                                    "currency": "RUB"
                                }
                            }
                        ],
                        "on_behalf_of": "string"
                    }
                ]
            }

            params = {"refund_id": "24be8857-000f-5000-a000-1833ed1577f3"}
            rec_list = Receipt.list(params)

            self.assertIsInstance(rec_list, ReceiptListResponse)
            self.assertEqual(rec_list.type, "list")
            self.assertIsInstance(rec_list.items[0], ReceiptResponse)

        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "type": "list",
                "items": None
            }

            params = {"refund_id": "24be8857-000f-5000-a000-1833ed1577f3"}
            rec_list = Receipt.list(params)

            self.assertIsInstance(rec_list, ReceiptListResponse)
            self.assertEqual(rec_list.type, "list")
            self.assertIsNone(rec_list.items)

    def test_create(self):
        self.maxDiff = None
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "id": "rt_1da5c87d-0984-50e8-a7f3-8de646dd9ec9",
                "type": "payment",
                "refund_id": "215d8da0-000f-50be-b000-0003308c89be",
                "fiscal_document_number": "3986",
                "fiscal_storage_number": "9288000100115785",
                "fiscal_attribute": "2617603921",
                "registered_at": "2019-05-13T17:56:00.000+03:00",
                "fiscal_provider_id": "fd9e9404-eaca-4000-8ec9-dc228ead2345",
                "tax_system_code": 1,
                "internet": False,
                "timezone": 1,
                "receipt_registration": 'succeeded',
                "items": None,
                "settlements": [
                    {
                        "type": "cashless",
                        "amount": {
                            "value": "45.67",
                            "currency": "RUB"
                        }
                    }
                ],
                "on_behalf_of": "string"
            }

            params = {
                'type': ReceiptType.PAYMENT,
                'send': True,
                'email': 'test@email.com',
                'phone': '79990000000',
                'items': [
                    {
                        'description': 'Product 1',
                        'quantity': 2.0,
                        'amount': Amount({
                            'value': 250.0,
                            'currency': Currency.RUB
                        }),
                        'vat_code': 2,
                        "planned_status": 1,
                        'payment_mode': 'full_payment',
                        'payment_subject': 'commodity',
                        'country_of_origin_code': 'CN',
                        'product_code': '00 00 00 01 00 21 FA 41 00 23 05 41 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 12 00 AB 00',
                        'customs_declaration_number': '10714040/140917/0090376',
                        'excise': '20.00',
                        'supplier': {
                            'name': 'string',
                            'phone': 'string',
                            'inn': 'string'
                        }
                    },
                    {
                        'description': 'Product 2',
                        'quantity': 1.0,
                        'amount': {
                            'value': 100.0,
                            'currency': Currency.RUB
                        },
                        'vat_code': 2,
                        "planned_status": 2,
                        'supplier': ReceiptItemSupplier({
                            'name': 'string',
                            'phone': 'string',
                            'inn': 'string'
                        })
                    }
                ],
                'settlements': [
                    {
                        'type': SettlementType.CASHLESS,
                        'amount': {
                            'value': 250.0,
                            'currency': Currency.RUB
                        }
                    }
                ],
                'tax_system_code': 1,
                "internet": False,
                "timezone": 1,
                'payment_id': '215d8da0-000f-50be-b000-0003308c89be',
                'on_behalf_of': 'string'
            }
            rec = Receipt.create(params)

            self.assertIsInstance(rec, ReceiptResponse)
            self.assertEqual(rec.type, ReceiptType.PAYMENT)
            self.assertEqual(rec.internet, False)
            self.assertEqual(rec.timezone, 1)

            request_mock.return_value = {
                "id": "rt_2da5c87d-0984-50e8-a7f3-8de646dd9ec9",
                "type": "payment",
                "refund_id": "215d8da0-000f-50be-b000-0003308c89be",
                "fiscal_document_number": "3987",
                "fiscal_storage_number": "9288000100115785",
                "fiscal_attribute": "2617603921",
                "registered_at": "2019-05-13T17:56:00.000+03:00",
                "fiscal_provider_id": "fd9e9404-eaca-4000-8ec9-dc228ead2345",
                "tax_system_code": 1,
                "internet": True,
                "timezone": 10,
                "receipt_registration": 'succeeded',
                "items": None,
                "settlements": [
                    {
                        "type": "cashless",
                        "amount": {
                            "value": "45.67",
                            "currency": "RUB"
                        }
                    }
                ],
                "on_behalf_of": "string"
            }

            request = ReceiptRequest()
            request.type = ReceiptType.PAYMENT
            request.send = True
            request.customer = ReceiptCustomer({'phone': '79990000000', 'email': 'test@email.com'})
            request.items.append(
                ReceiptItemRequest({
                    "description": "Product 1",
                    "quantity": 2.0,
                    "amount": Amount({'value': 250.0, 'currency': Currency.RUB}),
                    "vat_code": 2,
                    "planned_status": 1,
                }))
            request.items.append(
                ReceiptItemRequest({
                    "description": "Product 2",
                    "quantity": 1.0,
                    "amount": Amount({'value': 100.0, 'currency': Currency.RUB}),
                    "vat_code": 2,
                    "planned_status": 2,
                }))
            request.settlements.append(
                Settlement({
                    'type': SettlementType.CASHLESS,
                    'amount': Amount({'value': 250.0, 'currency': Currency.RUB})
                }))
            request.tax_system_code = 1
            request.internet = True
            request.timezone = 10
            request.payment_id = '215d8da0-000f-50be-b000-0003308c89be'
            rec = Receipt.create(request)

            self.assertIsInstance(rec, ReceiptResponse)
            self.assertEqual(rec.type, "payment")
            self.assertEqual(rec.internet, True)
            self.assertEqual(rec.timezone, 10)

        with self.assertRaises(TypeError):
            Receipt.create('invalid data')

    def test_receipt_info(self):
        receipt_facade = Receipt()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "id": "rt_1da5c87d-0984-50e8-a7f3-8de646dd9ec9",
                "type": "payment",
                "refund_id": "215d8da0-000f-50be-b000-0003308c89be",
                "fiscal_document_number": "3986",
                "fiscal_storage_number": "9288000100115785",
                "fiscal_attribute": "2617603921",
                "registered_at": "2019-05-13T17:56:00.000+03:00",
                "fiscal_provider_id": "fd9e9404-eaca-4000-8ec9-dc228ead2345",
                "tax_system_code": 1,
                "internet": True,
                "timezone": 5,
                "receipt_registration": 'succeeded',
                "items": None,
                "settlements": [
                    {
                        "type": "cashless",
                        "amount": {
                            "value": "45.67",
                            "currency": "RUB"
                        }
                    }
                ],
                "on_behalf_of": "string"
            }

            receipt_id = 'po-2855a19a-0003-5000-a000-0efa9e7f4264'
            rec = receipt_facade.find_one(receipt_id)

            request_mock.assert_called_once()

        self.assertIsInstance(rec, ReceiptResponse)
        self.assertEqual(rec.type, "payment")
        self.assertEqual(rec.id, "rt_1da5c87d-0984-50e8-a7f3-8de646dd9ec9")
        self.assertEqual(rec.internet, True)
        self.assertEqual(rec.timezone, 5)
        self.assertEqual(rec.receipt_registration, 'succeeded')

    def test_invalid_data(self):
        with self.assertRaises(ValueError):
            Receipt().find_one('')

        with self.assertRaises(TypeError):
            Receipt().create('invalid params')
