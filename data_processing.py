#!/usr/bin/env python
# -*- coding:utf-8-*-

# from judge_chinese_number_alphabet import *
from input_mode import *
import csv
import datetime

def input_data(data_path):

    date = datetime.datetime.now()
    # print("当前的日期和时间是 %s" % date)
    # print("year-month-day 格式是  %s-%s-%s" % (date.year, date.month, date.day))

    # 将文件名称命名依据日期命名，格式为year-month-day
    name_saved_file = str(date.year) + "-" + str(date.month) + "-" + str(date.day) + ".csv"

    try:
        with open(name_saved_file, "r", newline='') as juduge_csv_exist:
            # read = csv.reader(juduge_csv_exist)
            juduge_csv_exist.close()
    except FileNotFoundError:
        with open(name_saved_file, "a+", newline='') as csvfile:

            # 写入多行用writerows
            writer = csv.writer(csvfile)
            writer.writerow(["收件人姓名", "收件人电话", "收件人地址", "物品名称", "价格", "价格", "	下单微信名称", "下单时间"])

    each_message = []  # 各商户信息
    each_message_element = 0  # 用于计数每单信息元素收集量

    # 打开一个文件
    try:
        infile = open(data_path, "r", encoding='UTF-8')
        for line in infile:  # print(len(line))

            # line = filter(lambda ch: ch not in ' ', line)
            # line.strip()
            # each_message_element=0
            if not line.strip():  # 空行下操作
                if each_message_element == 0:
                    continue
                elif each_message_element == 1:
                    print("使用模式一（一行输入）下的数据录入")
                    each_message, each_message_element, exception_signal = mode_one(each_message, name_saved_file)
                    if exception_signal:
                        break
                elif each_message_element == 2:
                    print("使用模式二（两行输入）下的数据录入")
                elif each_message_element == 3:
                    print("使用模式三（三行输入）下的数据录入")
                elif each_message_element == 4:
                    print("使用模式四（四行标准输入）下的数据录入")
                    each_message, each_message_element, exception_signal = mode_four(each_message, name_saved_file)
                    if exception_signal:
                        break
                elif each_message_element >= 5:
                    print("使用模式五（五行及五行以上标准输入）下的数据录入")
                    each_message, each_message_element, exception_signal = \
                        mode_five(each_message, name_saved_file, each_message_element)
                else:
                    print("输入操作失败")
                    break
            else: # 非空行下的操作
                each_message_element += 1
                each_message.append(line)

            print(line, end='')

        if each_message_element == 0 and exception_signal == False:
            print("操作完毕")
        elif each_message_element == 1:
            print("使用模式一（一行输入）下的数据录入")
            each_message, each_message_element, exception_signal = mode_one(each_message, name_saved_file)
        elif each_message_element == 2:
            print("使用模式二（两行输入）下的数据录入")
        elif each_message_element == 3:
            print("使用模式三（三行输入）下的数据录入")
        elif each_message_element == 4:
            print("使用模式四（四行标准输入）下的数据录入")
            each_message, each_message_element, exception_signal = mode_four(each_message, name_saved_file)
        elif each_message_element >= 5:
            print("使用模式五（五行及五行以上标准输入）下的数据录入")
            each_message, each_message_element, exception_signal = \
                mode_five(each_message, name_saved_file, each_message_element)
        elif exception_signal:
            print("输入操作失败")
        else:
            print("操作失败")

    except FileNotFoundError:
        print("读取txt文件路径错误")

    finally:
        if not exception_signal:
            with open(name_saved_file, "a+", newline='') as csvfile:
                # 写入多行用writerows
                writer = csv.writer(csvfile)
                # writer.writerow(["111".encode(),"fefe".encode(),"fef33".encode(),"fef".encode()])
                writer.writerow([])

        infile.close()  # 关闭打开的文件

