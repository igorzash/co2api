from uvicorn.config import LOG_LEVELS
from data.fetcher import DataFetcher
import uvicorn
import falcon
import falcon.asgi

from resources.distribution.regions import RegionsResource
from resources.distribution.data_types import DataTypesResource
from resources.distribution.summary import SummaryResource

from middleware.cache import Cache


app = falcon.asgi.App(cors_enable=True, middleware=[Cache()])


app.add_route('/api/v1/distribution/regions', RegionsResource())
app.add_route('/api/v1/distribution/dataTypes', DataTypesResource())
app.add_route('/api/v1/distribution/summary', SummaryResource())
