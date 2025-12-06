# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.common import PaymentMethodType
from yookassa.domain.models import Currency
from yookassa.domain.models.payment_data.card_type import CardType
from yookassa.domain.models.payment_data.request.credit_card import CreditCard as RequestCreditCard
from yookassa.domain.models.payment_data.request.payment_data_applepay import \
    PaymentDataApplepay as RequestPaymentDataApplepay
from yookassa.domain.models.payment_data.request.payment_data_b2b_sberbank import \
    PaymentDataB2bSberbank as RequestPaymentDataB2bSberbank, VatDataType, VatDataRate
from yookassa.domain.models.payment_data.request.payment_data_bank_card import \
    PaymentDataBankCard as RequestPaymentDataBankCard
from yookassa.domain.models.payment_data.request.payment_data_cash import \
    PaymentDataCash as RequestPaymentDataCash
from yookassa.domain.models.payment_data.request.payment_data_google_pay import \
    PaymentDataGooglePay as RequestPaymentDataGooglePay
from yookassa.domain.models.payment_data.request.payment_data_mobile_balance import \
    PaymentDataMobileBalance as RequestPaymentDataMobileBalance
from yookassa.domain.models.payment_data.request.payment_data_sberbank import \
    PaymentDataSberbank as RequestPaymentDataSberbank
from yookassa.domain.models.payment_data.request.payment_data_sbp import \
    PaymentDataSbp as RequestPaymentDataSbp
from yookassa.domain.models.payment_data.request.payment_data_sber_loan import \
    PaymentDataSberLoan as RequestPaymentDataSberLoan
from yookassa.domain.models.payment_data.request.payment_data_sber_bnpl import \
    PaymentDataSberBnpl as RequestPaymentDataSberBnpl
from yookassa.domain.models.payment_data.response.credit_card import CreditCard as ResponseCreditCard
from yookassa.domain.models.payment_data.response.payment_data_alfabank import \
    PaymentDataAlfabank as ResponsePaymentDataAlfabank
from yookassa.domain.models.payment_data.response.payment_data_applepay import \
    PaymentDataApplepay as ResponsePaymentDataApplepay
from yookassa.domain.models.payment_data.response.payment_data_b2b_sberbank import \
    PaymentDataB2bSberbank as ResponsePaymentDataB2bSberbank
from yookassa.domain.models.payment_data.response.payment_data_bank_card import \
    PaymentDataBankCard as ResponsePaymentDataBankCard
from yookassa.domain.models.payment_data.response.payment_data_cash import \
    PaymentDataCash as ResponsePaymentDataCash
from yookassa.domain.models.payment_data.response.payment_data_google_pay import \
    PaymentDataGooglePay as ResponsePaymentDataGooglePay
from yookassa.domain.models.payment_data.response.payment_data_mobile_balance import \
    PaymentDataMobileBalance as ResponsePaymentDataMobileBalance
from yookassa.domain.models.payment_data.response.payment_data_psb import \
    PaymentDataPsb as ResponsePaymentDataPsb
from yookassa.domain.models.payment_data.response.payment_data_sberbank import \
    PaymentDataSberbank as ResponsePaymentDataSberbank
from yookassa.domain.models.payment_data.response.payment_data_sbp import \
    PaymentDataSbp as ResponsePaymentDataSbp
from yookassa.domain.models.payment_data.response.payment_data_sber_loan import \
    PaymentDataSberLoan as ResponsePaymentDataSberLoan
from yookassa.domain.models.payment_data.response.payment_data_sber_bnpl import \
    PaymentDataSberBnpl as ResponsePaymentDataSberBnpl
from yookassa.domain.models.payment_data.response.payment_data_unknown import \
    PaymentDataUnknown as ResponsePaymentDataUnknown


