# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.common import DataContext
from yookassa.domain.models.payment_data.statement import StatementFactory, StatementType
from yookassa.domain.models.payment_data.statement.request.statement_payment_overview import StatementPaymentOverview


class TestStatementFactory(unittest.TestCase):
    def test_factory_method(self):
        req_redirect_instance = StatementFactory().create({'type': StatementType.PAYMENT_OVERVIEW}, DataContext.REQUEST)
        self.assertIsInstance(req_redirect_instance, StatementPaymentOverview)
