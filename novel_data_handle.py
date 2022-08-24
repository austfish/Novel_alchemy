import re
import os
import json

class text_processing(object):
    # 类的初始化操作
    def __init__(self):
        # txt文本目录
        self.source_path = './source/'
        self.handle_path = './handle/'
        # 用正则表达式匹配txt文档中的第N章
        self.zhangjie_pattern = r'===第(.*?)章 (.*?)==='
        self.split_flag = u'章'
        self.xunlianji_name = './data.txt'
        self.date = {}
        

    # 获取到文件夹里面的txt文件
    def get_text_file_url(self):
        # 得到文件夹下的所有文件名称
        files = os.listdir(self.source_path)
        # 遍历文件夹
        for file in files:
            if file.split('.')[-1] == 'txt':
                # 获取txt文件地址
                position = self.source_path + file
                # 返回文件地址
                yield position

    def set_json(self, test_dict, json_name):
        try:
            json_str = json.dumps(test_dict, ensure_ascii=False)
            with open(f'{self.handle_path}{json_name}.json', 'w') as json_file:
                json_file.write(json_str)
        except Exception as e:
            print(e)
    
    def set_txt(self, test_dict, txt_name):
        try:
            with open(f'{self.handle_path}{txt_name}.txt',"a") as file:   #只需要将之前的”w"改为“a"即可，代表追加内容
                for a in test_dict.keys():
                    file.write(a+'\n')
                    file.write(test_dict[a])
                    file.write('\n')
            
        except Exception as e:
            print(e)

    def set_txt_shujuji(self, xiaoshuo_content):
        try:
            with open(self.xunlianji_name,"a") as file:   #只需要将之前的”w"改为“a"即可，代表追加内容
                file.write(xiaoshuo_content)
        except Exception as e:
            print(e)

    # 处理txt文本方法
    def text_handle(self):
        for file_name in self.get_text_file_url():
            if os.path.exists(file_name):
                xiaoshuo_name = file_name.split("/")[-1].split(".")[0]
                print(f'开始处理小说：{xiaoshuo_name}')
                # 打开txt文件
                input = open(file_name, encoding='utf-8')
                # 读取txt文件内容
                line = input.readline()
                zhangjie_data = {}
                xiaoshuo_content = ''
                flag = ''
                while line:
                    if not line.strip():
                        # 跳掉空行
                        line = input.readline()
                        continue
                    line = line.encode('utf-8').decode('utf-8')
                    match = re.match(self.zhangjie_pattern, line.strip())
                    if match:
                        flag = f'第{match.group(1)}章 {match.group(2)}'
                        zhangjie_data[flag] = ''
                        xiaoshuo_content += '\n'
                        line = input.readline()
                        continue
                    # print line.split(u'节')[0]
                    zhangjie_data[flag] += line.strip(' ')
                    xiaoshuo_content += line.strip(' ')
                    line = input.readline()
                print(f'小说处理完成：{xiaoshuo_name} 章节数：{len(zhangjie_data.keys())}')
                self.set_json(zhangjie_data, xiaoshuo_name)
                self.set_txt(zhangjie_data, xiaoshuo_name)
                self.set_txt_shujuji(xiaoshuo_content)


    def run(self):
        # 调用处理txt文本方法
        self.text_handle()


if __name__ == '__main__':
    text_proces = text_processing()
    text_proces.run()