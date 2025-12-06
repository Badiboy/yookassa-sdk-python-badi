# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.common.confirmation_type import ConfirmationType
from yookassa.domain.common.payment_method_type import PaymentMethodType
from yookassa.domain.request.payment_method_request_builder import PaymentMethodRequestBuilder


class TestPaymentMethodRequestBuilder(unittest.TestCase):

    def test_build_object(self):
        builder = PaymentMethodRequestBuilder()
        builder.set_type(PaymentMethodType.BANK_CARD) \
            .set_card({
            'number': '4444444444444444',
            'expiry_year': '2024',
            'expiry_month': '12',
            'csc': '123',
            'cardholder': 'John Doe'
        }) \
            .set_client_ip('192.0.0.0')

        request = builder.build()

        self.assertEqual(PaymentMethodType.BANK_CARD, request.type)
        self.assertEqual('192.0.0.0', request.client_ip)
        self.assertEqual('4444444444444444', request.card.number)
        self.assertEqual('2024', request.card.expiry_year)
        self.assertEqual('12', request.card.expiry_month)
        self.assertEqual('123', request.card.csc)
        self.assertEqual('John Doe', request.card.cardholder)

    def test_build_minimal_object(self):
        builder = PaymentMethodRequestBuilder()
        builder.set_type(PaymentMethodType.BANK_CARD) \
            .set_card({
            'expiry_year': '2024',
            'expiry_month': '12'
        })

        request = builder.build()

        self.assertEqual(PaymentMethodType.BANK_CARD, request.type)
        self.assertEqual('2024', request.card.expiry_year)
        self.assertEqual('12', request.card.expiry_month)
        self.assertIsNone(request.card.number)
        self.assertIsNone(request.card.csc)
        self.assertIsNone(request.card.cardholder)

    def test_build_with_partial_data(self):
        builder = PaymentMethodRequestBuilder()
        builder.set_type(PaymentMethodType.BANK_CARD) \
            .set_client_ip('192.0.0.0')

        request = builder.build()

        self.assertEqual(PaymentMethodType.BANK_CARD, request.type)
        self.assertEqual('192.0.0.0', request.client_ip)
        self.assertIsNone(request.card)

    def test_build_with_confirmation(self):
        builder = PaymentMethodRequestBuilder()
        builder.set_type(PaymentMethodType.BANK_CARD) \
            .set_confirmation({
            'type': ConfirmationType.REDIRECT,
            'return_url': 'https://test.test/return'
        })

        request = builder.build()

        self.assertEqual(PaymentMethodType.BANK_CARD, request.type)
        self.assertEqual(ConfirmationType.REDIRECT, request.confirmation.type)
        self.assertEqual('https://test.test/return', request.confirmation.return_url)

    def test_invalid_card_data(self):
        builder = PaymentMethodRequestBuilder()

        with self.assertRaises(ValueError):
            builder.set_card({
                'number': 'invalid',
                'expiry_year': '2024',
                'expiry_month': '12'
            })

        with self.assertRaises(ValueError):
            builder.set_card({
                'number': '4444444444444444',
                'expiry_year': '1999',  # Invalid year
                'expiry_month': '12'
            })

        with self.assertRaises(ValueError):
            builder.set_card({
                'number': '4444444444444444',
                'expiry_year': '2024',
                'expiry_month': '13'  # Invalid month
            })
