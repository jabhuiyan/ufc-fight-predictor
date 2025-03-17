import scrapy
from ..items import FighterItem

class FightersSpider(scrapy.Spider):
    name = "fighters"
    allowed_domains = ["ufcstats.com"]
    start_urls = ["http://ufcstats.com/statistics/fighters?char=a&page=all"]

    def parse(self, response):
        # Extract links to individual fighter pages
        fighter_links = response.css("td.b-statistics__table-col a::attr(href)").getall()
        for link in fighter_links:
            yield scrapy.Request(url=link, callback=self.parse_fighter)

        # Extract pagination links and follow them
        pagination_links = response.css("ul.b-statistics__pagination a::attr(href)").getall()
        for link in pagination_links:
            yield scrapy.Request(url=link, callback=self.parse)

    def parse_fighter(self, response):
        item = FighterItem()
        item['name'] = response.css("span.b-content__title-highlight::text").get().strip()

        # Extract fighter details
        details = response.css("li.b-list__box-list-item.b-list__box-list-item_type_block")
        for detail in details:
            label = detail.css("i::text").get().strip()
            value = detail.css("::text").getall()[-1].strip()
            if label == "Height:":
                item['height_cm'] = self.convert_height(value)
            elif label == "Weight:":
                item['weight_kg'] = self.convert_weight(value)
            elif label == "Reach:":
                item['reach_cm'] = self.convert_reach(value)
            elif label == "Stance:":
                item['stance'] = value
            elif label == "Record:":
                item['wins'], item['losses'], item['draws'] = self.parse_record(value)

        # Extract fighter statistics
        stats = response.css("li.b-list__box-list-item.b-list__box-list-item_type_block")
        for stat in stats:
            label = stat.css("i::text").get().strip()
            value = stat.css("::text").getall()[-1].strip()
            if label == "SLpM:":
                item['strikes_per_min'] = float(value)
            elif label == "Str. Acc.:":
                item['striking_accuracy'] = float(value.replace("%", "")) / 100
            elif label == "SApM:":
                item['takedown_avg'] = float(value)
            elif label == "TD Acc.:":
                item['takedown_accuracy'] = float(value.replace("%", "")) / 100
            elif label == "TD Def.:":
                item['takedown_defense'] = float(value.replace("%", "")) / 100
            elif label == "Sub. Avg.:":
                item['submission_avg'] = float(value)

        yield item

    def convert_height(self, height_str):
        try:
            feet, inches = height_str.split("'")
            inches = inches.replace('"', '').strip()
            cm = int(feet) * 30.48 + int(inches) * 2.54
            return round(cm, 2)
        except:
            return None

    def convert_weight(self, weight_str):
        try:
            lbs = int(weight_str.replace(" lbs.", "").strip())
            kg = lbs * 0.453592
            return round(kg, 2)
        except:
            return None

    def convert_reach(self, reach_str):
        try:
            inches = int(reach_str.replace('"', '').strip())
            cm = inches * 2.54
            return round(cm, 2)
        except:
            return None

    def parse_record(self, record_str):
        try:
            wins, losses, draws = record_str.split('-')
            return int(wins), int(losses), int(draws)
        except:
            return None
 
