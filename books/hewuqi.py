#!/usr/bin/env python
# -*- coding:utf-8 -*-

from base import BaseFeedBook # 继承基类BaseFeedBook


def getBook():
    return hewuqi

class hewuqi(BaseFeedBook):
    title                 = u'2048核基地'# 设定标题
    description           = u'人人为我，我为人人'# 设定简介
    language              = 'zh-cn'# 设定语言
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_2048.gif"# 设定标头图片
    coverfile             = "cv_2048.jpg"# 设定封面图片
    oldest_article        = 1  # 设定文章的时间范围。小于等于365则单位为天，否则单位为秒，0为不限制
    max_articles_per_feed = 40 # 设定每个主题下要最多可抓取的文章数量
    fulltext_by_readability = True    
    
    # 指定要提取的包含文章列表的主题页面链接
    # 每个主题是包含主题名和主题页面链接的元组
    feeds = [
            (u'综合小说', 'https://rsshub.app/2048/bbs/105'),
            (u'乱伦迷情', 'https://rsshub.app/2048/bbs/50'),
            (u'武侠虚幻', 'https://rsshub.app/2048/bbs/52'),
            (u'青春校园', 'https://rsshub.app/2048/bbs/51'),
            (u'人妻意淫', 'https://rsshub.app/2048/bbs/103'),
            (u'激情都市', 'https://rsshub.app/2048/bbs/49'),
            (u'长篇连载', 'https://rsshub.app/2048/bbs/54'),
            (u'卡通动漫', 'https://rsshub.app/2048/bbs/28'),
            (u'露出偷窺', 'https://rsshub.app/2048/bbs/26'),
            (u'COSPLAY', 'https://rsshub.app/2048/bbs/277'),
            (u'原创自拍', 'https://rsshub.app/2048/bbs/135'),
            ]
            

    
    def fetcharticle(self, url, opener, decoder):
        #每个URL都增加一个后缀full=y，如果有分页则自动获取全部分页
        url += '?full=y'
        return BaseFeedBook.fetcharticle(self,url,opener,decoder)

        