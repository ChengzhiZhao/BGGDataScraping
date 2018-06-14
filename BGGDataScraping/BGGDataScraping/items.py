from scrapy.item import Item, Field

class BggdatascrapingItem(Item):
    title = Field()
    rank = Field()
    release_date = Field()
    geek_rating = Field()
    avg_rating = Field()
    num_voters = Field()
    url = Field()
