import os
import configparser
from datetime import datetime, timedelta


def project_path():
    # 获取当前文件的文件名包括后缀
    # print(os.path.basename(__file__))

    # 获取当前文件的所在目录
    # print(os.path.dirname(__file__))
    # print(os.getcwd())

    # print(os.path.realpath(__file__))
    # print(os.path.abspath(__file__))

    # print(os.path.join(os.getcwd(), ".."))

    # 获取当前文件所在目录的上级目录
    # print(os.path.abspath(os.path.join(os.getcwd(), "..")))

    # 获取当前文件所在目录的上上级目录
    # print(os.path.abspath(os.path.join(os.getcwd(), "../..")))

    dir_of_file = os.path.abspath(os.path.join(os.getcwd(), ".")) + os.path.sep
    # print(dir_of_file)
    return dir_of_file


def config_url():
    config = configparser.ConfigParser()
    # print(os.path.join(project_path() + "config.ini"))
    config.read(os.path.join(project_path() + "config.ini"))
    # print(config.get('testURL', 'url'))
    return config.get('testURL', 'url')


def next_day_date(n):
    """
    返回第二天日期，n为1即：今天加1天为明天，n=2即：今天加2天，一次类推
    :param n:
    :return: 例如：2020-12-12
    """
    return str((datetime.today() + timedelta(days=+int(n))).strftime("%Y-%m-%d"))


if __name__ == "__main__":
    # print("项目的目录为：%s" % project_path())
    # print(os.path.sep + os.path.sep)
    # print("被测试系统的地址为： %s" % config_url())

    # 获取当前文件的文件名包括后缀
    print(os.path.basename(__file__))

    # 获取当前文件的所在目录
    print(os.path.dirname(__file__))
    print(os.getcwd())

    # print(os.path.realpath(__file__))
    # print(os.path.abspath(__file__))

    # print(os.path.join(os.getcwd(), ".."))

    # 获取当前文件所在目录的上级目录
    # print(os.path.abspath(os.path.join(os.getcwd(), "..")))

    # 获取当前文件所在目录的上上级目录
    # print(os.path.abspath(os.path.join(os.getcwd(), "../..")))