#!/usr/bin/env python
# encoding: utf-8

"""
    File name: vip.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""
from flask.ext.restful import reqparse


# ------------ vip add parser ------------
vip_post_parser = reqparse.RequestParser()
vip_post_parser.add_argument(
    'username', dest='username',
    type=unicode, location='form',
    required=True, help='The vip\'s username',
)

vip_post_parser.add_argument(
    'nickname', dest='nickname',
    type=unicode, location='form',
    required=True, help='The vip\'s nickname',
)

vip_post_parser.add_argument(
    'phone', dest='phone',
    type=str, location='form',
    required=False, help='The vip\'s phone',
)
