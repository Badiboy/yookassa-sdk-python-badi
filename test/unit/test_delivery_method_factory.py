import unittest

from yookassa.domain.common import DataContext
from yookassa.domain.models.payment_data.statement.delivery_method.delivery_method_factory import DeliveryMethodFactory
from yookassa.domain.models.payment_data.statement.delivery_method.delivery_method_type import DeliveryMethodType
from yookassa.domain.models.payment_data.statement.delivery_method.request.delivery_method_email import \
    DeliveryMethodEmail


class TestDeliveryMethodFactory(unittest.TestCase):
    def test_factory_method(self):
        req_redirect_instance = DeliveryMethodFactory().create({'type': DeliveryMethodType.EMAIL}, DataContext.REQUEST)
        self.assertIsInstance(req_redirect_instance, DeliveryMethodEmail)
