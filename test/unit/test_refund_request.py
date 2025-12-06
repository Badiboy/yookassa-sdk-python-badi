# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch

from datetime import datetime, timezone, timedelta
from yookassa.domain.models.payment_data.request.payment_data_bank_card import PaymentDataBankCard
from yookassa.domain.models.amount import Amount
from yookassa.domain.models.currency import Currency
from yookassa.domain.models.receipt import Receipt
from yookassa.domain.models import RefundSource, RefundDealData, Settlement
from yookassa.domain.request.payment_request import PaymentRequest
from yookassa.domain.request.refund_request import RefundRequest


class TestRefundRequest(unittest.TestCase):

    def test_refund_cast(self):
        self.maxDiff = None
        request = RefundRequest()
        request.payment_id = '21a632d2-000f-5061-a000-01e90bc2de12'
        request.description = 'test comment'
        request.receipt = Receipt({
            'phone': '79990000000',
            'email': 'test@email.com',
            'tax_system_code': 1,
            'items': [
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
            ]})

        request.amount = Amount({'value': 0.1, 'currency': Currency.RUB})
        request.sources.append(RefundSource({
            'account_id': '79990000000',
            "amount": {
                "value": 100.01,
                "currency": Currency.RUB
            },
            "platform_fee_amount": {
                "value": 10.01,
                "currency": Currency.RUB
            }
        }))
        request.deal = RefundDealData({
            'refund_settlements': [{
                'type': 'payout',
                'amount': {
                    'value': 80.0,
                    'currency': 'RUB'
                }
            }]
        })

        self.assertEqual({
            'payment_id': '21a632d2-000f-5061-a000-01e90bc2de12',
            'description': 'test comment',
            'receipt': {
                'customer': {'email': 'test@email.com', 'phone': '79990000000'},
                'tax_system_code': 1,
                'items': [
                    {
                        "description": "Product 1",
                        "quantity": "2.0",
                        "amount": {
                            "value": "250.00",
                            "currency": Currency.RUB
                        },
                        "vat_code": 2
                    },
                    {
                        "description": "Product 2",
                        "quantity": "1.0",
                        "amount": {
                            "value": "100.00",
                            "currency": Currency.RUB
                        },
                        "vat_code": 2
                    }
                ]},
            'amount': {'value': '0.10', 'currency': Currency.RUB},
            'sources': [
                {
                    'account_id': '79990000000',
                    "amount": {
                        "value": "100.01",
                        "currency": Currency.RUB
                    },
                    "platform_fee_amount": {
                        "value": "10.01",
                        "currency": Currency.RUB
                    }
                }
            ],
            'deal': {
                'refund_settlements': [{
                    'type': 'payout',
                    'amount': {
                        'value': "80.00",
                        'currency': 'RUB'
                    }
                }]
            }
        }, dict(request))

        request = RefundRequest()
        request.payment_id = '21a632d2-000f-5061-a000-01e90bc2de12'
        request.description = 'test comment'
        request.sources = None

        self.assertIsInstance(request.sources, list)

    def test_request_setters(self):
        request = RefundRequest({
            'payment_id': '21a632d2-000f-5061-a000-01e90bc2de12',
            'description': 'test comment',
            'receipt': {
                'phone': '79990000000',
                'email': 'test@email.com',
                'tax_system_code': 1,
                'items': [
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
                ]},
            'amount': {'value': 0.1, 'currency': Currency.RUB},
            'sources': [
                {
                    'account_id': '79990000000',
                    "amount": {
                        "value": 100.01,
                        "currency": Currency.RUB
                    },
                    "platform_fee_amount": {
                        "value": 10.01,
                        "currency": Currency.RUB
                    }
                }
            ],
            'deal': {
                'refund_settlements': [
                    Settlement({
                        'type': 'payout',
                        'amount': {
                            'value': 80.0,
                            'currency': 'RUB'
                        }
                    })
                ]
            }
        })

        self.assertIsInstance(request.receipt, Receipt)
        self.assertIsInstance(request.amount, Amount)

    def test_invalid_values(self):
        request = RefundRequest()
        with self.assertRaises(TypeError):
            request.receipt = 'invalid receipt'

        with self.assertRaises(TypeError):
            request.amount = 'invalid amount'

        with self.assertRaises(ValueError):
            request.payment_id = 'invalid payment_id'

        with self.assertRaises(ValueError):
            request.description = ''

        with self.assertRaises(TypeError):
            request.sources = 'invalid sources'

        with self.assertRaises(TypeError):
            request.deal = 'invalid deal'

    def test_request_validate(self):
        request = RefundRequest()
        with self.assertRaises(ValueError):
            request.validate()

        request.payment_id = '21a632d2-000f-5061-a000-01e90bc2de12'
        with self.assertRaises(ValueError):
            request.validate()

        request.amount = Amount({'value': 0.0, 'currency': Currency.RUB})
        with self.assertRaises(ValueError):
            request.validate()

        request.amount.value = 0.1

        request.receipt = {
            'phone': '79990000000',
            'items': [
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

        request.receipt = {
            'tax_system_code': 1,
            'items': [
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

        with self.assertRaises(TypeError):
            request.deal = {
                'id': 'dl-28646d17-0022-5000-8000-01e154d1324b',
                'refund_settlements': ['invalid data']
            }

        with self.assertRaises(TypeError):
            request.deal = {
                'id': 'dl-28646d17-0022-5000-8000-01e154d1324b',
                'refund_settlements': 'invalid data'
            }

        request.deal = {
            'id': 'dl-28646d17-0022-5000-8000-01e154d1324b',
            'refund_settlements': None
        }
        self.assertEqual(request.deal.refund_settlements, [])

    @unittest.mock.patch('yookassa.domain.request.payment_request.datetime', side_effect=datetime)
    def test_request_validate_expiry(self, modtime):
        modtime.now.return_value = datetime(year=2019, month=3, day=10)

        request = PaymentRequest()
        request.amount = Amount({'value': 0.1, 'currency': Currency.RUB})
        request.payment_method_data = PaymentDataBankCard(card={
            "number": "4111111111111111",
            "expiry_year": "2019",
            "expiry_month": "11",
            "csc": "111"
        })

        # Should pass other validations
        request.validate()

        # Obviously expired
        request.payment_method_data.card.expiry_year = '2018'
        with self.assertRaises(ValueError):
            request.validate()

        # Same month
        request.payment_method_data.card.expiry_year = '2019'
        request.payment_method_data.card.expiry_month = '03'
        request.validate()

        # Just a notch before expiration (same timezone)
        modtime.now.return_value = datetime(year=2019, month=3, day=31,
                                            hour=23, minute=59, second=59)
        request.payment_method_data.card.expiry_year = '2019'
        request.payment_method_data.card.expiry_month = '03'
        request.validate()

        # Just a notch before expiration (worst timezone case)
        client_tz = timezone(timedelta(hours=-12))
        bank_tz = timezone(timedelta(hours=+14))
        tz_offset = datetime.now(client_tz) - datetime.now(bank_tz)
        tz_offset += timedelta(hours=1)  # DST
        modtime.now.return_value += tz_offset
        request.validate()

        # Couple days after expiration
        modtime.now.return_value = datetime(year=2019, month=4, day=3)
        with self.assertRaises(ValueError):
            request.validate()
