# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models.payment_method.response.payment_method_holder import PaymentMethodHolder
from yookassa.domain.models.payment_data.response.credit_card import CreditCard
from yookassa.domain.models.payment_data.card_type import CardType
from yookassa.domain.response import PaymentMethodResponse


class TestPaymentMethodResponse(unittest.TestCase):

    def test_response_cast(self):
        self.maxDiff = None
        response = PaymentMethodResponse({
            "id": "21b23365-000f-500b-9000-070fa3554403",
            "type": "bank_card",
            "card": {
                "first6": "123456",
                "last4": "7890",
                "expiry_year": "2024",
                "expiry_month": "12",
                "card_type": CardType.MASTER_CARD,
                "issuer_country": "RU",
                "issuer_name": "Sberbank",
                "source": "google_pay",
                "id": "card-123456"
            },
            "saved": True,
            "status": "active",
            "holder": {
                "account_id": "67192",
                "gateway_id": "352780"
            },
            "title": "Card *7890",
            "confirmation": {
                "type": "redirect",
                "return_url": "https://test.test/test",
                "confirmation_url": "https://url",
                "enforce": False
            }
        })

        self.assertEqual(response.id, "21b23365-000f-500b-9000-070fa3554403")
        self.assertEqual(response.type, "bank_card")
        self.assertTrue(response.saved)
        self.assertEqual(response.status, "active")
        self.assertEqual(response.title, "Card *7890")

        self.assertIsInstance(response.card, CreditCard)
        self.assertEqual(response.card.first6, "123456")
        self.assertEqual(response.card.last4, "7890")
        self.assertEqual(response.card.expiry_year, "2024")
        self.assertEqual(response.card.expiry_month, "12")
        self.assertEqual(response.card.card_type, CardType.MASTER_CARD)
        self.assertEqual(response.card.issuer_country, "RU")
        self.assertEqual(response.card.issuer_name, "Sberbank")
        self.assertEqual(response.card.source, "google_pay")
        self.assertEqual(response.card.id, "card-123456")

        self.assertIsInstance(response.holder, PaymentMethodHolder)
        self.assertEqual(response.holder.account_id, "67192")
        self.assertEqual(response.holder.gateway_id, "352780")

        self.assertIsNotNone(response.confirmation)
        self.assertEqual(response.confirmation.type, "redirect")

    def test_response_invalid_card(self):
        with self.assertRaises(ValueError):
            CreditCard({
                "first6": "invalid",
                "last4": "7890",
                "expiry_year": "2024",
                "expiry_month": "12"
            })

        with self.assertRaises(ValueError):
            card = CreditCard({
                "first6": "123456",
                "last4": "7890",
                "expiry_year": "2024",
                "expiry_month": "12"
            })
            card.first6 = "invalid"

    def test_response_minimal(self):
        response = PaymentMethodResponse({
            "id": "21b23365-000f-500b-9000-070fa3554403",
            "type": "bank_card",
            "card": {
                "first6": "123456",
                "last4": "7890",
                "expiry_year": "2024",
                "expiry_month": "12"
            }
        })

        self.assertEqual(response.id, "21b23365-000f-500b-9000-070fa3554403")
        self.assertEqual(response.type, "bank_card")
        self.assertIsNone(response.saved)
        self.assertIsNone(response.status)
        self.assertIsNone(response.title)
        self.assertIsNone(response.holder)
        self.assertIsNone(response.confirmation)

    def test_response_setters(self):
        response = PaymentMethodResponse()
        response.id = "21b23365-000f-500b-9000-070fa3554403"
        response.type = "bank_card"
        response.saved = True
        response.status = "active"
        response.title = "Card *7890"

        card = {
            "first6": "123456",
            "last4": "7890",
            "expiry_year": "2024",
            "expiry_month": "12",
            "card_type": CardType.VISA,
            "issuer_country": "RU",
            "issuer_name": "Tinkoff",
            "source": "apple_pay",
            "id": "card-654321"
        }
        response.card = card

        holder = {
            "account_id": "67192",
            "gateway_id": "352780"
        }
        response.holder = holder

        confirmation = {
            "type": "redirect",
            "return_url": "https://test.test/test",
            "confirmation_url": "https://url",
            "enforce": False
        }
        response.confirmation = confirmation

        self.assertEqual(response.id, "21b23365-000f-500b-9000-070fa3554403")
        self.assertEqual(response.type, "bank_card")
        self.assertTrue(response.saved)
        self.assertEqual(response.status, "active")
        self.assertEqual(response.title, "Card *7890")

        self.assertIsInstance(response.card, CreditCard)
        self.assertEqual(response.card.first6, "123456")
        self.assertEqual(response.card.last4, "7890")
        self.assertEqual(response.card.card_type, CardType.VISA)

        self.assertIsInstance(response.holder, PaymentMethodHolder)
        self.assertEqual(response.holder.account_id, "67192")

        self.assertIsNotNone(response.confirmation)
        self.assertEqual(response.confirmation.type, "redirect")
