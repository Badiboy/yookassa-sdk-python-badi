# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.common import PaymentMethodType
from yookassa.domain.models import PayoutSelfEmployed
from yookassa.domain.models.amount import Amount
from yookassa.domain.models.currency import Currency
from yookassa.domain.models.deal import PayoutDealInfo
from yookassa.domain.models.payout_data.request.income_receipt import IncomeReceiptData
from yookassa.domain.models.payout_data.request.payout_destination_sbp import PayoutDestinationSbp

from yookassa.domain.models.payout_data.request.payout_destination_yoomoney_wallet import \
    PayoutDestinationYooMoneyWallet
from yookassa.domain.models.personal_data import PayoutPersonalData
from yookassa.domain.request import PayoutRequest


class TestPayoutRequest(unittest.TestCase):

    def test_request_cast(self):
        self.maxDiff = None
        request = PayoutRequest()
        request.amount = Amount({"value": "320.00", "currency": "RUB"})
        request.description = "Выплата по заказу №37"
        request.payout_token = "<Синоним банковской карты>"
        request.metadata = {"order_id": "37"}
        request.deal = PayoutDealInfo({'id': 'dl-285e5ee7-0022-5000-8000-01516a44b147'})
        request.self_employed = PayoutSelfEmployed({"id": "se-7474a846-a965-498d-bbf9-1c3c8907cbbd"})
        request.personal_data = [
            {'id': 'pd-11e12f66-000f-5000-8000-18db351245c7'},
            PayoutPersonalData({'id': 'pd-22e12f66-000f-5000-8000-18db351245c7'})
        ]

        self.assertEqual({
            "amount": {
                "value": "320.00",
                "currency": Currency.RUB
            },
            "payout_token": "<Синоним банковской карты>",
            "description": "Выплата по заказу №37",
            "metadata": {
               "order_id": "37"
            },
            "deal": {
              "id": "dl-285e5ee7-0022-5000-8000-01516a44b147"
            },
            "self_employed": {"id": "se-7474a846-a965-498d-bbf9-1c3c8907cbbd"},
            "personal_data": [
                {"id": "pd-11e12f66-000f-5000-8000-18db351245c7"},
                {"id": "pd-22e12f66-000f-5000-8000-18db351245c7"}
            ]
          }, dict(request))

    def test_request_cast_sbp(self):
        self.maxDiff = None
        request = PayoutRequest()
        request.amount = Amount({"value": "320.00", "currency": "RUB"})
        request.description = "Выплата по заказу №37"
        request.payout_token = "<Синоним банковской карты>"
        request.metadata = {"order_id": "37"}
        request.personal_data = [
            {'id': 'pd-11e12f66-000f-5000-8000-18db351245c7'},
            PayoutPersonalData({'id': 'pd-22e12f66-000f-5000-8000-18db351245c7'})
        ]
        request.payout_destination_data = PayoutDestinationSbp({
            "phone": "220220",
            "bank_id": "000001111111"
        })
        request.receipt_data = IncomeReceiptData({
            "service_name": "Оказание услуг по доставке товара",
            "amount": Amount({
                "value": 320.0,
                "currency": Currency.RUB
            }),
        })

        self.assertEqual({
            "amount": {
                "value": "320.00",
                "currency": Currency.RUB
            },
            "payout_token": "<Синоним банковской карты>",
            "description": "Выплата по заказу №37",
            "metadata": {
               "order_id": "37"
            },
            "payout_destination_data": {
                "type": "sbp",
                "phone": "220220",
                "bank_id": "000001111111",
            },
            "personal_data": [
                {"id": "pd-11e12f66-000f-5000-8000-18db351245c7"},
                {"id": "pd-22e12f66-000f-5000-8000-18db351245c7"}
            ],
            "receipt_data": {
                "service_name": "Оказание услуг по доставке товара",
                "amount": {
                    "value": '320.00',
                    "currency": Currency.RUB
                },
            },
          }, dict(request))

    def test_request_setters(self):
        request = PayoutRequest({
            "amount": {"value": 320.0, "currency": Currency.RUB},
            "payout_destination_data": {'type': PaymentMethodType.YOO_MONEY, 'account_number': '41001614575714'},
            "description": "Выплата по заказу №37",
            "metadata": {
               "order_id": "37"
            },
            "deal": {
              "id": "dl-285e5ee7-0022-5000-8000-01516a44b147"
            },
            "receipt_data": {
                "service_name": "Оказание услуг по доставке товара",
                "amount": {
                    "value": 320.0,
                    "currency": Currency.RUB
                },
            },
            "self_employed": {"id": "se-7474a846-a965-498d-bbf9-1c3c8907cbbd"},
            "payment_method_id": "123456789"
        })

        self.assertIsInstance(request.amount, Amount)
        self.assertIsInstance(request.payout_destination_data, PayoutDestinationYooMoneyWallet)
        self.assertIsInstance(request.deal, PayoutDealInfo)
        self.assertIsInstance(request.metadata, dict)
        self.assertIsInstance(request.receipt_data, IncomeReceiptData)
        self.assertIsInstance(request.self_employed, PayoutSelfEmployed)

        self.assertEqual(request.payment_method_id, "123456789")
        self.assertEqual(request.receipt_data.service_name, "Оказание услуг по доставке товара")
        self.assertEqual(request.receipt_data.amount.value, 320.0)

        self.assertEqual(request.self_employed.id, "se-7474a846-a965-498d-bbf9-1c3c8907cbbd")

        with self.assertRaises(TypeError):
            request.amount = 'invalid amount'

        with self.assertRaises(TypeError):
            request.payout_destination_data = 'invalid payout_destination_data'

        with self.assertRaises(TypeError):
            request.payout_token = ''

        with self.assertRaises(TypeError):
            request.deal = 'invalid deal'

        with self.assertRaises(TypeError):
            request.self_employed = 'invalid self_employed'

        with self.assertRaises(ValueError):
            request.self_employed = {'id': None}

        with self.assertRaises(ValueError):
            request.self_employed = {'id': '1234567890' * 2}

        with self.assertRaises(ValueError):
            request.self_employed = {'id': '1234567890' * 7}

        with self.assertRaises(TypeError):
            request.receipt_data = 'invalid receipt_data'

        with self.assertRaises(ValueError):
            request.receipt_data = {
                'service_name': None
            }

        with self.assertRaises(TypeError):
            request.receipt_data = {
                'amount': 'invalid receipt_data.amount'
            }

        with self.assertRaises(TypeError):
            request.personal_data = 'invalid personal_data'

        with self.assertRaises(ValueError):
            request.personal_data = []

        with self.assertRaises(TypeError):
            request.personal_data = ['invalid personal_data']

        with self.assertRaises(ValueError):
            request.personal_data = [
                {"id": "pd-11e12f66-000f-5000-8000-18db351245c7"},
                {"id": "pd-22e12f66-000f-5000-8000-18db351245c7"},
                {"id": "pd-33e12f66-000f-5000-8000-18db351245c7"}
            ]

        with self.assertRaises(ValueError):
            request.description = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                                  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

        with self.assertRaises(ValueError):
            request.receipt_data = {
                "service_name": 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ',
                "amount": None
            }

    def test_request_validate(self):
        request = PayoutRequest()

        with self.assertRaises(ValueError):
            request.validate()

        request.amount = Amount({'value': 0.0, 'currency': Currency.RUB})

        with self.assertRaises(ValueError):
            request.validate()

        request.amount = Amount({'value': 0.1, 'currency': Currency.RUB})
        request.description = "Выплата по заказу №37"
        with self.assertRaises(ValueError):
            request.validate()

        request = PayoutRequest()
        request.amount = Amount({'value': 0.1, 'currency': Currency.RUB})
        with self.assertRaises(ValueError):
            request.validate()

        request = PayoutRequest()
        request.amount = Amount({'value': 0.1, 'currency': Currency.RUB})
        request.payout_token = '123'
        request.payout_destination_data = PayoutDestinationYooMoneyWallet()
        with self.assertRaises(ValueError):
            request.validate()

        request = PayoutRequest()
        request.amount = Amount({'value': 0.1, 'currency': Currency.RUB})
        request.payment_method_id = '123'
        request.payout_destination_data = PayoutDestinationYooMoneyWallet()
        with self.assertRaises(ValueError):
            request.validate()

        request = PayoutRequest()
        request.amount = Amount({'value': 0.1, 'currency': Currency.RUB})
        request.payment_method_id = '123'
        request.payout_token = '123'
        with self.assertRaises(ValueError):
            request.validate()
