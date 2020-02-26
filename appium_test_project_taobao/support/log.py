# coding=utf-8

import logging
import time
import os
import datetime


def singleton(cls):
    instances = {}

    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton


@singleton
class AutoTestLog():
    def __init__(self):
        # 创建一个logger
        self.logger = logging.getLogger()

        # 置顶日志级别
        self.logger.setLevel(logging.DEBUG)
        # print(self.logger.handlers)

        # 给日志命名
        now = time.strftime("%Y-%m-%d %H-%M-%S")
        log_name = r'E:\software\JetBrains\pycharm\projects\appium_test_project_taobao\output\logs/' + now + '.log'

        # 将日志写入磁盘
        self.file_handle = logging.FileHandler(log_name, 'a', encoding='utf-8')
        self.file_handle.setLevel(logging.DEBUG)

        # 设置日志格式
        file_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s -%(message)s')
        self.file_handle.setFormatter(file_formatter)

        # 给log添加handle
        self.logger.addHandler(self.file_handle)

    def get_log(self):
        return self.logger

    # 关闭handle
    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()

    # def __del__(self):
    #     self.close_handle()
    #     print("销毁")


if __name__ == '__main__':
    obj = AutoTestLog()
    obj.get_log().debug('日志1')
    # obj.close_handle()

    obj2 = AutoTestLog()
    obj2.get_log().debug('日志2')
    # obj2.close_handle()
