# SPIKE backend
## based on Python Falcon

> How to run this backend: `gunicorn things:app`

主要文件:
* thing.py
基于Python Falcon框架。处理简单的get／post请求。
on_get方法处理前端发来的get请求。

* evalnn.py
根据输入，返回分诊结果。