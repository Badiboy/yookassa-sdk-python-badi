# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models.receipt_data.additional_user_props import AdditionalUserProps
from yookassa.domain.models.receipt_data.industry_details import IndustryDetails
from yookassa.domain.models.receipt_data.mark_code_info import MarkCodeInfo
from yookassa.domain.models.receipt_data.mark_quantity import MarkQuantity
from yookassa.domain.models.receipt_data.operational_details import OperationalDetails


class TestReceiptData(unittest.TestCase):
    def test_additional_user_props(self):
        model = AdditionalUserProps({
            'name': 'name',
            'value': 'value',
        })

        self.assertEqual({
            'name': 'name',
            'value': 'value',
        }, dict(model))

        with self.assertRaises(ValueError):
            model.name = None

        with self.assertRaises(ValueError):
            model.name = 'invalid additional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_props'  # noqa: E501

        with self.assertRaises(ValueError):
            model.value = None

        with self.assertRaises(ValueError):
            model.value = 'invalid additional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_propsadditional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_props'  # noqa: E501

    def test_industry_details(self):
        model = IndustryDetails({
            "federal_id": "004",
            "document_date": "2023-03-03",
            "document_number": "21102023",
            "value": "value",
        })

        self.assertEqual({
            "federal_id": "004",
            "document_date": "2023-03-03",
            "document_number": "21102023",
            "value": "value",
        }, dict(model))

        with self.assertRaises(ValueError):
            model.federal_id = None

        with self.assertRaises(ValueError):
            model.federal_id = 'invalid federal_id'  # noqa: E501

        with self.assertRaises(ValueError):
            model.document_date = None

        with self.assertRaises(ValueError):
            model.document_number = None

        with self.assertRaises(ValueError):
            model.document_number = 'invalid additional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_props'  # noqa: E501

        with self.assertRaises(ValueError):
            model.value = None

        with self.assertRaises(ValueError):
            model.value = 'invalid additional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_propsadditional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_props'  # noqa: E501

    def test_mark_code_info(self):
        model = MarkCodeInfo({
            "mark_code_raw": "010460406000590021N4N57RTCBUZTQ\\u001d2403054002410161218\\u001d1424010191ffd0\\u001g92tIAF/YVpU4roQS3M/m4z78yFq0nc/WsSmLeX6QkF/YVWwy5IMYAeiQ91Xa2m/fFSJcOkb2N+uUUtfr4n0mOX0Q==",
            'unknown': '123%123&sldkfjldksfj*(*',
            'ean_8': '46198532',
            'ean_13': '4006670128002',
            'itf_14': '01460123456789',
            'gs_10': '010460043993125621JgXJ5.T',
            "gs_1m": "010460406000590021N4N57RTCBUZTQ",
            'fur': 'RU-401301-AAA0277031',
            'short': '0004607006112575215MEZgB933==',
            'egais_20': '52419RAYLTL37TX31219019004460R96J',
            'egais_30': '19530126773682',
        })

        self.assertEqual({
            "mark_code_raw": "010460406000590021N4N57RTCBUZTQ\\u001d2403054002410161218\\u001d1424010191ffd0\\u001g92tIAF/YVpU4roQS3M/m4z78yFq0nc/WsSmLeX6QkF/YVWwy5IMYAeiQ91Xa2m/fFSJcOkb2N+uUUtfr4n0mOX0Q==",
            'unknown': '123%123&sldkfjldksfj*(*',
            'ean_8': '46198532',
            'ean_13': '4006670128002',
            'itf_14': '01460123456789',
            'gs_10': '010460043993125621JgXJ5.T',
            "gs_1m": "010460406000590021N4N57RTCBUZTQ",
            'fur': 'RU-401301-AAA0277031',
            'short': '0004607006112575215MEZgB933==',
            'egais_20': '52419RAYLTL37TX31219019004460R96J',
            'egais_30': '19530126773682',
        }, dict(model))

        with self.assertRaises(ValueError):
            model.unknown = ''

        with self.assertRaises(ValueError):
            model.unknown = 'invalid unknown_unknown_unknown_unknown'  # noqa: E501

        with self.assertRaises(ValueError):
            model.ean_8 = '1234567'

        with self.assertRaises(ValueError):
            model.ean_8 = '123456789'

        with self.assertRaises(ValueError):
            model.ean_13 = '123456789012'

        with self.assertRaises(ValueError):
            model.ean_13 = '12345678901234'

        with self.assertRaises(ValueError):
            model.itf_14 = '1234567890123'

        with self.assertRaises(ValueError):
            model.itf_14 = '123456789012345'

        with self.assertRaises(ValueError):
            model.gs_10 = ''

        with self.assertRaises(ValueError):
            model.gs_10 = 'invalid unknown_unknown_unknown_unknown'  # noqa: E501

        with self.assertRaises(ValueError):
            model.gs_1m = ''

        with self.assertRaises(ValueError):
            model.gs_1m = 'invalid additional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_propsadditional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_props'  # noqa: E501

        with self.assertRaises(ValueError):
            model.fur = 'RU401301AAA0277031'

        with self.assertRaises(ValueError):
            model.fur = 'RU-401301-AAA-0277031'

        with self.assertRaises(ValueError):
            model.short = ''

        with self.assertRaises(ValueError):
            model.short = 'invalid additional_payment_subject_props_additional_payment_subject_props'  # noqa: E501

        with self.assertRaises(ValueError):
            model.egais_20 = '52419RAYLTL37TX31219019004460R96'

        with self.assertRaises(ValueError):
            model.egais_20 = '52419RAYLTL37TX31219019004460R96J0'

        with self.assertRaises(ValueError):
            model.egais_30 = '1953012677368'

        with self.assertRaises(ValueError):
            model.egais_30 = '195301267736820'

    def test_mark_quantity(self):
        model = MarkQuantity({
            "numerator": 5,
            "denominator": 10
        })

        self.assertEqual({
            "numerator": 5,
            "denominator": 10
        }, dict(model))

        with self.assertRaises(ValueError):
            model.numerator = None

        with self.assertRaises(ValueError):
            model.numerator = 0

        with self.assertRaises(ValueError):
            model.denominator = None

        with self.assertRaises(ValueError):
            model.denominator = 0

    def test_operational_details(self):
        model = OperationalDetails({
            'operation_id': 111,
            'value': 'Данные операции',
            'created_at': '2023-03-03T11:52:31.827Z',
        })

        self.assertEqual({
            'operation_id': 111,
            'value': 'Данные операции',
            'created_at': '2023-03-03T11:52:31.827Z',
        }, dict(model))

        with self.assertRaises(ValueError):
            model.operation_id = None

        with self.assertRaises(TypeError):
            model.operation_id = 'invalid operation_id'

        with self.assertRaises(ValueError):
            model.operation_id = -100

        with self.assertRaises(ValueError):
            model.operation_id = 300

        with self.assertRaises(ValueError):
            model.value = None

        with self.assertRaises(ValueError):
            model.value = 'invalid additional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_propsadditional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_props'  # noqa: E501

        with self.assertRaises(ValueError):
            model.created_at = None
