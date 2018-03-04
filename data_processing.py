#!/usr/bin/env python
# -*- coding:utf-8-*-

import csv
import datetime
import re
from pandas import DataFrame

def input_data(data_path):
    # !/usr/bin/python3

    # 打开一个文件
    infile = open(data_path, "r", encoding='UTF-8')
    # blank_removed_file = open("blank_removed_file.txt", 'wb')

    with open("C:\\Users\\dby_freedom\\Desktop\\data_processing\\2018-3-2.csv", "a+", newline='') as csvfile:
        # 写入多行用writerows
        writer = csv.writer(csvfile, delimiter=' ', quotechar='|', dialect='excel')
        writer.writerow(["收件人姓名","收件人电话","收件人地址","物品名称","价格","价格","	下单微信名称","下单时间"])

    each_message=[] # 各商户信息
    each_message_element=0 #用于计数每单信息元素收集量

    try:
        for line in infile:        # print(len(line))

            # line = filter(lambda ch: ch not in ' ', line)
            # line.strip()
            if not line.strip():
                continue
            else:
                line_next=line
                eachline_length=0
                for line_element in line: #将含有中文、数字、英文的行放入各发单信息中
                    if is_chinese_number_alphabet(line_element):
                        eachline_length+=1
                each_message.append(line)
                each_message_element+=1
                if each_message_element==4: # 将收集到完整商户信息分别找出姓名、电话、地址、物品名称，写入csv文件

                    message_element_product = each_message[3].strip() # 默认商品名称是最后元素，直接提取

                    print("----------------message_element_product----------------------")
                    print(message_element_product)

                    final_first_element=[]
                    final_first_element_name=[]
                    final_first_element_phone=[]
                    final_first_element_address=[]
                    length_first_element_count=0
                    length_first_element_number_count=0
                    length_first_element_chinese_count=0

                    final_second_element=[]
                    final_second_element_name=[]
                    final_second_element_phone=[]
                    final_second_element_address=[]
                    length_second_element_count=0
                    length_second_element_number_count=0
                    length_second_element_chinese_count=0

                    final_third_element=[]
                    final_third_element_name=[]
                    final_third_element_phone=[]
                    final_third_element_address=[]
                    length_third_element_count=0
                    length_third_element_number_count=0
                    length_third_element_chinese_count=0

                    final_fourth_element=[]

                    # # 将商品信息中的空格去除
                    # each_message[3].strip()
                    # for uchar in each_message[3]:  # 将含有中文、数字、英文的行放入各发单信息中
                    #     if uchar in " \t":
                    #         continue
                    #     else:
                    #
                    #     final_fourth_element.append(uchar)


                    # 统计各行信息中汉字、数字、英文长度
                    for uchar in each_message[0]:  # 将含有中文、数字、英文的行放入各发单信息中
                        if is_chinese_number_alphabet(uchar):
                            length_first_element_count += 1

                        if is_number(uchar):
                            length_first_element_number_count += 1
                        if is_chinese(uchar):
                            length_first_element_chinese_count += 1


                    for uchar in each_message[1]:  # 将含有中文、数字、英文的行放入各发单信息中
                        if is_chinese_number_alphabet(uchar):
                            length_second_element_count += 1
                        if is_number(uchar):
                            length_second_element_number_count += 1
                        if is_chinese(uchar):
                            length_second_element_chinese_count += 1


                    for uchar in each_message[2]:  # 将含有中文、数字、英文的行放入各发单信息中
                        if is_chinese_number_alphabet(uchar):
                            length_third_element_count += 1
                        if is_number(uchar):
                            length_third_element_number_count += 1
                        if is_chinese(uchar):
                            length_third_element_chinese_count += 1

                    # 首先提取出最大长度行作为地址，其次，依照行所含数字长度与汉字长度进行比较判定电话、名字
                    if length_first_element_count >= length_second_element_count \
                            and length_first_element_count >= length_third_element_count:
                        message_element_address=each_message[0].strip() #依据各行字符长度，默认最大长度为地址行

                        print("----------------message_element_address----------------------")
                        print(message_element_address)

                        if length_second_element_number_count>=length_second_element_chinese_count: # 依据数字长度、汉字长度判定电话及姓名
                            message_element_phone=each_message[1].strip()
                            message_element_name=each_message[2].strip()
                        else:
                            message_element_name=each_message[1].strip()
                            message_element_phone=each_message[2].strip()

                    elif length_second_element_count >= length_first_element_count \
                            and length_second_element_count >= length_third_element_count:
                        message_element_address=each_message[1].strip()

                        if length_first_element_number_count >= length_first_element_chinese_count:  # 依据数字长度、汉字长度判定电话及姓名
                            message_element_phone = each_message[0].strip()
                            message_element_name = each_message[2].strip()
                        else:
                            message_element_name = each_message[0].strip()
                            message_element_phone = each_message[2].strip()

                    else:
                        message_element_address=each_message[2].strip()

                        if length_first_element_number_count >= length_first_element_chinese_count:  # 依据数字长度、汉字长度判定电话及姓名
                            message_element_phone = each_message[0].strip()
                            message_element_name = each_message[1].strip()
                        else:
                            message_element_name = each_message[0].strip()
                            message_element_phone = each_message[1].strip()
                    each_message_element=0

                    # 输出信息到以日期命名的文件中

                    final_message=[]
                    final_message.append(message_element_name)
                    final_message.append(message_element_phone)
                    final_message.append(message_element_address)
                    final_message.append(message_element_product)

                    print("--------------------final_message-----------------------")
                    print(final_message)
                    #
                    # df=DataFrame({"收件人姓名":message_element_name,"收件人电话":message_element_phone,
                    #               "收件人地址":message_element_address,"物品名称":message_element_product,
                    #               "价格":[],"价格":[],"	下单微信名称":[],"下单时间":[]})
                    # df.to_excel('test.xlsx', sheet_name='sheet1', index=False)
                    with open("C:\\Users\\dby_freedom\\Desktop\\data_processing\\2018-3-2.csv", "a+", newline='') as csvfile:
                        # 写入多行用writerows
                        writer=csv.writer(csvfile,delimiter=' ',quotechar='|', dialect='excel')
                        # writer.writerow(["111".encode(),"fefe".encode(),"fef33".encode(),"fef".encode()])
                        writer.writerow(final_message)
                        # writer.writerow([str.encode(message_element_name),str.encode(message_element_phone),str.encode(message_element_address),str.encode(message_element_product)])
                        # writer.writerows([[0, 1, 3], [1, 2, 3], [2, 3, 4]])

                print(eachline_length)
            # if line.strip():

            print(line, end='')


    finally:
        infile.close()    # 关闭打开的文件

    # for eachline in infile.readlines():
    #     # 去掉文本行里面的空格、\t、数字（其他有要去除的也可以放到' \t1234567890'里面）
    #     lines = filter(lambda ch: ch not in ' ', eachline)
    #
    #     blank_removed_file.write(lines)  # 写入train_output.txt(此处是一股脑的全写进去，并没有做任何的分行处理)


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
        writer.writerows([[0, 1, 3], [1, 2, 3], [2, 3, 4]])


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
    input_data("C:\\Users\\dby_freedom\\Desktop\\data_processing\\data_input_3.4.txt")
    # output_data()
