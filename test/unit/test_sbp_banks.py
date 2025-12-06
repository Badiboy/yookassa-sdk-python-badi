# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch

from yookassa import SbpBanks
from yookassa.configuration import Configuration
from yookassa.domain.models import SbpParticipantBank
from yookassa.domain.response import SbpBankListResponse


class TestPersonalDataFacade(unittest.TestCase):
    def setUp(self):
        Configuration.configure(account_id='test_account_id', secret_key='test_secret_key')

    def test_list(self):
        self.maxDiff = None
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "type": "list",
                "items": [
                    {
                        "bank_id": "100000000111",
                        "name": "Сбербанк",
                        "bic": "044525225"
                    }
                ]
            }

            rec_list = SbpBanks.list()

            self.assertIsInstance(rec_list, SbpBankListResponse)
            self.assertEqual(rec_list.type, "list")
            self.assertIsInstance(rec_list.items[0], SbpParticipantBank)
            self.assertEqual(rec_list.items[0].bank_id, "100000000111")
            self.assertEqual(rec_list.items[0].name, "Сбербанк")
            self.assertEqual(rec_list.items[0].bic, "044525225")
