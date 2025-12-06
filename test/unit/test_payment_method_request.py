# -*- coding: utf-8 -*-
import unittest
from yookassa.domain.common.payment_method_type import PaymentMethodType
from yookassa.domain.models.payment_data.request.credit_card import CreditCard
from yookassa.domain.models.payment_method.request.payment_method_holder import PaymentMethodHolder
from yookassa.domain.models.payment_method.payment_method_confirmation import PaymentMethodConfirmation
from yookassa.domain.request import PaymentMethodRequest


class TestPaymentMethodRequest(unittest.TestCase):

    def test_type_property(self):
        request = PaymentMethodRequest()
        request.type = PaymentMethodType.BANK_CARD
        self.assertEqual(request.type, PaymentMethodType.BANK_CARD)
        with self.assertRaises(ValueError):
            request.type = None

    def test_card_property(self):
        request = PaymentMethodRequest()
        card_data = {'number': '4444444444444444', 'expiry_year': '2025', 'expiry_month': '12'}
        request.card = card_data
        self.assertIsInstance(request.card, CreditCard)
        self.assertEqual(request.card.number, '4444444444444444')
        with self.assertRaises(TypeError):
            request.card = 'invalid'

    def test_holder_property(self):
        request = PaymentMethodRequest()
        holder_data = {'gateway_id': 'test_gateway'}
        request.holder = holder_data
        self.assertIsInstance(request.holder, PaymentMethodHolder)
        self.assertEqual(request.holder.gateway_id, 'test_gateway')
        with self.assertRaises(TypeError):
            request.holder = 'invalid'

    def test_client_ip_property(self):
        request = PaymentMethodRequest()

        self.assertIsNone(request.client_ip)

        request.client_ip = '192.168.0.1'
        self.assertEqual(request.client_ip, '192.168.0.1')

        request.client_ip = ''
        self.assertEqual(request.client_ip, '192.168.0.1')

        request.client_ip = '10.0.0.1'
        self.assertEqual(request.client_ip, '10.0.0.1')

        request.client_ip = 12345
        self.assertEqual(request.client_ip, '12345')

    def test_confirmation_property(self):
        request = PaymentMethodRequest()
        confirmation_data = {'type': 'redirect', 'return_url': 'https://example.com'}
        request.confirmation = confirmation_data
        self.assertIsInstance(request.confirmation, PaymentMethodConfirmation)
        with self.assertRaises(TypeError):
            request.confirmation = 'invalid'

    def test_request_validation(self):
        request = PaymentMethodRequest()
        with self.assertRaises(ValueError):
            request.validate()

        request.type = PaymentMethodType.BANK_CARD
        try:
            request.validate()
        except ValueError as e:
            self.fail(f"Validation failed unexpectedly: {e}")

    def test_request_to_dict(self):
        request = PaymentMethodRequest()
        request.type = PaymentMethodType.BANK_CARD
        request.card = {'number': '4444444444444444', 'expiry_year': '2025', 'expiry_month': '12'}
        request.holder = {'gateway_id': 'test_gateway'}
        request.client_ip = '192.168.0.1'

        result = dict(request)
        self.assertEqual(result['type'], PaymentMethodType.BANK_CARD)
        self.assertEqual(result['card']['number'], '4444444444444444')
        self.assertEqual(result['holder']['gateway_id'], 'test_gateway')
        self.assertEqual(result['client_ip'], '192.168.0.1')
