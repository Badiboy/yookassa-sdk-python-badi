# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.common.receipt_type import ReceiptType
from yookassa.domain.models.currency import Currency
from yookassa.domain.models.receipt_data.additional_user_props import AdditionalUserProps
from yookassa.domain.models.receipt_data.industry_details import IndustryDetails
from yookassa.domain.models.receipt_data.operational_details import OperationalDetails
from yookassa.domain.models.settlement import Settlement, SettlementType
from yookassa.domain.request.receipt_request_builder import ReceiptRequestBuilder


class TestReceiptRequestBuilder(unittest.TestCase):

    def test_build_object(self):
        self.maxDiff = None
        builder = ReceiptRequestBuilder()
        builder.set_customer({'phone': '79990000000', 'email': 'test@email.com'}) \
            .set_phone("79990000000") \
            .set_email("test@email.com") \
            .set_type(ReceiptType.PAYMENT) \
            .set_send(True) \
            .set_internet(True) \
            .set_tax_system_code(1) \
            .set_items([
                {
                    "description": "Product 1",
                    "quantity": 2.0,
                    "amount": {
                        "value": 250.0,
                        "currency": Currency.RUB
                    },
                    "vat_code": 2
                },
                {
                    "description": "Product 2",
                    "quantity": 1.0,
                    "amount": {
                        "value": 100.0,
                        "currency": Currency.RUB
                    },
                    "vat_code": 2
                }
            ]) \
            .set_settlements([
                Settlement({
                    'type': SettlementType.CASHLESS,
                    'amount': {
                        'value': 350.0,
                        'currency': Currency.RUB
                    }
                })
            ]) \
            .set_payment_id('215d8da0-000f-50be-b000-0003308c89be') \
            .set_on_behalf_of(123456) \
            .set_timezone(10) \
            .set_receipt_operational_details(OperationalDetails({
                'operation_id': 111,
                'value': 'Данные операции',
                'created_at': '2023-03-03T11:52:31.827Z',
            })) \
            .set_receipt_industry_details([
                IndustryDetails({
                    'federal_id': '004',
                    'document_date': '2023-03-03',
                    'document_number': '21102023',
                    'value': 'value',
                })
            ]) \
            .set_additional_user_props(AdditionalUserProps({
                'name': 'name',
                'value': 'value',
            })) \
            .set_refund_id('215d8da0-000f-50be-b000-0003308c89be')

        request = builder.build()

        self.assertEqual({
            'customer': {'email': 'test@email.com', 'phone': '79990000000'},
            'type': 'payment',
            'send': True,
            'internet': True,
            'tax_system_code': 1,
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
                    'vat_code': 2
                },
                {
                    'description': 'Product 2',
                    'quantity': '1.0',
                    'amount': {
                        'value': '100.00',
                        'currency': Currency.RUB
                    },
                    'vat_code': 2
                }
            ],
            'settlements': [
                {
                    'type': 'cashless',
                    'amount': {
                        'value': '350.00',
                        'currency': 'RUB'
                    }
                }
            ],
            'refund_id': '215d8da0-000f-50be-b000-0003308c89be',
            'on_behalf_of': '123456',
            'timezone': 10,
            'receipt_operational_details': {
                'operation_id': 111,
                'value': 'Данные операции',
                'created_at': '2023-03-03T11:52:31.827Z',
            },
            'receipt_industry_details': [
                {
                    'federal_id': '004',
                    'document_date': '2023-03-03',
                    'document_number': '21102023',
                    'value': 'value',
                }
            ],
            'additional_user_props': {
                'name': 'name',
                'value': 'value',
            }
        }, dict(request))
