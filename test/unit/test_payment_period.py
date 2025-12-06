# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models.payment_data.payment_order.payment_period import PaymentPeriod


class TestPaymentPeriod(unittest.TestCase):
    def setUp(self):
        self.valid_data = {
            "month": 7,
            "year": 2023
        }

    def test_payment_period_valid(self):
        period = PaymentPeriod()
        period.month = self.valid_data["month"]
        period.year = self.valid_data["year"]
        self.assertEqual(self.valid_data["month"], period.month)
        self.assertEqual(self.valid_data["year"], period.year)
        self.assertEqual(self.valid_data, dict(period))

    def test_payment_period_dict_initialization(self):
        period = PaymentPeriod(self.valid_data)
        self.assertEqual(self.valid_data["month"], period.month)
        self.assertEqual(self.valid_data["year"], period.year)
        self.assertEqual(self.valid_data, dict(period))

    def test_payment_period_month_validation(self):
        period = PaymentPeriod()
        period.month = 1
        self.assertEqual(1, period.month)
        period.month = 12
        self.assertEqual(12, period.month)

        with self.assertRaises(ValueError):
            period.month = 0
        with self.assertRaises(ValueError):
            period.month = 13
        with self.assertRaises(ValueError):
            period.month = -5

    def test_payment_period_year_validation(self):
        period = PaymentPeriod()
        period.year = 2023
        self.assertEqual(2023, period.year)
        period.year = 1999
        self.assertEqual(1999, period.year)
        period.year = 2100
        self.assertEqual(2100, period.year)
        period.year = None
        self.assertIsNone(period.year)

    def test_payment_period_edge_cases(self):
        period = PaymentPeriod({"month": 1, "year": 2000})
        self.assertEqual(1, period.month)
        self.assertEqual(2000, period.year)
        period.month = 12
        period.year = 9999
        self.assertEqual(12, period.month)
        self.assertEqual(9999, period.year)
