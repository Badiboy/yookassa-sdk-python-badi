# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.common.data_context import DataContext
from yookassa.domain.common.payment_method_type import PaymentMethodType
from yookassa.domain.models.payment_data.payment_data_factory import PaymentDataFactory
from yookassa.domain.models.payment_data.request.payment_data_yoomoney_wallet import PaymentDataYooMoneyWallet
from yookassa.domain.models.payment_data.response.payment_data_sberbank import PaymentDataSberbank
from yookassa.domain.models.payment_data.response.payment_data_sbp import PaymentDataSbp


class TestPaymentDataFactory(unittest.TestCase):
    def test_factory_method(self):
        factory = PaymentDataFactory()
        request_payment_data = factory.create({'type': PaymentMethodType.YOO_MONEY}, DataContext.REQUEST)
        self.assertIsInstance(request_payment_data, PaymentDataYooMoneyWallet)

        response_payment_data = factory.create({'type': PaymentMethodType.SBERBANK}, DataContext.RESPONSE)
        self.assertIsInstance(response_payment_data, PaymentDataSberbank)

        response_payment_data = factory.create({'type': PaymentMethodType.SBP}, DataContext.RESPONSE)
        self.assertIsInstance(response_payment_data, PaymentDataSbp)
