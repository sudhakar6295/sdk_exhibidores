# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from exhibidoreschile_scraping.models import Products
from datetime import datetime,timezone

class ExhibidoreschileScrapingPipeline:

    def  __init__(self):
        #engine = engine = create_engine('mysql://root:sudhakar@localhost/sdk_exhibidores')
        engine = create_engine('mysql://sdk:TKnApQsKErGlXv6H@localhost/sdk_exhibidores')
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        # Create a session
        session = self.Session()

        # Create a session
        session = self.Session()

        try:
            # Query the database for the record you want to update
            record = session.query(Products).filter_by(sku=item['sku']).first()
            
            # Update the record if found
            if record:
                record.name = item['title']
                record.sku = item['sku']
                record.price = item['price']
                record.url_scraped = item['url_scraped']
                record.stock_1 = item['stock_1']
                record.stock_2 = item['stock_2']
                record.stock_3 = item['stock_3']
                record.stock_comentarie_1 = item['stock_comentarie_1']
                record.stock_comentarie_2 = item['stock_comentarie_2']
                record.stock_comentarie_3 = item['stock_comentarie_3']
                record.images = item['images']
                record.long_description = item['long_description']
                record.specifications = item['features']
                record.last_scraped_date = datetime.now(timezone.utc)
                record.updated_date = datetime.now(timezone.utc)
                record.route_product1 = item['route_product1']
                record.route_product2 = item['route_product2']
                record.route_product3 = item['route_product3']
                record.route_product4 = item['route_product4']
                record.route_product5 = item['route_product5']
                record.route_product6 = item['route_product6']
                record.route_product7 = item['route_product7']
                record.route_product8 = item['route_product8']
                record.route_product9 = item['route_product9']
                record.route_product10 = item['route_product10']
                
                # Commit the changes to the database
                session.commit()
                spider.logger.info("Record updated successfully.")   
            else:
                new_record = Products(
                name = item['title'],
                sku = item['sku'],
                price = item['price'],
                url_scraped = item['url_scraped'],
                stock_1 = item['stock_1'],
                stock_2 = item['stock_2'],
                stock_3 = item['stock_3'],
                stock_comentarie_1 = item['stock_comentarie_1'],
                stock_comentarie_2 = item['stock_comentarie_2'],
                stock_comentarie_3 = item['stock_comentarie_3'],
                images = item['images'],
                route_product1 = item['route_product1'],
                route_product2 = item['route_product2'],
                route_product3 = item['route_product3'],
                route_product4 = item['route_product4'],
                route_product5 = item['route_product5'],
                route_product6 = item['route_product6'],
                route_product7 = item['route_product7'],
                route_product8 = item['route_product8'],
                route_product9 = item['route_product9'],
                route_product10 = item['route_product10'],
                long_description = item['long_description'],
                specifications	 = item['features'],
                created_date	 = datetime.now(timezone.utc),
                last_scraped_date = datetime.now(timezone.utc),
                updated_date = datetime.now(timezone.utc),
                  )
                
                # Add more columns and values as needed
            
                # Add the new record to the session
                session.add(new_record)
                
                # Commit the changes to the database
                session.commit()
                spider.logger.info("New record created successfully.")
        except Exception as e:
            # Rollback the changes in case of an error
            session.rollback()
            spider.logger.error("Failed to update record:", e)



