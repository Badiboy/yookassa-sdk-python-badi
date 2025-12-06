# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models import PersonalDataType
from yookassa.domain.request import PersonalDataRequestBuilder


class TestPersonalDataRequestBuilder(unittest.TestCase):

    def test_build_object(self):
        self.maxDiff = None
        request = None
        builder = PersonalDataRequestBuilder() \
            .set_type(PersonalDataType.SBP_PAYOUT_RECIPIENT) \
            .set_last_name("Иванов") \
            .set_first_name("Иван") \
            .set_middle_name("Иванович") \
            .set_metadata({"cms_name": "Django"})

        request = builder.build()

        self.assertEqual({
            "type": "sbp_payout_recipient",
            "last_name": "Иванов",
            "first_name": "Иван",
            "middle_name": "Иванович",
            "metadata": {
                "cms_name": "Django"
            }
          }, dict(request))
