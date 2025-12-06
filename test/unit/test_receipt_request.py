# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.common.receipt_type import ReceiptType, ReceiptItemAgentType
from yookassa.domain.models import Amount, Currency, ReceiptCustomer, ReceiptItemSupplier
from yookassa.domain.models.receipt_data.additional_user_props import AdditionalUserProps
from yookassa.domain.models.receipt_data.industry_details import IndustryDetails
from yookassa.domain.models.receipt_data.mark_code_info import MarkCodeInfo
from yookassa.domain.models.receipt_data.mark_quantity import MarkQuantity
from yookassa.domain.models.receipt_data.operational_details import OperationalDetails
from yookassa.domain.models.receipt_data.receipt_item import ReceiptItemMeasure
from yookassa.domain.models.settlement import SettlementType, Settlement
from yookassa.domain.request.receipt_item_request import ReceiptItemRequest
from yookassa.domain.request.receipt_request import ReceiptRequest


class TestReceiptRequest(unittest.TestCase):

    def test_request_cast(self):
        request = ReceiptRequest()
        request.type = ReceiptType.PAYMENT
        request.send = True
        request.internet = True
        request.customer = ReceiptCustomer({'phone': '79990000000', 'email': 'test@email.com'})
        request.items = [
            ReceiptItemRequest({
                "description": "Product 1",
                "quantity": 2.0,
                "amount": {
                    "value": 250.0,
                    "currency": Currency.RUB
                },
                "vat_code": 2,
                "country_of_origin_code": "RU",
                "customs_declaration_number": "10714040/140917/0090376",
                "excise": "20.00",
                "supplier": {
                    "name": "Поставщик денег",
                    "phone": "79000000000",
                    "inn": "770055684973",
                },
                "agent_type": ReceiptItemAgentType.PAYMENT_AGENT,
                "mark_code_info": {
                    "mark_code_raw": "010460406000590021N4N57RTCBUZTQ\\u001d2403054002410161218\\u001d1424010191ffd0\\u001g92tIAF/YVpU4roQS3M/m4z78yFq0nc/WsSmLeX6QkF/YVWwy5IMYAeiQ91Xa2m/fFSJcOkb2N+uUUtfr4n0mOX0Q==",
                    "gs_1m": "010460406000590021N4N57RTCBUZTQ"
                },
                "planned_status": 6,
                "measure": ReceiptItemMeasure.PIECE,
                "payment_subject_industry_details": [
                    {
                        "federal_id": "004",
                        "document_date": "2023-03-03",
                        "document_number": "21102023",
                        "value": "value",
                    }
                ],
                "product_code": "44 4D 04 2F F7 5C 76 0C 4E 34 4E 35 37 52 54 43 42 55 5A 54 51",
                "mark_mode": "0",
                "mark_quantity": {
                    "numerator": 5,
                    "denominator": 10
                },
            }),
            {
                "description": "Product 2",
                "quantity": 1.0,
                "amount": Amount({
                    "value": 100.0,
                    "currency": Currency.RUB
                }),
                "vat_code": 2,
                "country_of_origin_code": "RU",
                "customs_declaration_number": "10714040/140917/0090376",
                "excise": "20.00",
                "additional_payment_subject_props": "123",
                "supplier": ReceiptItemSupplier({
                    "name": "Поставщик денег",
                    "phone": "79000000000",
                    "inn": "770055684973",
                }),
                "agent_type": ReceiptItemAgentType.PAYMENT_AGENT,
                "mark_code_info": MarkCodeInfo({
                    "mark_code_raw": "010460406000590021N4N57RTCBUZTQ\\u001d2403054002410161218\\u001d1424010191ffd0\\u001g92tIAF/YVpU4roQS3M/m4z78yFq0nc/WsSmLeX6QkF/YVWwy5IMYAeiQ91Xa2m/fFSJcOkb2N+uUUtfr4n0mOX0Q==",
                    "gs_1m": "010460406000590021N4N57RTCBUZTQ"
                }),
                "planned_status": 6,
                "measure": ReceiptItemMeasure.PIECE,
                "payment_subject_industry_details": [
                    IndustryDetails({
                        "federal_id": "004",
                        "document_date": "2023-03-03",
                        "document_number": "21102023",
                        "value": "value",
                    })
                ],
                "product_code": "44 4D 04 2F F7 5C 76 0C 4E 34 4E 35 37 52 54 43 42 55 5A 54 51",
                "mark_mode": "0",
                "mark_quantity": MarkQuantity({
                    "numerator": 5,
                    "denominator": 10
                }),
            }
        ]
        request.settlements = [
            Settlement({
                'type': SettlementType.CASHLESS,
                'amount': {
                    'value': 250.0,
                    'currency': Currency.RUB
                }
            })
        ]
        request.tax_system_code = 1
        request.payment_id = '215d8da0-000f-50be-b000-0003308c89be'
        request.additional_user_props = AdditionalUserProps({
            'name': 'name',
            'value': 'value',
        })
        request.receipt_industry_details = [
            IndustryDetails({
                'federal_id': '004',
                'document_date': '2023-03-03',
                'document_number': '21102023',
                'value': 'value',
            })
        ]
        request.receipt_operational_details = OperationalDetails({
            'operation_id': 111,
            'value': 'Данные операции',
            'created_at': '2023-03-03T11:52:31.827Z',
        })
        request.timezone = 5

        self.assertEqual({
            'type': ReceiptType.PAYMENT,
            'send': True,
            'internet': True,
            'customer': {'email': 'test@email.com', 'phone': '79990000000'},
            'email': 'test@email.com',
            'phone': '79990000000',
            'items': [
                {
                    'description': 'Product 1',
                    'quantity': '2.0',
                    'amount': {
                        'value': '250.00',
                        'currency': Currency.RUB
                    },
                    'vat_code': 2,
                    "country_of_origin_code": "RU",
                    "customs_declaration_number": "10714040/140917/0090376",
                    "excise": "20.0",
                    "supplier": {
                        "name": "Поставщик денег",
                        "phone": "79000000000",
                        "inn": "770055684973",
                    },
                    "agent_type": ReceiptItemAgentType.PAYMENT_AGENT,
                    "mark_code_info": {
                        "mark_code_raw": "010460406000590021N4N57RTCBUZTQ\\u001d2403054002410161218\\u001d1424010191ffd0\\u001g92tIAF/YVpU4roQS3M/m4z78yFq0nc/WsSmLeX6QkF/YVWwy5IMYAeiQ91Xa2m/fFSJcOkb2N+uUUtfr4n0mOX0Q==",
                        "gs_1m": "010460406000590021N4N57RTCBUZTQ"
                    },
                    "planned_status": 6,
                    "measure": ReceiptItemMeasure.PIECE,
                    "payment_subject_industry_details": [
                        {
                            "federal_id": "004",
                            "document_date": "2023-03-03",
                            "document_number": "21102023",
                            "value": "value",
                        }
                    ],
                    "product_code": "44 4D 04 2F F7 5C 76 0C 4E 34 4E 35 37 52 54 43 42 55 5A 54 51",
                    "mark_mode": "0",
                    "mark_quantity": {
                        "numerator": 5,
                        "denominator": 10
                    },
                },
                {
                    'description': 'Product 2',
                    'quantity': '1.0',
                    'amount': {
                        'value': '100.00',
                        'currency': Currency.RUB
                    },
                    'vat_code': 2,
                    "country_of_origin_code": "RU",
                    "customs_declaration_number": "10714040/140917/0090376",
                    "excise": "20.0",
                    "additional_payment_subject_props": "123",
                    "supplier": {
                        "name": "Поставщик денег",
                        "phone": "79000000000",
                        "inn": "770055684973",
                    },
                    "agent_type": ReceiptItemAgentType.PAYMENT_AGENT,
                    "mark_code_info": {
                        "mark_code_raw": "010460406000590021N4N57RTCBUZTQ\\u001d2403054002410161218\\u001d1424010191ffd0\\u001g92tIAF/YVpU4roQS3M/m4z78yFq0nc/WsSmLeX6QkF/YVWwy5IMYAeiQ91Xa2m/fFSJcOkb2N+uUUtfr4n0mOX0Q==",
                        "gs_1m": "010460406000590021N4N57RTCBUZTQ"
                    },
                    "planned_status": 6,
                    "measure": ReceiptItemMeasure.PIECE,
                    "payment_subject_industry_details": [
                        {
                            "federal_id": "004",
                            "document_date": "2023-03-03",
                            "document_number": "21102023",
                            "value": "value",
                        }
                    ],
                    "product_code": "44 4D 04 2F F7 5C 76 0C 4E 34 4E 35 37 52 54 43 42 55 5A 54 51",
                    "mark_mode": "0",
                    "mark_quantity": {
                        "numerator": 5,
                        "denominator": 10
                    },
                }
            ],
            'settlements': [
                {
                    'type': SettlementType.CASHLESS,
                    'amount': {
                        'value': '250.00',
                        'currency': Currency.RUB
                    }
                }
            ],
            'tax_system_code': 1,
            'timezone': 5,
            'payment_id': '215d8da0-000f-50be-b000-0003308c89be',
            'additional_user_props': {
                'name': 'name',
                'value': 'value',
            },
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
        }, dict(request))

    def test_request_setters(self):
        request = ReceiptRequest({
            'type': ReceiptType.PAYMENT,
            'send': True,
            'internet': False,
            'email': 'test@email.com',
            'phone': '79990000000',
            'items': [
                {
                    'description': 'Product 1',
                    'quantity': 2.0,
                    'amount': Amount({
                        'value': 250.0,
                        'currency': Currency.RUB
                    }),
                    'vat_code': 2,
                    "planned_status": 6,
                    'payment_mode': 'full_payment',
                    'payment_subject': 'commodity',
                    'country_of_origin_code': 'CN',
                    'product_code': '00 00 00 01 00 21 FA 41 00 23 05 41 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 12 00 AB 00',
                    'customs_declaration_number': '10714040/140917/0090376',
                    'excise': '20.00',
                    'supplier': {
                        'name': 'string',
                        'phone': 'string',
                        'inn': 'string'
                    }
                },
                {
                    'description': 'Product 2',
                    'quantity': 1.0,
                    'amount': {
                        'value': 100.0,
                        'currency': Currency.RUB
                    },
                    'vat_code': 2,
                    'supplier': ReceiptItemSupplier({
                        'name': 'string',
                        'phone': 'string',
                        'inn': 'string'
                    })
                }
            ],
            'settlements': [
                {
                    'type': SettlementType.CASHLESS,
                    'amount': {
                        'value': 250.0,
                        'currency': Currency.RUB
                    }
                }
            ],
            'tax_system_code': 1,
            'timezone': 11,
            'payment_id': '215d8da0-000f-50be-b000-0003308c89be',
            'on_behalf_of': 'string',
            'additional_user_props': {
                'name': 'name',
                'value': 'value',
            },
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
        })

        self.assertIsInstance(request.customer, ReceiptCustomer)
        self.assertIsInstance(request.additional_user_props, AdditionalUserProps)
        self.assertIsInstance(request.receipt_operational_details, OperationalDetails)
        self.assertIsInstance(request.items, list)
        self.assertIsInstance(request.settlements, list)
        self.assertIsInstance(request.receipt_industry_details, list)
        self.assertIsInstance(request.internet, bool)
        self.assertIsInstance(request.timezone, int)

        with self.assertRaises(TypeError):
            request.items[0].supplier = 'invalid supplier'

        with self.assertRaises(TypeError):
            request.items[0].amount = 'invalid amount'

        with self.assertRaises(TypeError):
            request.items[0].mark_quantity = 'invalid mark_quantity'

        with self.assertRaises(TypeError):
            request.items[0].mark_code_info = 'invalid mark_code_info'

        with self.assertRaises(ValueError):
            request.items[0].mark_mode = 'invalid mark_mode'

        with self.assertRaises(ValueError):
            request.items[0].planned_status = 0

        with self.assertRaises(TypeError):
            request.items[0].payment_subject_industry_details = ['invalid payment_subject_industry_details']

        with self.assertRaises(TypeError):
            request.items[0].payment_subject_industry_details = 'invalid payment_subject_industry_details'

        with self.assertRaises(ValueError):
            request.items[0].additional_payment_subject_props = 'invalid additional_payment_subject_props_additional_payment_subject_props_additional_payment_subject_props'  # noqa: E501

        with self.assertRaises(TypeError):
            request.customer = 'invalid customer'

        with self.assertRaises(TypeError):
            request.items = 'invalid items'

        with self.assertRaises(TypeError):
            request.items = ['invalid item']

        with self.assertRaises(TypeError):
            request.settlements = 'invalid settlements'

        with self.assertRaises(TypeError):
            request.settlements = ['invalid settlement']

        with self.assertRaises(TypeError):
            request.send = 'invalid send'

        with self.assertRaises(TypeError):
            request.internet = 'invalid internet'

        with self.assertRaises(TypeError):
            request.timezone = 'invalid timezone'

        with self.assertRaises(TypeError):
            request.tax_system_code = 'invalid tax_system_code'

        with self.assertRaises(TypeError):
            request.additional_user_props = 'invalid additional_user_props'

        with self.assertRaises(TypeError):
            request.receipt_industry_details = 'invalid receipt_industry_details'

        with self.assertRaises(TypeError):
            request.receipt_industry_details = ['invalid receipt_industry_details']

        with self.assertRaises(TypeError):
            request.receipt_operational_details = 'invalid receipt_operational_details'

    def test_request_validate(self):
        request = ReceiptRequest()
        with self.assertRaises(ValueError):
            request.validate()

        request.type = ReceiptType.PAYMENT
        with self.assertRaises(ValueError):
            request.validate()

        request.send = True
        with self.assertRaises(ValueError):
            request.validate()

        request.phone = '79998887766'
        with self.assertRaises(ValueError):
            request.validate()

        request.customer = {}
        with self.assertRaises(ValueError):
            request.validate()

        request.customer = {}
        with self.assertRaises(ValueError):
            request.validate()

        request.customer = ReceiptCustomer({'phone': '79990000000', 'email': 'test@email.com'})
        with self.assertRaises(ValueError):
            request.validate()

        request.items = [
            ReceiptItemRequest({
                "description": "Product 1",
                "quantity": 2.0,
                "amount": {
                    "value": 250.0,
                    "currency": Currency.RUB
                },
                "vat_code": 2,
                "planned_status": 6,
            }),
            ReceiptItemRequest({
                "description": "Product 2",
                "quantity": 1.0,
                "amount": {
                    "value": 100.0,
                    "currency": Currency.RUB
                },
                "vat_code": 2,
                "planned_status": 6,
            })
        ]
        with self.assertRaises(ValueError):
            request.validate()

        request.settlements = [
            Settlement({
                'type': SettlementType.CASHLESS,
                'amount': {
                    'value': 250.0,
                    'currency': Currency.RUB
                }
            })
        ]
        with self.assertRaises(ValueError):
            request.validate()

        request.tax_system_code = 1
        with self.assertRaises(ValueError):
            request.validate()

        request.type = ReceiptType.REFUND
        with self.assertRaises(ValueError):
            request.validate()

        request.type = ReceiptType.PAYMENT
        request.refund_id = '215d8da0-000f-50be-b000-0003308c89be'
        with self.assertRaises(ValueError):
            request.validate()

        request.items = None
        with self.assertRaises(ValueError):
            request.validate()

        request.settlements = None
        with self.assertRaises(ValueError):
            request.validate()
