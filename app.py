#!/usr/bin/env python 
# -*- coding: UTF-8 -*-
#
# Copyright 2014 Eric Zhong 
#


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()


# vim: tabstop=4 shiftwidth=4 softtabstop=4

