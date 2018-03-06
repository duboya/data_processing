#!/usr/bin/env python
# -*- coding:utf-8-*-

import csv
import datetime
import re
from pandas import DataFrame

def input_data(data_path):
    # !/usr/bin/python3

    # 打开一个文件
    try:
        infile = open(data_path, "r", encoding='UTF-8')
    except FileNotFoundError:
        print("文件路径错误")

    date = datetime.datetime.now()
    print("当前的日期和时间是 %s" % date)
    print("year-month-day 格式是  %s-%s-%s" % (date.year, date.month, date.day))

    # 将文件名称命名依据日期命名，格式为year-month-day
    name_saved_file=str(date.year)+"-"+str(date.month)+"-"+str(date.day)+".csv"

    try:
        with open(name_saved_file, "r", newline='') as juduge_csv_exist:
            read = csv.reader(juduge_csv_exist)
    except FileNotFoundError:
        with open(name_saved_file, "a+", newline='') as csvfile:

            # 写入多行用writerows
            writer = csv.writer(csvfile)
            writer.writerow(["收件人姓名","收件人电话","收件人地址","物品名称","价格","价格","	下单微信名称","下单时间"])

    each_message=[] # 各商户信息
    each_message_element=0 #用于计数每单信息元素收集量

    try:
        for line in infile:        # print(len(line))

            # line = filter(lambda ch: ch not in ' ', line)
            # line.strip()
            # each_message_element=0
            if not line.strip(): # 空行下操作
                if each_message_element==0:
                    continue
                elif each_message_element==1:
                    print("使用模式一（一行输入）下的数据录入")
                elif each_message_element==2:
                    print("使用模式二（两行输入）下的数据录入")
                elif each_message_element==3:
                    print("使用模式三（三行输入）下的数据录入")
                elif each_message_element==4:
                    print("使用模式四（四行标准输入）下的数据录入")

                    each_message,each_message_element = mode_four(each_message, name_saved_file)

                else:
                    print("输入操作失败")
                    break

            else:
                each_message_element+=1
                each_message.append(line)

            print(line, end='')

        if each_message_element == 0:
            print("操作完毕")

        elif each_message_element == 1:
            print("使用模式一（一行输入）下的数据录入")
        elif each_message_element == 2:
            print("使用模式二（两行输入）下的数据录入")
        elif each_message_element == 3:
            print("使用模式三（三行输入）下的数据录入")
        elif each_message_element == 4:
            print("使用模式四（四行标准输入）下的数据录入")

            each_message, each_message_element = mode_four(each_message, name_saved_file)

        else:
            print("操作失败")


    finally:
        infile.close()    # 关闭打开的文件

    # for eachline in infile.readlines():
    #     # 去掉文本行里面的空格、\t、数字（其他有要去除的也可以放到' \t1234567890'里面）
    #     lines = filter(lambda ch: ch not in ' ', eachline)
    #
    #     blank_removed_file.write(lines)  # 写入train_output.txt(此处是一股脑的全写进去，并没有做任何的分行处理)

