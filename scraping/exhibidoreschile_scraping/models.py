from sqlalchemy import create_engine, Column, String, ForeignKey, Integer, DECIMAL, DateTime, Text,JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sku = Column(String(255), nullable=False)
    url_scraped = Column(Text, nullable=False)
    price = Column(DECIMAL(10, 2))
    percent_discount = Column(DECIMAL(5, 2))
    price_discount = Column(DECIMAL(10, 4))
    tax = Column(DECIMAL(10, 4))
    price_included_taxes = Column(DECIMAL(10,4))
    price_mt2 = Column(DECIMAL(10, 4))
    price_mtl = Column(DECIMAL(10, 4))
    stock_1 = Column(Integer)
    stock_2 = Column(Integer)
    stock_3 = Column(Integer)
    stock_comentarie_1 = Column(String(100))
    stock_comentarie_2 = Column(String(100))
    stock_comentarie_3 = Column(String(100))
    images = Column(JSON)  # SQLAlchemy does not have a direct JSON type, but you can use JSON type if your database supports it
    route_product = Column(Text)
    short_description = Column(Text)
    long_description = Column(Text)
    pdf = Column(Text)
    length = Column(DECIMAL(10, 2))
    width = Column(DECIMAL(10, 2))
    height = Column(DECIMAL(10, 2))
    weight = Column(DECIMAL(10, 2))
    main_color = Column(String(255))
    glossy_or_matte = Column(String(50))
    main_material = Column(String(255))
    origen = Column(String(255))
    last_scraped_date = Column(DateTime, onupdate=func.now())
    updated_date = Column(DateTime, onupdate=func.now())
    created_date = Column(DateTime, default=func.now())
    status = Column(String(50))
    name = Column(String(255), nullable=True)
    specifications = Column(JSON)


# Define your database connection
#engine = create_engine('mysql://root:sudhakar@localhost/sdk_exhibidores')
engine = create_engine('mysql://root:sdk@TKnApQsKErGlXv6H/sdk_exhibidores')

# Create the tables
Base.metadata.create_all(engine)