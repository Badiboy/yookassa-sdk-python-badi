from unittest import TestCase

from yookassa.domain.models.payment_data.statement.delivery_method.delivery_method import DeliveryMethod


class TestDeliveryMethod(TestCase):
    def setUp(self):
        pass

    def test_payment_order(self):
        delivery_method = DeliveryMethod()

        delivery_method.type = "test_type"
        self.assertEqual(delivery_method.type, "test_type")
        self.assertIsInstance(delivery_method.type, str)

        delivery_method.type = 123
        self.assertEqual(delivery_method.type, "123")
        self.assertIsInstance(delivery_method.type, str)

        with self.assertRaises(ValueError):
            delivery_method.type = None
