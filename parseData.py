import re
import base64
from fontTools.ttLib import TTFont
from lxml import etree
import xml.etree.ElementTree as et


class parseData():
    '''
    解析提取数据模块
    '''
    def get_car_urls(self,html):
        '''
        提取这一页中的车辆详细信息的 url
        :param html:
        :return:
        '''
        html = etree.HTML(html)
        car_urls = html.xpath('//a[@target="_blank"]/@data-url')
        car_urls = list(car_urls)
        return car_urls

    def get_info(self,html):
        '''
        提取详情页的信息
        '''
        try: # 过滤掉不是二手车的 url
            # 字体加密文件 url
            fontUrl = re.findall("base64,(.*?)'", html,re.S)[0]

            # 交易地点
            add = re.findall('data-adress="(.*?)"',html,re.S)[0]
            # 标题
            title = re.findall('<h1 class="info-title">(.*?)</h1>',html,re.S)[0]
            # 交易价
            price = re.findall('<em class="info-price_usedcar strongbox">(.*?)</em>', html, re.S)[0]
            # 新车报价
            newPrice = re.findall('d="financeNewcar" >新车报价：(.*?)万</a>',html,re.S)[0]

            html = etree.HTML(html)
            # 表显里程
            mileage = html.xpath('/html/body/section[1]/div/div[3]/ul/li[1]/span[1]/text()')[0]
            # 首次上牌
            numberTime = html.xpath('/html/body/section[1]/div/div[3]/ul/li[2]/span[1]/text()')[0]
            # 排量
            displacement = html.xpath('/html/body/section[1]/div/div[3]/ul/li[3]/span[1]/text()')[0]
            # 变速箱
            speedBox = html.xpath('/html/body/section[1]/div/div[3]/ul/li[4]/span[1]/text()')[0]
            # 排放标准
            standard = html.xpath('/html/body/section[1]/div/div[3]/ul/li[5]/span[1]/text()')[0]


            # price 字体反爬破解
            #print(price) # 调试用确认字体对应上了
            price = self.get_price(price,fontUrl)

            return [title,price,newPrice,add,mileage,numberTime,displacement,speedBox,standard]
        except:
            return []

    def get_price(self,price,fontUrl):
        '''
        解码字体反爬
        '''
        # 将字体文件 base64 解码，以二进制写入 woff 文件
        fontdata = base64.b64decode(fontUrl)
        file = open('58.woff', 'wb')
        file.write(fontdata)
        file.close()

        # 读取字体
        font = TTFont("58.woff")
        # 生存成 xml 文件
        font.saveXML('font.xml')

        # 读取 xml 文件，映射对应正确的数字
        root = et.parse('font.xml').getroot()
        con = root.find('cmap').find('cmap_format_4').findall('map')
        for i in con:
            num = i.attrib['name']
            code = i.attrib['code'].replace('0x', '&#x') + ';'
            price = price.replace(code, str(int(num[-2:]) - 1))

        return price






