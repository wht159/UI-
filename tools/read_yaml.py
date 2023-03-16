# 定义函数
import yaml

from config import BASE_PATH
import os


def read_yaml(filename):
    file_path = BASE_PATH + os.sep + "data" + os.sep + filename
    with open(file_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
        return data


def read_yaml2(filename):
    file_path = BASE_PATH + os.sep + "data" + os.sep + filename
    # 定义空列表组装测试数据
    arr = []
    # 获取文件流

    with open(file_path, "r", encoding="utf-8") as f:
        # 遍历调用yaml.safe_ load(f) .values( )方法
        for datas in yaml.safe_load(f).values():
            arr.append(tuple(datas.values()))
    # 返回结果
    return arr


