# -*- coding: utf-8 -*-
import unittest
from unittest.mock import Mock, patch

from yookassa.domain.errors.error import ErrorFactory, UnknownError
from yookassa.domain.exceptions.api_error import ApiError


class TestApiError(unittest.TestCase):
    def test_init_with_error_data(self):
        error_data = {
            'type': 'error',
            'id': 'test_id',
            'code': 'test_code',
            'description': 'test_description'
        }

        with patch.object(ErrorFactory, 'create') as mock_create:
            mock_error = Mock()
            mock_create.return_value = mock_error

            exception = ApiError(error_data)

            mock_create.assert_called_once_with(error_data)
            assert exception.error == mock_error
            assert exception.content == error_data

    def test_init_with_none_data(self):
        exception = ApiError(None)
        assert exception.error is None
        assert exception.content is None

    def test_error_property(self):
        error_data = {
            'type': 'error',
            'id': 'test_id',
            'code': 'test_code',
            'description': 'test_description'
        }

        with patch.object(ErrorFactory, 'create') as mock_create:
            mock_error = Mock()
            mock_create.return_value = mock_error

            exception = ApiError(error_data)

            assert exception.error == mock_error
            assert hasattr(exception, 'error')
            assert exception.error is not None
            assert exception.content == error_data

    def test_content_property(self):
        error_data = {
            'type': 'error',
            'id': 'test_id',
            'description': 'test_description'
        }

        exception = ApiError(error_data)

        assert hasattr(exception, 'content')
        assert exception.content == error_data
        assert exception.content['type'] == 'error'
        assert exception.content['id'] == 'test_id'

    def test_http_code_constant(self):
        assert hasattr(ApiError, 'HTTP_CODE')
        assert ApiError.HTTP_CODE == 0

    def test_string_representation(self):
        error_data = {
            'type': 'error',
            'description': 'Test error description'
        }

        with patch.object(ErrorFactory, 'create') as mock_create:
            mock_error = Mock()
            mock_error.__str__ = Mock(return_value="Test error")
            mock_create.return_value = mock_error

            exception = ApiError(error_data)

            str_repr = str(exception)
            assert "Test error" in str_repr
            assert exception.content == error_data

    def test_unknown_error_creation_on_type_error(self):
        error_data = {'description': 'invalid'}

        with patch.object(ErrorFactory, 'create') as mock_create:
            mock_create.side_effect = TypeError("Type error")

            exception = ApiError(error_data)

            mock_create.assert_called_once_with(error_data)
            assert isinstance(exception.error, UnknownError)
            assert exception.error.description == error_data['description']
            assert exception.content == error_data

    def test_multiple_arguments_passed(self):
        error_data = {'test': 'data'}
        additional_arg = "additional"

        exception = ApiError(error_data, additional_arg)

        assert exception.error is not None
        assert exception.content == error_data

    def test_keyword_arguments(self):
        error_data = {'test': 'data'}

        exception = ApiError(error_data, "value")

        assert exception.error is not None
        assert exception.content == error_data

    def test_content_with_empty_dict(self):
        error_data = {}

        exception = ApiError(error_data)

        assert exception.content == error_data
        assert exception.error is not None

    def test_content_preserves_original_data(self):
        error_data = {
            'type': 'error',
            'id': 'test_id',
            'code': 'test_code',
            'description': 'test_description',
            'extra_field': 'extra_value'
        }

        exception = ApiError(error_data)

        assert exception.content == error_data
        assert exception.content['extra_field'] == 'extra_value'
