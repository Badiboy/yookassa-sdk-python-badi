# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models.payment_data.payment_order.request.payment_order_utilities import PaymentOrderUtilities


class TestPaymentOrderUtilities(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.valid_data = {
            "type": "utilities",
            "amount": {"value": "100.00", "currency": "RUB"},
            "payment_purpose": "Оплата ЖКУ за июль 2023",
            "recipient": {
                "name": "ООО УК Жилфонд",
                "inn": "1234567890",
                "kpp": "987654321",
                "bank": {
                    "name": "ПАО Сбербанк",
                    "bic": "044525225",
                    "account": "40702810000000000001",
                    "correspondent_account": "30101810400000000225"
                }
            },
            "kbk": "18210102000011000110",
            "oktmo": "45382000",
            "payment_period": {"month": 7, "year": 2023},
            "payment_document_id": "123456789012345678",
            "payment_document_number": "123-456",
            "account_number": "1234567890",
            "unified_account_number": "1234567890",
            "service_id": "1234567890123"
        }

    def test_utilities_cast(self):
        utilities = PaymentOrderUtilities()
        utilities.amount = self.valid_data["amount"]
        utilities.payment_purpose = self.valid_data["payment_purpose"]
        utilities.recipient = self.valid_data["recipient"]
        utilities.kbk = self.valid_data["kbk"]
        utilities.oktmo = self.valid_data["oktmo"]
        utilities.payment_period = self.valid_data["payment_period"]
        utilities.payment_document_id = self.valid_data["payment_document_id"]
        utilities.payment_document_number = self.valid_data["payment_document_number"]
        utilities.account_number = self.valid_data["account_number"]
        utilities.unified_account_number = self.valid_data["unified_account_number"]
        utilities.service_id = self.valid_data["service_id"]

        result_dict = dict(utilities)

        self.assertEqual(self.valid_data["payment_period"], dict(utilities.payment_period))
        self.assertEqual(self.valid_data["type"], result_dict["type"])
        self.assertEqual(self.valid_data["amount"], result_dict["amount"])
        self.assertEqual(self.valid_data["payment_purpose"], result_dict["payment_purpose"])
        self.assertEqual(self.valid_data["recipient"], result_dict["recipient"])
        self.assertEqual(self.valid_data["kbk"], result_dict["kbk"])
        self.assertEqual(self.valid_data["oktmo"], result_dict["oktmo"])
        self.assertEqual(self.valid_data["payment_document_id"], result_dict["payment_document_id"])
        self.assertEqual(self.valid_data["payment_document_number"], result_dict["payment_document_number"])
        self.assertEqual(self.valid_data["account_number"], result_dict["account_number"])
        self.assertEqual(self.valid_data["unified_account_number"], result_dict["unified_account_number"])
        self.assertEqual(self.valid_data["service_id"], result_dict["service_id"])

    def test_utilities_dict_initialization(self):
        utilities = PaymentOrderUtilities(self.valid_data)

        self.assertEqual(self.valid_data["payment_period"], dict(utilities.payment_period))
        self.assertEqual(float(self.valid_data["amount"]["value"]), float(utilities.amount.value))
        self.assertEqual(self.valid_data["payment_purpose"], utilities.payment_purpose)
        self.assertEqual(self.valid_data["kbk"], utilities.kbk)
        self.assertEqual(self.valid_data["oktmo"], utilities.oktmo)
        self.assertEqual(self.valid_data["payment_document_id"], utilities.payment_document_id)
        self.assertEqual(self.valid_data["payment_document_number"], utilities.payment_document_number)
        self.assertEqual(self.valid_data["account_number"], utilities.account_number)
        self.assertEqual(self.valid_data["unified_account_number"], utilities.unified_account_number)
        self.assertEqual(self.valid_data["service_id"], utilities.service_id)

        result_dict = dict(utilities)
        self.assertEqual(self.valid_data, result_dict)

    def test_utilities_invalid(self):
        utilities = PaymentOrderUtilities()

        with self.assertRaises(TypeError):
            utilities.amount = "invalid_amount"

        with self.assertRaises(TypeError):
            utilities.recipient = "invalid_recipient"

        with self.assertRaises(TypeError):
            utilities.payment_period = "invalid_period"

        with self.assertRaises(ValueError):
            utilities.kbk = "123"

        with self.assertRaises(ValueError):
            utilities.kbk = "123456789012345678901"

        with self.assertRaises(ValueError):
            utilities.kbk = "abcdefghijklmnopqrst"

        with self.assertRaises(ValueError):
            utilities.oktmo = "123"

        with self.assertRaises(ValueError):
            utilities.oktmo = "123456789"

        with self.assertRaises(ValueError):
            utilities.oktmo = "abcdefgh"

        with self.assertRaises(ValueError):
            utilities.payment_document_id = "123"

        with self.assertRaises(ValueError):
            utilities.payment_document_id = "1234567890123456789"

        with self.assertRaises(ValueError):
            utilities.payment_document_number = ""

        with self.assertRaises(ValueError):
            utilities.payment_document_number = "1" * 31

        with self.assertRaises(ValueError):
            utilities.account_number = ""

        with self.assertRaises(ValueError):
            utilities.account_number = "1" * 31

        with self.assertRaises(ValueError):
            utilities.unified_account_number = "123"

        with self.assertRaises(ValueError):
            utilities.unified_account_number = "12345678901"

        with self.assertRaises(ValueError):
            utilities.service_id = "123"

        with self.assertRaises(ValueError):
            utilities.service_id = "12345678901234"

    def test_utilities_none_values(self):
        utilities = PaymentOrderUtilities()

        utilities.type = None
        utilities.payment_purpose = None
        utilities.kbk = None
        utilities.oktmo = None
        utilities.payment_document_id = None
        utilities.payment_document_number = None
        utilities.account_number = None
        utilities.unified_account_number = None
        utilities.service_id = None

        self.assertIsNone(utilities.type)
        self.assertIsNone(utilities.payment_purpose)
        self.assertIsNone(utilities.kbk)
        self.assertIsNone(utilities.oktmo)
        self.assertIsNone(utilities.payment_document_id)
        self.assertIsNone(utilities.payment_document_number)
        self.assertIsNone(utilities.account_number)
        self.assertIsNone(utilities.unified_account_number)
        self.assertIsNone(utilities.service_id)
