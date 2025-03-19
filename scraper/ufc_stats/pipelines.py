# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# from itemadapter import ItemAdapter
# import psycopg2
# from db.db_config import get_connection

# class PostgresPipeline:
#     def open_spider(self, spider):
#         self.conn = get_connection()
#         self.cursor = self.conn.cursor()

#     def close_spider(self, spider):
#         self.cursor.close()
#         self.conn.commit()
#         self.conn.close()

#     def process_item(self, item, spider):
#         try:
#             self.cursor.execute("""
#                 INSERT INTO fighters (
#                     name, height_cm, weight_kg, reach_cm, stance, dob,
#                     wins, losses, draws, strikes_per_min, striking_accuracy,
#                     takedown_avg, takedown_accuracy, takedown_defense, submission_avg
#                 ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#                 ON CONFLICT (name) DO NOTHING;
#             """, (
#                 item.get('name'),
#                 item.get('height_cm'),
#                 item.get('weight_kg'),
#                 item.get('reach_cm'),
#                 item.get('stance'),
#                 item.get('dob'),
#                 item.get('wins', 0),
#                 item.get('losses', 0),
#                 item.get('draws', 0),
#                 item.get('strikes_per_min'),
#                 item.get('striking_accuracy'),
#                 item.get('takedown_avg'),
#                 item.get('takedown_accuracy'),
#                 item.get('takedown_defense'),
#                 item.get('submission_avg')
#             ))
#         except Exception as e:
#             spider.logger.error(f"Failed to insert item: {e}")
#         return item

import csv

class CsvExportPipeline:
    def open_spider(self, spider):
        if spider.name == 'fighters_spider':
            self.file = open('fighters_data.csv', mode='w', newline='', encoding='utf-8')
        elif spider.name == 'fight_spider':
            self.file = open('fights_data.csv', mode='w', newline='', encoding='utf-8')
        self.writer = None

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if self.writer is None:
            # Initialize CSV headers from item keys
            fieldnames = list(item.keys())
            self.writer = csv.DictWriter(self.file, fieldnames=fieldnames)
            self.writer.writeheader()
        
        self.writer.writerow(item)
        return item
