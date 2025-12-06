# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.common.confirmation_type import ConfirmationType
from yookassa.domain.common.payment_method_type import PaymentMethodType
from yookassa.domain.models.payment_data.payment_order.payment_order import PaymentOrder
from yookassa.domain.models.payment_data.payment_order.request.payment_order_utilities import PaymentOrderUtilities
from yookassa.domain.models.payment_data.request.airline import Airline
from yookassa.domain.models.amount import Amount
from yookassa.domain.models.confirmation.confirmation import Confirmation
from yookassa.domain.models.confirmation.request.confirmation_redirect import ConfirmationRedirect
from yookassa.domain.models.currency import Currency
from yookassa.domain.models.deal import PaymentDealInfo
from yookassa.domain.models.payment_data.payment_data import PaymentData
from yookassa.domain.models.payment_data.request.fraud_data import FraudData
from yookassa.domain.models.payment_data.request.payment_data_tinkoff_bank import PaymentDataTinkoffBank
from yookassa.domain.models.payment_data.request.receiver import Receiver, ReceiverBankAccount
from yookassa.domain.models.payment_data.statement import StatementType
from yookassa.domain.models.payment_data.statement.delivery_method.delivery_method_type import DeliveryMethodType
from yookassa.domain.models.payment_data.statement.delivery_method.request.delivery_method_email import \
    DeliveryMethodEmail
from yookassa.domain.models.payment_data.statement.request.statement_payment_overview import StatementPaymentOverview
from yookassa.domain.models.receipt import Receipt
from yookassa.domain.models.payment_data.recipient import Recipient
from yookassa.domain.models.settlement import SettlementPayoutType, Settlement
from yookassa.domain.models.transfer import Transfer
from yookassa.domain.request.payment_request import PaymentRequest


