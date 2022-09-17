from http. server import BaseHTTPRequestHandler
from http import HTTPStatus
from typing import Callable


class Router:
    ALLOWED_METHODS: list[str] = [
        "GET",
        "POST",
        "PUT",
        "DELETE",
        "HEAD",
        "PATCH",
        "OPTIONS"
    ]

    _routes: dict[str: list[tuple[str, Callable]]] = {}

    def add(self, method: str, path: str, func: Callable) -> None:
        if method not in Router.ALLOWED_METHODS:
            raise ValueError(f'method {method} is not alLowed')
        if not isinstance(func, Callable):
            raise TypeError(f'func should be callable {type(func)} received')
    # TODO add path validation

        self._routes.setdefault(method, []).append((path, func))

    def serve_request(self, req: BaseHTTPRequestHandler) -> None:
        if req.command not in Router.ALLOWED_METHODS:
            raise Exception('received unknown method freq.command}')
        try:
            func = next(x[1] for x in self._routes[req.command] if x[0] == req.path)
            func(req)
        except StopIteration:
            req.send_error(HTTPStatus.NOT_FOUND)


class Handler(BaseHTTPRequestHandler):
    ROUTER: Router = None

    def do_GET(self):
        Handler.ROUTER.serve_request(self)

    def do_POST (self):
        Handler.ROUTER.serve_request(self)

    def do_PUT(self):
        Handler.ROUTER.serve_request(self)

    def do_DELETE(self):
        Handler.ROUTER.serve_request(self)

    def do_HEAD(self):
        Handler.ROUTER.serve_request(self)

    def do_PATCH(self):
        Handler.ROUTER.serve_request(self)

    def do_OPTIONS(self):
        Handler.ROUTER.serve_request(self)



