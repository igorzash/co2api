import aiosqlite
import datetime

from src.model.data_type import DataType
from src.model.region import Region


SQLITE_DB_PATH = './co2.db'


class DataFetcher:

    async def get_region(region_id):
        async with aiosqlite.connect(SQLITE_DB_PATH) as db:
            async with db.execute('select id, name from regions where id=?', (region_id,)) as cur:
                async for row in cur:
                    return Region(id=row[0], name=row[1])

    
    async def get_regions():
        async with aiosqlite.connect(SQLITE_DB_PATH) as db:
            async with db.execute('select id, name from regions') as cur:
                async for row in cur:
                    yield Region(id=row[0], name=row[1])
    
    
    async def get_data_type(data_type_id):
        async with aiosqlite.connect(SQLITE_DB_PATH) as db:
            async with db.execute('select id, name, units from data_types where id=?', (data_type_id,)) as cur:
                async for row in cur:
                    return DataType(id=row[0], name=row[1], units=row[2])


    async def get_data_types():
        async with aiosqlite.connect(SQLITE_DB_PATH) as db:
            async with db.execute('select id, name, units from data_types') as cur:
                async for row in cur:
                    yield DataType(id=row[0], name=row[1], units=row[2])

    
    async def get_summary_results(year: str, data_type_id: int, region_id: int):
        async with aiosqlite.connect(SQLITE_DB_PATH) as db:
            async with db.execute('select year, month, region_id,'
                                  'co2_output, trees_num from reports '
                                  'where year=? and region_id=?',
                                  (year, region_id)) as cur:
                async for row in cur:
                    yield {
                        'dateStart': datetime.date(int(year), int(row[1]), 1).isoformat(),
                        'value': row[-2] if data_type_id == 1 else row[-1]
                    }
