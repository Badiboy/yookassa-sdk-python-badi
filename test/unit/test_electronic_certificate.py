# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models.payment_data.electronic_certificate.electronic_certificate import ElectronicCertificate
from yookassa.domain.models.payment_data.electronic_certificate.electronic_certificate_approved_payment_article import \
    ElectronicCertificateApprovedPaymentArticle
from yookassa.domain.models.payment_data.electronic_certificate.electronic_certificate_article import \
    ElectronicCertificateArticle
from yookassa.domain.models.refund_data.electronic_certificate_refund_article import ElectronicCertificateRefundArticle
from yookassa.domain.models.refund_data.request.electronic_certificate_refund_data_request import \
    ElectronicCertificateRefundDataRequest
from yookassa.domain.models.refund_data.response.electronic_certificate_refund_data_response import \
    ElectronicCertificateRefundDataResponse


class TestElectronicCertificate(unittest.TestCase):

    def test_electronic_certificate(self):
        model = ElectronicCertificate({
            "certificate_id": "12345678901234567890",
            "tru_quantity": "1",
            "available_compensation": {
                "value": "200.00",
                "currency": "RUB"
            },
            "applied_compensation": {
                "value": "200.00",
                "currency": "RUB"
            },
        })

        self.assertEqual({
            "certificate_id": "12345678901234567890",
            "tru_quantity": "1",
            "available_compensation": {
                "value": "200.00",
                "currency": "RUB"
            },
            "applied_compensation": {
                "value": "200.00",
                "currency": "RUB"
            },
        }, dict(model))

        with self.assertRaises(ValueError):
            model.certificate_id = None

        with self.assertRaises(ValueError):
            model.tru_quantity = None

        with self.assertRaises(ValueError):
            model.available_compensation = None

        with self.assertRaises(ValueError):
            model.applied_compensation = None

    def test_electronic_certificate_approved_payment_article(self):
        model = ElectronicCertificateApprovedPaymentArticle({
            "article_number": 1,
            "tru_code": "329921120.06001010200080001643",
            "article_code": "123-456-789",
            "certificates": [
                {
                    "certificate_id": "12345678901234567890",
                    "tru_quantity": "1",
                    "available_compensation": {
                        "value": "200.00",
                        "currency": "RUB"
                    },
                    "applied_compensation": {
                        "value": "200.00",
                        "currency": "RUB"
                    },
                }
            ],
        })

        self.assertEqual({
            "article_number": 1,
            "tru_code": "329921120.06001010200080001643",
            "article_code": "123-456-789",
            "certificates": [
                {
                    "certificate_id": "12345678901234567890",
                    "tru_quantity": "1",
                    "available_compensation": {
                        "value": "200.00",
                        "currency": "RUB"
                    },
                    "applied_compensation": {
                        "value": "200.00",
                        "currency": "RUB"
                    },
                }
            ],
        }, dict(model))


    def test_electronic_certificate_article(self):
        model = ElectronicCertificateArticle({
            "article_number": 1,
            "tru_code": "329921120.06001010200080001643",
            "article_code": "123-456-789",
            "article_name": "Product Test",
            "quantity": 1,
            "price": {
                "value": "200.00",
                "currency": "RUB"
            },
            "metadata": {
                "test": "test",
            },
        })

        self.assertEqual({
            "article_number": 1,
            "tru_code": "329921120.06001010200080001643",
            "article_code": "123-456-789",
            "article_name": "Product Test",
            "quantity": 1,
            "price": {
                "value": "200.00",
                "currency": "RUB"
            },
            "metadata": {
                "test": "test",
            },
        }, dict(model))

        with self.assertRaises(ValueError):
            model.article_number = None

        with self.assertRaises(ValueError):
            model.article_number = 0

        with self.assertRaises(ValueError):
            model.article_number = 1000

        with self.assertRaises(ValueError):
            model.tru_code = None

        with self.assertRaises(ValueError):
            model.article_name = None

        with self.assertRaises(ValueError):
            model.quantity = None

        with self.assertRaises(ValueError):
            model.price = None

    def test_electronic_certificate_refund_article(self):
        model = ElectronicCertificateRefundArticle({
            "article_number": 1,
            "payment_article_number": "123-456-789",
            "tru_code": "329921120.06001010200080001643",
            "quantity": 1,
        })

        self.assertEqual({
            "article_number": 1,
            "payment_article_number": "123-456-789",
            "tru_code": "329921120.06001010200080001643",
            "quantity": 1,
        }, dict(model))


    def test_electronic_certificate_refund_data_request(self):
        model = ElectronicCertificateRefundDataRequest({
            "amount": {
                "value": "200.00",
                "currency": "RUB"
            },
             "basket_id": "123-789-456"
        })

        self.assertEqual({
            "amount": {
                "value": "200.00",
                "currency": "RUB"
            },
             "basket_id": "123-789-456"
        }, dict(model))


    def test_electronic_certificate_refund_data_response(self):
        model = ElectronicCertificateRefundDataResponse({
            "amount": {
                "value": "200.00",
                "currency": "RUB"
            },
             "basket_id": "123-789-456"
        })

        self.assertEqual({
            "amount": {
                "value": "200.00",
                "currency": "RUB"
            },
             "basket_id": "123-789-456"
        }, dict(model))

