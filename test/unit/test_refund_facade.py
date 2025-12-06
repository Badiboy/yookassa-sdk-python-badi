# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch

from yookassa import Configuration
from yookassa.domain.models import Currency
from yookassa.domain.models.amount import Amount
from yookassa.domain.request.refund_request import RefundRequest
from yookassa.domain.response.refund_response import RefundResponse
from yookassa.refund import Refund


class TestRefundFacade(unittest.TestCase):

    def setUp(self):
        Configuration.configure(account_id='test_account_id', secret_key='test_secret_key')

    def test_create_payment_with_dict(self):
        self.maxDiff = None
        refund_facade = Refund()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "id": "216749f7-0016-50be-b000-078d43a63ae4",
                "status": "succeeded",
                "amount": {
                    "value": "1",
                    "currency": "RUB"
                },
                "created_at": "2017-10-04T19:27:51.407Z",
                "payment_id": "216749da-000f-50be-b000-096747fad91e"
            }
            refund = refund_facade.create({
                "payment_id": "21b36369-000f-500b-9000-070b97dced26",
                "amount": {
                    "value": 1000.01,
                    "currency": "RUB"
                },
                "comment": "Comment here",
                "receipt": {
                    "items": [
                        {
                            "description": "string",
                            "quantity": 1,
                            "amount": {
                                "value": "10.00",
                                "currency": "RUB"
                            },
                            "vat_code": 1
                        }
                    ],
                    "tax_system_code": 1,
                    "phone": "79000000000",
                    "email": "johndoe@yoomoney.ru"
                }
            })

        self.assertIsInstance(refund, RefundResponse)
        self.assertIsInstance(refund.amount, Amount)

    def test_create_payment_with_object(self):

        self.maxDiff = None
        refund_facade = Refund()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "id": "216749f7-0016-50be-b000-078d43a63ae4",
                "status": "succeeded",
                "amount": {
                    "value": "1",
                    "currency": "RUB"
                },
                "created_at": "2017-10-04T19:27:51.407Z",
                "payment_id": "216749da-000f-50be-b000-096747fad91e"
            }
            refund = refund_facade.create(RefundRequest({
                "payment_id": "21b36369-000f-500b-9000-070b97dced26",
                "amount": {
                    "value": 1000.01,
                    "currency": "RUB"
                },
                "comment": "Comment here",
                "receipt": {
                    "items": [
                        {
                            "description": "string",
                            "quantity": 1,
                            "amount": {
                                "value": "10.00",
                                "currency": "RUB"
                            },
                            "vat_code": 1
                        }
                    ],
                    "tax_system_code": 1,
                    "phone": "79000000000",
                    "email": "johndoe@yoomoney.ru"
                }
            }))

        self.assertIsInstance(refund, RefundResponse)
        self.assertIsInstance(refund.amount, Amount)

    def test_refund_info(self):
        self.maxDiff = None
        refund_facade = Refund()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "id": "216749f7-0016-50be-b000-078d43a63ae4",
                "status": "succeeded",
                "amount": {
                    "value": "1",
                    "currency": "RUB"
                },
                "created_at": "2017-10-04T19:27:51.407Z",
                "payment_id": "216749da-000f-50be-b000-096747fad91e"
            }

            refund = refund_facade.find_one("216749f7-0016-50be-b000-078d43a63ae4")

        self.assertIsInstance(refund, RefundResponse)
        self.assertIsInstance(refund.amount, Amount)

    def test_refund_list(self):
        self.maxDiff = None
        refund_facade = Refund()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "type": "list",
                "items": [
                    {
                        "id": "21b23b5b-000f-5061-a000-0674e49a8c10",
                        "payment_id": "21b23365-000f-500b-9000-070fa3554403",
                        "created_at": "2017-11-30T15:11:33+00:00",
                        "amount": {
                            "value": 250.0,
                            "currency": Currency.RUB
                        },
                        "receipt_registration": "pending",
                        "comment": "test comment",
                        "status": "pending"
                    }
                ],
                "next_cursor": "fda5c87d-5984-50e8-a7f3-1de646dd9ec9"
            }

            params = {"payment_id": "21b23365-000f-500b-9000-070fa3554403"}
            refund_list = refund_facade.list(params)

        self.assertEqual(refund_list.type, 'list')
        self.assertIsInstance(refund_list.items[0], RefundResponse)

        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "type": "list",
                "items": None
            }

            params = {"payment_id": "21b23365-000f-500b-9000-070fa3554403"}
            refund_list = refund_facade.list(params)

        self.assertEqual(refund_list.type, 'list')
        self.assertIsNone(refund_list.items)

    def test_invalid_data(self):
        with self.assertRaises(TypeError):
            Refund().create('')

        with self.assertRaises(ValueError):
            Refund().find_one('')

