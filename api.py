import time
from threading import Thread

import graphene as graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from stopcoronavirus import get_data

app = FastAPI()


class CacheCleaner(Thread):
    def run(self) -> None:
        print("Cache cleaner running...")
        while True:
            get_data.cache_clear()
            time.sleep(60 * 60)


class Region(graphene.ObjectType):
    region = graphene.String()
    infected = graphene.Int()
    recovered = graphene.Int()
    dead = graphene.Int()


class Query(graphene.ObjectType):
    coronavirus_info = graphene.Field(
        graphene.List(Region),
        regions=graphene.Argument(
            graphene.List(graphene.String), default_value=(None, ), required=False
        ),
    )

    def resolve_coronavirus_info(self, info, regions):
        return list(get_data(*regions))


# noinspection PyTypeChecker
app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query)))
cleaner = CacheCleaner()
cleaner.setDaemon(True)
cleaner.start()
