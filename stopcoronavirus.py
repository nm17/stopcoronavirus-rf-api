from functools import lru_cache
from typing import Tuple

import bs4
import httpx


@lru_cache(3)
def get_data(regions: Tuple[str]):
    data = httpx.get("http://стопкоронавирус.рф/").text
    doc = bs4.BeautifulSoup(data, "html.parser")
    for el in doc.select_one(".d-map__list").select("tr"):
        region, infected, recovered, dead = list(
            map(lambda a: list(a.strings)[0], el.select("th, td"))
        )
        region = region.strip()
        if len(regions) == 0 or region in regions:
            yield dict(
                region=region,
                infected=int(infected),
                recovered=int(recovered),
                dead=int(dead),
            )