# 模式四（四行标准输入）下的数据录入
def mode_four(each_message, name_saved_file):
    # eachline_length = 0  # 待检测行的行长
    message_element_product = each_message[3].strip()  # 默认商品名称是最后元素，直接提取

    print("----------------message_element_product----------------------")
    print(message_element_product)

    final_first_element = []
    final_first_element_name = []
    final_first_element_phone = []
    final_first_element_address = []
    length_first_element_count = 0
    length_first_element_number_count = 0
    length_first_element_chinese_count = 0
    length_first_element_alpha_count=0

    final_second_element = []
    final_second_element_name = []
    final_second_element_phone = []
    final_second_element_address = []
    length_second_element_count = 0
    length_second_element_number_count = 0
    length_second_element_chinese_count = 0
    length_second_element_alpha_count=0

    final_third_element = []
    final_third_element_name = []
    final_third_element_phone = []
    final_third_element_address = []
    length_third_element_count = 0
    length_third_element_number_count = 0
    length_third_element_chinese_count = 0
    length_third_element_alpha_count=0

    final_fourth_element = []


    # 统计各行信息中汉字、数字、英文长度
    for uchar in each_message[0]:  # 将含有中文、数字、英文的行放入各发单信息中
        if is_chinese_number_alphabet(uchar):
            length_first_element_count += 1

        if is_number(uchar):
            length_first_element_number_count += 1
        if is_chinese(uchar):
            length_first_element_chinese_count += 1
        if is_alphabet(uchar):
            length_first_element_alpha_count += 1

    for uchar in each_message[1]:  # 将含有中文、数字、英文的行放入各发单信息中
        if is_chinese_number_alphabet(uchar):
            length_second_element_count += 1
        if is_number(uchar):
            length_second_element_number_count += 1
        if is_chinese(uchar):
            length_second_element_chinese_count += 1
        if is_alphabet(uchar):
            length_second_element_alpha_count += 1

    for uchar in each_message[2]:  # 将含有中文、数字、英文的行放入各发单信息中
        if is_chinese_number_alphabet(uchar):
            length_third_element_count += 1
        if is_number(uchar):
            length_third_element_number_count += 1
        if is_chinese(uchar):
            length_third_element_chinese_count += 1
        if is_alphabet(uchar):
            length_third_element_alpha_count += 1

    # 首先提取出最大长度行作为地址，其次，依照行所含数字长度与汉字长度进行比较判定电话、名字
    if length_first_element_count >= length_second_element_count \
            and length_first_element_count >= length_third_element_count:
        message_element_address = each_message[0].strip()  # 依据各行字符长度，默认最大长度为地址行

        print("----------------message_element_address----------------------")
        print(message_element_address)

        if length_second_element_number_count >= length_second_element_chinese_count+length_second_element_alpha_count:  # 依据数字长度、汉字长度判定电话及姓名
            message_element_phone = each_message[1].strip()
            message_element_name = each_message[2].strip()
        else:
            message_element_name = each_message[1].strip()
            message_element_phone = each_message[2].strip()




    elif length_second_element_count >= length_first_element_count \
            and length_second_element_count >= length_third_element_count:
        message_element_address = each_message[1].strip()

        if length_first_element_number_count >= length_first_element_chinese_count+length_first_element_alpha_count:  # 依据数字长度、汉字长度判定电话及姓名
            message_element_phone = each_message[0].strip()
            message_element_name = each_message[2].strip()
        else:
            message_element_name = each_message[0].strip()
            message_element_phone = each_message[2].strip()

    else:
        message_element_address = each_message[2].strip()

        if length_first_element_number_count >= length_first_element_chinese_count+length_first_element_alpha_count:  # 依据数字长度、汉字长度判定电话及姓名
            message_element_phone = each_message[0].strip()
            message_element_name = each_message[1].strip()
        else:
            message_element_name = each_message[0].strip()
            message_element_phone = each_message[1].strip()

    # 判定是否包含冒号“：或者:”，包含的话，则冒号为界限，只保留冒号后内容；
    # 不包含的话，则去除关键字：收货人、电话、地址、收款人、名字、姓名等关键字
    final_first_element = each_message[0].strip()
    final_second_element = each_message[1].strip()
    final_third_element = each_message[2].strip()

    # symbol_set = ":："

    # # if symbol_set in final_first_element:

    # final_first_element = filter(lambda ch: ch not in '：:', final_first_element)
    # print(re.split(r'(?:,|;|\s)\s*：'.decode("utf-8"), final_first_element))
    # print('--------------------final_first_element----------------------')
    # print(final_first_element)

    # final_first_element = final_first_element.split(':', 1)[1]

    if re.search('[:：]', message_element_name):
        message_element_name = re.split('[:：]', message_element_name, 1)[1]

    elif re.search('[姓名 名字]', message_element_name):
        message_element_name = re.split('[姓名 名字]', message_element_name, 2)[-1]
        # final_first_element_final = [x for x in re.split(":：".decode, final_first_element, 1) if x]
    print('--------------------message_element_name----------------------')
    print(message_element_name)

    if re.search('[:：]', message_element_phone):
        message_element_phone = re.split('[:：]', message_element_phone, 1)[1]
    elif re.search('[电话 号码 手机]', message_element_phone):
        message_element_phone = re.split('[电话 号码 手机]', message_element_phone, 2)[-1]
        # final_first_element_final = [x for x in re.split(":：".decode, final_first_element, 1) if x]
    print('--------------------message_element_phone----------------------')
    print(message_element_phone)

    if re.search('[:：]', message_element_address):
        message_element_address = re.split('[:：]', message_element_address, 1)[1]
    elif re.search('[地址]', message_element_address):
        message_element_address = re.split('[地址]', message_element_address, 2)[-1]
        # final_first_element_final = [x for x in re.split(":：".decode, final_first_element, 1) if x]
    print('--------------------message_element_address----------------------')
    print(message_element_address.strip())

    # 删除特定字符，如句号等
    message_element_name = message_element_name.strip('。')
    message_element_name = message_element_name.strip('.')
    message_element_phone = message_element_phone.strip('。')
    message_element_phone = message_element_phone.strip('.')
    message_element_address = message_element_address.strip('。')
    message_element_address = message_element_address.strip('.')

    message_element_name = message_element_name.strip()
    message_element_phone = message_element_phone.strip()
    message_element_address = message_element_address.strip()

    # 检验录入数据是否合乎逻辑，如手机号码：188 8384 8682 一共11位
    if len(message_element_phone) == 11:
        print("手机号码验证正常")
    else:
        message_element_phone=message_element_phone+"（有问题）"
        print("手机号码验证有误")

    # 输出信息到以日期命名的文件中
    final_message = []
    final_message.append(message_element_name)
    final_message.append(message_element_phone)
    final_message.append(message_element_address)
    final_message.append(message_element_product)

    print("--------------------final_message-----------------------")
    print(final_message)
    #
    # df=DataFrame({"收件人姓名":message_element_name,"收件人电话":message_element_phone,
    #               "收件人地址":message_element_addr
    # ess,"物品名称":message_element_product,
    #               "价格":[],"价格":[],"	下单微信名称":[],"下单时间":[]})
    # df.to_excel('test.xlsx', sheet_name='sheet1', index=False)
    with open(name_saved_file, "a+", newline='') as csvfile:
        # 写入多行用writerows
        writer = csv.writer(csvfile)
        # writer.writerow(["111".encode(),"fefe".encode(),"fef33".encode(),"fef".encode()])
        writer.writerow(final_message)
        # writer.writerow([message_element_name,message_element_phone,message_element_address,message_element_product])
        # writer.writerows([[0, 1, 3, 1], [1, 2, 3, 1], [2, 3, 4, 1]])

    # print(eachline_length)
    each_message = []
    each_message_element = 0
    return each_message,each_message_element


