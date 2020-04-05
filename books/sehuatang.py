#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return sehuatang

class sehuatang(BaseFeedBook):
    title                 = u'色花堂'# 设定标题:
    title                 = u''
    description           = u''
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_SHT.gif"
    coverfile             = "cv_SHT.jpg"
    oldest_article        = 1
    
    feeds = [
            (u'卡通动漫', 'https://rsshub.app/dsndsht23/117/648'),
            (u'武侠虚幻', 'https://rsshub.app/dsndsht23/138'),
            (u'青春校园', 'https://rsshub.app/dsndsht23/137'),
            (u'乱伦人妻', 'https://rsshub.app/dsndsht23/135'),
            (u'激情都市', 'https://rsshub.app/dsndsht23/136'),
            ]
    
    def fetcharticle(self, url, opener, decoder):
        #每个URL都增加一个后缀full=y，如果有分页则自动获取全部分页
        url += '?full=y'
        return BaseFeedBook.fetcharticle(self,url,opener,decoder)
        