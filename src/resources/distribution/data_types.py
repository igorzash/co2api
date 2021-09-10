import dataclasses
import json

import falcon

from src.data.fetcher import DataFetcher


class DataTypesResource:

    async def on_get(self, req, resp):
        data_types = []

        async for data_type in DataFetcher.get_data_types():
            data_types.append(dataclasses.asdict(data_type))
        
        resp.text = json.dumps(data_types)
