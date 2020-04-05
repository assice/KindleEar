#!/usr/bin/env python
# -*- coding:utf-8 -*-

from base import BaseFeedBook # 继承基类BaseFeedBook


def getBook():
    return SIS

class SIS(BaseFeedBook):
    title                 = u'SexinSex'# 设定标题
    description           = u''# 设定简介
    language              = 'zh-cn'# 设定语言
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_SIS.gif"# 设定标头图片
    coverfile             = "cv_SIS.jpg"# 设定封面图片
    oldest_article        = 1  # 设定文章的时间范围。小于等于365则单位为天，否则单位为秒，0为不限制
    max_articles_per_feed = 40 # 设定每个主题下要最多可抓取的文章数量
    
    
    # 指定要提取的包含文章列表的主题页面链接
    # 每个主题是包含主题名和主题页面链接的元组
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
 
    
        