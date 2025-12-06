# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.common import PaymentMethodType
from yookassa.domain.models import Amount, Currency, RefundSource, Settlement
from yookassa.domain.models import RefundDealInfo
from yookassa.domain.models.refund_data.response.refund_data_sbp import RefundDataSbp
from yookassa.domain.models.refund_data.response.refund_data_unknown import RefundDataUnknown
from yookassa.domain.response import RefundResponse


class TestRefundResponse(unittest.TestCase):
    def test_response_cast(self):
        response = RefundResponse({
            'id': '21b23b5b-000f-5061-a000-0674e49a8c10',
            'payment_id': '21b23365-000f-500b-9000-070fa3554403',
            'created_at': "2017-11-30T15:11:33+00:00",
            'amount': {
                "value": 250.0,
                "currency": Currency.RUB
            },
            'receipt_registration': 'pending',
            'description': 'test comment',
            'status': 'pending',
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
                'id': 'dl-28646d17-0022-5000-8000-01e154d1324b',
                'refund_settlements': [
                    {
                        'type': 'payout',
                        'amount': {
                            'value': 40.0,
                            'currency': 'RUB'
                        }
                    },
                    Settlement({
                        'type': 'payout',
                        'amount': {
                            'value': 40.0,
                            'currency': 'RUB'
                        }
                    })
                ]
            },
            'refund_method': {
                'type': PaymentMethodType.SBP,
                'sbp_operation_id': '1027088AE4CB48CB81287833347A8777'
            },
            "cancellation_details": {
                "party": "yoo_money",
                "reason": "insufficient_funds"
            },
            "refund_authorization_details": {
                "rrn": "603668680243"
            },
        })

        self.assertEqual(response.id, '21b23b5b-000f-5061-a000-0674e49a8c10')
        self.assertEqual(response.payment_id, '21b23365-000f-500b-9000-070fa3554403')
        self.assertEqual(response.created_at, "2017-11-30T15:11:33+00:00")
        self.assertEqual(response.receipt_registration, 'pending')
        self.assertEqual(response.description, 'test comment')
        self.assertIsInstance(response.amount, Amount)
        self.assertIsInstance(response.sources[0], RefundSource)
        self.assertEqual(response.status, 'pending')
        self.assertIsInstance(response.deal, RefundDealInfo)
        self.assertEqual(response.deal.id, 'dl-28646d17-0022-5000-8000-01e154d1324b')
        self.assertIsInstance(response.deal.refund_settlements[0], Settlement)
        self.assertIsInstance(response.deal.refund_settlements[1], Settlement)
        self.assertIsInstance(response.refund_method, RefundDataSbp)
        self.assertEqual(response.refund_method.sbp_operation_id, '1027088AE4CB48CB81287833347A8777')
        self.assertEqual(response.cancellation_details.party, 'yoo_money')
        self.assertEqual(response.refund_authorization_details.rrn, '603668680243')

        with self.assertRaises(TypeError):
            response.deal.refund_settlements = 'invalid settlements'

        with self.assertRaises(TypeError):
            response.deal.refund_settlements = ['invalid settlements']

        response.deal.refund_settlements = None
        self.assertEqual(response.deal.refund_settlements, [])

    def test_response_unknown_method(self):
        response = RefundResponse({
            'id': '21b23b5b-000f-5061-a000-0674e49a8c10',
            'payment_id': '21b23365-000f-500b-9000-070fa3554403',
            'created_at': "2017-11-30T15:11:33+00:00",
            'amount': {
                "value": 250.0,
                "currency": Currency.RUB
            },
            'receipt_registration': 'pending',
            'description': 'test comment',
            'status': 'pending',
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
                'id': 'dl-28646d17-0022-5000-8000-01e154d1324b',
                'refund_settlements': [
                    {
                        'type': 'payout',
                        'amount': {
                            'value': 40.0,
                            'currency': 'RUB'
                        }
                    },
                    Settlement({
                        'type': 'payout',
                        'amount': {
                            'value': 40.0,
                            'currency': 'RUB'
                        }
                    })
                ]
            },
            'refund_method': {
                'type': 'new_method',
                'new_prop': 'value'
            },
            "cancellation_details": {
                "party": "yoo_money",
                "reason": "insufficient_funds"
            },
            "refund_authorization_details": {
                "rrn": "603668680243"
            }
        })

        self.assertIsInstance(response.refund_method, RefundDataUnknown)
