#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return Caoliu

class Caoliu(BaseFeedBook):
    title                 = u'草榴社区'
    description           = u'1024。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_1024.gif"
    coverfile             = "cv_1024.jpg"
    oldest_article        = 1
    
    feeds = [
            (u'技術討論區', 'https://rsshub.app/t66y/7'),
            (u'達蓋爾的旗幟', 'https://rsshub.app/t66y/16'),
            (u'文學交流區', 'https://rsshub.app/t66y/70'),
            ]
    
    def fetcharticle(self, url, opener, decoder):
        #每个URL都增加一个后缀full=y，如果有分页则自动获取全部分页
        url += '?full=y'
        return BaseFeedBook.fetcharticle(self,url,opener,decoder)
        