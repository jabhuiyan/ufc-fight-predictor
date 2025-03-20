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
    winner = scrapy.Field()
    method = scrapy.Field()
    kd1 = scrapy.Field()
    sig_str1_p = scrapy.Field()
    head1_p = scrapy.Field()
    body1_p = scrapy.Field()
    leg1_p = scrapy.Field()
    str_distance1 = scrapy.Field()
    str_clinch1 = scrapy.Field()
    str_ground1 = scrapy.Field()
    td1_p = scrapy.Field()
    sub_att1 = scrapy.Field()
    rev1 = scrapy.Field()
    ctr1 = scrapy.Field()
    kd2 = scrapy.Field()
    sig_str2_p = scrapy.Field()
    head2_p = scrapy.Field()
    body2_p = scrapy.Field()
    leg2_p = scrapy.Field()
    str_distance2 = scrapy.Field()
    str_clinch2 = scrapy.Field()
    str_ground2 = scrapy.Field()
    td2_p = scrapy.Field()
    sub_att2 = scrapy.Field()
    rev2 = scrapy.Field()
    ctr2 = scrapy.Field()
    round_num = scrapy.Field()
    time = scrapy.Field()
    
    