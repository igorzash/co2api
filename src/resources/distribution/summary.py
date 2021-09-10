import json
import dataclasses

import falcon

from src.data.fetcher import DataFetcher


class SummaryResource:

    async def on_get(self, req, resp):

        def invalid_query_params():
            resp.content_type = 'text/plain'
            resp.text = ('Query parameters: dataType, region, and year - '
                         'required and should be valid values')
            resp.status = falcon.HTTP_400

        if 'dataType' not in req.params or\
            'region' not in req.params or\
            'year' not in req.params:
            invalid_query_params()
            return

        try:
            data_type_id = int(req.params['dataType'])
            region_id = int(req.params['region'])
            year = req.params['year']

            data_type = await DataFetcher.get_data_type(data_type_id)
            region = await DataFetcher.get_region(region_id)
        except:
            invalid_query_params()
            return

        try:
            results = [result async for result in DataFetcher.get_summary_results(year=year,
                data_type_id=data_type_id, region_id=region_id)]

            resp.text = json.dumps({
                'dataType': dataclasses.asdict(data_type),
                'region': dataclasses.asdict(region),
                'results': results
            })
        except Exception as e:
            print(e)
