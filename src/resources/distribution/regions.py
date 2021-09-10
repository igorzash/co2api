import json
import dataclasses

from src.data.fetcher import DataFetcher


class RegionsResource:

    async def on_get(self, req, resp):
        regions = []

        async for region in DataFetcher.get_regions():
            regions.append(dataclasses.asdict(region))
        
        resp.text = json.dumps(regions)

