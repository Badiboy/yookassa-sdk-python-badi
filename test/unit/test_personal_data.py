# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch

from yookassa import PersonalData
from yookassa.configuration import Configuration
from yookassa.domain.request import SbpPayoutRecipientPersonalDataRequest
from yookassa.domain.response import PersonalDataResponse


class TestPersonalDataFacade(unittest.TestCase):
    def setUp(self):
        Configuration.configure(account_id='test_account_id', secret_key='test_secret_key')

    def test_create_personal_data_with_dict(self):
        self.maxDiff = None
        personal_data_facade = PersonalData()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "id": "pd-22e12f66-000f-5000-8000-18db351245c7",
                "status": "waiting_for_operation",
                "created_at": "2022-09-15T07:28:39.390513Z",
                "metadata": {
                    "recipient_id": "37"
                },
                "type": "sbp_payout_recipient"
            }
            personal_data1 = personal_data_facade.create({
                "type": "sbp_payout_recipient",
                "last_name": "Иванов",
                "first_name": "Иван",
                "middle_name": "Иванович",
                "metadata": {
                    "recipient_id": "37"
                }
            }, 'asd213')

        self.assertIsInstance(personal_data1, PersonalDataResponse)

        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "id": "pd-22e12f66-000f-5000-8000-18db351245c7",
                "status": "waiting_for_operation",
                "created_at": "2022-09-15T07:28:39.390513Z",
                "metadata": {
                    "recipient_id": "37"
                },
                "type": "payout_statement_recipient"
            }
            personal_data2 = personal_data_facade.create({
                "type": "payout_statement_recipient",
                "last_name": "Иванов",
                "first_name": "Иван",
                "middle_name": "Иванович",
                "birthdate": "2000-01-02",
                "metadata": {
                    "recipient_id": "37"
                }
            }, 'asd213')

        self.assertIsInstance(personal_data2, PersonalDataResponse)

    def test_create_personal_data_with_object(self):
        self.maxDiff = None
        personal_data_facade = PersonalData()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "id": "pd-22e12f66-000f-5000-8000-18db351245c7",
                "status": "waiting_for_operation",
                "created_at": "2022-09-15T07:28:39.390513Z",
                "metadata": {
                    "recipient_id": "37"
                },
                "type": "sbp_payout_recipient"
            }
            personal_data = personal_data_facade.create(SbpPayoutRecipientPersonalDataRequest({
                "type": "sbp_payout_recipient",
                "last_name": "Иванов",
                "first_name": "Иван",
                "middle_name": "Иванович",
                "metadata": {
                    "recipient_id": "37"
                }
            }))

        self.assertIsInstance(personal_data, PersonalDataResponse)

    def test_personal_data_info(self):
        personal_data_facade = PersonalData()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "id": "pd-22e12f66-000f-5000-8000-18db351245c7",
                "status": "active",
                "created_at": "2022-09-15T07:28:39.390513Z",
                "expires_at": "2022-09-16T07:28:39.390513Z",
                "metadata": {
                    "recipient_id": "37"
                },
                "type": "sbp_payout_recipient"
            }
            personal_data = personal_data_facade.find_one('pd-22e12f66-000f-5000-8000-18db351245c7')

        self.assertIsInstance(personal_data, PersonalDataResponse)

    def test_invalid_data(self):
        with self.assertRaises(ValueError):
            PersonalData().find_one('')

        with self.assertRaises(TypeError):
            PersonalData().create('invalid params')
