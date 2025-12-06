# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models import PayoutSelfEmployed
from yookassa.domain.models.amount import Amount
from yookassa.domain.models.cancellation_details import CancellationDetails
from yookassa.domain.models.currency import Currency
from yookassa.domain.models.deal import PayoutDealInfo
from yookassa.domain.models.payout import PayoutStatus
from yookassa.domain.models.payout_data.response.income_receipt import IncomeReceipt
from yookassa.domain.models.payout_data.response.payout_destination_bank_card import PayoutDestinationBankCard
from yookassa.domain.models.payout_data.response.payout_destination_sbp import PayoutDestinationSbp
from yookassa.domain.models.payout_data.response.payout_destination_unknown import PayoutDestinationUnknown
from yookassa.domain.response.payout_response import PayoutResponse


class TestPayoutResponse(unittest.TestCase):

    def test_response_cast(self):
        self.maxDiff = None
        response = PayoutResponse({
            "id": "po-2855a19a-0003-5000-a000-0efa9e7f4264",
            "amount": {
                "value": "320.00",
                "currency": Currency.RUB
            },
            "status": "succeeded",
            "payout_destination": {
                "type": "bank_card",
                "card": {
                    "first6": "220220",
                    "last4": "2537",
                    "card_type": "MIR",
                    "issuer_country": "RU",
                    "issuer_name": "Sberbank Of Russia"
                }
            },
            "cancellation_details": {
                "party": "yoo_money",
                "reason": "one_time_limit_exceeded"
            },
            "description": "Выплата по заказу №37",
            "created_at": "2021-06-21T16:22:50.512Z",
            "succeeded_at": "2021-06-21T16:22:50.512Z",
            "deal": {
                "id": "dl-285e5ee7-0022-5000-8000-01516a44b147"
            },
            "metadata": {
                "order_id": "37"
            },
            "test": False
        })

        self.assertIsInstance(response.amount, Amount)
        self.assertIsInstance(response.payout_destination, PayoutDestinationBankCard)
        self.assertIsInstance(response.cancellation_details, CancellationDetails)
        self.assertIsInstance(response.deal, PayoutDealInfo)

        self.assertEqual(response.metadata, {
            "order_id": "37"
        })
        self.assertFalse(response.test)
        self.assertEqual(response.id, "po-2855a19a-0003-5000-a000-0efa9e7f4264")
        self.assertEqual(response.status, PayoutStatus.SUCCEEDED)
        self.assertEqual(response.amount.value, 320.00)

        self.assertEqual(response.description, "Выплата по заказу №37")
        self.assertEqual(response.created_at, "2021-06-21T16:22:50.512Z")
        self.assertEqual(response.succeeded_at, "2021-06-21T16:22:50.512Z")

    def test_response_cast_sbp(self):
        self.maxDiff = None
        response = PayoutResponse({
            "id": "po-2855a19a-0003-5000-a000-0efa9e7f4264",
            "amount": {
                "value": "320.00",
                "currency": Currency.RUB
            },
            "status": "succeeded",
            "payout_destination": {
                "type": "sbp",
                "phone": "220220",
                "bank_id": "000001",
                "recipient_checked": False
            },
            "receipt": {
                "service_name": "Оказание услуг по доставке товара",
                "amount": {
                    "value": 320.0,
                    "currency": Currency.RUB
                },
                "npd_receipt_id": "208jd98zqe",
                "url": "https://www.nalog.gov.ru/api/v1/receipt/208jd98zqe/print",
            },
            "self_employed": {"id": "se-7474a846-a965-498d-bbf9-1c3c8907cbbd"},
            "description": "Выплата по заказу №37",
            "created_at": "2021-06-21T16:22:50.512Z",
            "succeeded_at": "2021-06-21T16:22:50.512Z",
            "metadata": {
                "order_id": "37"
            },
            "test": False
        })

        self.assertIsInstance(response.amount, Amount)
        self.assertIsInstance(response.payout_destination, PayoutDestinationSbp)
        self.assertIsInstance(response.receipt, IncomeReceipt)
        self.assertIsInstance(response.self_employed, PayoutSelfEmployed)

        self.assertEqual(response.metadata, {
            "order_id": "37"
        })
        self.assertFalse(response.test)
        self.assertEqual(response.id, "po-2855a19a-0003-5000-a000-0efa9e7f4264")
        self.assertEqual(response.status, PayoutStatus.SUCCEEDED)
        self.assertEqual(response.amount.value, 320.00)

        self.assertEqual(response.description, "Выплата по заказу №37")
        self.assertEqual(response.created_at, "2021-06-21T16:22:50.512Z")
        self.assertEqual(response.succeeded_at, "2021-06-21T16:22:50.512Z")

        self.assertEqual(response.payout_destination.phone, "220220")
        self.assertEqual(response.payout_destination.bank_id, "000001")
        self.assertEqual(response.payout_destination.recipient_checked, False)

        self.assertEqual(response.receipt.service_name, "Оказание услуг по доставке товара")
        self.assertEqual(response.receipt.amount.value, 320.0)
        self.assertEqual(response.receipt.npd_receipt_id, "208jd98zqe")
        self.assertEqual(response.receipt.url, "https://www.nalog.gov.ru/api/v1/receipt/208jd98zqe/print")

        self.assertEqual(response.self_employed.id, "se-7474a846-a965-498d-bbf9-1c3c8907cbbd")

    def test_response_cast_unknown(self):
        self.maxDiff = None
        response = PayoutResponse({
            "id": "po-2855a19a-0003-5000-a000-0efa9e7f4264",
            "amount": {
                "value": "320.00",
                "currency": Currency.RUB
            },
            "status": "succeeded",
            "payout_destination": {
                "type": "new_method",
            },
            "receipt": {
                "service_name": "Оказание услуг по доставке товара",
                "amount": {
                    "value": 320.0,
                    "currency": Currency.RUB
                },
                "npd_receipt_id": "208jd98zqe",
                "url": "https://www.nalog.gov.ru/api/v1/receipt/208jd98zqe/print",
            },
            "self_employed": {"id": "se-7474a846-a965-498d-bbf9-1c3c8907cbbd"},
            "description": "Выплата по заказу №37",
            "created_at": "2021-06-21T16:22:50.512Z",
            "succeeded_at": "2021-06-21T16:22:50.512Z",
            "metadata": {
                "order_id": "37"
            },
            "test": False
        })

        self.assertIsInstance(response.amount, Amount)
        self.assertIsInstance(response.payout_destination, PayoutDestinationUnknown)
        self.assertIsInstance(response.receipt, IncomeReceipt)
        self.assertIsInstance(response.self_employed, PayoutSelfEmployed)

        self.assertEqual(response.metadata, {
            "order_id": "37"
        })
        self.assertFalse(response.test)
        self.assertEqual(response.id, "po-2855a19a-0003-5000-a000-0efa9e7f4264")
        self.assertEqual(response.status, PayoutStatus.SUCCEEDED)
        self.assertEqual(response.amount.value, 320.00)

        self.assertEqual(response.description, "Выплата по заказу №37")
        self.assertEqual(response.created_at, "2021-06-21T16:22:50.512Z")
        self.assertEqual(response.succeeded_at, "2021-06-21T16:22:50.512Z")

        self.assertEqual(response.receipt.service_name, "Оказание услуг по доставке товара")
        self.assertEqual(response.receipt.amount.value, 320.0)
        self.assertEqual(response.receipt.npd_receipt_id, "208jd98zqe")
        self.assertEqual(response.receipt.url, "https://www.nalog.gov.ru/api/v1/receipt/208jd98zqe/print")

        self.assertEqual(response.self_employed.id, "se-7474a846-a965-498d-bbf9-1c3c8907cbbd")
