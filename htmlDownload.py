import requests
from fake_useragent import UserAgent


class htmlDownload():
    '''
    下载 html 模块
    '''
    def get_html(self,url,i):
        """
        请求 url 获得 html
        :param url:
        :return:
        """
        i += 1
        headers = {
            'User-agent': UserAgent().random,
            'cookie' : 'f=n; commontopbar_new_city_info=4%7C%E6%B7%B1%E5%9C%B3%7Csz; f=n; commontopbar_new_city_info=4%7C%E6%B7%B1%E5%9C%B3%7Csz; userid360_xml=749BD78641598CE9024E6AF170047A16; time_create=1586144934369; id58=e87rZl5hy6aTbfsHDHdKAg==; 58tj_uuid=2db3f8a5-c1a2-4729-bcd0-84f8c03126a5; als=0; wmda_uuid=1be013d936269e38ff5b69af68b19b87; wmda_new_uuid=1; xxzl_deviceid=Zd%2BUwi7GWjjPmAhGXwEoPG5MwW9kjB1TzcegXAg2ZmJOBkqk8Gz%2FnYF587zbIE06; wmda_visited_projects=%3B11187958619315%3B6333604277682%3B1732038237441; gr_user_id=e82dfdbe-8049-4702-80e2-c2d980c03096; xxzl_sid="6EOlhA-Ur7-LxW-Slh-1vUmXyoNk"; ppStore_fingerprint=2BDF61F13E4C90A0269CDD22837323DC4DBD0F6A1A72022A%EF%BC%BF1583506630712; xxzl_token="O83rdEaQFKJIb5hAMPM9NYVjBpLK6PhZM0gC28pw2mwbqQoyMpyx68EWGCY1QfLrin35brBb//eSODvMgkQULA=="; f=n; commontopbar_new_city_info=4%7C%E6%B7%B1%E5%9C%B3%7Csz; new_uv=9; utm_source=; init_refer=https%253A%252F%252Fwww.58.com%252Fchangecity.html%253Ffullpath%253D0%2526PGTID%253D0d100000-007d-f3e8-0b7b-cf726e795193%2526ClickID%253D3; spm=; commontopbar_ipcity=gy%7C%E8%B4%B5%E9%98%B3%7C0; sessionid=c7839c54-f399-4bcc-968e-cce88f2c7140; wmda_session_id_1732038237441=1583552930897-504682f2-9b90-85df; wmda_session_id_11187958619315=1583552931130-42c270b6-a8eb-dd9f; new_session=0; city=gz; 58home=gz; xxzl_cid=9402ed209b6b4f5c9409a804c0605309; xzuid=e9ef5897-0f67-4f3c-9af3-882112739c10',
            'referer' : 'https://sz.58.com/ershouche/pn{}/?PGTID=0d100000-0000-47cd-346a-1ea93a99e1ce&ClickID=55'.format(str(i))
        }
        while True: # 代理出问题换代理
            try:
                proxies = self.get_proxy()
                response = requests.get(url, headers=headers,proxies=proxies)
                break
            except:
                continue
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        else:
            return None

    def get_proxy(self):
        '''
        获得代理
        阿布云代理：
        '''
        # 代理服务器
        proxyHost = "http-dyn.abuyun.com"
        proxyPort = "9020"

        # 代理隧道验证信息
        proxyUser = 'H6822Y7628879Q7D'
        proxyPass = '5BB2C6EB864BCFC1'

        proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
            "user": proxyUser,
            "pass": proxyPass,
        }

        proxies = {
            "http": proxyMeta,
            "https": proxyMeta,
        }

        return proxies

