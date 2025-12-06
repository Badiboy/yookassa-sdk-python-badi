# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models.confirmation.request.confirmation_redirect import ConfirmationRedirect
from yookassa.domain.models.self_employed_data.confirmation import SelfEmployedConfirmation
from yookassa.domain.models.self_employed_data.request.confirmation_redirect import SelfEmployedConfirmationRedirect
from yookassa.domain.request import SelfEmployedRequest


class TestSelfEmployedRequest(unittest.TestCase):

    def test_request_cast(self):
        self.maxDiff = None
        request = SelfEmployedRequest()
        request.itn = "123456789012"
        request.description = "Test"
        request.metadata = {"cms_name": "Django"}
        request.confirmation = SelfEmployedConfirmation({
          "type": "redirect"
        })

        self.assertEqual({
            "itn": "123456789012",
            "description": "Test",
            "metadata": {
                "cms_name": "Django"
            },
            "confirmation": {
                "type": "redirect"
            }
          }, dict(request))

    def test_request_setters(self):
        request = SelfEmployedRequest({
            "itn": "123456789012",
            "phone": "79998887766",
            "description": "Test",
            "confirmation": {
                "type": "redirect"
            }
        })

        self.assertIsInstance(request.confirmation, SelfEmployedConfirmationRedirect)
        self.assertEqual('123456789012', request.itn)
        self.assertEqual('79998887766', request.phone)
        self.assertEqual('Test', request.description)

        with self.assertRaises(ValueError):
            request.description = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                                  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

        with self.assertRaises(TypeError):
            request.confirmation = ConfirmationRedirect({
                "type": "redirect"
            })

    def test_request_validate(self):
        request = SelfEmployedRequest()

        with self.assertRaises(ValueError):
            request.validate()

        request.confirmation = SelfEmployedConfirmationRedirect()

        with self.assertRaises(ValueError):
            request.validate()
