#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/7 15:44
# @Author  : Jia Huameng
# @File    : et_sitemap.py
import scrapy
from scrapy.spiders import SitemapSpider
from ..items import ImgItem


class UGirlsSpider(SitemapSpider):
    name = 'ugirls'
    sitemap_urls = ['http://www.ugirls.com/sitemap.xml']
    sitemap_rules = [
        ('/Models/Detail/', 'parse_model_detail'),
        # ('/Models/', 'parse_category'),
        ('/Content/ListModel/', 'parse_content_list_model'),
        ('/Content/List/', 'parse_content_list'),
        # ('/Content/', 'parse_product'),
        # ('/Shop/Detail/', 'parse_shop_detail'),
        # ('/Video/Detail', 'parse_video_detail'),
        # ('/Video/', 'parse_video'),
        # ('/Shop/Magazine/', 'parse_category'),
        # ('/Shop/', 'parse_category'),
    ]

    def parse_model_detail(self, response):
        name = response.xpath('//h1[@class="name"]/text()').extract_first()
        image_urls = response.xpath('//img[@class="scaleimg"]/@src').extract()
        if image_urls:
            yield ImgItem(name=name, image_urls=image_urls)

    def parse_content_list(self, response):
        name = response.xpath('//div[@class="ren_head_c"]/a/text()').extract_first()
        image_urls = response.xpath('//img[@class="gallery"]/@src').extract()
        if image_urls:
            yield ImgItem(name=name, image_urls=image_urls)

    def parse_content_list_model(self, response):
        name = response.xpath('//div[@class="ren_head"]/h3/text()').extract_first()
        image_urls = response.xpath('//img[@class="gallery"]/@src').extract()
        if image_urls:
            yield ImgItem(name=name, image_urls=image_urls)


#
#  http://www.ugirls.com/Models/Detail/Model-25.html
#  <div class="beautys"><img src="http://img.ugirls.tv/uploads/magazine/content/2014/08/25/834b79959ba74b39680e0f0d21ec0950_magazine_web_l.jpg" class="scaleimg" alt="小潘鼠美女高清原创写真图片" /><a href="/Content/List/Magazine-49.html" class="view" >查看套图</a></div>
#
#  http://www.ugirls.com/Content/ListModel/Model-82.html
#  <li><img src="http://img.ugirls.tv/uploads/magazine/content/2015/05/08/fed5b78baaff23c8af73cdb6fcf44960_magazine_web_l.jpg" title="平面模特:小软 三围:88/64/89 身高:170 年龄:23" class="gallery" id="1061" data="FC87Qg83WEN8C1xFLx5cQzZBW0xScX1EES8wBAgrdUZSC3ZaFh5QBjUkU11VVFxELzRQGA5BAgVqbgUBOR0gBSEnYkN9fWVHOCMOBDYeYV5+bnkCOiAjGjUkbVh9U35bOiAvHyIJeV9qfnkDLwonHyI3ZgB+U3FEFAkrHA==" modelid="82" votecount="1" pid="82" alt="" mem="" /></li>
#
#  http://www.ugirls.com/Content/List/Magazine-204.html
#  <li><img src="http://img.ugirls.tv/uploads/magazine/content/a381ea8328cd2fc698e3029d657061a6_magazine_web_m.jpg" title="梓安高清原创图片6" class="gallery" id="1432" data="FC87Qg83WEN8C1xFLx5cQzZBW0xScX1EES8wBAgrdUZSC3ZaFh5QBjUkU11VVFxELzRQGA5BAgVqbgUBOVUsCCM3cVlpbVdLOA0BGDY3fVhpQ2kEOiA8CCE3fgBqfWkAOx0oQCEkcgd8VEBGLxBUTw==" modelid="149" votecount="1" pid="204" alt="梓安高清原创图片6" mem="0" /></li>
#
#  http://www.ugirls.com/Shop/Detail/Product-267.html
#  <a href="http://www.ugirls.com/Content/List/Magazine-267.html" target="_blank"><img src="http://img.ugirls.tv/uploads/magazine/content/854659de354a39aa55e78f90c2296b0e_magazine_web_m.jpg" class="scaleimg" alt="温鈊怡高清原创图片1" /></a>
#
#  http://www.ugirls.com/Video
#  <a class="this" href="javascript:void(0)" >1</a><a href="Page-2.html" title="第2页" >2</a><a href="Page-3.html" title="第3页" >3</a><a href='Page-2.html' title="第2页" ><img src='/images/xlist_aaaBg.png' alt='页码' /></a>
#  <a class="video_cover" href="http://www.ugirls.com/Video/Detail/Video-38.html" title="尤果网-性感女神宇琦儿拍写真现场 美得不像话"><img class="lazy" data-original="http://img.ugirls.tv/uploads/video/qq/cover/b032464d85251ae157c23d5e1daa9a74.jpg" alt="尤果网-性感女神宇琦儿拍写真现场 美得不像话"/><span class="cover_hover">尤果网-性感女神宇琦儿拍写真现场 美得不像话</span></a>
#  <a href="http://www.ugirls.com/Video/Detail/Video-82.html" class="swiper-slide swiper-no-swiping lazy" data-original="http://img.ugirls.tv/uploads/video/qq/cover/11ea5a772eb6ebb8a5ed380c59cffac2.jpg" title="尤果网-FIFA女玩家李娅萦助阵法国队 事业线如同球队晋级之路">
#
#  http://www.ugirls.com/Video/Detail/Video-83.html
#  <a href="http://static.video.qq.com/TPout.swf?vid=x032440kmix&amp;auto=0" rel="nofollow" target="_blank" style="position: absolute; text-indent: -999999px; width: 700px; height: 100%; left: 0; top: 0;">播放</a>
#  <embed src="http://static.video.qq.com/TPout.swf?vid=x032440kmix&amp;auto=0" allowFullScreen="true" quality="high" width="700" height="495" align="middle" allowScriptAccess="always" type="application/x-shockwave-flash"></embed>

