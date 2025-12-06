# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models import PersonalDataType
from yookassa.domain.request import SbpPayoutRecipientPersonalDataRequest, PayoutStatementRecipientPersonalDataRequest


class TestPersonalDataRequest(unittest.TestCase):

    def test_request_cast1(self):
        self.maxDiff = None
        request = SbpPayoutRecipientPersonalDataRequest()
        request.type = PersonalDataType.SBP_PAYOUT_RECIPIENT
        request.last_name = "Иванов"
        request.first_name = "Иван"
        request.middle_name = "Иванович"
        request.metadata = {"cms_name": "Django"}

        self.assertEqual({
            "type": "sbp_payout_recipient",
            "last_name": "Иванов",
            "first_name": "Иван",
            "middle_name": "Иванович",
            "metadata": {
                "cms_name": "Django"
            }
          }, dict(request))

        request = SbpPayoutRecipientPersonalDataRequest()

        with self.assertRaises(ValueError):
            request.type = None

        with self.assertRaises(ValueError):
            request.last_name = None

        with self.assertRaises(ValueError):
            request.last_name = ''

        with self.assertRaises(ValueError):
            request.last_name = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                                'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                                'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

        with self.assertRaises(ValueError):
            request.last_name = '%'

        with self.assertRaises(ValueError):
            request.first_name = None

        with self.assertRaises(ValueError):
            request.first_name = ''

        with self.assertRaises(ValueError):
            request.first_name = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                                 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

        with self.assertRaises(ValueError):
            request.first_name = '%'

        with self.assertRaises(ValueError):
            request.middle_name = ''

        with self.assertRaises(ValueError):
            request.middle_name = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                                  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                                  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

        with self.assertRaises(ValueError):
            request.middle_name = '%'
    def test_request_cast2(self):
        self.maxDiff = None
        request = PayoutStatementRecipientPersonalDataRequest()
        request.type = PersonalDataType.SBP_PAYOUT_RECIPIENT
        request.last_name = "Иванов"
        request.first_name = "Иван"
        request.middle_name = "Иванович"
        request.birthdate = "2000-01-02"
        request.metadata = {"cms_name": "Django"}

        self.assertEqual({
            "type": "sbp_payout_recipient",
            "last_name": "Иванов",
            "first_name": "Иван",
            "middle_name": "Иванович",
            "birthdate": "2000-01-02",
            "metadata": {
                "cms_name": "Django"
            }
          }, dict(request))

        request = PayoutStatementRecipientPersonalDataRequest()

        with self.assertRaises(ValueError):
            request.type = None

        with self.assertRaises(ValueError):
            request.last_name = None

        with self.assertRaises(ValueError):
            request.last_name = ''

        with self.assertRaises(ValueError):
            request.last_name = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                                'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                                'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

        with self.assertRaises(ValueError):
            request.last_name = '%'

        with self.assertRaises(ValueError):
            request.first_name = None

        with self.assertRaises(ValueError):
            request.first_name = ''

        with self.assertRaises(ValueError):
            request.first_name = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                                 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

        with self.assertRaises(ValueError):
            request.first_name = '%'

        with self.assertRaises(ValueError):
            request.middle_name = ''

        with self.assertRaises(ValueError):
            request.middle_name = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                                  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                                  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

        with self.assertRaises(ValueError):
            request.middle_name = '%'

        with self.assertRaises(ValueError):
            request.birthdate = '%'

    def test_request_setters(self):
        request = SbpPayoutRecipientPersonalDataRequest({
            "type": "sbp_payout_recipient",
            "last_name": "Иванов",
            "first_name": "Иван",
            "middle_name": "Иванович",
            "metadata": {
                "cms_name": "Django"
            }
        })

        self.assertEqual(PersonalDataType.SBP_PAYOUT_RECIPIENT, request.type)
        self.assertEqual('Иванов', request.last_name)
        self.assertEqual('Иван', request.first_name)
        self.assertEqual('Иванович', request.middle_name)
        self.assertIsInstance(request.metadata, dict)

        request = PayoutStatementRecipientPersonalDataRequest({
            "type": "payout_statement_recipient",
            "last_name": "Иванов",
            "first_name": "Иван",
            "middle_name": "Иванович",
            "birthdate": "2000-01-02",
            "metadata": {
                "cms_name": "Django"
            }
        })

        self.assertEqual(PersonalDataType.PAYOUT_STATEMENT_RECIPIENT, request.type)
        self.assertEqual('Иванов', request.last_name)
        self.assertEqual('Иван', request.first_name)
        self.assertEqual('Иванович', request.middle_name)
        self.assertEqual('2000-01-02', request.birthdate)
        self.assertIsInstance(request.metadata, dict)

    def test_request_validate(self):
        request1 = SbpPayoutRecipientPersonalDataRequest()

        with self.assertRaises(ValueError):
            request1.validate()

        request1.type = PersonalDataType.SBP_PAYOUT_RECIPIENT
        with self.assertRaises(ValueError):
            request1.validate()

        request1.last_name = "Иванов"
        with self.assertRaises(ValueError):
            request1.validate()

        request2 = PayoutStatementRecipientPersonalDataRequest()

        with self.assertRaises(ValueError):
            request2.validate()

        request2.type = PersonalDataType.PAYOUT_STATEMENT_RECIPIENT
        with self.assertRaises(ValueError):
            request2.validate()

        request2.last_name = "Иванов"
        with self.assertRaises(ValueError):
            request2.validate()

        request2.birthdate = "2000-01-02"
        with self.assertRaises(ValueError):
            request2.validate()
