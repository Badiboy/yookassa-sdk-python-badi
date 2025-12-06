# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models import Currency
from yookassa.domain.models.receipt_data.receipt_item import PaymentMode, PaymentSubject
from yookassa.domain.models.sbp_participant_bank import SbpParticipantBank
from yookassa.domain.response import PaymentListResponse, PaymentResponse, \
    ReceiptListResponse, ReceiptResponse, \
    RefundListResponse, RefundResponse, DealListResponse, DealResponse
from yookassa.domain.response.sbp_bank_list_response import SbpBankListResponse


class TestAnyListResponse(unittest.TestCase):

    def test_response_cast_receipt(self):
        response = ReceiptListResponse({
            "type": "list",
            "items": [
                {
                    "id": "rt_1da5c87d-0984-50e8-a7f3-8de646dd9ec9",
                    "type": "payment",
                    "payment_id": "215d8da0-000f-50be-b000-0003308c89be",
                    "status": "succeeded",
                    "fiscal_document_number": "3986",
                    "fiscal_storage_number": "9288000100115785",
                    "fiscal_attribute": "2617603921",
                    "registered_at": "2019-05-13T17:56:00.000+03:00",
                    "fiscal_provider_id": "fd9e9404-eaca-4000-8ec9-dc228ead2345",
                    "tax_system_code": 1,
                    "items": [{
                        "description": "Capybara",
                        "quantity": 5,
                        "amount": {
                            "value": "2500.50",
                            "currency": "RUB"
                        },
                        "vat_code": 2,
                        "payment_mode": PaymentMode.FULL_PAYMENT,
                        "payment_subject": PaymentSubject.COMMODITY
                    }],
                    "settlements": None
                }
            ],
            "next_cursor": "fda5c87d-5984-50e8-a7f3-1de646dd9ec9"
        })

        self.assertIsInstance(response.items, list)
        self.assertIsInstance(response.items[0], ReceiptResponse)

        self.assertEqual(response.type, 'list')
        self.assertEqual(response.next_cursor, 'fda5c87d-5984-50e8-a7f3-1de646dd9ec9')

    def test_response_cast_refund(self):
        response = RefundListResponse({
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
        })

        self.assertIsInstance(response.items, list)
        self.assertIsInstance(response.items[0], RefundResponse)

        self.assertEqual(response.type, 'list')
        self.assertEqual(response.next_cursor, 'fda5c87d-5984-50e8-a7f3-1de646dd9ec9')

    def test_response_cast_deal(self):
        response = DealListResponse({
            "items": [
                {
                    "type": "safe_deal",
                    "fee_moment": "deal_closed",
                    "id": "dl-285e5ee7-0022-5000-8000-01516a44b147",
                    "balance": {
                        "value": -45,
                        "currency": "RUB"
                    },
                    "payout_balance": {
                        "value": 0,
                        "currency": "RUB"
                    },
                    "status": "closed",
                    "created_at": "2021-06-18T07:28:39.390Z",
                    "expires_at": "2021-09-16T07:28:39.390Z",
                    "metadata": {
                        "order_id": 37
                    },
                    "description": "SAFE_DEAL 123554642-2432FF344R",
                    "test": False
                }
            ],
            "type": "list",
            "next_cursor": "37a5c87d-3984-51e8-a7f3-8de646d39ec15"
        })

        self.assertIsInstance(response.items, list)
        self.assertIsInstance(response.items[0], DealResponse)

        self.assertEqual(response.type, 'list')
        self.assertEqual(response.next_cursor, '37a5c87d-3984-51e8-a7f3-8de646d39ec15')

    def test_response_cast_payment(self):
        response = PaymentListResponse({
            "type": "list",
            "items": [
                {
                    "id": "21b23365-000f-500b-9000-070fa3554403",
                    "amount": {
                        "value": "1000.00",
                        "currency": "RUB"
                    },
                    "description": "Заказ №72",
                    "confirmation": {
                        "type": "redirect",
                        "return_url": "https://test.test/test",
                        "confirmation_url": "https://url",
                        "enforce": False
                    },
                    "payment_method": {
                        "type": "bank_card",
                        "id": "21b23365-000f-500b-9000-070fa3554403",
                        "saved": False
                    },
                    "status": "pending",
                    "recipient": {
                        "account_id": "67192",
                        "gateway_id": "352780"
                    },
                    "refunded_amount": {
                        "value": "1000.00",
                        "currency": "RUB"
                    },
                    "receipt_registration": "pending",
                    "created_at": "2017-11-30T15:11:33+00:00",
                    "expires_at": "2017-11-30T15:11:33+00:00",
                    "captured_at": "2017-11-30T15:11:33+00:00",
                    "paid": False,
                    "refundable": False,
                    "test": False,
                    "metadata": {
                        "float_value": "123.32",
                        "key": "data"
                    },
                    "cancellation_details": {
                        "party": "yoo_kassa",
                        "reason": "fraud_suspected"
                    },
                    "authorization_details": {
                        "rrn": "rrn",
                        "auth_code": "auth_code",
                        "three_d_secure": {
                            "applied": True
                        }
                    },
                    "transfers": [
                        {
                            "account_id": "79990000000",
                            "amount": {
                                "value": 100.01,
                                "currency": "RUB"
                            },
                            "status": "succeeded",
                            "description": "Test description",
                            "metadata": {
                                "meta1": 'metatest 1',
                                "meta2": 'metatest 2'
                            }
                        }
                    ],
                    "income_amount": {
                        "value": "990.00",
                        "currency": "RUB"
                    }
                }
            ],
            "next_cursor": "fda5c87d-5984-50e8-a7f3-1de646dd9ec9"
        })

        self.assertIsInstance(response.items, list)
        self.assertIsInstance(response.items[0], PaymentResponse)

        self.assertEqual(response.type, 'list')
        self.assertEqual(response.next_cursor, 'fda5c87d-5984-50e8-a7f3-1de646dd9ec9')

    def test_response_cast_sbp_banks(self):
        response = SbpBankListResponse({
            "type": "list",
            "items": [
                {
                    "bank_id": "100000000111",
                    "name": "Сбербанк",
                    "bic": "044525225"
                },
                {
                    "bank_id": "100000000004",
                    "name": "T-Pay",
                    "bic": "04452500"
                },
                {
                    "bank_id": "100000000005",
                    "name": "ВТБ",
                    "bic": "0445251"
                },
                {
                    "bank_id": "100000000008",
                    "name": "Альфа Банк",
                    "bic": "044525593"
                },
                {
                    "bank_id": "000000000001",
                    "name": "Куар Банк",
                    "bic": "044525500"
                },
                {
                    "bank_id": "100000000022",
                    "name": "ЮМани",
                    "bic": "044525444"
                }
            ]
        })

        self.assertIsInstance(response.items, list)
        self.assertIsInstance(response.items[0], SbpParticipantBank)

        self.assertEqual(response.type, 'list')
