# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.helpers import ProductCode


class TestProductCode(unittest.TestCase):
    def test_product_code_initialization(self):
        code_data = "0104860019002077215'u0E0AeTToec93L6Wj"
        product_code = ProductCode(code_data)

        self.assertEqual(product_code.type, ProductCode.TYPE_GS_1M)
        self.assertEqual(product_code.gtin, "04860019002077")
        self.assertEqual(product_code.serial, "5'u0E0AeTToec")
        self.assertTrue(product_code.validate())
        self.assertIsNotNone(product_code.get_result())

    def test_prefix_handling(self):
        product_code = ProductCode("010460406000590021N4N57RTCBUZTQ", use_prefix=True)
        self.assertTrue(product_code.use_prefix)
        self.assertEqual(product_code.prefix, ProductCode.PREFIX_DATA_MATRIX)

        product_code = ProductCode("010460406000590021N4N57RTCBUZTQ", use_prefix=False)
        self.assertFalse(product_code.use_prefix)
        self.assertIsNotNone(product_code.prefix)

    def test_code_type_detection(self):
        code_data = "0104860019002077215'u0E0AeTToec93L6Wj"
        product_code = ProductCode(code_data)
        self.assertEqual(product_code.type, ProductCode.TYPE_GS_1M)

        code_data = "010460406000590021N4N57RTCBUZTQ\x1d2403054002410161218"
        product_code = ProductCode(code_data)
        self.assertEqual(product_code.type, ProductCode.TYPE_GS_10)

        code_data = "4006670128002"
        product_code = ProductCode(code_data)
        self.assertEqual(product_code.type, ProductCode.TYPE_EAN_13)

        code_data = "01460123456789"
        product_code = ProductCode(code_data)
        self.assertEqual(product_code.type, ProductCode.TYPE_ITF_14)

        code_data = "22N00002NU5DBKYDOT17ID980726019019608CW1A4XR5EJ7JKFX50FHHGV92ZR2GZRZ"
        product_code = ProductCode(code_data)
        self.assertEqual(product_code.type, ProductCode.TYPE_EGAIS_20)

        code_data = "invalid_code_123"
        product_code = ProductCode(code_data)
        self.assertEqual(product_code.type, ProductCode.TYPE_UNKNOWN)

    def test_result_calculation(self):
        code_data = "010460406000590021N4N57RTCBUZTQ"
        product_code = ProductCode(code_data, use_prefix=True)
        expected_result = "44 4D 04 2F F7 5C 76 0C 4E 34 4E 35 37 52 54 43 42 55 5A 54 51"
        self.assertEqual(product_code.get_result(), expected_result)

        code_data = "4006670128002"
        product_code = ProductCode(code_data, use_prefix=False)
        expected_result = "03 A4 E0 26 53 82"
        self.assertEqual(product_code.get_result(), expected_result)

    def test_mark_code_info(self):
        code_data = "010460043993125621JgXJ5.T"
        product_code = ProductCode(code_data)
        expected_info = {"gs_10": "010460043993125621JgXJ5.T"}
        self.assertEqual(product_code.get_mark_code_info(), expected_info)

        code_data = "some_unknown_code_123"
        product_code = ProductCode(code_data)
        expected_info = {"unknown": "some_unknown_code_123"}
        self.assertEqual(product_code.get_mark_code_info(), expected_info)

    def test_validation(self):
        product_code = ProductCode("")
        self.assertFalse(product_code.validate())

        product_code = ProductCode("4006670128002")
        self.assertTrue(product_code.validate())

        product_code = ProductCode("0104604060005900")
        self.assertEqual(product_code.type, ProductCode.TYPE_UNKNOWN)
        self.assertTrue(product_code.validate())

    def test_properties(self):
        product_code = ProductCode("010460406000590021N4N57RTCBUZTQ")

        product_code.gtin = "12345678901234"
        self.assertEqual(product_code.gtin, "12345678901234")

        product_code.serial = "SERIAL123"
        self.assertEqual(product_code.serial, "SERIAL123")

        product_code.app_identifiers = ["AI1", "AI2"]
        self.assertEqual(product_code.app_identifiers, ["AI1", "AI2"])

        product_code.type = "invalid_type"
        self.assertEqual(product_code.type, "invalid_type")
        self.assertFalse(product_code.validate())

    def test_edge_cases(self):
        max_length_code = "a" * ProductCode.MAX_PRODUCT_CODE_LENGTH
        product_code = ProductCode(max_length_code)
        self.assertEqual(len(product_code.gtin), ProductCode.MAX_PRODUCT_CODE_LENGTH)

        long_code = "a" * (ProductCode.MAX_PRODUCT_CODE_LENGTH + 10)
        product_code = ProductCode(long_code)
        self.assertEqual(len(product_code.gtin), ProductCode.MAX_PRODUCT_CODE_LENGTH)
        self.assertEqual(len(product_code.serial), ProductCode.MAX_MARK_CODE_LENGTH)

    def test_conversion_methods(self):
        product_code = ProductCode("010460406000590021N4N57RTCBUZTQ")

        hex_result = product_code._num_to_hex("1234")
        self.assertEqual(hex_result, "0000000004d2")
        self.assertEqual(product_code._str_to_hex("AB"), "4142")
        self.assertEqual(product_code._hex_to_str("4142"), "AB")
        self.assertEqual(product_code._chunk_str("414243"), "41 42 43")

    def test_invalid_codes(self):
        product_code = ProductCode("123456789012")
        self.assertEqual(product_code.type, ProductCode.TYPE_UNKNOWN)
