# -*- coding: utf-8 -*-
import unittest
from yookassa.domain.models.payment_data.payment_order.payment_order_recipient_utilities import PaymentOrderRecipientUtilities
from yookassa.domain.models.payment_data.payment_order.payment_order_recipient_bank_utilities import PaymentOrderRecipientBankUtilities


class TestPaymentOrderRecipient(unittest.TestCase):
    def setUp(self):
        self.valid_bank_data = {
            "name": "ПАО Сбербанк",
            "bic": "044525225",
            "account": "40702810000000000001",
            "correspondent_account": "30101810400000000225"
        }
        self.valid_recipient_data = {
            "name": "ООО Тестовая компания",
            "inn": "1234567890",
            "kpp": "987654321",
            "bank": self.valid_bank_data
        }

    def test_recipient_cast(self):
        self.maxDiff = None
        recipient = PaymentOrderRecipientUtilities()
        recipient.name = self.valid_recipient_data["name"]
        recipient.inn = self.valid_recipient_data["inn"]
        recipient.kpp = self.valid_recipient_data["kpp"]
        recipient.bank = self.valid_bank_data

        self.assertEqual(self.valid_recipient_data, dict(recipient))
        self.assertEqual(self.valid_recipient_data["name"], recipient.name)
        self.assertEqual(self.valid_recipient_data["inn"], recipient.inn)
        self.assertEqual(self.valid_recipient_data["kpp"], recipient.kpp)

        self.assertIsInstance(recipient.bank, PaymentOrderRecipientBankUtilities)
        self.assertEqual(self.valid_bank_data["name"], recipient.bank.name)
        self.assertEqual(self.valid_bank_data["bic"], recipient.bank.bic)
        self.assertEqual(self.valid_bank_data["account"], recipient.bank.account)
        self.assertEqual(self.valid_bank_data["correspondent_account"], recipient.bank.correspondent_account)

    def test_recipient_invalid(self):
        recipient = PaymentOrderRecipientUtilities()

        with self.assertRaises(ValueError):
            recipient.inn = "invalid_inn"

        with self.assertRaises(ValueError):
            recipient.inn = "123456789"

        with self.assertRaises(ValueError):
            recipient.kpp = "invalid_kpp"

        with self.assertRaises(ValueError):
            recipient.kpp = "12345678"

        with self.assertRaises(TypeError):
            recipient.bank = "invalid_bank_type"

        recipient.name = None
        recipient.inn = None
        recipient.kpp = None

        self.assertIsNone(recipient.name)
        self.assertIsNone(recipient.inn)
        self.assertIsNone(recipient.kpp)

        with self.assertRaises(TypeError):
            recipient.bank = None

    def test_recipient_bank_validation(self):
        recipient = PaymentOrderRecipientUtilities()
        recipient.bank = PaymentOrderRecipientBankUtilities()

        with self.assertRaises(ValueError):
            recipient.bank.bic = "12345678"

        with self.assertRaises(ValueError):
            recipient.bank.bic = "abcdefghi"

        valid_bic = "044525225"
        recipient.bank.bic = valid_bic
        self.assertEqual(valid_bic, recipient.bank.bic)

    def test_recipient_bank_full_cycle(self):
        bank = PaymentOrderRecipientBankUtilities()
        bank.name = "ПАО Сбербанк"
        bank.bic = "044525225"
        bank.account = "40702810000000000001"
        bank.correspondent_account = "30101810400000000225"

        recipient = PaymentOrderRecipientUtilities()
        recipient.name = "ООО Тестовая компания"
        recipient.inn = "1234567890"
        recipient.kpp = "987654321"
        recipient.bank = bank

        result_dict = dict(recipient)
        self.assertEqual("ПАО Сбербанк", result_dict["bank"]["name"])
        self.assertEqual("044525225", result_dict["bank"]["bic"])
        self.assertEqual("40702810000000000001", result_dict["bank"]["account"])
        self.assertEqual("30101810400000000225", result_dict["bank"]["correspondent_account"])
