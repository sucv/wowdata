import scrapy

class TwoHandedWeaponSpider(scrapy.Spider):
    name = "twoHandedWeapons"

    def start_requests(self):
        urls = [
            'https://cn.classic.wowhead.com/weapons/type:6:1:5:8',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # paths = ["substring-after(//script[@type='text/javascript'], 'WH.Gatherer.addData(3, 4,')", "substring-after(//script[@type='text/javascript'], 'var listviewitems = [')"]
        # rears = [");", "];"]
        # filenames = ["cn_weapon.json", "cn_weaponsupp.json"]
        filename = "test.html"
        # for path, rear, filename in zip(paths, rears, filenames):
        #     content = response.xpath(path).get()
        #     content = content.split(rear)[0].encode()
        with open(filename, 'wb') as f:
            f.write(response.body)
            f.close()

