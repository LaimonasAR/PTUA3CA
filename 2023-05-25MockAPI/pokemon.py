from dataclasses import dataclass
from typing import List


@dataclass
class Statistics:
    base_stat: str
    name: str


# @dataclass
# class Pokemon:
#     name: str
#     stats: List[Statistics]
@dataclass
class Pokemon:
    name: str
    stats: List[Statistics]

    def get_statistic_base_stat(self, stat_name: str):
        for statistic in self.stats:
            if statistic.name == stat_name:
                return statistic.base_stat
        return 0
