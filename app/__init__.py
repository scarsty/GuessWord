#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
