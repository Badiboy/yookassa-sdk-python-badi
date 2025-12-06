# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models import Settlement
from yookassa.domain.models.amount import Amount
from yookassa.domain.models.payment_data.electronic_certificate.electronic_certificate import ElectronicCertificate
from yookassa.domain.models.payment_data.electronic_certificate.electronic_certificate_approved_payment_article import \
    ElectronicCertificateApprovedPaymentArticle
from yookassa.domain.models.payment_data.response.authorization_details import AuthorizationDetails, ThreeDSecure
from yookassa.domain.models.cancellation_details import CancellationDetails
from yookassa.domain.models.confirmation.confirmation import Confirmation
from yookassa.domain.models.currency import Currency
from yookassa.domain.models.deal import PaymentDealInfo
from yookassa.domain.models.payment_data.card_type import CardType
from yookassa.domain.models.payment_data.response.credit_card import CreditCard
from yookassa.domain.models.payment_data.response.payment_data_bank_card import PaymentDataBankCard
from yookassa.domain.models.payment_data.response.payment_data_electronic_certificate import \
    PaymentDataElectronicCertificate
from yookassa.domain.models.payment_data.response.payment_data_sber_loan import PaymentDataSberLoan
from yookassa.domain.models.payment_data.response.payment_data_sberbank import PaymentDataSberbank
from yookassa.domain.models.payment_data.response.payment_data_unknown import PaymentDataUnknown
from yookassa.domain.models.payment_data.recipient import Recipient
from yookassa.domain.response.payment_response import PaymentResponse
from yookassa.domain.response.transfer_response import TransferStatus


