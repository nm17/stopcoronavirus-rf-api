from functools import lru_cache
from typing import Tuple

import bs4
import requests


@lru_cache(20, typed=True)
def get_data(*regions: str):
    data = requests.get("https://стопкоронавирус.рф/").text
    doc = bs4.BeautifulSoup(data, "html.parser")
    result = []
    if len(regions) == 0:
        regions = (None, )
    for el in doc.select_one(".d-map__list").select("tr"):
        region, infected, recovered, dead = list(
            map(lambda a: list(a.strings)[0], el.select("th, td"))
        )
        region = region.strip()
        if (len(regions) >= 0 and regions[0] is None) or region in regions:
            result.append(dict(
                region=region,
                infected=int(infected),
                recovered=int(recovered),
                dead=int(dead),
            ))
    return tuple(result)
