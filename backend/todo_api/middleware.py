from typing import Optional

from helpers import decode_user_dict, generate_token, get_user_from_db
from settings import SETTINGS
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response, JSONResponse


class AuthenticationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:

        if SETTINGS.spoof_user and not AuthenticationMiddleware._is_login_url(request):
            auth_header = request.headers.get("authorization")
            if not auth_header:
                token = generate_token("default", "1234")
                request.scope["headers"].append((b"authorization", bytes(token, encoding="UTF_8")))

                request = Request(request.scope, request.receive, request._send)

        is_authorized, error = AuthenticationMiddleware._check_header(request)

        if not is_authorized and not AuthenticationMiddleware._is_login_url(request):
            return error

        return await call_next(request)

    @staticmethod
    def _check_header(request: Request) -> (bool, Optional[Response]):
        auth = request.headers.get("authorization")
        if not auth:
            return False, AuthenticationMiddleware._auth_error("No auth header was found")

        try:
            auth_header = decode_user_dict(request)
        except Exception as e:
            print(e)
            return False, AuthenticationMiddleware._auth_error("Could not decode auth header")

        if "username" not in auth_header or "password" not in auth_header:
            return False, AuthenticationMiddleware._auth_error("`username` or `password field not in header`")

        user = get_user_from_db(auth_header["username"])
        if not user.password_valid(auth_header["password"]):
            return False, AuthenticationMiddleware._auth_error("Token invalid")

        return True, None

    @staticmethod
    def _auth_error(body) -> Response:
        response = {"detail": body}
        return JSONResponse(response, status_code=403)

    @staticmethod
    def _is_login_url(request: Request) -> bool:
        return request.url.path == "/login"
