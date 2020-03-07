from urlManager import urlManager
from htmlDownload import htmlDownload
from parseData import parseData
from dataOutput import dataOutput
import time


class spider():
    '''
    爬虫主逻辑
    '''
    def __init__(self):
        '''
        初始化各个模块
        '''
        self.manager = urlManager()
        self.download = htmlDownload()
        self.parse = parseData()
        self.output = dataOutput()

    def start(self):
        '''
        爬虫开始
        :return:
        '''
        page_urls = self.manager.get_page_urls()
        for i,page_url in enumerate(page_urls):
            html = self.download.get_html(page_url,i)
            car_urls = self.parse.get_car_urls(html)
            for car_url in car_urls:
                html = self.download.get_html(car_url,i)
                # print(car_url) # 调试用，确认字体破解的正确
                infos = self.parse.get_info(html)
                if infos == []: # 过滤不是二手车的 url
                    continue
                infos.append(car_url)
                self.output.write_to_csv(infos)
                time.sleep(1)
            print('第 %s 页爬取完毕' % str(i+1))


if __name__ == '__main__':
    '''
    主接口
    '''
    spider = spider()
    spider.start()