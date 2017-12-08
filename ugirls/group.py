#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/8 16:10
# @Author  : Jia Huameng
# @File    : group.py
import os
import json
import shutil


def group():
    with open('ugirls.json', 'r') as fp:
        ugirls = json.load(fp)
        for name, image_paths in ugirls.iteritems():
            dir_name = u'images/models/{}'.format(name)
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            for path in image_paths:
                if not path:
                    continue
                path = path.split('/')[-1]
                src = u'images/models/{}'.format(path)
                dst = u'{}/{}'.format(dir_name, path)
                if os.path.exists(src):
                    if not os.path.exists(dst):
                        shutil.move(src, dst)
                    else:
                        os.remove(src)

# group()
with open('images.json', 'r') as fp:
    images = json.load(fp)
    print len(images)
    images = [img for img in images if img.endswith('magazine_web_m.jpg')]
    print len(images)
    images = list(set([img.split('_')[0] for img in images]))
    print len(images)

# with open('images.json', 'w') as fp:
#     json.dump(images, fp)


