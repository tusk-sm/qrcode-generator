from aiohttp import web
from aiohttp_middlewares import cors_middleware
import os

from routes import setup_routes


app = web.Application(
        middlewares=[cors_middleware(allow_all=True)]
    )

setup_routes(app)

web.run_app(app, port=os.getenv('PORT', 5000))