# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.common.confirmation_type import ConfirmationType
from yookassa.domain.common.payment_method_type import PaymentMethodType
from yookassa.domain.models.currency import Currency
from yookassa.domain.models.settlement import SettlementPayoutType
from yookassa.domain.request.payment_request_builder import PaymentRequestBuilder


class TestPaymentRequestBuilder(unittest.TestCase):

    def test_build_object(self):
        self.maxDiff = None
        request = None
        builder = PaymentRequestBuilder()
        builder.set_payment_order({
            "type": "utilities",
            "amount": {"value": "600.00", "currency": "RUB"},
            "payment_purpose": "Оплата ЖКУ за июль 2023",
            "recipient": {
                "name": "ООО УК Жилфонд",
                "inn": "6321341814",
                "kpp": "987654321",
                "bank": {
                    "name": "ПАО Сбербанк",
                    "bic": "044525225",
                    "account": "40702810000000000001",
                    "correspondent_account": "30101810400000000225"
                }
            },
            "kbk": "18210102000011000110",
            "oktmo": "45382000",
            "payment_period": {"month": 7, "year": 2023},
            "payment_document_id": "123456789012345678",
            "payment_document_number": "123-456",
            "account_number": "1234567890",
            "unified_account_number": "1234567890",
            "service_id": "1234567890123"
        })
        builder.set_statements(
            [
                {
                    "type": "payment_overview",
                    "delivery_method": {
                        "type": "email",
                        "email": "test@test.ru"
                    }
                },
                {
                    "type": "payment_overview",
                    "delivery_method": {
                         "type": "email",
                        "email": "admin@test.ru"
                    }
                }
            ]
        )

        builder.set_receipt({
            'phone': '79990000000',
            'email': 'test@email.com',
            'tax_system_code': 1,
            'items': [
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
            ]}) \
            .set_description('Оплата заказа №37') \
            .set_amount({'value': 0.1, 'currency': Currency.RUB}) \
            .set_recipient({'account_id': '213', 'gateway_id': '123'}) \
            .set_capture(False) \
            .set_save_payment_method(True) \
            .set_confirmation({'type': ConfirmationType.REDIRECT, 'return_url': 'return.url'}) \
            .set_payment_method_data({'type': PaymentMethodType.TINKOFF_BANK}) \
            .set_client_ip('192.0.0.0') \
            .set_payment_method_id('123') \
            .set_payment_token('99091209012') \
            .set_metadata({'key': 'value'}) \
            .set_transfers([
                {
                    'account_id': '79990000000',
                    "amount": {
                        "value": 100.01,
                        "currency": Currency.RUB
                    },
                    "platform_fee_amount": {
                        "value": 10.01,
                        "currency": Currency.RUB
                    },
                    "description": "Test description",
                    "metadata": {
                        "meta1": 'metatest 1',
                        "meta2": 'metatest 2'
                    }
                }
            ]) \
            .set_deal({
                'id': 'dl-28646d17-0022-5000-8000-01e154d1324b',
                'settlements': [
                    {
                        "type": SettlementPayoutType.PAYOUT,
                        "amount": {
                            "value": "80.00",
                            "currency": Currency.RUB
                        }
                    }
                ]
            }) \
            .set_airline({
                'booking_reference': '123123',
                'ticket_number': '5551238432721',
                'passengers': [
                    {
                        'first_name': 'Joe',
                        'last_name': 'Doe'
                    }
                ],
                'legs': [
                    {
                        'departure_airport': 'IVA',
                        'destination_airport': 'NYC',
                        'departure_date': '2017-01-02'
                    }
                ]
            }) \
            .set_fraud_data({
                'topped_up_phone': '79990001122',
                'merchant_customer_bank_account': {
                    'account_number': '12345678901234567890',
                    'bic': '123456789',
                }
            }) \
            .set_merchant_customer_id('79990001122')

        request = builder.build()

        self.assertEqual({
            'description': 'Оплата заказа №37',
            'amount': {'value': '0.10', 'currency': Currency.RUB},
            'recipient': {
                'account_id': '213',
                'gateway_id': '123'
            },
            'save_payment_method': True,
            'capture': False,
            'payment_method_data': {'type': PaymentMethodType.TINKOFF_BANK},
            'receipt': {
                'customer': {'email': 'test@email.com', 'phone': '79990000000'},
                'tax_system_code': 1,
                'items': [
                    {
                        "description": "Product 1",
                        "quantity": "2.0",
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
                            "value": "100.00",
                            "currency": Currency.RUB
                        },
                        "vat_code": 2
                    }
                ]},
            'payment_method_id': '123',
            'payment_token': '99091209012',
            'confirmation': {'type': ConfirmationType.REDIRECT, 'return_url': 'return.url'},
            'client_ip': '192.0.0.0',
            'metadata': {'key': 'value'},
            'transfers': [{
                'account_id': '79990000000',
                "amount": {
                    "value": "100.01",
                    "currency": Currency.RUB
                },
                "platform_fee_amount": {
                    "value": "10.01",
                    "currency": Currency.RUB
                },
                "description": "Test description",
                "metadata": {
                    "meta1": 'metatest 1',
                    "meta2": 'metatest 2'
                }
            }],
            'deal': {
                'id': 'dl-28646d17-0022-5000-8000-01e154d1324b',
                'settlements': [{
                    'type': 'payout',
                    'amount': {
                        'value': "80.00",
                        'currency': 'RUB'
                    }
                }]
            },
            'airline': {
                'booking_reference': '123123',
                'ticket_number': '5551238432721',
                'passengers': [
                    {
                        'first_name': 'Joe',
                        'last_name': 'Doe'
                    }
                ],
                'legs': [
                    {
                        'departure_airport': 'IVA',
                        'destination_airport': 'NYC',
                        'departure_date': '2017-01-02'
                    }
                ]
            },
            'fraud_data': {
                'topped_up_phone': '79990001122',
                'merchant_customer_bank_account': {
                    'account_number': '12345678901234567890',
                    'bic': '123456789',
                }
            },
            'merchant_customer_id': '79990001122',
            'payment_order': {
                "type": "utilities",
                "amount": {
                    "value": "600.00",
                    "currency": "RUB"
                },
                "payment_purpose": "Оплата ЖКУ за июль 2023",
                "recipient": {
                    "name": "ООО УК Жилфонд",
                    "inn": "6321341814",
                    "kpp": "987654321",
                    "bank": {
                        "name": "ПАО Сбербанк",
                        "bic": "044525225",
                        "account": "40702810000000000001",
                        "correspondent_account": "30101810400000000225"
                    }
                },
                "kbk": "18210102000011000110",
                "oktmo": "45382000",
                "payment_period": {
                    "month": 7,
                    "year": 2023
                },
                "payment_document_id": "123456789012345678",
                "payment_document_number": "123-456",
                "account_number": "1234567890",
                "unified_account_number": "1234567890",
                "service_id": "1234567890123"
            },
            'statements': [
                {
                    "type": "payment_overview",
                    "delivery_method": {
                        "type": "email",
                        "email": "test@test.ru"
                    }
                },
                {
                    "type": "payment_overview",
                    "delivery_method": {
                        "type": "email",
                        "email": "admin@test.ru"
                    }
                }
            ]
        }, dict(request))
