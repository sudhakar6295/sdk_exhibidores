import scrapy , requests,re
from scrapy.http import Request
from scrapy import Selector

class ExhibidoreschileSpider(scrapy.Spider):
    name = "exhibidoreschile"
    allowed_domains = ["www.exhibidoreschile.cl"]
    start_urls = ["https://www.exhibidoreschile.cl/"]

    def parse(self, response):
        categorys = response.xpath('.//*[@class="nav-bounds nav-default-desktop-categories-popover"]//*[contains(@class,"nav-default-list--horizontal__item")]')
        for category_val in categorys:
            category= category_val.xpath('.//@data-toggle').get()
            sub_category_vals = category_val.xpath('.//li')
            for sub_category_val in sub_category_vals:
                sub_category_url = sub_category_val.xpath('.//a/@href').get()
                sub_category_name = sub_category_val.xpath('.//a//text()').get() 
                sub_category_name = sub_category_val.xpath('.//a//text()').get() 
                if category and sub_category_url and sub_category_name:
                    data = {'category':category,
                        'sub_category_url':sub_category_url,
                        'sub_category_name':sub_category_name
                        }

                    yield Request (url=sub_category_url,callback=self.parse_category,meta={'data':data})

    def parse_category(self,response):
        
        data = response.meta['data']
        products = response.xpath('//*[@class="ui-search-item__group ui-search-item__group--title shops__items-group"]/a/@href').extract()                
        for product in products:
            yield Request (url=product,callback=self.parse_product,meta={'data':data})

    def clean_stock(self,stock):

        pattern = r"(\d+)"
        qty = stock
        match = re.search(pattern, stock)
        if match:
            qty = match.group(1)

        try:
            qty = int(qty)
        except Exception as e:
            print(f"Not able to convert {qty} to int {e}")

        return qty
    
    def get_stock_key(self,stock_dict):
        return len(stock_dict)+1
    
    def parse_product(self,response):

        product_url = response.url
        title = response.xpath('.//*[@class="ui-pdp-title"]/text()').get()

        price = response.xpath('//*[@itemprop="price"]/following-sibling::span/text()[not(contains(.,"$"))]').get()


        feature_dict = {}
        main_feature_rows = response.xpath('//*[@class="andes-table"]//tr')
        for main_feature_row in main_feature_rows:
            key = main_feature_row.xpath('.//th//text()').get()
            value = main_feature_row.xpath('.//td//text()').get()
            feature_dict[key] = value

        other_feature_rows = response.xpath('//*[@class="ui-pdp-list ui-pdp-specs__list"]//ul/li')
        for other_feature_row in other_feature_rows:
            values_lst = other_feature_row.xpath('.//text()').extract()
            values_lst = [x.replace(':','').strip() for x in values_lst if x.strip() ]
            if len(values_lst) == 2:
                feature_dict[values_lst[0]] = values_lst[1]

        description = response.xpath('//*[@class="ui-pdp-container__row ui-pdp-container__row--description"]').extract()
           
            
        breadcrum_lst = response.xpath('//*[@class="andes-breadcrumb"]//li//text()').extract()
        breadcrum = '/'.join(breadcrum_lst)
        sku = feature_dict.get('Modelo')
        images_lst= []
        stock_dict = {}
        stock_comentarie = {}
        variations = response.xpath('//*[@class="ui-pdp-variations__picker-default-container"]/a')
        for i,variation in enumerate(variations,1):
            default = variation.xpath('.//aria-current').get()
            variation_id = variation.xpath('.//@title').get()
            variation_url = variation.xpath('.//@href').get()
            if default:
                
                variation_qty = response.xpath('.//*[@class="ui-pdp-buybox__quantity__available"]/text()').get()
                key_stock = self.get_stock_key(stock_dict)
                stock_dict[f"stock_{key_stock}"] = self.clean_stock(variation_qty)
                stock_comentarie[f"stock_comentarie_{i}"] = variation_id
                images = response.xpath('.//*[@class="ui-pdp-image lazy-loadable"]/@data-src').extract()
                images_lst = images_lst + images
                sku = f"{feature_dict.get('Modelo')}_{variation_id}"

            else:
                abs_variation_url = f"https://www.exhibidoreschile.cl{variation_url}"
                data = requests.get(abs_variation_url)
                response = Selector(data)
                variation_qty = response.xpath('.//*[@class="ui-pdp-buybox__quantity__available"]/text()').get()
                key_stock = self.get_stock_key(stock_dict)
                stock_dict[f"stock_{key_stock}"] = self.clean_stock(variation_qty)
                stock_comentarie[f"stock_comentarie_{i}"] = variation_id
                images = response.xpath('.//*[@class="ui-pdp-image lazy-loadable"]/@data-src').extract()
                images_lst = images_lst + images
                sku = f"{feature_dict.get('Modelo')}_{variation_id}"
            images_lst = list(set(images_lst))
            image_dict = {}
            for i,image in enumerate(images_lst):
                image_dict[f"image_{i}"] = image

            data = {

                'title':title,
                'sku' : sku,
                'url_scraped' : product_url, 
                'price' : price,
                'percent_discount' : None,
                'price_discount' : None,
                'tax' : None,
                'price_included_taxes' : None,
                'price_mt2' : None,
                'price_mtl' : None,
                'stock_1' : stock_dict.get('stock_1'),
                'stock_2' : stock_dict.get('stock_2'),
                'stock_3' : stock_dict.get('stock_3'),
                'stock_comentarie_1' : stock_comentarie.get('stock_comentarie_1'),
                'stock_comentarie_2' : stock_comentarie.get('stock_comentarie_2'),
                'stock_comentarie_3' : stock_comentarie.get('stock_comentarie_3'),
                'images' : image_dict,
                'route_product' : breadcrum,
                'short_description' :None,
                'long_description' :description,
                'pdf' :None,
                'length' : None,
                'width' : None,
                'height' : None,
                'weight' : None,
                'main_color' :  None,
                'glossy_or_matte' : None,
                'main_material' :None,
                'origen' : None ,
                'features':feature_dict } 
            
            yield data

