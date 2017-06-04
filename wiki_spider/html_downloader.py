# coding: utf8

from urllib import request

class HtmlDownloader(object):
    
    def download(self, url):
        if url is None:
            return None
        
        with request.urlopen(url) as response:
            if response.getcode() != 200:
                return None
            
            return response.read()

if __name__ == '__main__':
    downloader = HtmlDownloader()
    content = downloader.download('http://www.baidu.com/')
    print(content)
