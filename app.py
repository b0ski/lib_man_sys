from router.router import Router, Handler
from server.routes import get_routes
from server.library_resource import LibraryResource
from library.library import Library
from server.server import run_server
from http.server import HTTPServer


if __name__ == "__main__":
    library = Library('address', 'telephone', [], [])
    library_resource = LibraryResource(library)
    routes = get_routes(library_resource)
    router = Router()

    for route in routes:
        router.add(route["method"], route["path"], route["call"])

    Handler.ROUTER = router
    run_server(HTTPServer, Handler)

