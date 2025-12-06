# -*- coding: utf-8 -*-
import unittest
from unittest.mock import Mock, patch

from yookassa.domain.errors.error import (
    Error, InvalidRequestError, InvalidCredentialsError, ForbiddenError,
    NotFoundError, GoneError, TooManyRequestsError, InternalServerError,
    CommonError, UnknownError, ErrorFactory
)
from yookassa.domain.errors.error_code import ErrorCode


class TestError(unittest.TestCase):

    def test_init_with_none_data(self):
        error = Error()
        self.assertIsNone(error.type)
        self.assertIsNone(error.id)
        self.assertIsNone(error.description)
        self.assertIsNone(error.parameter)
        self.assertIsNone(error.retry_after)
        self.assertIsNone(error.code)

    def test_init_with_data(self):
        data = {
            'type': ErrorCode.ERROR,
            'id': 'test_id',
            'description': 'Test description',
            'parameter': 'test_param',
            'retry_after': 1000,
            'code': 'test_code'
        }

        error = Error(data)

        self.assertEqual(error.type, 'error')
        self.assertEqual(error.id, 'test_id')
        self.assertEqual(error.description, 'Test description')
        self.assertEqual(error.parameter, 'test_param')
        self.assertEqual(error.retry_after, 1000)
        self.assertEqual(error.code, 'test_code')

    def test_from_dict_partial_data(self):
        data = {
            'id': 'partial_id',
            'description': 'Partial description'
        }

        error = Error()
        error.from_dict(data)

        self.assertEqual(error.id, 'partial_id')
        self.assertEqual(error.description, 'Partial description')
        self.assertIsNone(error.type)
        self.assertIsNone(error.parameter)

    def test_property_setters(self):
        error = Error()

        error.type = 'test_type'
        error.id = 'test_id'
        error.description = 'test_description'
        error.parameter = 'test_parameter'
        error.retry_after = 500
        error.code = 'test_code'

        self.assertEqual(error.type, 'test_type')
        self.assertEqual(error.id, 'test_id')
        self.assertEqual(error.description, 'test_description')
        self.assertEqual(error.parameter, 'test_parameter')
        self.assertEqual(error.retry_after, 500)
        self.assertEqual(error.code, 'test_code')

    def test_inheritance_from_base_object(self):
        error = Error()
        self.assertTrue(hasattr(error, 'from_dict'))
        self.assertTrue(hasattr(error, '__init__'))


    def test_invalid_request_error_default_type(self):
        error = InvalidRequestError()
        self.assertEqual(error.type, ErrorCode.INVALID_REQUEST)

    def test_invalid_credentials_error_default_type(self):
        error = InvalidCredentialsError()
        self.assertEqual(error.type, ErrorCode.INVALID_CREDENTIALS)

    def test_forbidden_error_default_type(self):
        error = ForbiddenError()
        self.assertEqual(error.type, ErrorCode.FORBIDDEN)

    def test_not_found_error_default_type(self):
        error = NotFoundError()
        self.assertEqual(error.type, ErrorCode.NOT_FOUND)

    def test_gone_error_default_type(self):
        error = GoneError()
        self.assertEqual(error.type, ErrorCode.GONE)

    def test_too_many_requests_error_default_type(self):
        error = TooManyRequestsError()
        self.assertEqual(error.type, ErrorCode.TOO_MANY_REQUESTS)

    def test_internal_server_error_default_type(self):
        error = InternalServerError()
        self.assertEqual(error.type, ErrorCode.INTERNAL_SERVER_ERROR)

    def test_common_error_default_type(self):
        error = CommonError()
        self.assertEqual(error.type, ErrorCode.ERROR)

    def test_unknown_error_default_type(self):
        error = UnknownError()
        self.assertEqual(error.type, ErrorCode.UNKNOWN)

    def test_error_classes_preserve_custom_type(self):
        data = {'type': 'custom_type', 'code': 'test_code'}
        error = UnknownError(data)
        self.assertEqual(error.type, 'custom_type')

    def test_error_classes_inherit_from_error(self):
        error = InvalidRequestError()
        self.assertIsInstance(error, Error)

    def test_create_with_valid_data(self):
        factory = ErrorFactory()
        data = {
            'code': ErrorCode.INVALID_REQUEST,
            'description': 'Invalid request',
            'id': 'test_id'
        }

        error = factory.create(data)

        self.assertIsInstance(error, InvalidRequestError)
        self.assertEqual(error.code, ErrorCode.INVALID_REQUEST)
        self.assertEqual(error.description, 'Invalid request')
        self.assertEqual(error.id, 'test_id')

    def test_create_invalid_request_error(self):
        factory = ErrorFactory()
        data = {'code': ErrorCode.INVALID_REQUEST, 'description': 'Test error'}
        error = factory.create(data)
        self.assertIsInstance(error, InvalidRequestError)

    def test_create_invalid_credentials_error(self):
        factory = ErrorFactory()
        data = {'code': ErrorCode.INVALID_CREDENTIALS, 'description': 'Test error'}
        error = factory.create(data)
        self.assertIsInstance(error, InvalidCredentialsError)

    def test_create_forbidden_error(self):
        factory = ErrorFactory()
        data = {'code': ErrorCode.FORBIDDEN, 'description': 'Test error'}
        error = factory.create(data)
        self.assertIsInstance(error, ForbiddenError)

    def test_create_not_found_error(self):
        factory = ErrorFactory()
        data = {'code': ErrorCode.NOT_FOUND, 'description': 'Test error'}
        error = factory.create(data)
        self.assertIsInstance(error, NotFoundError)

    def test_create_gone_error(self):
        factory = ErrorFactory()
        data = {'code': ErrorCode.GONE, 'description': 'Test error'}
        error = factory.create(data)
        self.assertIsInstance(error, GoneError)

    def test_create_too_many_requests_error(self):
        factory = ErrorFactory()
        data = {'code': ErrorCode.TOO_MANY_REQUESTS, 'description': 'Test error'}
        error = factory.create(data)
        self.assertIsInstance(error, TooManyRequestsError)

    def test_create_internal_server_error(self):
        factory = ErrorFactory()
        data = {'code': ErrorCode.INTERNAL_SERVER_ERROR, 'description': 'Test error'}
        error = factory.create(data)
        self.assertIsInstance(error, InternalServerError)

    def test_create_common_error(self):
        factory = ErrorFactory()
        data = {'code': ErrorCode.ERROR, 'description': 'Test error'}
        error = factory.create(data)
        self.assertIsInstance(error, CommonError)

    def test_create_unknown_error_for_unknown_code(self):
        factory = ErrorFactory()
        data = {'code': 'unknown_code', 'description': 'Test error'}
        error = factory.create(data)
        self.assertIsInstance(error, UnknownError)

    def test_create_missing_code_raises_value_error(self):
        factory = ErrorFactory()
        data = {'description': 'No code provided'}

        with self.assertRaises(ValueError) as context:
            factory.create(data)

        self.assertIn('should contain "code" field', str(context.exception))

    def test_create_with_non_dict_raises_type_error(self):
        factory = ErrorFactory()

        with self.assertRaises(TypeError) as context:
            factory.create('not_a_dict')

        self.assertIn('should be "dict"', str(context.exception))

    def test_create_with_none_data_raises_type_error(self):
        factory = ErrorFactory()

        with self.assertRaises(TypeError) as context:
            factory.create(None)

        self.assertIn('should be "dict"', str(context.exception))

    def test_create_with_empty_dict_raises_value_error(self):
        factory = ErrorFactory()

        with self.assertRaises(ValueError) as context:
            factory.create({})

        self.assertIn('should contain "code" field', str(context.exception))

    def test_get_error_class_unknown_code_returns_unknown_error(self):
        factory = ErrorFactory()
        error_class = factory._get_error_class('non_existent_code')
        self.assertEqual(error_class, UnknownError)

    def test_create_from_data_method(self):
        factory = ErrorFactory()
        data = {
            'code': ErrorCode.FORBIDDEN,
            'description': 'Access denied',
            'parameter': 'auth_token'
        }

        error = factory._create_from_data(data)

        self.assertIsInstance(error, ForbiddenError)
        self.assertEqual(error.code, ErrorCode.FORBIDDEN)
        self.assertEqual(error.description, 'Access denied')
        self.assertEqual(error.parameter, 'auth_token')

    def test_error_with_retry_after_as_string(self):
        data = {
            'code': 'test_code',
            'retry_after': '1000'
        }

        error = Error(data)
        self.assertEqual(error.retry_after, '1000')

    def test_error_with_none_values_in_data(self):
        data = {
            'code': 'test_code',
            'description': None,
            'parameter': None,
            'retry_after': None
        }

        error = Error(data)
        self.assertEqual(error.code, 'test_code')
        self.assertIsNone(error.description)
        self.assertIsNone(error.parameter)
        self.assertIsNone(error.retry_after)

    def test_error_factory_with_minimal_data(self):
        factory = ErrorFactory()
        data = {'code': ErrorCode.INTERNAL_SERVER_ERROR}

        error = factory.create(data)

        self.assertIsInstance(error, InternalServerError)
        self.assertEqual(error.code, ErrorCode.INTERNAL_SERVER_ERROR)
        self.assertIsNone(error.description)

    def test_error_classes_with_additional_data(self):
        data = {
            'code': ErrorCode.TOO_MANY_REQUESTS,
            'retry_after': 30000,
            'custom_field': 'should_be_ignored'
        }

        error = TooManyRequestsError(data)

        self.assertEqual(error.code, ErrorCode.TOO_MANY_REQUESTS)
        self.assertEqual(error.retry_after, 30000)

