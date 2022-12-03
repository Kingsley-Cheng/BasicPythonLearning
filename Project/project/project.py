import re
from concurrent.futures import ThreadPoolExecutor

import requests
from lxml import etree

def get_detail_href(url):
    """
    该函数负责获取到每一个详情页的值
    """
    print("开始分析主界面")
    resp = requests.get(url)
    resp.encoding = "utf-8"
    et = etree.HTML(resp.text)
    hrefs = et.xpath("//div[@class = 'each_truyen']/a/@href")
    print("分析完成")
    return hrefs[0]

def get_page_srcs(url):
    print("开始抓取子页面")
    resp = requests.get(url)
    resp.encoding = "utf-8"
    et = etree.HTML(resp.text)
    hrefs = et.xpath("//ul[@class='list-chapter']/li/a/@href")
    hrefs = [hrefs[0], hrefs[6]]
    print("抓取成功")
    return hrefs

# src1：下载小说起始页url, src2：终止页url
def download_text(src1, src2):
    # 下载章节计数器
    t = 0
    print("开始下载章节")
    while True:
        # 请求对于章节的url
        resp = requests.get(src1)
        # 定义返回response对象编码形式
        resp.encoding = "utf-8"
        # 定义正则表达式
        obj = re.compile(r'<p>(.*?)</p>', re.S)
        # 使用正则表达式匹配返回的html页面，得到章节小说内容
        content1 = obj.findall(resp.text)
        # 将返回的列表转化为字符串
        content = "".join(content1)
        # 做初步的内容清洗，将&#8230转译为"..."
        content = content.replace("&#8230", "...")
        # 编写写入函数，写入程序文件下的book.text文件，写入方式是追加
        with open(f"book", mode="a") as f:
            f.write(content)
        # 判断是否是最后一页，或者章节下载次数超过5000，提高程序的鲁棒性
        if src1 == src2 or t > 5000:
            break
        # 用xpath的方法匹配出下一章节的url
        et = etree.HTML(resp.text)
        src1 = et.xpath('//a[@id = "next_chap" ]/@href')[0]
        # 计数器加一
        t = t + 1
        print(t)
    print("下载本书完毕")

def main():
    url = "https://engnovel.com/most-popular-novels"
    # 1. 抓取到首页中详情页到href
    hrefs = get_detail_href(url)
    # 2. 获得第一章和最后一章的url
    page_src_list = get_page_srcs(hrefs)
    # 3. 下载小说
    download_text(page_src_list[1],page_src_list[0])


if __name__ == "__main__":
    main()
