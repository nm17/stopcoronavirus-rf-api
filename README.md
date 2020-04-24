# stopcoronavirus-rf-api
GraphQL API для стопкоронавирус.рф

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Примеры запросов
### Получить информацию о всех регионах
```graphql
{
  coronavirusInfo {
    region
    infected
    recovered
    dead
  }
}
```

### Получить информацию об Москве и Ульяновской области
```graphql
{
  coronavirusInfo(regions: ["Москва", "Ульяновская область"]) {
    region
    infected
    recovered
    dead
  }
}
```

### Получить информацию только о количестве выздоровевших и умерших в Москве
```graphql
{
  coronavirusInfo(regions: ["Москва"]) {
    region
    recovered
    dead
  }
}
