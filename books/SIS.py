#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return SIS

class SIS(BaseFeedBook):
    title                 = u'SexInSex'
    description           = u''
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_SIS.gif"
    coverfile             = "cv_SIS.jpg"
    oldest_article        = 1
    
    feeds = [
            (u'新文发布区', 'https://rsshub.app/sexinsex/372'),
            (u'武侠玄幻区', 'https://rsshub.app/sexinsex/96'),
            (u'凌辱情感区', 'https://rsshub.app/sexinsex/279'),
            (u'另类酷文区', 'https://rsshub.app/sexinsex/31'),
            (u'乱伦人妻区', 'https://rsshub.app/sexinsex/110'),
            ]
    
    def fetcharticle(self, url, opener, decoder):
        #每个URL都增加一个后缀full=y，如果有分页则自动获取全部分页
        url += '?full=y'
        return BaseFeedBook.fetcharticle(self,url,opener,decoder)
        