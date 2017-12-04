# -*- coding: utf-8 -*-
import json
import requests

class servicerequest(object):
    def get(url,para,headers):
        try:
            r = requests.get(url,params=para,headers=headers)
            print("获取返回的状态码",r.status_code)
            json_r = r.json()
            print("json类型转化成python数据类型",json_r)
        except BaseException as e:
            print("请求失败！",str(e))
    def post(url,para,headers):
        try:
            r = requests.post(url,data=para,headers=headers)
            print("获取返回的状态码",r.status_code)
            json_r = r.json()
            print("json类型转化成python数据类型",json_r)
        except BaseException as e:
            print("请求失败！",str(e))
    def post_json(url,para,headers):
        try:
            data = para
            data = json.dumps(data)   #python数据类型转化为json数据类型
            r = requests.post(url,data=data,headers=headers)
            print("获取返回的状态码",r.status_code)
            json_r = r.json()
            print("json转换为python数据类型：",json_r)
        except BaseException as e:
            print("请求失败！",str(e))
