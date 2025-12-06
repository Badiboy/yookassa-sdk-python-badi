# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models.currency import Currency
from yookassa.domain.request.capture_payment_builder import CapturePaymentBuilder
from yookassa.domain.request.capture_payment_request import CapturePaymentRequest


class TestCapturePaymentBuilder(unittest.TestCase):
    def test_build_object(self):
        builder = CapturePaymentBuilder()
        builder \
            .set_amount({'value': 0.1, 'currency': Currency.RUB}) \
            .set_receipt({
                'phone': '79990000000', 'email': 'test@email.com',
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
                ]
            }) \
            .set_airline({
                "booking_reference": "IIIKRV",
                "passengers": [
                    {
                        "first_name": "SERGEI",
                        "last_name": "IVANOV"
                    }
                ],
                "legs": [
                    {
                        "departure_airport": "LED",
                        "destination_airport": "AMS",
                        "departure_date": "2018-06-20"
                    }
                ]
            }) \
            .set_transfers(None) \
            .set_deal({
                'id': 'dl-2909e77d-0022-5000-8000-0c37205b3208',
                'settlements': [
                    {
                        'type': 'payout',
                        'amount': {
                            'value': '100.00',
                            'currency': 'RUB',
                        },
                    },
                ],
            })

        request = builder.build()

        self.assertIsInstance(request, CapturePaymentRequest)
        self.assertEqual(
            {
                'amount': {'value': '0.10', 'currency': Currency.RUB},
                'receipt': {
                    'customer': {'phone': '79990000000', 'email': 'test@email.com'},
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
                    ],
                    'tax_system_code': 1
                },
                'airline': {
                    "booking_reference": "IIIKRV",
                    "passengers": [
                        {
                            "first_name": "SERGEI",
                            "last_name": "IVANOV"
                        }
                    ],
                    "legs": [
                        {
                            "departure_airport": "LED",
                            "destination_airport": "AMS",
                            "departure_date": "2018-06-20"
                        }
                    ]
                },
                'transfers': [],
                'deal': {
                    'id': 'dl-2909e77d-0022-5000-8000-0c37205b3208',
                    'settlements': [
                        {
                            'type': 'payout',
                            'amount': {
                                'value': '100.00',
                                'currency': 'RUB',
                            },
                        },
                    ],
                }
            }, dict(request))
