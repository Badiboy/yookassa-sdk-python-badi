# -*- coding: utf-8 -*-
import unittest
from yookassa.domain.models.payment_data.payment_order.payment_order_recipient_bank_utilities import PaymentOrderRecipientBankUtilities


class TestPaymentOrderRecipientBank(unittest.TestCase):
    def setUp(self):
        self.valid_bank_data = {
            "name": "ПАО Сбербанк",
            "bic": "044525225",
            "account": "40702810000000000001",
            "correspondent_account": "30101810400000000225"
        }

    def test_bank_cast(self):
        self.maxDiff = None
        bank = PaymentOrderRecipientBankUtilities()
        bank.name = self.valid_bank_data["name"]
        bank.bic = self.valid_bank_data["bic"]
        bank.account = self.valid_bank_data["account"]
        bank.correspondent_account = self.valid_bank_data["correspondent_account"]

        self.assertEqual(self.valid_bank_data, dict(bank))
        self.assertEqual(self.valid_bank_data["name"], bank.name)
        self.assertEqual(self.valid_bank_data["bic"], bank.bic)
        self.assertEqual(self.valid_bank_data["account"], bank.account)
        self.assertEqual(self.valid_bank_data["correspondent_account"], bank.correspondent_account)

    def test_bank_invalid_bic(self):
        bank = PaymentOrderRecipientBankUtilities()

        with self.assertRaises(ValueError):
            bank.bic = "12345678"

        with self.assertRaises(ValueError):
            bank.bic = "abcdefghi"

        with self.assertRaises(ValueError):
            bank.bic = "1234567890"

        bank.bic = None
        self.assertIsNone(bank.bic)

    def test_bank_properties(self):
        bank = PaymentOrderRecipientBankUtilities()

        bank.name = "АО Банк Тест"
        self.assertEqual("АО Банк Тест", bank.name)

        bank.account = "40702810400000000002"
        self.assertEqual("40702810400000000002", bank.account)

        bank.correspondent_account = "30101810600000000226"
        self.assertEqual("30101810600000000226", bank.correspondent_account)

        bank.name = None
        bank.account = None
        bank.correspondent_account = None

        self.assertIsNone(bank.name)
        self.assertIsNone(bank.account)
        self.assertIsNone(bank.correspondent_account)

    def test_bank_dict_initialization(self):
        bank = PaymentOrderRecipientBankUtilities(self.valid_bank_data)

        self.assertEqual(self.valid_bank_data["name"], bank.name)
        self.assertEqual(self.valid_bank_data["bic"], bank.bic)
        self.assertEqual(self.valid_bank_data["account"], bank.account)
        self.assertEqual(self.valid_bank_data["correspondent_account"], bank.correspondent_account)

        result_dict = dict(bank)
        self.assertEqual(self.valid_bank_data, result_dict)
