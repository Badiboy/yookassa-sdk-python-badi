# -*- coding: utf-8 -*-
import unittest
from decimal import Decimal

from yookassa.domain.models.amount import Amount
from yookassa.domain.models.currency import Currency
from yookassa.domain.models.receipt import Receipt
from yookassa.domain.models.receipt_data.receipt_customer import ReceiptCustomer
from yookassa.domain.models.receipt_data.industry_details import IndustryDetails
from yookassa.domain.models.receipt_data.mark_code_info import MarkCodeInfo
from yookassa.domain.models.receipt_data.mark_quantity import MarkQuantity
from yookassa.domain.models.receipt_data.operational_details import OperationalDetails
from yookassa.domain.models.receipt_data.receipt_item import ReceiptItem, PaymentSubject, PaymentMode, ReceiptItemMeasure


class TestReceiptModel(unittest.TestCase):

    def test_receipt_cast(self):
        self.maxDiff = None
        receipt = Receipt()
        receipt.customer = {'phone': '79990000000', 'email': 'test@email.com'}
        receipt.phone = '79990000000'
        receipt.email = 'test@email.com'
        receipt.tax_system_code = 1
        receipt.internet = True
        receipt.timezone = 6

        receipt.receipt_industry_details = [
            IndustryDetails({
                'federal_id': '004',
                'document_date': '2023-03-03',
                'document_number': '21102023',
                'value': 'value',
            })
        ]
        receipt.receipt_operational_details = OperationalDetails({
            'operation_id': 111,
            'value': 'Данные операции',
            'created_at': '2023-03-03T11:52:31.827Z',
        })

        receipt.items = None
        self.assertFalse(receipt.has_items())

        receipt.items = [
            {
                "description": "Product 1",
                "quantity": '2.1',
                "amount": {
                    "value": 250.0,
                    "currency": Currency.RUB
                },
                "vat_code": "2"
            },
            ReceiptItem(
                {
                    "description": "Product 2",
                    "quantity": 1.0,
                    "amount": {
                        "value": '100.01',
                        "currency": Currency.RUB
                    },
                    "vat_code": 2,
                    "planned_status": 3,
                    "payment_subject": PaymentSubject.AGENT_COMMISSION,
                    "payment_mode": PaymentMode.ADVANCE,
                    "product_code": "00 00 00 01 00 21 FA 41 00 23 05 41 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 12 00 AB 00",
                    "country_of_origin_code": "RU",
                    "customs_declaration_number": "90/210",
                    "excise": 2.00,
                    "mark_code_info": {
                        "mark_code_raw": "010460406000590021N4N57RTCBUZTQ\\u001d2403054002410161218\\u001d1424010191ffd0\\u001g92tIAF/YVpU4roQS3M/m4z78yFq0nc/WsSmLeX6QkF/YVWwy5IMYAeiQ91Xa2m/fFSJcOkb2N+uUUtfr4n0mOX0Q==",
                        "gs_1m": "010460406000590021N4N57RTCBUZTQ"
                    },
                    "measure": ReceiptItemMeasure.PIECE,
                    "payment_subject_industry_details": [
                        {
                            "federal_id": "004",
                            "document_date": "2023-03-03",
                            "document_number": "21102023",
                            "value": "value",
                        }
                    ],
                    "mark_mode": "0",
                    "mark_quantity": {
                        "numerator": 5,
                        "denominator": 10
                    },
                }
            )

        ]

        self.assertTrue(receipt.has_items())

        expected = {
            'customer': {
                'phone': '79990000000',
                'email': 'test@email.com',
            },
            'tax_system_code': 1,
            "internet": True,
            "timezone": 6,
            'items': [
                {
                    "description": "Product 1",
                    "quantity": "2.1",
                    "amount": {
                        "value": "250.00",
                        "currency": Currency.RUB
                    },
                    "vat_code": 2
                },
                {
                    "description": "Product 2",
                    "quantity": "1.0",
                    "amount": {
                        "value": "100.01",
                        "currency": Currency.RUB
                    },
                    "vat_code": 2,
                    "planned_status": 3,
                    'payment_subject': PaymentSubject.AGENT_COMMISSION,
                    'payment_mode': PaymentMode.ADVANCE,
                    "product_code": "00 00 00 01 00 21 FA 41 00 23 05 41 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 12 00 AB 00",
                    "country_of_origin_code": "RU",
                    "customs_declaration_number": "90/210",
                    "excise": "2.0",
                    "mark_code_info": {
                        "mark_code_raw": "010460406000590021N4N57RTCBUZTQ\\u001d2403054002410161218\\u001d1424010191ffd0\\u001g92tIAF/YVpU4roQS3M/m4z78yFq0nc/WsSmLeX6QkF/YVWwy5IMYAeiQ91Xa2m/fFSJcOkb2N+uUUtfr4n0mOX0Q==",
                        "gs_1m": "010460406000590021N4N57RTCBUZTQ"
                    },
                    "measure": ReceiptItemMeasure.PIECE,
                    "payment_subject_industry_details": [
                        {
                            "federal_id": "004",
                            "document_date": "2023-03-03",
                            "document_number": "21102023",
                            "value": "value",
                        }
                    ],
                    "mark_mode": "0",
                    "mark_quantity": {
                        "numerator": 5,
                        "denominator": 10
                    },
                }
            ],
            'receipt_industry_details': [
                {
                    'federal_id': '004',
                    'document_date': '2023-03-03',
                    'document_number': '21102023',
                    'value': 'value',
                }
            ],
            'receipt_operational_details': {
                'operation_id': 111,
                'value': 'Данные операции',
                'created_at': '2023-03-03T11:52:31.827Z',
            },
        }

        self.assertEqual(expected, dict(receipt))

        receipt.receipt_industry_details = [
            {
                'federal_id': '004',
                'document_date': '2023-03-03',
                'document_number': '21102023',
                'value': 'value',
            }
        ]
        receipt.receipt_operational_details = {
            'operation_id': 111,
            'value': 'Данные операции',
            'created_at': '2023-03-03T11:52:31.827Z',
        }

        self.assertEqual(expected, dict(receipt))

        customer = ReceiptCustomer({'phone': '79990000000', 'email': 'test@email.com', 'full_name': 'Merchant Big', 'inn': '770123456789'})
        self.assertEqual({'phone': '79990000000', 'email': 'test@email.com'}, dict(receipt.customer))
        self.assertEqual(dict(customer), {'phone': '79990000000', 'email': 'test@email.com', 'full_name': 'Merchant Big', 'inn': '770123456789'})

        with self.assertRaises(ValueError):
            customer.email = 'invalid email'

        with self.assertRaises(TypeError):
            receipt.customer = 'invalid customer'

        with self.assertRaises(TypeError):
            receipt.tax_system_code = 'invalid type'

        with self.assertRaises(TypeError):
            receipt.internet = 'invalid type'

        with self.assertRaises(TypeError):
            receipt.timezone = 'invalid type'

        with self.assertRaises(TypeError):
            receipt.receipt_industry_details = 'invalid receipt_industry_details'

        with self.assertRaises(TypeError):
            receipt.receipt_industry_details = ['invalid receipt_industry_details']

        with self.assertRaises(TypeError):
            receipt.receipt_operational_details = 'invalid receipt_operational_details'

        with self.assertRaises(TypeError):
            receipt.items = 'invalid items'

        with self.assertRaises(TypeError):
            receipt.items = [
                'invalid item value',
                {
                    "description": "Product 2",
                    "quantity": 1.0,
                    "amount": {
                        "value": 100.0,
                        "currency": Currency.RUB
                    },
                    "vat_code": 2,
                    "payment_subject": PaymentSubject.AGENT_COMMISSION,
                    "payment_mode": PaymentMode.ADVANCE,
                    "product_code": "00 00 00 01 00 21 FA 41 00 23 05 41 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 12 00 AB 00",
                    "country_of_origin_code": "RU",
                    "customs_declaration_number": "90/210",
                    "excise": 2.00,
                }
            ]

        receipt_item = ReceiptItem()

        with self.assertRaises(TypeError):
            receipt_item.mark_quantity = 'invalid mark_quantity'

        with self.assertRaises(TypeError):
            receipt_item.mark_code_info = 'invalid mark_code_info'

        with self.assertRaises(ValueError):
            receipt_item.mark_mode = 'invalid mark_mode'

        with self.assertRaises(TypeError):
            receipt_item.payment_subject_industry_details = ['invalid payment_subject_industry_details']

        with self.assertRaises(TypeError):
            receipt_item.payment_subject_industry_details = 'invalid payment_subject_industry_details'

    def test_receipt_item(self):
        receipt_item = ReceiptItem()
        receipt_item.description = "Product"
        receipt_item.quantity = 1.0
        receipt_item.amount = Amount({
            "value": 100.0,
            "currency": Currency.RUB
        })
        receipt_item.vat_code = 2
        receipt_item.planned_status = 4
        receipt_item.payment_subject = PaymentSubject.AGENT_COMMISSION
        receipt_item.payment_mode = PaymentMode.ADVANCE
        receipt_item.product_code = '00 00 00 01 00 21 FA 41 00 23 05 41 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 12 00 AB 00'
        receipt_item.country_of_origin_code = "RU"
        receipt_item.customs_declaration_number = "90/210"
        receipt_item.excise = 2.00
        receipt_item.mark_code_info = MarkCodeInfo({
            "mark_code_raw": "010460406000590021N4N57RTCBUZTQ\\u001d2403054002410161218\\u001d1424010191ffd0\\u001g92tIAF/YVpU4roQS3M/m4z78yFq0nc/WsSmLeX6QkF/YVWwy5IMYAeiQ91Xa2m/fFSJcOkb2N+uUUtfr4n0mOX0Q==",
            "gs_1m": "010460406000590021N4N57RTCBUZTQ"
        })
        receipt_item.measure = ReceiptItemMeasure.PIECE
        receipt_item.payment_subject_industry_details = [
            IndustryDetails({
                "federal_id": "004",
                "document_date": "2023-03-03",
                "document_number": "21102023",
                "value": "value",
            })
        ]
        receipt_item.mark_mode = "0"
        receipt_item.mark_quantity = MarkQuantity({
            "numerator": 5,
            "denominator": 10
        })

        self.assertEqual({
            "description": "Product",
            "quantity": "1.0",
            "amount": {
                "value": "100.00",
                "currency": Currency.RUB
            },
            "vat_code": 2,
            "planned_status": 4,
            "payment_subject": PaymentSubject.AGENT_COMMISSION,
            "payment_mode": PaymentMode.ADVANCE,
            "product_code": "00 00 00 01 00 21 FA 41 00 23 05 41 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 12 00 AB 00",
            "country_of_origin_code": "RU",
            "customs_declaration_number": "90/210",
            "excise": "2.0",
            "mark_code_info": {
                "mark_code_raw": "010460406000590021N4N57RTCBUZTQ\\u001d2403054002410161218\\u001d1424010191ffd0\\u001g92tIAF/YVpU4roQS3M/m4z78yFq0nc/WsSmLeX6QkF/YVWwy5IMYAeiQ91Xa2m/fFSJcOkb2N+uUUtfr4n0mOX0Q==",
                "gs_1m": "010460406000590021N4N57RTCBUZTQ"
            },
            "measure": ReceiptItemMeasure.PIECE,
            "payment_subject_industry_details": [
                {
                    "federal_id": "004",
                    "document_date": "2023-03-03",
                    "document_number": "21102023",
                    "value": "value",
                }
            ],
            "mark_mode": "0",
            "mark_quantity": {
                "numerator": 5,
                "denominator": 10
            },
        }, dict(receipt_item))

        with self.assertRaises(TypeError):
            receipt_item.amount = 'invalid amount'

    def test_decimal_calc(self):
        receipt = Receipt()
        receipt.customer = ReceiptCustomer({
            'phone': '79990000000',
            'email': 'test@email.com'
        })
        receipt.tax_system_code = 1
        receipt.items = [
            {
                "description": "Product 1",
                "quantity": '2.1',
                "amount": {
                    "value": 250.0,
                    "currency": Currency.RUB
                },
                "vat_code": "2"
            },
            {
                "description": "Product 2",
                "quantity": 1.0,
                "amount": {
                        "value": '100.01',
                        "currency": Currency.RUB
                    },
                "vat_code": "2"
            }
        ]

        summ = round(receipt.items[0].amount.value * receipt.items[0].quantity, 2)
        self.assertEqual(Decimal('525.00'), Decimal(summ))

        summ = round(receipt.items[1].amount.value * receipt.items[1].quantity, 2)
        self.assertEqual(Decimal('100.01'), Decimal(summ))
