# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class DuplicatesPipeline(object):

    def open_spider(self, spider):
        if os.path.exists('images.json'):
            with open('images.json', 'r') as fp:
                self.images = json.load(fp)
        else:
            self.images = []

    def close_spider(self, spider):
        with open('images.json', 'w') as fp:
            json.dump(self.images, fp)

    def process_item(self, item, spider):
        image_urls = item.get('image_urls', [])
        image_urls = [url for url in image_urls if url and url.split('/')[-1] not in self.images]
        if not image_urls:
            raise DropItem("Duplicate, no need download")
        self.images.extend([url.split('/')[-1] for url in image_urls])
        item['image_urls'] = image_urls
        return item


class ImgPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]      # ok判断是否下载成功
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item


class UgirlsPipeline(object):
    def open_spider(self, spider):
        if os.path.exists('ugirls.json'):
            with open('ugirls.json', 'r') as fp:
                self.ugirls = json.load(fp)
        else:
            self.ugirls = {}

    def close_spider(self, spider):
        with open('ugirls.json', 'w') as fp:
            json.dump(self.ugirls, fp)

    def process_item(self, item, spider):
        name = item.get('name')
        if name:
            image_paths = self.ugirls.get(name, [])
            image_paths.extend(item.get('image_paths', []))
            image_paths = list(set(image_paths))
            self.ugirls[name] = image_paths
        return item