class TestPaymentResponse(unittest.TestCase):

    def test_response_cast(self):
        self.maxDiff = None
        response = PaymentResponse({
            "id": "21b23365-000f-500b-9000-070fa3554403",
            "amount": {
                "value": "1000.00",
                "currency": "RUB"
            },
            "description": "Заказ №72",
            "confirmation": {
                "type": "redirect",
                "return_url": "https://test.test/test",
                "confirmation_url": "https://url",
                "enforce": False
            },
            "payment_method": {
                "type": "bank_card",
                "id": "21b23365-000f-500b-9000-070fa3554403",
                "saved": False
            },
            "status": "pending",
            "recipient": {
                "account_id": "67192",
                "gateway_id": "352780"
            },
            "refunded_amount": {
                "value": "1000.00",
                "currency": "RUB"
            },
            "receipt_registration": "pending",
            "created_at": "2017-11-30T15:11:33+00:00",
            "expires_at": "2017-11-30T15:11:33+00:00",
            "captured_at": "2017-11-30T15:11:33+00:00",
            "paid": False,
            "refundable": False,
            "test": False,
            "metadata": {
                "float_value": "123.32",
                "key": "data"
            },
            "cancellation_details": {
                "party": "yoo_money",
                "reason": "fraud_suspected"
            },
            "authorization_details": {
                "rrn": "rrn",
                "auth_code": "auth_code",
                "three_d_secure": {
                    "applied": True
                }
            },
            "transfers": [
                {
                    "account_id": "79990000000",
                    "amount": {
                        "value": 100.01,
                        "currency": "RUB"
                    },
                    "platform_fee_amount": {
                        "value": 10.01,
                        "currency": Currency.RUB
                    },
                    "status": "succeeded",
                    "description": "Test description",
                    "metadata": {
                        "meta1": 'metatest 1',
                        "meta2": 'metatest 2'
                    }
                }
            ],
            "income_amount": {
                "value": "990.00",
                "currency": "RUB"
            },
            'deal': {
                'id': 'dl-28646d17-0022-5000-8000-01e154d1324b',
                'settlements': [{
                    'type': 'payout',
                    'amount': {
                        'value': 80.0,
                        'currency': 'RUB'
                    }
                }]
            },
            'merchant_customer_id': '79990001122'
        })

        self.assertIsInstance(response.amount, Amount)
        self.assertIsInstance(response.recipient, Recipient)
        self.assertIsInstance(response.payment_method, PaymentDataBankCard)
        self.assertIsInstance(response.confirmation, Confirmation)
        self.assertIsInstance(response.cancellation_details, CancellationDetails)
        self.assertIsInstance(response.authorization_details, AuthorizationDetails)
        self.assertIsInstance(response.authorization_details.three_d_secure, ThreeDSecure)
        self.assertEqual(response.authorization_details.three_d_secure.applied, True)
        self.assertEqual(response.authorization_details.rrn, "rrn")
        self.assertEqual(response.authorization_details.auth_code, "auth_code")
        self.assertIsInstance(response.transfers, list)
        self.assertIsInstance(response.income_amount, Amount)
        self.assertIsInstance(response.deal, PaymentDealInfo)

        self.assertEqual(response.metadata, {
            "float_value": "123.32",
            "key": "data"
        })
        self.assertFalse(response.paid)
        self.assertFalse(response.refundable)
        self.assertFalse(response.test)
        self.assertEqual(response.id, "21b23365-000f-500b-9000-070fa3554403")
        self.assertEqual(response.status, "pending")
        self.assertEqual(response.amount.value, 1000.00)

        self.assertEqual(response.recipient.account_id, "67192")

        self.assertEqual(response.description, "Заказ №72")
        self.assertEqual(response.created_at, "2017-11-30T15:11:33+00:00")
        self.assertEqual(response.expires_at, "2017-11-30T15:11:33+00:00")
        self.assertEqual(response.captured_at, "2017-11-30T15:11:33+00:00")
        self.assertEqual(response.receipt_registration, "pending")
        self.assertEqual(dict(response.refunded_amount), {
            "value": "1000.00",
            "currency": "RUB"
        })
        self.assertEqual(response.refunded_amount.value, 1000.00)

        self.assertEqual(dict(response.income_amount), {
            "value": "990.00",
            "currency": "RUB"
        })
        self.assertEqual(response.income_amount.value, 990.00)

        self.assertEqual(dict(response.transfers[0]), dict({
            "account_id": "79990000000",
            "amount": {
                "value": "100.01",
                "currency": Currency.RUB
            },
            "platform_fee_amount": {
                "value": "10.01",
                "currency": Currency.RUB
            },
            "status": TransferStatus.SUCCEEDED,
            "description": "Test description",
            "metadata": {
                "meta1": 'metatest 1',
                "meta2": 'metatest 2'
            }
        }))

        response.transfers = None
        self.assertEqual(response.transfers, None)

        with self.assertRaises(TypeError):
            response.transfers = {}

        self.assertEqual(response.merchant_customer_id, "79990001122")

        self.assertIsInstance(response.deal, PaymentDealInfo)
        self.assertEqual(response.deal.id, 'dl-28646d17-0022-5000-8000-01e154d1324b')
        self.assertIsInstance(response.deal.settlements[0], Settlement)

        with self.assertRaises(TypeError):
            response.deal.settlements = 'invalid settlements'

        response.deal.settlements = None
        self.assertEqual(response.deal.settlements, [])

    def test_response_sberpay_cast(self):
        self.maxDiff = None
        response = PaymentResponse({
            "id": "21b23365-000f-500b-9111-070fa3554403",
            "amount": {
                "value": "1000.00",
                "currency": "RUB"
            },
            "description": "Заказ №72",
            "confirmation": {
                "type": "redirect",
                "return_url": "https://test.test/test",
                "confirmation_url": "https://url",
                "enforce": False
            },
            "payment_method": {
                "type": "sberbank",
                "id": "21b23365-000f-500b-9111-070fa3554403",
                "saved": False,
                "card": {
                    'last4': '0000',
                    'expiry_year': '2024',
                    'expiry_month': '02',
                    'card_type': CardType.VISA,
                    'issuer_country': 'RU',
                    'issuer_name': 'Sberbank'
                }
            },
            "status": "pending",
            "recipient": {
                "account_id": "67192",
                "gateway_id": "352780"
            },
            "refunded_amount": {
                "value": "1000.00",
                "currency": "RUB"
            },
            "receipt_registration": "pending",
            "created_at": "2017-11-30T15:11:33+00:00",
            "expires_at": "2017-11-30T15:11:33+00:00",
            "captured_at": "2017-11-30T15:11:33+00:00",
            "paid": False,
            "refundable": False,
            "test": False,
            "metadata": {
                "float_value": "123.32",
                "key": "data"
            },
            "cancellation_details": {
                "party": "yookassa",
                "reason": "fraud_suspected"
            },
            "authorization_details": {
                "rrn": "rrn",
                "auth_code": "auth_code",
                "three_d_secure": ThreeDSecure({
                    "applied": True
                })
            },
            "transfers": [
                {
                    "account_id": "79990000000",
                    "amount": {
                        "value": 100.01,
                        "currency": "RUB"
                    },
                    "platform_fee_amount": {
                        "value": 10.01,
                        "currency": Currency.RUB
                    },
                    "status": "succeeded",
                    "metadata": {
                        "meta1": 'metatest 1',
                        "meta2": 'metatest 2'
                    }
                }
            ],
            "income_amount": {
                "value": "990.00",
                "currency": "RUB"
            },
            'deal': {
                'id': 'dl-28646d17-0022-5000-8000-01e154d1324b',
                'settlements': [{
                    'type': 'payout',
                    'amount': {
                        'value': 80.0,
                        'currency': 'RUB'
                    }
                }]
            },
            'merchant_customer_id': '79990001122'
        })

        self.assertIsInstance(response.amount, Amount)
        self.assertIsInstance(response.recipient, Recipient)
        self.assertIsInstance(response.payment_method, PaymentDataSberbank)
        self.assertIsInstance(response.payment_method.card, CreditCard)
        self.assertIsInstance(response.confirmation, Confirmation)
        self.assertIsInstance(response.cancellation_details, CancellationDetails)
        self.assertIsInstance(response.authorization_details, AuthorizationDetails)
        self.assertIsInstance(response.authorization_details.three_d_secure, ThreeDSecure)
        self.assertEqual(response.authorization_details.three_d_secure.applied, True)
        self.assertIsInstance(response.transfers, list)
        self.assertIsInstance(response.income_amount, Amount)
        self.assertIsInstance(response.deal, PaymentDealInfo)

        self.assertEqual(response.payment_method.card.issuer_name, "Sberbank")

        self.assertEqual(response.metadata, {
            "float_value": "123.32",
            "key": "data"
        })
        self.assertFalse(response.paid)
        self.assertFalse(response.refundable)
        self.assertFalse(response.test)
        self.assertEqual(response.id, "21b23365-000f-500b-9111-070fa3554403")
        self.assertEqual(response.status, "pending")
        self.assertEqual(response.amount.value, 1000.00)

        self.assertEqual(response.recipient.account_id, "67192")

        self.assertEqual(response.description, "Заказ №72")
        self.assertEqual(response.created_at, "2017-11-30T15:11:33+00:00")
        self.assertEqual(response.expires_at, "2017-11-30T15:11:33+00:00")
        self.assertEqual(response.captured_at, "2017-11-30T15:11:33+00:00")
        self.assertEqual(response.receipt_registration, "pending")
        self.assertEqual(dict(response.refunded_amount), {
            "value": "1000.00",
            "currency": "RUB"
        })
        self.assertEqual(response.refunded_amount.value, 1000.00)

        self.assertEqual(dict(response.income_amount), {
            "value": "990.00",
            "currency": "RUB"
        })
        self.assertEqual(response.income_amount.value, 990.00)

        self.assertEqual(dict(response.transfers[0]), dict({
            "account_id": "79990000000",
            "amount": {
                "value": "100.01",
                "currency": Currency.RUB
            },
            "platform_fee_amount": {
                "value": "10.01",
                "currency": Currency.RUB
            },
            "status": TransferStatus.SUCCEEDED,
            "metadata": {
                "meta1": 'metatest 1',
                "meta2": 'metatest 2'
            }
        }))

        response.transfers = None
        self.assertEqual(response.transfers, None)

        with self.assertRaises(TypeError):
            response.transfers = {}

        self.assertEqual(response.merchant_customer_id, "79990001122")

        self.assertIsInstance(response.deal, PaymentDealInfo)
        self.assertEqual(response.deal.id, 'dl-28646d17-0022-5000-8000-01e154d1324b')
        self.assertIsInstance(response.deal.settlements[0], Settlement)

        with self.assertRaises(TypeError):
            response.deal.settlements = 'invalid settlements'

        with self.assertRaises(TypeError):
            response.authorization_details.three_d_secure = 'invalid settlements'

        response.deal.settlements = None
        self.assertEqual(response.deal.settlements, [])

    def test_response_unknown(self):
        self.maxDiff = None
        response = PaymentResponse({
            "id": "21b23365-000f-500b-9000-070fa3554403",
            "amount": {
                "value": "1000.00",
                "currency": "RUB"
            },
            "description": "Заказ №72",
            "confirmation": {
                "type": "redirect",
                "return_url": "https://test.test/test",
                "confirmation_url": "https://url",
                "enforce": False
            },
            "payment_method": {
                "type": "new_method",
                "id": "21b23365-000f-500b-9000-070fa3554403",
                "saved": False
            },
            "status": "pending",
            "recipient": {
                "account_id": "67192",
                "gateway_id": "352780"
            },
            "receipt_registration": "pending",
            "created_at": "2017-11-30T15:11:33+00:00",
            "expires_at": "2017-11-30T15:11:33+00:00",
            "captured_at": "2017-11-30T15:11:33+00:00",
            "paid": False,
            "refundable": False,
            "test": False,
            "metadata": {
                "float_value": "123.32",
                "key": "data"
            },
        })

        self.assertIsInstance(response.amount, Amount)
        self.assertIsInstance(response.recipient, Recipient)
        self.assertIsInstance(response.payment_method, PaymentDataUnknown)
        self.assertIsInstance(response.confirmation, Confirmation)
        self.assertEqual(response.metadata, {
            "float_value": "123.32",
            "key": "data"
        })
        self.assertFalse(response.paid)
        self.assertFalse(response.refundable)
        self.assertFalse(response.test)
        self.assertEqual(response.id, "21b23365-000f-500b-9000-070fa3554403")
        self.assertEqual(response.status, "pending")
        self.assertEqual(response.amount.value, 1000.00)

        self.assertEqual(response.recipient.account_id, "67192")

        self.assertEqual(response.description, "Заказ №72")
        self.assertEqual(response.created_at, "2017-11-30T15:11:33+00:00")
        self.assertEqual(response.expires_at, "2017-11-30T15:11:33+00:00")
        self.assertEqual(response.captured_at, "2017-11-30T15:11:33+00:00")
        self.assertEqual(response.receipt_registration, "pending")

    def test_response_sber_loan(self):
        self.maxDiff = None
        response = PaymentResponse({
            "id": "21b23365-000f-500b-9000-070fa3554403",
            "amount": {
                "value": "1000.00",
                "currency": "RUB"
            },
            "description": "Заказ №72",
            "confirmation": {
                "type": "redirect",
                "return_url": "https://test.test/test",
                "confirmation_url": "https://url",
                "enforce": False
            },
            "payment_method": {
                "type": "sber_loan",
                "id": "21b23365-000f-500b-9000-070fa3554403",
                "saved": False,
                "loan_option": "installments_3",
                "discount_amount": {
                    "value": "1000.00",
                    "currency": "RUB"
                },
                'suspended_until': '2017-11-03T11:52:31.827Z'
            },
            "status": "pending",
            "recipient": {
                "account_id": "67192",
                "gateway_id": "352780"
            },
            "receipt_registration": "pending",
            "created_at": "2017-11-30T15:11:33+00:00",
            "expires_at": "2017-11-30T15:11:33+00:00",
            "captured_at": "2017-11-30T15:11:33+00:00",
            "paid": False,
            "refundable": False,
            "test": False,
            "metadata": {
                "float_value": "123.32",
                "key": "data"
            },
        })

        self.assertIsInstance(response.amount, Amount)
        self.assertIsInstance(response.recipient, Recipient)
        self.assertIsInstance(response.payment_method, PaymentDataSberLoan)
        self.assertEqual(response.payment_method.loan_option, "installments_3")

        self.assertIsInstance(response.confirmation, Confirmation)
        self.assertEqual(response.metadata, {
            "float_value": "123.32",
            "key": "data"
        })
        self.assertFalse(response.paid)
        self.assertFalse(response.refundable)
        self.assertFalse(response.test)
        self.assertEqual(response.id, "21b23365-000f-500b-9000-070fa3554403")
        self.assertEqual(response.status, "pending")
        self.assertEqual(response.amount.value, 1000.00)

        self.assertEqual(response.recipient.account_id, "67192")

        self.assertEqual(response.description, "Заказ №72")
        self.assertEqual(response.created_at, "2017-11-30T15:11:33+00:00")
        self.assertEqual(response.expires_at, "2017-11-30T15:11:33+00:00")
        self.assertEqual(response.captured_at, "2017-11-30T15:11:33+00:00")
        self.assertEqual(response.receipt_registration, "pending")

        with self.assertRaises(ValueError):
            response.payment_method.loan_option = 'invalid loan_option'

        with self.assertRaises(TypeError):
            response.payment_method.discount_amount = 'invalid discount_amount'

        response.payment_method.discount_amount = Amount({'value': 10.0, 'currency': Currency.RUB})
        self.assertEqual(response.payment_method.discount_amount.value, 10.0)


    def test_response_electronic_certificate(self):
        self.maxDiff = None
        response = PaymentResponse({
            "id": "21b23365-000f-500b-9000-070fa3554403",
            "amount": {
                "value": "1000.00",
                "currency": "RUB"
            },
            "description": "Заказ №72",
            "confirmation": {
                "type": "redirect",
                "return_url": "https://test.test/test",
                "confirmation_url": "https://url",
                "enforce": False
            },
            "payment_method": {
                "type": "electronic_certificate",
                "id": "21b23365-000f-500b-9000-070fa3554403",
                "saved": False,
                "title": "Электронный сертификат",
                "articles": [
                    {
                        "article_number": "1",
                        "tru_code": "329921120.06001010200080001643",
                        "article_code": "123-789-456",
                        "certificates": [
                            {
                                "certificate_id": "12345678901234567890",
                                "tru_quantity": 1,
                                "available_compensation": {
                                    "value": "1000.00",
                                    "currency": "RUB"
                                },
                                "applied_compensation": {
                                    "value": "500.00",
                                    "currency": "RUB"
                                },
                            }
                        ]
                    }
                ],
                "electronic_certificate": {
                    "amount": {
                        "value": "1000.00",
                        "currency": "RUB"
                    },
                    "basket_id": "123-789-456"
                }
            },
            "status": "pending",
            "recipient": {
                "account_id": "67192",
                "gateway_id": "352780"
            },
            "receipt_registration": "pending",
            "created_at": "2017-11-30T15:11:33+00:00",
            "expires_at": "2017-11-30T15:11:33+00:00",
            "captured_at": "2017-11-30T15:11:33+00:00",
            "paid": False,
            "refundable": False,
            "test": False,
            "metadata": {
                "float_value": "123.32",
                "key": "data"
            },
        })

        self.assertIsInstance(response.amount, Amount)
        self.assertIsInstance(response.recipient, Recipient)
        self.assertIsInstance(response.payment_method, PaymentDataElectronicCertificate)
        self.assertEqual(response.payment_method.title, "Электронный сертификат")

        self.assertIsInstance(response.confirmation, Confirmation)
        self.assertEqual(response.metadata, {
            "float_value": "123.32",
            "key": "data"
        })
        self.assertFalse(response.paid)
        self.assertFalse(response.refundable)
        self.assertFalse(response.test)
        self.assertEqual(response.id, "21b23365-000f-500b-9000-070fa3554403")
        self.assertEqual(response.status, "pending")
        self.assertEqual(response.amount.value, 1000.00)

        self.assertEqual(response.recipient.account_id, "67192")

        self.assertEqual(response.description, "Заказ №72")
        self.assertEqual(response.created_at, "2017-11-30T15:11:33+00:00")
        self.assertEqual(response.expires_at, "2017-11-30T15:11:33+00:00")
        self.assertEqual(response.captured_at, "2017-11-30T15:11:33+00:00")
        self.assertEqual(response.receipt_registration, "pending")

        with self.assertRaises(TypeError):
            response.payment_method.electronic_certificate = 'invalid loan_option'

        with self.assertRaises(TypeError):
            response.payment_method.articles = 'invalid discount_amount'

        response.payment_method.electronic_certificate = ElectronicCertificate({
            "amount": {'value': 10.0, 'currency': Currency.RUB},
            "basket_id": "123-789-456"
        })

        self.assertEqual(len(response.payment_method.articles), 1)
        self.assertIsInstance(response.payment_method.articles[0], ElectronicCertificateApprovedPaymentArticle)
