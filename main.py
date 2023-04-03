from push import *                  # 导入编写的推送模块
import time                         # 导入python自带时间模块
import urllib.request,urllib.error  # 获取网页数据

# 编写主函数
def main():
    baseurl = "https://www.18art.art/html/notices/"     # 网站url
    askURL(baseurl)

# 爬取网站
def askURL(url):
    head = {  # 模拟浏览器头部信息，向服务器发送消息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.198Safari / 537.36"
    }  # 用户代理——表示告诉服务器，我们是什么类型的机器·浏览器（本质上是告诉浏览器，我们可以接受什么水平的文件内容）

    request = urllib.request.Request(url, headers=head)
    html = ''

    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print("---正在爬取页面HTML，请稍等---")
        print(html)       #测试：查看页面HTML

        date = time.strftime('%Y-%m-%d',time.localtime(time.time()))    # 获取今天日期
        # print(date)
        if date in html:                    # 如果今天有更新的就推送
            push(1)
            print("更新啦")
        else:
            push(0)
            print("未更新")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):       #判断e对象是否包含对应的属性
            e = str(e.code)
            print("爬取失败，e.code" + e)
        if hasattr(e,"reason"):
            e = str(e.reason)
            print("爬取失败，e.reason:" + e)
    return html

if __name__ == "__main__":
    #调用函数
    main()
    print("运行完毕")
