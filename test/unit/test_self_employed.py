# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch

from yookassa import SelfEmployed
from yookassa.configuration import Configuration
from yookassa.domain.request import SelfEmployedRequest
from yookassa.domain.response import SelfEmployedResponse


class TestSelfEmployedFacade(unittest.TestCase):
    def setUp(self):
        Configuration.configure(account_id='test_account_id', secret_key='test_secret_key')

    def test_create_self_employed_with_dict(self):
        self.maxDiff = None
        self_employed_facade = SelfEmployed()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "id": "se-d6b9b3fa-0cb8-4aa8-b3c0-254bf0358d4c",
                "status": "pending",
                "confirmation": {
                    "type": "redirect",
                    "confirmation_url": "https://lknpd.nalog.ru/settings/partners/"
                },
                "created_at": "2020-02-12T11:10:41.802Z",
                "itn": "123456789012",
                "test": False
            }
            self_employed = self_employed_facade.create({
                "itn": "123456789012",
                "confirmation": {
                    "type": "redirect"
                }
            }, 'asd213')

        self.assertIsInstance(self_employed, SelfEmployedResponse)

    def test_create_self_employed_with_object(self):
        self.maxDiff = None
        self_employed_facade = SelfEmployed()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "id": "se-d6b9b3fa-0cb8-4aa8-b3c0-254bf0358d4c",
                "status": "pending",
                "confirmation": {
                    "type": "redirect",
                    "confirmation_url": "https://lknpd.nalog.ru/settings/partners/"
                },
                "created_at": "2020-02-12T11:10:41.802Z",
                "itn": "123456789012",
                "test": False
            }
            self_employed = self_employed_facade.create(SelfEmployedRequest({
                "itn": "123456789012",
                "confirmation": {
                    "type": "redirect"
                }
            }))

        self.assertIsInstance(self_employed, SelfEmployedResponse)

    def test_self_employed_info(self):
        self_employed_facade = SelfEmployed()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "id": "se-d6b9b3fa-0cb8-4aa8-b3c0-254bf0358d4c",
                "status": "pending",
                "created_at": "2019-03-12T11:10:41.802Z",
                "email": "self@employed.com",
                "itn": "123456789012",
                "phone": "79297771234",
                "confirmation": {
                    "type": "redirect",
                    "confirmation_url": "https://himself-ktr.nalog.ru/settings/partners"
                },
                "test": False
            }
            self_employed = self_employed_facade.find_one('se-d6b9b3fa-0cb8-4aa8-b3c0-254bf0358d4c')

        self.assertIsInstance(self_employed, SelfEmployedResponse)

    def test_invalid_data(self):
        with self.assertRaises(ValueError):
            SelfEmployed().find_one('')

        with self.assertRaises(TypeError):
            SelfEmployed().create('invalid params')