def output_data():
    date = datetime.datetime.now()
    print("当前的日期和时间是 %s" % date)
    print("year-month-day 格式是  %s-%s-%s" % (date.year, date.month, date.day))
    # python2可以用file替代open
    with open("C:\\Users\\dby_freedom\\Desktop\\data_processing\\2018-3-2.csv", "a+") as csvfile:
        writer = csv.writer(csvfile)

        # 先写入columns_name
        writer.writerow(["收件人姓名","收件人电话","收件人地址","物品名称","价格","价格","	下单微信名称","下单时间"])
        # 写入多行用writerows
        # writer.writerows([[0, 1, 3], [1, 2, 3], [2, 3, 4]])


# 判断一个unicode是否是汉字
def is_chinese(uchar):
    if '\u4e00' <= uchar<='\u9fff':
        return True
    else:
        return False

# 判断一个unicode是否是数字
def is_number(uchar):
    if '\u0030' <= uchar<='\u0039':
        return True
    else:
        return False

# 判断一个unicode是否是英文字母
def is_alphabet(uchar):
    if ('\u0041' <= uchar<='\u005a') or ('\u0061' <= uchar<='\u007a'):
        return True
    else:
        return False

# 判断是否非汉字，数字和英文字符
def is_other(uchar):
    if not (is_chinese(uchar) or is_number(uchar) or is_alphabet(uchar)):
        return True
    else:
        return False

# 判断是否为汉字，数字和英文字符
def is_chinese_number_alphabet(uchar):
    if (is_chinese(uchar) or is_number(uchar) or is_alphabet(uchar)):
        return True
    else:
        return False


if __name__ == '__main__':
    # 读取文件
    input_data("C:\\Users\\dby_freedom\\Desktop\\data_processing\\data_input.txt")
    # output_data()
