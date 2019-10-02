from unittest import TestCase

from httmock import HTTMock

from pybotman import BotmanApi
from tests.mocks import *


class StatusTest(TestCase):

    def setUp(self):
        self.client = BotmanApi(base_url, "TEST", False)

    def test_get_api_status(self):
        with HTTMock(status_success_mock):
            status = self.client.get_api_status()
        self.assertEqual(status, True)

        with HTTMock(status_stopped_mock):
            status = self.client.get_api_status()
        self.assertEqual(status, False)

        with HTTMock(missing_token_mock):
            status = self.client.get_api_status()
        self.assertEqual(status, False)

        with HTTMock(invalid_token_mock):
            status = self.client.get_api_status()
        self.assertEqual(status, False)

    def test_get_bot_status(self):
        with HTTMock(status_success_mock):
            status = self.client.get_bot_status()
        self.assertEqual(status, True)

        with HTTMock(status_stopped_mock):
            status = self.client.get_bot_status()
        self.assertEqual(status, False)

        with HTTMock(missing_token_mock):
            status = self.client.get_bot_status()
        self.assertEqual(status, False)

        with HTTMock(invalid_token_mock):
            status = self.client.get_bot_status()
        self.assertEqual(status, False)

    def test_start_bot(self):
        with HTTMock(bot_start_success_mock):
            result = self.client.start_bot()
        self.assertEqual(result, True)

        with HTTMock(bot_start_error_mock):
            result = self.client.start_bot()
        self.assertEqual(result, False)

        with HTTMock(missing_token_mock):
            result = self.client.start_bot()
        self.assertEqual(result, False)

        with HTTMock(invalid_token_mock):
            result = self.client.start_bot()
        self.assertEqual(result, False)

    def test_stop_bot(self):
        with HTTMock(bot_stop_success_mock):
            result = self.client.stop_bot()
        self.assertEqual(result, True)

        with HTTMock(bot_stop_error_mock):
            result = self.client.stop_bot()
        self.assertEqual(result, False)

        with HTTMock(missing_token_mock):
            result = self.client.stop_bot()
        self.assertEqual(result, False)

        with HTTMock(invalid_token_mock):
            result = self.client.stop_bot()
        self.assertEqual(result, False)