class TestPaymentRequest(unittest.TestCase):

    def test_request_cast(self):
        self.maxDiff = None
        request = PaymentRequest()
        request.amount = Amount({'value': 0.1, 'currency': Currency.RUB})
        request.description = 'Test description'
        request.recipient = Recipient({
            'account_id': '213',
            'gateway_id': '123'
        })
        request.save_payment_method = True
        request.capture = False
        request.payment_method_data = PaymentDataTinkoffBank()
        request.receipt = Receipt({
            'phone': '79990000000', 'email': 'test@email.com', 'tax_system_code': 1,
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
        })
        request.airline = Airline({
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
        })
        request.payment_method_id = '123'
        request.payment_token = '99091209012'
        request.confirmation = ConfirmationRedirect({'locale': 'ru_RU', 'return_url': 'return.url'})
        request.client_ip = '192.0.0.0'
        request.metadata = {'key': 'value'}
        request.transfers.append(Transfer({
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
        }))
        request.deal = PaymentDealInfo({
            'id': 'dl-28646d17-0022-5000-8000-01e154d1324b',
            'settlements': [
                {
                    "type": SettlementPayoutType.PAYOUT,
                    "amount": {
                        "value": "40.00",
                        "currency": Currency.RUB
                    }
                },
                Settlement({
                    "type": SettlementPayoutType.PAYOUT,
                    "amount": {
                        "value": "40.00",
                        "currency": Currency.RUB
                    }
                })
            ]
        })
        request.fraud_data = FraudData({
            'topped_up_phone': '79990000000',
            'merchant_customer_bank_account': {
                "account_number": '12345678901234567890',
                "bic": '123456789'
            }
        })
        request.merchant_customer_id = '79990001122'
        request.receiver = ReceiverBankAccount({
            "account_number": '12345678901234567890',
            "bic": '123456789'
        })
        request.payment_order = PaymentOrderUtilities({
            "amount": {"value": "100.00", "currency": "RUB"},
            "payment_purpose": "Оплата ЖКУ за июль 2023",
            "recipient": {
                "name": "ООО УК Жилфонд",
                "inn": "1234567890",
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
        request.statements = [
            StatementPaymentOverview({
                "delivery_method": DeliveryMethodEmail({
                    "email": "test@test.ru"
                })
            }),
            {
                "type": StatementType.PAYMENT_OVERVIEW,
                "delivery_method": {
                    "type": DeliveryMethodType.EMAIL,
                    "email": "admin@test.ru"
                }
            }
        ]

        self.assertEqual({
            'amount': {'value': '0.10', 'currency': Currency.RUB},
            'recipient': {
                'account_id': '213',
                'gateway_id': '123'
            },
            'description': 'Test description',
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
            'confirmation': {'type': ConfirmationType.REDIRECT, 'locale': 'ru_RU', 'return_url': 'return.url'},
            'client_ip': '192.0.0.0',
            'metadata': {'key': 'value'},
            "airline": {
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
            'transfers': [
                {
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
                }
            ],
            'deal': {
                'id': 'dl-28646d17-0022-5000-8000-01e154d1324b',
                'settlements': [
                    {
                        'type': 'payout',
                        'amount': {
                            'value': '40.00',
                            'currency': 'RUB'
                        }
                    },
                    {
                        "type": SettlementPayoutType.PAYOUT,
                        "amount": {
                            "value": "40.00",
                            "currency": Currency.RUB
                        }
                    }
                ]
            },
            'fraud_data': {
                'topped_up_phone': '79990000000',
                'merchant_customer_bank_account': {
                    "account_number": '12345678901234567890',
                    "bic": '123456789'
                }
            },
            'merchant_customer_id': '79990001122',
            'receiver': {
                "type": "bank_account",
                "account_number": '12345678901234567890',
                "bic": '123456789'
            },
            'payment_order': {
                "type": "utilities",
                "amount": {"value": "100.00", "currency": "RUB"},
                "payment_purpose": "Оплата ЖКУ за июль 2023",
                "recipient": {
                    "name": "ООО УК Жилфонд",
                    "inn": "1234567890",
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

    def test_request_setters(self):
        request = PaymentRequest({
            'amount': {'value': '0.10', 'currency': Currency.RUB},
            'recipient': {
                'account_id': '213',
                'gateway_id': '123'
            },
            'save_payment_method': True,
            'capture': False,
            'payment_method_data': {'type': PaymentMethodType.ELECTRONIC_CERTIFICATE},
            'receipt': {
                'phone': '79990000000',
                'email': 'test@email.com',
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
            'confirmation': {'type': ConfirmationType.MOBILE_APPLICATION, 'return_url': 'return.url'},
            'client_ip': '192.0.0.0',
            "airline": {
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
            'transfers': [
                {
                    'account_id': '79990000000',
                    "amount": {
                        "value": "100.01",
                        "currency": Currency.RUB
                    },
                    "platform_fee_amount": Amount({
                        "value": "10.01",
                        "currency": Currency.RUB
                    }),
                    "description": "Test description",
                    "metadata": {
                        "meta1": 'metatest 1',
                        "meta2": 'metatest 2'
                    }
                }
            ],
            'metadata': {'key': 'value'},
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
            'fraud_data': {
                'topped_up_phone': '79990000000',
                'merchant_customer_bank_account': {
                    "account_number": '12345678901234567890',
                    "bic": '123456789'
                }
            },
            'merchant_customer_id': '79990001122',
            'receiver': {
                "type": "bank_account",
                "account_number": '12345678901234567890',
                "bic": '123456789'
            },
            'payment_order': {
                "type": "utilities",
                "amount": {"value": "100.00", "currency": "RUB"},
                "payment_purpose": "Оплата ЖКУ за июль 2023",
                "recipient": {
                    "name": "ООО УК Жилфонд",
                    "inn": "1234567890",
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
        })

        self.assertIsInstance(request.confirmation, Confirmation)
        self.assertIsInstance(request.amount, Amount)
        self.assertIsInstance(request.receipt, Receipt)
        self.assertIsInstance(request.recipient, Recipient)
        self.assertIsInstance(request.payment_method_data, PaymentData)
        self.assertIsInstance(request.airline, Airline)
        self.assertIsInstance(request.transfers, list)
        self.assertIsInstance(request.deal, PaymentDealInfo)
        self.assertIsInstance(request.fraud_data, FraudData)
        self.assertIsInstance(request.receiver, Receiver)
        self.assertIsInstance(request.payment_order, PaymentOrder)
        self.assertIsInstance(request.statements, list)

        with self.assertRaises(TypeError):
            request.receipt = 'invalid receipt'

        with self.assertRaises(TypeError):
            request.amount = 'invalid amount'

        with self.assertRaises(TypeError):
            request.recipient = 'invalid recipient'

        with self.assertRaises(TypeError):
            request.confirmation = 'invalid confirmation'

        with self.assertRaises(TypeError):
            request.payment_method_data = 'invalid payment_method_data'

        with self.assertRaises(TypeError):
            request.payment_token = ''

        with self.assertRaises(ValueError):
            request.description = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                                  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

        with self.assertRaises(TypeError):
            request.airline = 'Invalid airline'

        with self.assertRaises(TypeError):
            request.transfers = 'Invalid transfers'

        with self.assertRaises(TypeError):
            request.fraud_data = 'Invalid fraud_data'

        with self.assertRaises(TypeError):
            request.deal = 'Invalid deal_data'

        with self.assertRaises(ValueError):
            request.merchant_customer_id = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                                           'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                                           'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

        with self.assertRaises(TypeError):
            request.deal.settlements[0].amount = 'invalid data'

        with self.assertRaises(TypeError):
            request.receiver = 'Invalid receiver'

        with self.assertRaises(TypeError):
            request.payment_order = 'Invalid payment_order'

        with self.assertRaises(TypeError):
            request.statements = 'Invalid statements data type in payment_request.statements'

    def test_request_validate(self):
        request = PaymentRequest()

        with self.assertRaises(ValueError):
            request.validate()

        request.amount = Amount({'value': 0.0, 'currency': Currency.RUB})

        with self.assertRaises(ValueError):
            request.validate()

        request.amount = Amount({'value': 0.1, 'currency': Currency.RUB})

        request.receipt = {
            'customer': {'full_name': 'Ivanov Ivan Ivanovich'},
            'items': [
                {
                    "description": "Product 1",
                    "quantity": 2.0,
                    "amount": {
                        "value": 250.0,
                        "currency": Currency.RUB
                    },
                }
            ]}

        with self.assertRaises(ValueError):
            request.validate()

        request.receipt = {'phone': '79990000000', 'items': [
            {
                "description": "Product 1",
                "quantity": 2.0,
                "amount": {
                    "value": 250.0,
                    "currency": Currency.RUB
                },
            },
            {
                "description": "Product 2",
                "quantity": 1.0,
                "amount": {
                    "value": 100.0,
                    "currency": Currency.RUB
                },
            }
        ]}
        with self.assertRaises(ValueError):
            request.validate()

        request.receipt = {'tax_system_code': 1, 'items': [
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
        ]}
        with self.assertRaises(ValueError):
            request.validate()

        request.transfers = None
        with self.assertRaises(ValueError):
            request.validate()

        with self.assertRaises(TypeError):
            request.deal = {
                'id': 'dl-28646d17-0022-5000-8000-01e154d1324b',
                'settlements': ['invalid data']
            }

        request = PaymentRequest()
        request.amount = Amount({'value': 0.1, 'currency': Currency.RUB})
        request.payment_token = '123'
        request.payment_method_id = '123'
        with self.assertRaises(ValueError):
            request.validate()

        request = PaymentRequest()
        request.amount = Amount({'value': 0.1, 'currency': Currency.RUB})
        request.payment_token = '123'
        request.payment_method_data = PaymentDataTinkoffBank()
        with self.assertRaises(ValueError):
            request.validate()

        request = PaymentRequest()
        request.amount = Amount({'value': 0.1, 'currency': Currency.RUB})
        request.payment_method_id = '123'
        request.payment_method_data = PaymentDataTinkoffBank()
        with self.assertRaises(ValueError):
            request.validate()
