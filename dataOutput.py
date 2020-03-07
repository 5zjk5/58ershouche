import csv


class dataOutput():
    '''
    数据输出模块
    '''
    def __init__(self):
        '''
        初始化文件，创建 csv
        '''
        head = ['车辆名称','交易价（万）','新车报价（万）','交易地址','行驶里程',
                '上牌时间','排量','变速箱','排放标准']
        with open('ershou.csv','w+',encoding='utf8',newline='') as f:
            w = csv.writer(f)
            w.writerow(head)

    def write_to_csv(self,infos):
        '''
        写入 csv:
        :return:
        '''
        with open('ershou.csv','a+',encoding='utf8',newline='') as f:
            w = csv.writer(f)
            w.writerow(infos)
