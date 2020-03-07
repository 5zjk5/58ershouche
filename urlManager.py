class urlManager():
    '''
    管理 url 模块
    '''
    def __init__(self):
        '''
        初始化 url
        '''
        # 页数 url 构造
        # 此 url 是深圳的
        self.page_urls = ['https://sz.58.com/ershouche/pn{}/?PGTID=0d100000-0000-47cd-346a-1ea93a99e1ce&ClickID=55'
                              .format(str(i)) for i in range(1,71)]

    def get_page_urls(self):
        '''
        返回页面 url
        :return:
        '''
        return self.page_urls

