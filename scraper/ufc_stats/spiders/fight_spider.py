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

        kd1 = response.xpath('//html/body/section/div/div/section[2]/table/tbody/tr/td[2]/p[1]/text()').get().strip()
        kd2 = response.xpath('//html/body/section/div/div/section[2]/table/tbody/tr/td[2]/p[2]/text()').get().strip()

        sig_str1 = response.xpath('//html/body/section/div/div/section[2]/table/tbody/tr/td[4]/p[1]/text()').get().strip()
        if sig_str1 == "---":
            sig_str1_p = 0.00
        else:
            sig_str1_p = float(sig_str1.replace("%", ""))/100
        
        head1 = response.xpath('/html/body/section/div/div/section[6]/div/div/div[1]/div[1]/div/div[2]/div[1]/i[1]/text()').get().strip()
        head1_p = float(head1.replace("%", ""))/100
        body1 = response.xpath('/html/body/section/div/div/section[6]/div/div/div[1]/div[1]/div/div[2]/div[2]/i[1]/text()').get().strip()
        body1_p = float(body1.replace("%", ""))/100
        leg1 = response.xpath('/html/body/section/div/div/section[6]/div/div/div[1]/div[1]/div/div[2]/div[3]/i[1]/text()').get().strip()
        leg1_p = float(leg1.replace("%", ""))/100

        distance1 = response.xpath('/html/body/section/div/div/section[6]/div/div/div[1]/div[2]/div/div[2]/div[1]/i[1]/text()').get().strip()
        str_distance1 = float(distance1.replace("%", ""))/100
        clinch1 = response.xpath('/html/body/section/div/div/section[6]/div/div/div[1]/div[2]/div/div[2]/div[2]/i[1]/text()').get().strip()
        str_clinch1 = float(clinch1.replace("%", ""))/100
        ground1 = response.xpath('/html/body/section/div/div/section[6]/div/div/div[1]/div[2]/div/div[2]/div[3]/i[1]/text()').get().strip()
        str_ground1 = float(ground1.replace("%", ""))/100

        sig_str2 = response.xpath('//html/body/section/div/div/section[2]/table/tbody/tr/td[4]/p[2]/text()').get().strip()
        if sig_str2 == "---":
            sig_str2_p = 0.00
        else:
            sig_str2_p = float(sig_str2.replace("%", ""))/100
        
        head2 = response.xpath('/html/body/section/div/div/section[6]/div/div/div[1]/div[1]/div/div[2]/div[1]/i[3]/text()').get().strip()
        head2_p = float(head2.replace("%", ""))/100
        body2 = response.xpath('/html/body/section/div/div/section[6]/div/div/div[1]/div[1]/div/div[2]/div[2]/i[3]/text()').get().strip()
        body2_p = float(body2.replace("%", ""))/100
        leg2 = response.xpath('/html/body/section/div/div/section[6]/div/div/div[1]/div[1]/div/div[2]/div[3]/i[3]/text()').get().strip()
        leg2_p = float(leg2.replace("%", ""))/100

        distance2 = response.xpath('/html/body/section/div/div/section[6]/div/div/div[1]/div[2]/div/div[2]/div[1]/i[3]/text()').get().strip()
        str_distance2 = float(distance2.replace("%", ""))/100
        clinch2 = response.xpath('/html/body/section/div/div/section[6]/div/div/div[1]/div[2]/div/div[2]/div[2]/i[3]/text()').get().strip()
        str_clinch2 = float(clinch2.replace("%", ""))/100
        ground2 = response.xpath('/html/body/section/div/div/section[6]/div/div/div[1]/div[2]/div/div[2]/div[3]/i[3]/text()').get().strip()
        str_ground2 = float(ground2.replace("%", ""))/100

        td1 = response.xpath('//html/body/section/div/div/section[2]/table/tbody/tr/td[7]/p[1]/text()').get().strip()
        if td1 == "---":
            td1_p = 0.00
        else:
            td1_p = float(td1.replace("%", ""))/100
        td2 = response.xpath('//html/body/section/div/div/section[2]/table/tbody/tr/td[7]/p[2]/text()').get().strip()
        if td2 == "---":
            td2_p = 0.00
        else:
            td2_p = float(td2.replace("%", ""))/100

        sub_att1 = response.xpath('//html/body/section/div/div/section[2]/table/tbody/tr/td[8]/p[1]/text()').get().strip()
        sub_att2 = response.xpath('//html/body/section/div/div/section[2]/table/tbody/tr/td[8]/p[2]/text()').get().strip()
        
        rev1 = response.xpath('/html/body/section/div/div/section[2]/table/tbody/tr/td[9]/p[1]/text()').get().strip()
        rev2 = response.xpath('/html/body/section/div/div/section[2]/table/tbody/tr/td[9]/p[2]/text()').get().strip()

        ctr1 = response.xpath('/html/body/section/div/div/section[2]/table/tbody/tr/td[10]/p[1]/text()').get().strip()
        if ctr1 == "--":
            ctr1_p = 0.0
        else:
            ctr1_p = float(ctr1.replace(":", "."))
        ctr2 = response.xpath('/html/body/section/div/div/section[2]/table/tbody/tr/td[10]/p[2]/text()').get().strip()
        if ctr2 == "--":
            ctr2_p = 0.0
        else:
            ctr2_p = float(ctr2.replace(":", "."))



        yield {
            'event_name': event_name,
            'fighter_1': fighter_1,
            'fighter_2': fighter_2,
            'winner': winner,
            'method': method,
            'fighter_1_kd': kd1,
            'fighter_1_sig_str': sig_str1_p,
            'f1_sig_head': head1_p,
            'f1_sig_body': body1_p,
            'f1_sig_leg': leg1_p,
            'f1_sig_distance': str_distance1,
            'f1_sig_clinch': str_clinch1,
            'f1_sig_ground': str_ground1,
            'fighter_1_td': td1_p,
            'fighter_1_sub_att': sub_att1,
            'fighter_1_rev': rev1,
            'fighter_1_ctrl': ctr1_p,
            'fighter_2_kd': kd2,
            'fighter_2_sig_str': sig_str2_p,
            'f2_sig_head': head2_p,
            'f2_sig_body': body2_p,
            'f2_sig_leg': leg2_p,
            'f2_sig_distance': str_distance2,
            'f2_sig_clinch': str_clinch2,
            'f2_sig_ground': str_ground2,
            'fighter_2_td': td2_p,
            'fighter_2_sub_att': sub_att2,
            'fighter_2_rev': rev2,
            'fighter_2_ctrl': ctr2_p,
            'round_num': round_num,
            'time': time
            
        }

        