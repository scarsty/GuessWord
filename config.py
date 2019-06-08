#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
