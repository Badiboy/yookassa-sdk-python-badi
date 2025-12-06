# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models import SelfEmployedStatus
from yookassa.domain.models.self_employed_data.response.confirmation_redirect import SelfEmployedConfirmationRedirect
from yookassa.domain.response.self_employed_response import SelfEmployedResponse


class TestSelfEmployedResponse(unittest.TestCase):

    def test_response_cast(self):
        self.maxDiff = None
        response = SelfEmployedResponse({
            "id": "se-d6b9b3fa-0cb8-4aa8-b3c0-254bf0358d4c",
            "status": "pending",
            "confirmation": {
                "type": "redirect",
                "confirmation_url": "https://lknpd.nalog.ru/settings/partners/"
            },
            "metadata": {
                "order_id": "37"
            },
            "created_at": "2020-02-12T11:10:41.802Z",
            "description": "Test",
            "itn": "123456789012",
            "phone": "79998887766",
            "test": False
        })

        self.assertIsInstance(response.confirmation, SelfEmployedConfirmationRedirect)

        self.assertEqual(response.id, "se-d6b9b3fa-0cb8-4aa8-b3c0-254bf0358d4c")
        self.assertEqual(response.status, SelfEmployedStatus.PENDING)
        self.assertEqual(response.confirmation.confirmation_url, "https://lknpd.nalog.ru/settings/partners/")
        self.assertEqual(response.metadata, dict({"order_id": "37"}))
        self.assertEqual(response.created_at, "2020-02-12T11:10:41.802Z")
        self.assertEqual(response.description, "Test")
        self.assertEqual(response.itn, "123456789012")
        self.assertEqual(response.phone, "79998887766")
        self.assertFalse(response.test)

    def test_response_confirmation(self):
        response = SelfEmployedResponse({
            "id": "se-d6b9b3fa-0cb8-4aa8-b3c0-254bf0358d4c",
            "status": "pending",
            "confirmation": {
                "type": "redirect",
                "confirmation_url": "https://lknpd.nalog.ru/settings/partners/"
            },
            "metadata": {
                "order_id": "37"
            },
            "created_at": "2020-02-12T11:10:41.802Z",
            "description": "Test",
            "itn": "123456789012",
            "phone": "79998887766",
            "test": False
        })

        confirmation = SelfEmployedConfirmationRedirect()
        confirmation.confirmation_url = "https://lknpd.nalog.ru/settings/partners/"

        self.assertIsInstance(response.confirmation, SelfEmployedConfirmationRedirect)

        self.assertEqual(response.id, "se-d6b9b3fa-0cb8-4aa8-b3c0-254bf0358d4c")
        self.assertEqual(response.status, SelfEmployedStatus.PENDING)
        self.assertEqual(dict(response.confirmation), dict(confirmation))
        self.assertEqual(response.confirmation.confirmation_url, "https://lknpd.nalog.ru/settings/partners/")
        self.assertEqual(response.metadata, dict({"order_id": "37"}))
        self.assertEqual(response.created_at, "2020-02-12T11:10:41.802Z")
        self.assertEqual(response.description, "Test")
        self.assertEqual(response.itn, "123456789012")
        self.assertEqual(response.phone, "79998887766")
        self.assertFalse(response.test)
