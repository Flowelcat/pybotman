from httmock import all_requests, response
from requests.utils import default_headers

base_url = "https://example.com/v1/"

headers = default_headers()
headers.update({"content-type": "application/json"})

messages = {
    1: "Success",
    2: "Bot is running",
    3: "Bot is stopped",

    1001: "Token is missing",
    1002: "Token is wrong",
    1003: "Missing required parameters",
    1004: "User not found",
    1005: "Wrong parameter type",
    1006: "Date or time already passed",
    1007: "Table not found",
    1008: "Table column not found",
    1100: "Unknown error"
}


def create_response(success, data, message_code):
    return {
        "success": success,
        "data": data,
        "message": {"code": message_code, "message": messages[message_code]}
    }


@all_requests
def status_success_mock(url, request):
    content = create_response(True, {"status": True}, 1)
    return response(200, content, headers, request=request)


@all_requests
def status_stopped_mock(url, request):
    content = create_response(True, {"status": False}, 1)
    return response(200, content, headers, request=request)


@all_requests
def missing_token_mock(url, request):
    content = create_response(False, {}, 1001)
    return response(401, content, headers, request=request)


@all_requests
def invalid_token_mock(url, request):
    content = create_response(False, {}, 1002)
    return response(401, content, headers, request=request)


@all_requests
def bot_start_success_mock(url, request):
    content = create_response(True, {}, 1)
    return response(200, content, headers, request=request)


@all_requests
def bot_start_error_mock(url, request):
    content = create_response(False, {}, 2)
    return response(200, content, headers, request=request)

@all_requests
def bot_stop_success_mock(url, request):
    content = create_response(True, {}, 1)
    return response(200, content, headers, request=request)

@all_requests
def bot_stop_error_mock(url, request):
    content = create_response(False, {}, 3)
    return response(200, content, headers, request=request)
