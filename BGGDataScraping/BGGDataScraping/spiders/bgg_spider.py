from scrapy import Spider,Request, FormRequest
from scrapy.selector import Selector
from BGGDataScraping.items import BggdatascrapingItem

class BGGSpider(Spider):
    
    name = "bgg"
    BASE_URL = 'https://www.boardgamegeek.com'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

    def start_requests(self):
        url = "https://www.boardgamegeek.com/browse/boardgame/page/"
        for index in range(50):
            yield Request(url=url+str(index+1), callback=self.parse, headers=self.headers)

    def parse(self, response):
        games = Selector(response).xpath('//tr[@id="row_"]')
        for index, game in enumerate(games):
            item = BggdatascrapingItem()
            item['rank'] = int(game.xpath('td[@class="collection_rank"]/text()').extract()[1].replace('\t','').replace('\n',''))
            item['title'] = game.xpath('.//div["results_objectname{0}"]/a/text()'.format(index+1)).extract()[0]
            item['url'] = game.xpath('.//div["results_objectname{0}"]/a/@href'.format(index+1)).extract()[0]
            item['release_date'] = game.xpath('.//span[@class="smallerfont dull"]/text()').extract()[0][1:-1]
            rating = game.xpath('td[@class="collection_bggrating"]/text()')
            item['geek_rating'] = float(rating.extract()[0].replace('\t','').replace('\n',''))
            item['avg_rating'] = float(rating.extract()[1].replace('\t','').replace('\n',''))
            item['num_voters'] = float(rating.extract()[2].replace('\t','').replace('\n',''))
            yield item            