class TestPaymentData(unittest.TestCase):
    def test_alfabank_cast(self):
        payment_data = ResponsePaymentDataAlfabank()

        payment_data.type = PaymentMethodType.ALFABANK
        payment_data.login = 'login'

        self.assertEqual({'type': PaymentMethodType.ALFABANK, 'login': 'login'}, dict(payment_data))

    def test_bank_card_cast(self):
        payment_data = RequestPaymentDataBankCard()
        payment_data.type = PaymentMethodType.BANK_CARD
        payment_data.card = RequestCreditCard({
            'number': '8888888888880000',
            'expiry_year': '2018',
            'expiry_month': '10',
            'csc': '111',
            'cardholder': 'test'
        })

        self.assertEqual({'type': PaymentMethodType.BANK_CARD, 'card': {
            'number': '8888888888880000',
            'expiry_year': '2018',
            'expiry_month': '10',
            'csc': '111',
            'cardholder': 'test'
        }}, dict(payment_data))

        payment_data.card = {
            'number': '0000000000008888',
            'expiry_year': '2018',
            'expiry_month': '10',
            'csc': '111',
            'cardholder': 'test'
        }

        self.assertEqual({'type': PaymentMethodType.BANK_CARD, 'card': {
            'number': '0000000000008888',
            'expiry_year': '2018',
            'expiry_month': '10',
            'csc': '111',
            'cardholder': 'test'
        }}, dict(payment_data))

        with self.assertRaises(TypeError):
            payment_data.card = 'invalid type'

        payment_data = ResponsePaymentDataBankCard()
        payment_data.type = PaymentMethodType.BANK_CARD
        payment_data.card = ResponseCreditCard({
            'last4': '0000',
            'expiry_year': '2010',
            'expiry_month': '02',
            'card_type': CardType.VISA
        })

        self.assertEqual({'type': PaymentMethodType.BANK_CARD, 'card': {
            'last4': '0000',
            'expiry_year': '2010',
            'expiry_month': '02',
            'card_type': CardType.VISA
        }}, dict(payment_data))

        payment_data.card = {
            'last4': '0000',
            'expiry_year': '2010',
            'expiry_month': '02',
            'card_type': CardType.VISA
        }

        self.assertEqual({'type': PaymentMethodType.BANK_CARD, 'card': {
            'last4': '0000',
            'expiry_year': '2010',
            'expiry_month': '02',
            'card_type': CardType.VISA
        }}, dict(payment_data))

        with self.assertRaises(TypeError):
            payment_data.card = 'invalid type'

    def test_cash_cast(self):
        payment_data = RequestPaymentDataCash()
        payment_data.type = PaymentMethodType.CASH
        payment_data.phone = '799900000000'

        self.assertEqual({'type': PaymentMethodType.CASH, 'phone': '799900000000'}, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.phone = 'invalid phone'

        payment_data = ResponsePaymentDataCash()
        payment_data.type = PaymentMethodType.CASH
        payment_data.phone = '799900000000'

        self.assertEqual({'type': PaymentMethodType.CASH, 'phone': '799900000000'}, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.phone = 'invalid phone'

    def test_mobile_balance_cast(self):
        payment_data = RequestPaymentDataMobileBalance()
        payment_data.type = PaymentMethodType.MOBILE_BALANCE
        payment_data.phone = '799900000000'

        self.assertEqual({'type': PaymentMethodType.MOBILE_BALANCE, 'phone': '799900000000'}, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.phone = 'invalid phone'

        payment_data = ResponsePaymentDataMobileBalance()
        payment_data.type = PaymentMethodType.MOBILE_BALANCE
        payment_data.phone = '799900000000'

        self.assertEqual({'type': PaymentMethodType.MOBILE_BALANCE, 'phone': '799900000000'}, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.phone = 'invalid phone'

    def test_sberbank_cast(self):
        payment_data = RequestPaymentDataSberbank()
        payment_data.type = PaymentMethodType.SBERBANK
        payment_data.phone = '799900000000'

        self.assertEqual({'type': PaymentMethodType.SBERBANK, 'phone': '799900000000'}, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.phone = 'invalid phone'

        payment_data = ResponsePaymentDataSberbank()
        payment_data.type = PaymentMethodType.SBERBANK
        payment_data.phone = '799900000000'

        self.assertEqual({'type': PaymentMethodType.SBERBANK, 'phone': '799900000000'}, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.phone = 'invalid phone'

    def test_b2b_sberbank_cast(self):
        payment_data = RequestPaymentDataB2bSberbank()
        payment_data.type = PaymentMethodType.B2B_SBERBANK
        payment_data.payment_purpose = 'Test test test'
        payment_data.vat_data = {
            'type': VatDataType.MIXED,
            'rate': VatDataRate.RATE_5,
            'amount': {'value': 10, 'currency': Currency.RUB}
        }

        self.assertEqual({
            'type': PaymentMethodType.B2B_SBERBANK,
            'payment_purpose': 'Test test test',
            'vat_data': {
                'type': VatDataType.MIXED,
                'rate': VatDataRate.RATE_5,
                'amount': {'value': '10.00', 'currency': Currency.RUB}
            }
        }, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.vat_data.type = 'VatDataType.MIXED'

        with self.assertRaises(ValueError):
            payment_data.vat_data.rate = 9

        payment_data = ResponsePaymentDataB2bSberbank()
        payment_data.type = PaymentMethodType.B2B_SBERBANK
        payment_data.payment_purpose = 'Test test test'
        payment_data.vat_data = {
            'type': VatDataType.MIXED,
            'rate': VatDataRate.RATE_7,
            'amount': {'value': 10, 'currency': Currency.RUB}
        }

        self.assertEqual({
            'type': PaymentMethodType.B2B_SBERBANK,
            'payment_purpose': 'Test test test',
            'vat_data': {
                'type': VatDataType.MIXED,
                'rate': VatDataRate.RATE_7,
                'amount': {'value': '10.00', 'currency': Currency.RUB}
            }
        }, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.vat_data = {
                'type': VatDataType.MIXED,
                'rate': 'invalid rate'
            }

        with self.assertRaises(ValueError):
            payment_data.vat_data = {
                'type': 'invalid type',
                'rate': VatDataRate.RATE_20
            }

    def test_applepay_cast(self):
        payment_data = RequestPaymentDataApplepay()
        payment_data.payment_data = 'sampletoken'

        self.assertEqual({'type': PaymentMethodType.APPLEPAY, 'payment_data': 'sampletoken'}, dict(payment_data))

        payment_data = ResponsePaymentDataApplepay()

        self.assertEqual({'type': PaymentMethodType.APPLEPAY}, dict(payment_data))

    def test_google_pay_cast(self):
        payment_data = RequestPaymentDataGooglePay()
        payment_data.payment_method_token = 'sampletoken'
        payment_data.google_transaction_id = 'sampleid'

        self.assertEqual({
            'type': PaymentMethodType.GOOGLE_PAY,
            'payment_method_token': 'sampletoken',
            'google_transaction_id': 'sampleid',
        }, dict(payment_data))

        payment_data = ResponsePaymentDataGooglePay()

        self.assertEqual({'type': PaymentMethodType.GOOGLE_PAY}, dict(payment_data))

    def test_psb_cast(self):
        payment_data = ResponsePaymentDataPsb()
        self.assertEqual({'type': PaymentMethodType.PSB}, dict(payment_data))

    def test_unknown_cast(self):
        payment_data = ResponsePaymentDataUnknown()
        self.assertEqual({'type': PaymentMethodType.UNKNOWN}, dict(payment_data))

    def test_sbp_cast(self):
        payment_data = RequestPaymentDataSbp()
        payment_data.type = PaymentMethodType.SBP

        self.assertEqual({'type': PaymentMethodType.SBP}, dict(payment_data))

        payment_data = ResponsePaymentDataSbp()
        payment_data.type = PaymentMethodType.SBP

        self.assertEqual({'type': PaymentMethodType.SBP}, dict(payment_data))

    def test_sber_loan_cast(self):
        payment_data = RequestPaymentDataSberLoan()
        payment_data.type = PaymentMethodType.SBER_LOAN

        self.assertEqual({'type': PaymentMethodType.SBER_LOAN}, dict(payment_data))

        payment_data = ResponsePaymentDataSberLoan()
        payment_data.type = PaymentMethodType.SBER_LOAN
        payment_data.suspended_until = '2017-11-03T11:52:31.827Z'

        self.assertEqual({
            'type': PaymentMethodType.SBER_LOAN,
            'suspended_until': '2017-11-03T11:52:31.827Z'
        }, dict(payment_data)
        )

    def test_sber_bnpl_cast(self):
        payment_data = RequestPaymentDataSberBnpl()
        payment_data.type = PaymentMethodType.SBER_BNPL
        payment_data.phone = '799900000000'

        self.assertEqual({'type': PaymentMethodType.SBER_BNPL, 'phone': '799900000000'}, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.phone = 'invalid phone'

        payment_data = ResponsePaymentDataSberBnpl()
        payment_data.type = PaymentMethodType.SBER_BNPL

        self.assertEqual({'type': PaymentMethodType.SBER_BNPL}, dict(payment_data))

