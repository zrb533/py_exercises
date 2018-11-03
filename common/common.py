# -*- coding: utf-8 -*-#
import datetime

def logs(error,log_path):
    type_error = "错误类型：" + str(type(error))
    content_error = "错误内容：" + str(error)
    currency_time = "时间：" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    error = currency_time + ' ' * 5 + type_error + ' ' * 5 + content_error + ' ' * 5 + __file__
    file = open(log_path, 'a')
    file.write(error + '\n')
    file.close()