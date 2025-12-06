# -*- coding: utf-8 -*-
import unittest

from unittest.mock import patch

from yookassa import Settings, Configuration
from yookassa.domain.models import Me, Amount


class TestSettings(unittest.TestCase):

    def setUp(self):
        Configuration.configure(account_id='test_account_id', secret_key='test_secret_key')

    def test_get_account_settings(self):
        self.maxDiff = None
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "account_id": Configuration.account_id,
                "test": False,
                "fiscalization_enabled": False,
                "fiscalization": {
                    "enabled": True,
                    "provider": "atol"
                },
                "payment_methods": [
                    "yoo_money",
                    "cash",
                    "bank_card"
                ],
                "payout_methods": [
                    "yoo_money",
                    "sbp",
                    "bank_card"
                ],
                "payout_balance": {
                    "value": "100.50",
                    "currency": "RUB",
                },
                "status": "enabled",
                "itn": "123456789012",
                "name": "name",
            }
            settings = Settings.get_account_settings()

        self.assertIsInstance(settings, Me)
        self.assertIsInstance(settings['fiscalization'], dict)
        self.assertIsInstance(settings['payment_methods'], list)
        self.assertListEqual(settings['payment_methods'], ["yoo_money", "cash", "bank_card"])
        self.assertIsInstance(settings.payout_methods, list)
        self.assertListEqual(settings.payout_methods, ["yoo_money", "sbp", "bank_card"])
        self.assertIsInstance(settings.payout_balance, Amount)
        self.assertEqual(settings.account_id, Configuration.account_id)
        self.assertEqual(settings.status, "enabled")
        self.assertEqual(settings.itn, "123456789012")
        self.assertEqual(settings.name, "name")
