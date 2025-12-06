# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models.payment_data.statement import Statement


class TestStatement(unittest.TestCase):
    def setUp(self):
        pass

    def test_payment_order(self):
        statement = Statement()

        statement.type = "test_type"
        self.assertEqual(statement.type, "test_type")
        self.assertIsInstance(statement.type, str)

        statement.type = 123
        self.assertEqual(statement.type, "123")
        self.assertIsInstance(statement.type, str)

        with self.assertRaises(ValueError):
            statement.type = None
