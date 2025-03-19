import scrapy

class FightSpider(scrapy.Spider):
    name = "fight_spider"
    allowed_domains = ["ufcstats.com"]
    start_urls = ["http://ufcstats.com/statistics/events/completed?page=all"]

    def parse(self, response):
        # Extract event links from the events listing page.
        event_links = response.css("td.b-statistics__table-col a::attr(href)").getall()
        for link in event_links:
            yield scrapy.Request(url=link, callback=self.parse_event)

    def parse_event(self, response):
        # Get the event name from the event page.
        links = response.css('tr::attr(data-link)').extract()
        for link in links:
            yield scrapy.Request(url=link, callback=self.parse_fights)
    
    def parse_fights(self, response):
        # Get each fight of the event
        
        event_name = response.css("h2.b-content__title a::text").get().strip()
        fighters = response.css('div.b-fight-details__person')
        fighter_1 = fighters[0].css('a::text').get().strip()
        fighter1_result = fighters[0].css('i::text').get().strip()

        fighter_2 = fighters[1].css('a::text').get().strip()
        fighter2_result = fighters[1].css('i::text').get().strip()

        if fighter1_result == 'W':
            winner = fighter_1
        elif fighter2_result == 'W':
            winner = fighter_2
        else:
            winner = None
        
        method = response.css('i.b-fight-details__text-item_first i::text')[1].get()
        round_num = response.css('i.b-fight-details__text-item::text')[1].get().strip()
        time = response.css('i.b-fight-details__text-item::text')[3].get().strip()

        yield {
            'event_name': event_name,
            'fighter_1': fighter_1,
            'fighter_2': fighter_2,
            'winner': winner,
            'method': method,
            'round_num': round_num,
            'time': time
            
        }

        