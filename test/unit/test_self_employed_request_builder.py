# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.request import SelfEmployedRequestBuilder


class TestSelfEmployedRequestBuilder(unittest.TestCase):

    def test_build_object(self):
        self.maxDiff = None
        request = None
        builder = SelfEmployedRequestBuilder() \
            .set_itn('123456789012') \
            .set_phone('79998887766') \
            .set_description('Test') \
            .set_metadata({'order_id': '37'}) \
            .set_confirmation({"type": "redirect"})

        request = builder.build()

        self.assertEqual({
            "itn": "123456789012",
            "phone": "79998887766",
            "description": "Test",
            "metadata": {
                "order_id": "37"
            },
            "confirmation": {
                "type": "redirect"
            }
        }, dict(request))
