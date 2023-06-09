# coding:utf-8
import csv
import json
import time
import os.path
import requests
from datetime import datetime

# 创建文件夹
path1 = r'D:\数据\预约数据\\'


def create_folders(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"已创建文件夹: {path}")
    else:
        print(f"文件夹已存在: {path}")


create_folders(path1)
file_name = path1 + "预约数据.csv"  # 数据保存位置
file_error_name = path1 + "预约数据-出错信息.txt"  # 错误信息位置

while True:

    # "蔚蓝档案官网数据"
    try:
        url = 'https://bluearchive-cn.com/api/pre-reg/stats'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'}

        response = requests.get(url, headers=headers)
        data_dict = json.loads(response.text)
        Ba_ba_api = data_dict['data']['count']
        print("官网数据 " + str(Ba_ba_api))

    except Exception as e:
        # 获取当前时间
        now = datetime.now()
        minute = now.strftime("%Y-%m-%d %H:%M")  # 格式化为精确到分钟的字符串
        print("当前时间" + minute)
        # 输出出错信息到文件
        with open(file_error_name, mode='a', newline='') as f:
            f.write(minute + " 错误信息 蔚蓝档案官网 " + str(e) + '\r\n')
        print("Error:", e)
        Ba_ba_api = -1

    # "Bilibili数据"
    try:
        url = 'https://line1-h5-pc-api.biligame.com/game/detail/gameinfo?game_base_id=109864&ts=1680239994877&request_id=cbniUTkIyXpfwxAB83WGglr8getUcGIP&appkey=h9Ejat5tFh81cq8V&sign=b7c535ab5c6b5c9ca718dd430e8928bc'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'}

        response = requests.get(url, headers=headers)
        data_dict = json.loads(response.text)
        Bili_ba_api = data_dict['data']['book_num']
        print("B站数据 " + str(Bili_ba_api))

    except Exception as e:
        # 获取当前时间
        now = datetime.now()
        minute = now.strftime("%Y-%m-%d %H:%M")  # 格式化为精确到分钟的字符串
        print("当前时间" + minute)
        # 输出出错信息到文件
        with open(file_error_name, mode='a', newline='') as f:
            f.write(minute + " 错误信息 B站 " + str(e) + '\r\n')
        print("Error:", e)
        Bili_ba_api = -1

    # "TapTap数据"
    try:
        url = 'https://www.taptap.cn/webapiv2/app/v2/detail-by-id/316964?X-UA=V%3D1%26PN%3DWebApp%26LANG%3Dzh_CN%26VN_CODE%3D100%26VN%3D0.1.0%26LOC%3DCN%26PLT%3DPC%26DS%3DAndroid%26UID%3D403e642a-90ca-42a4-9bef-faa806d58dc1%26VID%3D3126483%26DT%3DPC%26OS%3DWindows%26OSV%3D10'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'}

        response = requests.get(url, headers=headers)
        data_dict = json.loads(response.text)
        Tap_ba_api = data_dict['data']['stat']['reserve_count']
        print("Tap数据 " + str(Tap_ba_api))
    except Exception as e:
        # 获取当前时间
        now = datetime.now()
        minute = now.strftime("%Y-%m-%d %H:%M")  # 格式化为精确到分钟的字符串
        print("当前时间" + minute)
        # 输出出错信息到文件
        with open(file_error_name, mode='a', newline='') as f:
            f.write(minute + " 错误信息 Tap " + str(e) + '\r\n')
        print("Error:", e)
        Tap_ba_api = -1

    #   写入文件
    try:
        sum = Ba_ba_api + Bili_ba_api + Tap_ba_api
        print("合计人数 " + str(sum))

        # 获取当前时间
        now = datetime.now()
        minute = now.strftime("%Y-%m-%d %H:%M")  # 格式化为精确到分钟的字符串
        print("当前时间 " + minute)

        # 定义CSV文件的字段名称
        field_names = ['时间', '官网数据', 'BiliBili数据', 'TapTap数据', '合计']  # 表头
        file_write = [minute, Ba_ba_api, Bili_ba_api, Tap_ba_api, sum]  # 写入变量数据

        # 检查CSV文件是否存在
        if os.path.exists(file_name):
            # 如果文件存在，则检查表头是否存在
            with open(file_name, 'r') as csvfile:
                reader = csv.reader(csvfile)
                headers = next(reader, None)  # 读取表头
                if headers == field_names:
                    print("表头已存在")
                    with open(file_name, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(file_write)  # 写入变量数据
                else:
                    print("表头与定义的字段名称不匹配,请检查")
                    with open(file_name, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(field_names)  # 写入CSV文件的表头
                        writer.writerow(file_write)  # 写入变量数据
                        exit(1)
        else:
            print("CSV文件不存在，已创建文件 " + file_name)
            with open(file_name, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(field_names)  # 写入CSV文件的表头
                writer.writerow(file_write)  # 写入变量数据

    except Exception as e:
        # 获取当前时间
        now = datetime.now()
        minute = now.strftime("%Y-%m-%d %H:%M")  # 格式化为精确到分钟的字符串
        print("当前时间" + minute)

        # 输出出错信息到文件
        with open(file_error_name, mode='a', newline='') as f:
            f.write(minute + " 错误信息 写入文件 " + str(e) + '\r\n')
        print("Error:", e)
    time.sleep(60)
