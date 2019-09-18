# -*- coding : utf-8 -*- #

__author__ = "Gallen_qiu"

import requests,json
class Fxbaogao:
    def __init__(self):
        self.user_id=''
        self.user_token=''

        self.headers={}
        self.headers1={}
        self.url_zt=input("粘贴报告地址(光标移动到着按enter)：")
        self.id=''
        self.fileName=''
    def req(self):
        url='https://api.mofoun.com/mofoun/file/pdf/url?docId={}&docType=2'.format(self.id)

        response=requests.get(url,headers=self.headers)
        data=json.loads(response.text)["data"]

        url1='https://oss-buy.hufangde.com'+data
        response = requests.get(url1, headers=self.headers)
        print("在下载了，等一哈啊!")
        with open("{}.pdf".format(self.fileName),"wb")as f:
            f.write(response.content)

    def scheduler(self):
        with open ('code.txt','r') as f :
            lines=f.readlines()
            self.user_id=lines[0].replace(" ",'').split(":")[1].replace("\n",'')
            self.user_token = lines[1].replace(" ", '').split(":")[1].replace("\n", '')

            self.headers1 = {'Host': 'api.mofoun.com',
                   'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64;rv:64.0)Gecko/20100101Firefox/64.0',
                   'Accept': '*/*',
                   'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                   'Accept-Encoding': 'gzip,deflate,br',
                   'Referer': 'https://www.fxbaogao.com/pdf/?id=1341436',
                   'version': '110100',
                 'user-id': str(self.user_id),
                 'user-token': str(self.user_token),
                   'content-type': 'application/json;charset=UTF-8',
                   'origin': 'https://www.fxbaogao.com',
                   'Content-Length': '49',
                   'Connection': 'keep-alive',
                   'TE': 'Trailers',
                   'Pragma': 'no-cache',
                   'Cache-Control': 'no-cache'
                   }
            self.headers = {
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Origin": "https://www.fxbaogao.com",
                "Referer": "https://www.fxbaogao.com/pdf/?id=1341436&query=%7B%22pageSize%22%3A20%2C%22pageNum%22%3A1%2C%22paragraphSize%22%3A3%2C%22keywords%22%3A%22%E4%BA%92%E8%81%94%E7%BD%91%E4%BF%9D%E9%99%A9%22%2C%22order%22%3A%222%22%2C%22pdfPage%22%3A%22-1%22%7D",
                "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/74.0.3729.169Safari/537.36",
                'user-id': self.user_id,
                'user-token': str(self.user_token),
                "VERSION": "000000",
            }
        # print(self.headers)
        print(self.id,self.user_token)
        self.id = self.url_zt.split("&query")[0].split("?id=")[1]
        self.req_main()
        self.req()

    def req_main(self):


        url='https://api.mofoun.com/mofoun/search/report/search'

        data={"docId":self.id,"pageNum":1,"paragraphSize":999}
        data = json.dumps(data)
        response=requests.post(url,headers=self.headers1,data=data)
        print(response.text)
        data = json.loads(response.content)["data"]["dataList"][0]
        try:
            title=data["title"]
        except:
            title="未知文件名"
        try:
            orgName=data["orgName"]
        except:
            orgName="未知机构"
        try:
            uploadUserName=data["uploadUserName"]
        except:
            uploadUserName="未知上传者"

        fileName='{}_{}'.format(title,orgName)
        self.fileName=fileName

if __name__ == '__main__':
    F=Fxbaogao()
    F.scheduler()

