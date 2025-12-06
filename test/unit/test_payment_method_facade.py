# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch
import uuid

from yookassa.configuration import Configuration
from yookassa.domain.request.payment_method_request import PaymentMethodRequest
from yookassa.domain.response.payment_method_response import PaymentMethodResponse
from yookassa.payment_method import PaymentMethod


class TestPaymentMethodFacade(unittest.TestCase):
    def setUp(self):
        Configuration.configure(account_id='test_account_id', secret_key='test_secret_key')

        self.mock_response = {
            'id': 'pm_123456789',
            'type': 'bank_card',
            'saved': False,
            'title': 'BANK_CARD *4444',
            'card': {
                'last4': '4444',
                'expiry_year': '2025',
                'expiry_month': '12',
                'card_type': 'MasterCard'
            }
        }

    @patch('yookassa.client.ApiClient.request')
    def test_find_one_success(self, mock_request):
        mock_request.return_value = self.mock_response

        payment_method = PaymentMethod().find_one('pm_123456789')

        self.assertIsInstance(payment_method, PaymentMethodResponse)
        self.assertEqual(payment_method.id, 'pm_123456789')
        self.assertEqual(payment_method.type, 'bank_card')
        mock_request.assert_called_once()

    @patch('yookassa.client.ApiClient.request')
    def test_create_with_dict(self, mock_request):
        mock_request.return_value = self.mock_response

        payment_method = PaymentMethod().create({
            'type': 'bank_card',
            'card': {
                'number': '4444444444444444',
                'expiry_year': '2025',
                'expiry_month': '12',
                'csc': '123'
            }
        }, 'test_idempotency_key')

        self.assertIsInstance(payment_method, PaymentMethodResponse)
        self.assertEqual(payment_method.id, 'pm_123456789')
        self.assertEqual(payment_method.type, 'bank_card')
        mock_request.assert_called_once()

    @patch('yookassa.client.ApiClient.request')
    def test_create_with_object(self, mock_request):
        mock_request.return_value = self.mock_response

        payment_method = PaymentMethod().create(PaymentMethodRequest({
            'type': 'bank_card',
            'card': {
                'number': '4444444444444444',
                'expiry_year': '2025',
                'expiry_month': '12',
                'csc': '123'
            }
        }))

        self.assertIsInstance(payment_method, PaymentMethodResponse)
        self.assertEqual(payment_method.id, 'pm_123456789')
        self.assertEqual(payment_method.type, 'bank_card')
        mock_request.assert_called_once()

    @patch('yookassa.client.ApiClient.request')
    def test_create_with_idempotency_key(self, mock_request):
        mock_request.return_value = self.mock_response
        idempotency_key = str(uuid.uuid4())

        payment_method = PaymentMethod().create({
            'type': 'bank_card',
            'card': {
                'number': '4444444444444444',
                'expiry_year': '2025',
                'expiry_month': '12',
                'csc': '123'
            }
        }, idempotency_key)

        self.assertIsInstance(payment_method, PaymentMethodResponse)
        mock_request.assert_called_once()

    def test_invalid_data(self):
        with self.assertRaises(ValueError):
            PaymentMethod().find_one('')

        with self.assertRaises(TypeError):
            PaymentMethod().create('invalid params')

        with self.assertRaises(ValueError):
            PaymentMethod().find_one(None)
