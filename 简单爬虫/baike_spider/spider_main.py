# coding:utf-8

from baike_spider import html_downloader,url_manager,html_parser,html_outputer

class SpiderMain(object):
    def __init__(self):
        #url 管理器
        self.urls = url_manager.Urlmanager()
        #网页下载器
        self.downoader = html_downloader.HtmlDownloader()
        #网页解析器
        self.paeser = html_parser.HtmlParser()
        #输出器
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        print(root_url)
        #记录当前爬去的第几个url
        count =1
        #将入口url添加进url管理器
        self.urls.add_new_url(root_url)
        #启动爬虫循环(如果有待爬去的url)
        while self.urls.has_new_url():

            try:
                # 获取一个待爬取的url
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                # 启动下载器下载页面
                html_cont = self.downoader.download(new_url)
                # 调用解析器解析数据，得到新的url列表和新的数据
                # new_url - 爬取好的url
                # html_cont - 下载好的页面数据
                new_urls, new_data = self.paeser.parse(new_url, html_cont)
                # 新的url和新的数据分别处理
                # 新的url添加进url管理器
                self.urls.add_new_urls(new_urls)
                # 收集数据
                self.outputer.collect_data(new_data)

                # 爬取1000个页面
                if count == 10:
                    break

                count = count + 1
            except:
                print("爬取失败")

        self.outputer.output_html()






# 创建main函数
if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/item/Python/407313'
    obj_spider = SpiderMain()
    # 启动爬虫
    obj_spider.craw(root_url)




