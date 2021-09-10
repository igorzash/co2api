from uvicorn.config import LOG_LEVELS
from data.fetcher import DataFetcher
import uvicorn
import falcon
import falcon.asgi

from resources.distribution.regions import RegionsResource
from resources.distribution.data_types import DataTypesResource
from resources.distribution.summary import SummaryResource


app = falcon.asgi.App()


app.add_route('/api/v1/distribution/regions', RegionsResource())
app.add_route('/api/v1/distribution/dataTypes', DataTypesResource())
app.add_route('/api/v1/distribution/summary', SummaryResource())
