# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models import PersonalDataStatus, PersonalDataType
from yookassa.domain.models.cancellation_details import PersonalDataCancellationDetailsReasonCode
from yookassa.domain.response.personal_data_response import PersonalDataResponse


class TestPersonalDataResponse(unittest.TestCase):

    def test_response_cast(self):
        self.maxDiff = None
        response = PersonalDataResponse({
            "id": "pd-22e12f66-000f-5000-8000-18db351245c7",
            "status": "active",
            "cancellation_details": {
                "party": "yoo_money",
                "reason": "expired_by_timeout",
            },
            "created_at": "2022-09-15T07:28:39.390513Z",
            "expires_at": "2022-09-16T07:28:39.390513Z",
            "metadata": {
                "recipient_id": "37"
            },
            "type": "sbp_payout_recipient"
        })

        self.assertEqual(response.id, "pd-22e12f66-000f-5000-8000-18db351245c7")
        self.assertEqual(response.status, PersonalDataStatus.ACTIVE)
        self.assertEqual(response.cancellation_details.party, "yoo_money")
        self.assertEqual(response.cancellation_details.reason, PersonalDataCancellationDetailsReasonCode.EXPIRED_BY_TIMEOUT)  # noqa: E501
        self.assertEqual(response.metadata, dict({"recipient_id": "37"}))
        self.assertEqual(response.created_at, "2022-09-15T07:28:39.390513Z")
        self.assertEqual(response.expires_at, "2022-09-16T07:28:39.390513Z")
        self.assertEqual(response.type, PersonalDataType.SBP_PAYOUT_RECIPIENT)
