import falcon
import falcon.asgi

from src.resources.distribution.regions import RegionsResource
from src.resources.distribution.data_types import DataTypesResource
from src.resources.distribution.summary import SummaryResource

from src.middleware.cache import Cache


def create_app():
    app = falcon.asgi.App(cors_enable=True, middleware=[Cache()])

    app.add_route('/api/v1/distribution/regions', RegionsResource())
    app.add_route('/api/v1/distribution/dataTypes', DataTypesResource())
    app.add_route('/api/v1/distribution/summary', SummaryResource())

    return app
