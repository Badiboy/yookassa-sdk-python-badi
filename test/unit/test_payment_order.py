# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models.payment_data.payment_order.payment_order import PaymentOrder


class TestPaymentOrder(unittest.TestCase):
    def setUp(self):
        pass

    def test_payment_order(self):
        payment_order = PaymentOrder()

        payment_order.type = "test_type"
        self.assertEqual(payment_order.type, "test_type")
        self.assertIsInstance(payment_order.type, str)

        payment_order.type = 123
        self.assertEqual(payment_order.type, 123)

        payment_order.type = None
        self.assertIsNone(payment_order.type)
