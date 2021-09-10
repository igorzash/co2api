from datetime import datetime, timedelta


class Cache:
    CACHE_HEADER = 'X-API-Cache'
    TTL = 60 * 60 * 12

    store = dict()
    cache_record = dict()

    async def process_request(self, req, resp):
        resp.context.cached = False

        data = self.store.get(req.path)
        expire_date = self.cache_record.get(req.path)


        if data is not None and expire_date is not None and datetime.now() < expire_date:
            resp.text = data
            resp.set_header(self.CACHE_HEADER, 'Hit')
            resp.context.cached = True
        else:
            resp.set_header(self.CACHE_HEADER, 'Miss')


    async def process_response(self, req, resp, resource, req_succeeded):
        if not req_succeeded:
            return

        if not resp.context.cached:
            self.store[req.path] = resp.text
            self.cache_record[req.path] = datetime.now() + timedelta(seconds=self.TTL)
