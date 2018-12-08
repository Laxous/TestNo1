# -*- coding: utf-8 -*-
# @Time    : 2018/09/29 17：00
# @File    : LogConfig.py
# @desc:配置文件获取辅助封装类
import os
import time


class PathConfig:
    """
    配置文件获取辅助封装类
    """

    @classmethod
    def logpath(self):
        # 获取系统当前时间，创建一个handler，用于写入日志文件
        rq = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))

        p = os.path.dirname(os.path.realpath(__file__))
        p = os.path.dirname(p)
        dir_path = os.path.join(p, 'logs', 'TestLog' + rq + '.logs')

        log_path = os.path.dirname(os.path.abspath('.')) + '\\logs\\'
        log_name = log_path + 'TestLog' + rq + '.logs'
        return dir_path


if __name__ == "__main__":
    print(PathConfig.logpath())
