# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class FighterItem(scrapy.Item):
    name = scrapy.Field()
    height_cm = scrapy.Field()
    weight_kg = scrapy.Field()
    reach_cm = scrapy.Field()
    stance = scrapy.Field()
    wins = scrapy.Field()
    losses = scrapy.Field()
    draws = scrapy.Field()
    strikes_per_min = scrapy.Field()
    striking_accuracy = scrapy.Field()
    takedown_avg = scrapy.Field()
    takedown_accuracy = scrapy.Field()
    takedown_defense = scrapy.Field()
    submission_avg = scrapy.Field()

class FightItem(scrapy.Item):
    event_name = scrapy.Field()
    fighter_1 = scrapy.Field()
    fighter_2 = scrapy.Field()
    # kd = scrapy.Field()
    # strikes = scrapy.Field()
    # td = scrapy.Field()
    # sub = scrapy.Field()
    winner = scrapy.Field()
    method = scrapy.Field()
    round_num = scrapy.Field()
    time = scrapy.Field()
    
    