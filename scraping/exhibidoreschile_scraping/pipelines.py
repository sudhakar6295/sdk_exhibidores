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
                record.route_product = item['route_product']
                record.long_description = item['long_description']
                record.specifications = item['features']
                record.last_scraped_date = datetime.now(timezone.utc)
                record.updated_date = datetime.now(timezone.utc)
                
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
                route_product = item['route_product'],
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



