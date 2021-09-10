from dataclasses import dataclass


@dataclass
class Report:
    year: str
    month: str
    region_id: int
    co2_output: float
    trees_num: int
