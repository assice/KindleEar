#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return hewuqi

class hewuqi(BaseFeedBook):
    title                 = u'2048核基地'
    description           = u'2048'# 设定标题:
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_2048.gif"
    coverfile             = "cv_2048.jpg"
    oldest_article        = 1
    
    feeds = [
            (u'综合小说', 'https://rsshub.app/2048/bbs/105'),
            (u'乱伦迷情', 'https://rsshub.app/2048/bbs/50'),
            (u'武侠虚幻', 'https://rsshub.app/2048/bbs/52'),
            (u'青春校园', 'https://rsshub.app/2048/bbs/51'),
            (u'人妻意淫', 'https://rsshub.app/2048/bbs/103'),
            (u'激情都市', 'https://rsshub.app/2048/bbs/49'),
            (u'长篇连载', 'https://rsshub.app/2048/bbs/54'),
            (u'原创自拍', 'https://rsshub.app/2048/bbs/135'),
            ]
    
    def fetcharticle(self, url, opener, decoder):
        #每个URL都增加一个后缀full=y，如果有分页则自动获取全部分页
        url += '?full=y'
        return BaseFeedBook.fetcharticle(self,url,opener,decoder)
        