import scrapy

class TwoHandedWeaponSpider(scrapy.Spider):
    name = "allWeapon"

    def start_requests(self):
        urls = [
            'https://classic.wowhead.com/weapons/type:15',
            'https://classic.wowhead.com/weapons/type:13',
            'https://classic.wowhead.com/weapons/type:0',
            'https://classic.wowhead.com/weapons/type:4',
            'https://classic.wowhead.com/weapons/type:7',
            'https://classic.wowhead.com/weapons/type:6',
            'https://classic.wowhead.com/weapons/type:10',
            'https://classic.wowhead.com/weapons/type:1',
            'https://classic.wowhead.com/weapons/type:5',
            'https://classic.wowhead.com/weapons/type:8',
            'https://classic.wowhead.com/weapons/type:2',
            'https://classic.wowhead.com/weapons/type:18',
            'https://classic.wowhead.com/weapons/type:3',
            'https://classic.wowhead.com/weapons/type:16',
            'https://classic.wowhead.com/weapons/type:19',
            'https://classic.wowhead.com/weapons/type:20',
            'https://classic.wowhead.com/weapons/type:14',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        paths = ["substring-after(//script[@type='text/javascript'], 'WH.Gatherer.addData(3, 4,')", "substring-after(//script[@type='text/javascript'], 'var listviewitems = [')"]
        rears = [");", "];"]
        filenames = ["all_weapon.json", "all_weapon_supp.json"]
        # filename = "all_test.html"
        for path, rear, filename in zip(paths, rears, filenames):
            content = response.xpath(path).get()
            content = content.split(rear)[0].encode()
            with open(filename, 'ab') as f:
                f.write(content)

