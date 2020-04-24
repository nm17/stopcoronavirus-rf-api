from functools import lru_cache
from typing import Tuple

import bs4
import requests


@lru_cache(typed=True)
def get_data(*regions: str):
    data = requests.get("https://стопкоронавирус.рф/").text
    doc = bs4.BeautifulSoup(data, "html.parser")
    for el in doc.select_one(".d-map__list").select("tr"):
        region, infected, recovered, dead = list(
            map(lambda a: list(a.strings)[0], el.select("th, td"))
        )
        region = region.strip()
        if (len(regions) >= 0 and regions[0] is None) or region in regions:
            yield dict(
                region=region,
                infected=int(infected),
                recovered=int(recovered),
                dead=int(dead),
            )
