# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.common import ReceiptItemAgentType
from yookassa.domain.models import Currency, ReceiptItemSupplier
from yookassa.domain.models.receipt_data.mark_code_info import MarkCodeInfo
from yookassa.domain.models.receipt_data.mark_quantity import MarkQuantity
from yookassa.domain.models.receipt_data.operational_details import OperationalDetails
from yookassa.domain.models.receipt_data.receipt_item import PaymentMode, PaymentSubject, ReceiptItemMeasure
from yookassa.domain.models.settlement import Settlement, SettlementType
from yookassa.domain.response.receipt_item_response import ReceiptItemResponse
from yookassa.domain.response.receipt_response import ReceiptResponse


class TestReceiptResponse(unittest.TestCase):

    def test_response_cast_payment(self):
        response = ReceiptResponse({
            "id": "rt_1da5c87d-0984-50e8-a7f3-8de646dd9ec9",
            "type": "payment",
            "payment_id": "215d8da0-000f-50be-b000-0003308c89be",
            "status": "succeeded",
            "fiscal_document_number": "3986",
            "fiscal_storage_number": "9288000100115785",
            "fiscal_attribute": "2617603921",
            "registered_at": "2019-05-13T17:56:00.000+03:00",
            "fiscal_provider_id": "fd9e9404-eaca-4000-8ec9-dc228ead2345",
            "tax_system_code": 1,
            "internet": True,
            "timezone": 1,
            "items": [
                {
                    "description": "Capybara",
                    "quantity": 5,
                    "amount": {
                        "value": "2500.50",
                        "currency": "RUB"
                    },
                    "vat_code": 2,
                    "planned_status": 5,
                    "payment_mode": PaymentMode.FULL_PAYMENT,
                    "payment_subject": PaymentSubject.COMMODITY,
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
                    "mark_mode": 0,
                    "mark_quantity": {
                        "numerator": 5,
                        "denominator": 10
                    },
                },
                {
                    "description": "Capybara",
                    "quantity": 5,
                    "amount": {
                        "value": "2500.50",
                        "currency": "RUB"
                    },
                    "vat_code": 2,
                    "payment_mode": PaymentMode.FULL_PAYMENT,
                    "payment_subject": PaymentSubject.COMMODITY,
                    "supplier": None,
                    "mark_code_info": None,
                    "payment_subject_industry_details": None,
                    "mark_quantity": None,
                },
            ],
            "settlements": None,
            "receipt_industry_details": [
                {
                    'federal_id': '004',
                    'document_date': '2023-03-03',
                    'document_number': '21102023',
                    'value': 'value',
                }
            ],
            "receipt_operational_details": {
                'operation_id': 111,
                'value': 'Данные операции',
                'created_at': '2023-03-03T11:52:31.827Z',
            }
        })

        self.assertIsInstance(response.items, list)
        self.assertIsInstance(response.items[0], ReceiptItemResponse)
        self.assertIsInstance(response.settlements, list)
        self.assertIsInstance(response.receipt_industry_details, list)
        self.assertIsInstance(response.receipt_operational_details, OperationalDetails)

        self.assertEqual(response.id, 'rt_1da5c87d-0984-50e8-a7f3-8de646dd9ec9')
        self.assertEqual(response.type, 'payment')
        self.assertEqual(response.payment_id, '215d8da0-000f-50be-b000-0003308c89be')
        self.assertEqual(response.status, 'succeeded')
        self.assertEqual(response.receipt_registration, 'succeeded')
        self.assertEqual(response.fiscal_document_number, '3986')
        self.assertEqual(response.fiscal_storage_number, '9288000100115785')
        self.assertEqual(response.fiscal_attribute, '2617603921')
        self.assertEqual(response.registered_at, '2019-05-13T17:56:00.000+03:00')
        self.assertEqual(response.tax_system_code, 1)
        self.assertEqual(response.fiscal_provider_id, 'fd9e9404-eaca-4000-8ec9-dc228ead2345')
        self.assertEqual(response.internet, True)
        self.assertEqual(response.timezone, 1)

        self.assertEqual(response.items[0].description, 'Capybara')
        self.assertEqual(response.items[0].quantity, 5.0)
        self.assertEqual(response.items[0].amount.value, 2500.50)
        self.assertEqual(response.items[0].amount.currency, 'RUB')
        self.assertEqual(response.items[0].vat_code, 2)
        self.assertEqual(response.items[0].planned_status, 5)
        self.assertEqual(response.items[0].payment_mode, PaymentMode.FULL_PAYMENT)
        self.assertEqual(response.items[0].payment_subject, PaymentSubject.COMMODITY)

        self.assertIsInstance(response.items[0].supplier, ReceiptItemSupplier)
        self.assertIsInstance(response.items[0].mark_code_info, MarkCodeInfo)
        self.assertIsInstance(response.items[0].payment_subject_industry_details, list)
        self.assertIsInstance(response.items[0].mark_quantity, MarkQuantity)

        self.assertEqual(response.items[0].country_of_origin_code, "RU")
        self.assertEqual(response.items[0].customs_declaration_number, "10714040/140917/0090376")
        self.assertEqual(response.items[0].excise, 20.00)
        self.assertEqual(response.items[0].agent_type, ReceiptItemAgentType.PAYMENT_AGENT)
        self.assertEqual(response.items[0].measure, ReceiptItemMeasure.PIECE)
        self.assertEqual(response.items[0].product_code, "44 4D 04 2F F7 5C 76 0C 4E 34 4E 35 37 52 54 43 42 55 5A 54 51")
        self.assertEqual(response.items[0].mark_mode, "0")

        self.assertIsNone(response.on_behalf_of)

        self.assertEqual(response.settlements.count(Settlement), 0)

    def test_response_cast_refund(self):
        response = ReceiptResponse({
            "id": "rt_1da5c87d-0984-50e8-a7f3-8de646dd9ec9",
            "type": "refund",
            "refund_id": "215d8da0-000f-50be-b000-0003308c89be",
            "fiscal_document_number": "3986",
            "fiscal_storage_number": "9288000100115785",
            "fiscal_attribute": "2617603921",
            "registered_at": "2019-05-13T17:56:00.000+03:00",
            "fiscal_provider_id": "fd9e9404-eaca-4000-8ec9-dc228ead2345",
            "tax_system_code": 1,
            "internet": False,
            "timezone": 3,
            "receipt_registration": 'succeeded',
            "items": None,
            "settlements": [
                {
                    "type": "cashless",
                    "amount": {
                        "value": "45.67",
                        "currency": "RUB"
                    }
                }
            ],
            "on_behalf_of": "string",
            "receipt_industry_details": None,
            "receipt_operational_details": None
        })

        self.assertIsInstance(response.items, list)
        self.assertIsInstance(response.settlements, list)
        self.assertIsInstance(response.settlements[0], Settlement)
        self.assertIsInstance(response.receipt_industry_details, list)

        self.assertEqual(response.id, 'rt_1da5c87d-0984-50e8-a7f3-8de646dd9ec9')
        self.assertEqual(response.type, 'refund')
        self.assertEqual(response.refund_id, '215d8da0-000f-50be-b000-0003308c89be')
        self.assertEqual(response.status, 'succeeded')
        self.assertEqual(response.receipt_registration, 'succeeded')
        self.assertEqual(response.fiscal_document_number, '3986')
        self.assertEqual(response.fiscal_storage_number, '9288000100115785')
        self.assertEqual(response.fiscal_attribute, '2617603921')
        self.assertEqual(response.registered_at, '2019-05-13T17:56:00.000+03:00')
        self.assertEqual(response.tax_system_code, 1)
        self.assertEqual(response.fiscal_provider_id, 'fd9e9404-eaca-4000-8ec9-dc228ead2345')
        self.assertEqual(response.on_behalf_of, 'string')
        self.assertEqual(response.receipt_operational_details, None)
        self.assertEqual(response.internet, False)
        self.assertEqual(response.timezone, 3)

        self.assertEqual(response.items.count(ReceiptItemResponse), 0)

        self.assertEqual(response.settlements[0].type, SettlementType.CASHLESS)
        self.assertEqual(float(response.settlements[0].amount.value), 45.67)
        self.assertEqual(response.settlements[0].amount.currency, Currency.RUB)
