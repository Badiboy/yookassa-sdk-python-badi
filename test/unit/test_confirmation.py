# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.common.confirmation_type import ConfirmationType
from yookassa.domain.models.confirmation.request.confirmation_redirect import \
    ConfirmationRedirect as RequestConfirmationRedirect
from yookassa.domain.models.confirmation.request.confirmation_qr import \
    ConfirmationQr as RequestConfirmationQr
from yookassa.domain.models.confirmation.request.confirmation_embedded import \
    ConfirmationEmbedded as RequestConfirmationEmbedded
from yookassa.domain.models.confirmation.request.confirmation_external import \
    ConfirmationExternal as RequestConfirmationExternal
from yookassa.domain.models.confirmation.request.confirmation_mobile_application import \
    ConfirmationMobileApplication as RequestConfirmationMobileApplication
from yookassa.domain.models.confirmation.response.confirmation_redirect import \
    ConfirmationRedirect as ResponseConfirmationRedirect
from yookassa.domain.models.confirmation.response.confirmation_qr import \
    ConfirmationQr as ResponseConfirmationQr
from yookassa.domain.models.confirmation.response.confirmation_embedded import \
    ConfirmationEmbedded as ResponseConfirmationEmbedded
from yookassa.domain.models.confirmation.response.confirmation_external import \
    ConfirmationExternal as ResponseConfirmationExternal
from yookassa.domain.models.confirmation.response.confirmation_mobile_application import \
    ConfirmationMobileApplication as ResponseConfirmationMobileApplication


class TestConfirmation(unittest.TestCase):
    def test_confirmation_request(self):
        confirmation = RequestConfirmationRedirect()
        confirmation.type = ConfirmationType.REDIRECT
        confirmation.locale = 'ru_RU'
        confirmation.enforce = True
        confirmation.return_url = 'return.url'

        self.assertEqual(confirmation.type, ConfirmationType.REDIRECT)
        self.assertTrue(confirmation.enforce)
        self.assertEqual(
            {'type': ConfirmationType.REDIRECT, 'locale': 'ru_RU', 'enforce': True, 'return_url': 'return.url'},
            dict(confirmation)
        )

        with self.assertRaises(ValueError):
            confirmation.return_url = ''

    def test_confirmation_response(self):
        confirmation = ResponseConfirmationRedirect()
        confirmation.type = ConfirmationType.REDIRECT
        confirmation.enforce = True
        confirmation.return_url = 'return.url'
        confirmation.confirmation_url = 'confirmation.url'
        self.assertEqual(confirmation.type, ConfirmationType.REDIRECT)
        self.assertTrue(confirmation.enforce)
        self.assertEqual(
            {
                'type': ConfirmationType.REDIRECT,
                'enforce': True,
                'return_url': 'return.url',
                'confirmation_url': 'confirmation.url'
            },
            dict(confirmation)
        )

        with self.assertRaises(ValueError):
            confirmation.return_url = ''

    def test_confirmation_request_qr(self):
        confirmation = RequestConfirmationQr()
        confirmation.return_url = 'return_url.url'
        self.assertEqual(confirmation.type, ConfirmationType.QR)
        self.assertEqual(
            {
                'type': ConfirmationType.QR,
                'return_url': 'return_url.url'
            },
            dict(confirmation)
        )

        with self.assertRaises(ValueError):
            confirmation.return_url = ''

    def test_confirmation_response_qr(self):
        confirmation = ResponseConfirmationQr()
        confirmation.confirmation_data = 'confirmation.url'
        self.assertEqual(confirmation.type, ConfirmationType.QR)
        self.assertEqual(
            {
                'type': ConfirmationType.QR,
                'confirmation_data': 'confirmation.url'
            },
            dict(confirmation)
        )

        with self.assertRaises(ValueError):
            confirmation.confirmation_data = ''

    def test_confirmation_request_mobile_application(self):
        confirmation = RequestConfirmationMobileApplication()
        confirmation.return_url = 'return_url.url'
        self.assertEqual(confirmation.type, ConfirmationType.MOBILE_APPLICATION)
        self.assertEqual(
            {
                'type': ConfirmationType.MOBILE_APPLICATION,
                'return_url': 'return_url.url'
            },
            dict(confirmation)
        )

        with self.assertRaises(ValueError):
            confirmation.return_url = ''

    def test_confirmation_response_mobile_application(self):
        confirmation = ResponseConfirmationMobileApplication()
        confirmation.confirmation_url = 'confirmation.url'
        self.assertEqual(confirmation.type, ConfirmationType.MOBILE_APPLICATION)
        self.assertEqual(
            {
                'type': ConfirmationType.MOBILE_APPLICATION,
                'confirmation_url': 'confirmation.url'
            },
            dict(confirmation)
        )

    def test_confirmation_request_embedded(self):
        confirmation = RequestConfirmationEmbedded()
        self.assertEqual(confirmation.type, ConfirmationType.EMBEDDED)
        self.assertEqual(
            {
                'type': ConfirmationType.EMBEDDED,
            },
            dict(confirmation)
        )

    def test_confirmation_response_embedded(self):
        confirmation = ResponseConfirmationEmbedded()
        confirmation.confirmation_token = 'confirmation_token'
        self.assertEqual(confirmation.type, ConfirmationType.EMBEDDED)
        self.assertEqual(
            {
                'type': ConfirmationType.EMBEDDED,
                'confirmation_token': 'confirmation_token'
            },
            dict(confirmation)
        )

    def test_confirmation_request_external(self):
        confirmation = RequestConfirmationExternal()
        self.assertEqual(confirmation.type, ConfirmationType.EXTERNAL)
        self.assertEqual(
            {
                'type': ConfirmationType.EXTERNAL,
            },
            dict(confirmation)
        )

    def test_confirmation_response_external(self):
        confirmation = ResponseConfirmationExternal()
        self.assertEqual(confirmation.type, ConfirmationType.EXTERNAL)
        self.assertEqual(
            {
                'type': ConfirmationType.EXTERNAL,
            },
            dict(confirmation)
        )
