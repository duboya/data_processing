# -*- coding:utf-8-*-

from judge_chinese_number_alphabet import *
# from input_mode import *
import csv
import re


def judge_message_element(each_message_input, name_saved_file, message_element_product):
    each_message = each_message_input
    exception_signal = False
    length_first_element_count = 0
    length_first_element_number_count = 0
    length_first_element_chinese_count = 0
    length_first_element_alpha_count = 0
    length_first_element_chinese_alpha_count = 0

    length_second_element_count = 0
    length_second_element_number_count = 0
    length_second_element_chinese_count = 0
    length_second_element_alpha_count = 0
    length_second_element_chinese_alpha_count = 0

    length_third_element_count = 0
    length_third_element_number_count = 0
    length_third_element_chinese_count = 0
    length_third_element_alpha_count = 0
    length_third_element_chinese_alpha_count = 0

    # 统计各行信息中汉字、数字、英文长度
    for uchar in each_message[0]:  # 将含有中文、数字、英文的行放入各发单信息中
        if is_chinese_number_alphabet(uchar):
            length_first_element_count += 1
        if is_chinese_alphabet(uchar):
            length_first_element_chinese_alpha_count += 1
        if is_number(uchar):
            length_first_element_number_count += 1
        if is_chinese(uchar):
            length_first_element_chinese_count += 1
        if is_alphabet(uchar):
            length_first_element_alpha_count += 1

    for uchar in each_message[1]:  # 将含有中文、数字、英文的行放入各发单信息中
        if is_chinese_number_alphabet(uchar):
            length_second_element_count += 1
        if is_chinese_alphabet(uchar):
            length_second_element_chinese_alpha_count += 1
        if is_number(uchar):
            length_second_element_number_count += 1
        if is_chinese(uchar):
            length_second_element_chinese_count += 1
        if is_alphabet(uchar):
            length_second_element_alpha_count += 1

    for uchar in each_message[2]:  # 将含有中文、数字、英文的行放入各发单信息中
        if is_chinese_number_alphabet(uchar):
            length_third_element_count += 1
        if is_chinese_alphabet(uchar):
            length_third_element_chinese_alpha_count += 1
        if is_number(uchar):
            length_third_element_number_count += 1
        if is_chinese(uchar):
            length_third_element_chinese_count += 1
        if is_alphabet(uchar):
            length_third_element_alpha_count += 1

    # 首先提取出最大长度行作为地址，其次，依照行所含数字长度与汉字长度进行比较判定电话、名字
    if length_first_element_chinese_alpha_count >= length_second_element_chinese_alpha_count \
            and length_first_element_chinese_alpha_count >= length_third_element_chinese_alpha_count:
        message_element_address = each_message[0].strip()  # 依据各行字符长度，默认最大长度为地址行

        print("----------------message_element_address----------------------")
        print(message_element_address)

        if length_second_element_number_count >= length_second_element_chinese_count + length_second_element_alpha_count:  # 依据数字长度、汉字长度判定电话及姓名
            message_element_phone = each_message[1].strip()
            message_element_name = each_message[2].strip()
        else:
            message_element_name = each_message[1].strip()
            message_element_phone = each_message[2].strip()

    elif length_second_element_chinese_alpha_count >= length_first_element_chinese_alpha_count \
            and length_second_element_chinese_alpha_count >= length_third_element_chinese_alpha_count:
        message_element_address = each_message[1].strip()

        if length_first_element_number_count >= length_first_element_chinese_count + length_first_element_alpha_count:  # 依据数字长度、汉字长度判定电话及姓名
            message_element_phone = each_message[0].strip()
            message_element_name = each_message[2].strip()
        else:
            message_element_name = each_message[0].strip()
            message_element_phone = each_message[2].strip()

    else:
        message_element_address = each_message[2].strip()

        if length_first_element_number_count >= length_first_element_chinese_count + length_first_element_alpha_count:  # 依据数字长度、汉字长度判定电话及姓名
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

    # 删除特定字符，如句号等
    message_element_name = message_element_name.strip('。')
    message_element_name = message_element_name.strip('.')
    message_element_name = message_element_name.strip('，')
    message_element_name = message_element_name.strip('收')

    message_element_phone = message_element_phone.strip('。')
    message_element_phone = message_element_phone.strip('.')
    message_element_phone = message_element_phone.strip('，')

    message_element_address = message_element_address.strip('。')
    message_element_address = message_element_address.strip('.')
    message_element_address = message_element_address.strip('！')
    message_element_address = message_element_address.strip('，')

    message_element_product = message_element_product.strip('（')
    message_element_product = message_element_product.strip('）')
    message_element_product = message_element_product.strip('(')
    message_element_product = message_element_product.strip(')')

    message_element_name = message_element_name.strip()
    message_element_phone = message_element_phone.strip()
    message_element_address = message_element_address.strip()

    if re.search('[:：]', message_element_name):
        message_element_name = re.split('[:：]', message_element_name, 1)[-1]

    elif re.search('[姓名 名字 收货人 收件人]', message_element_name):
        message_element_name = re.split('[姓名 名字 收货人 收件人]', message_element_name)[-1]
        # final_first_element_final = [x for x in re.split(":：".decode, final_first_element, 1) if x]
    print('--------------------message_element_name----------------------')
    print(message_element_name)

    if re.search('[:：]', message_element_phone):
        message_element_phone = re.split('[:：]', message_element_phone, 1)[1]
    elif re.search('[电话 号码 手机]', message_element_phone):
        message_element_phone = re.split('[电话 号码 手机]', message_element_phone)[-1]
        # final_first_element_final = [x for x in re.split(":：".decode, final_first_element, 1) if x]
    print('--------------------message_element_phone----------------------')
    print(message_element_phone)

    if re.search('[:：]', message_element_address):
        message_element_address = re.split('[:：]', message_element_address, 1)[1]
    elif re.search('[地址]', message_element_address):
        message_element_address = re.split('[地址]', message_element_address)[-1]
        # final_first_element_final = [x for x in re.split(":：".decode, final_first_element, 1) if x]
    print('--------------------message_element_address----------------------')
    print(message_element_address.strip())

    # 异常情况检查判断：
    # 1. 检验录入数据是否合乎逻辑，如手机号码：188 8384 8682 一共11位，如果电话号码长度不对，在号码后加上“（有问题）”
    if len(message_element_phone) == 11:
        print("手机号码验证正常")
    else:
        message_element_phone = message_element_phone + "（有问题）"
        print("手机号码验证有误")

    # 2. 当老用户只发来接收人信息（地址、电话、姓名），不带货物信息时候，物品名称栏填入信息“未发送发货信息”
    if (message_element_address in message_element_product) or (message_element_name in message_element_product) \
            or (message_element_phone in message_element_product):
        message_element_product = "未发送发货信息"

    # 输出信息到以日期命名的文件中
    final_message = []
    final_message.append(message_element_name)
    final_message.append(message_element_phone)
    final_message.append(message_element_address)
    final_message.append(message_element_product)

    print("--------------------final_message-----------------------")
    print(final_message)

    try:
        with open(name_saved_file, "a+", newline='') as csvfile:
            # 写入多行用writerows
            writer = csv.writer(csvfile)
            # writer.writerow(["111".encode(),"fefe".encode(),"fef33".encode(),"fef".encode()])
            writer.writerow(final_message)

    except PermissionError:
        print("写入文档需关闭: " + name_saved_file)
        exception_signal = True

    return exception_signal


# 模式一（单行标注你输入）下的数据录入（单行中不同信息以空格作为分界线）
def mode_one(each_message, name_saved_file):
    message_element_product = each_message[0].split()[-1]
    # each_message = each_message[0].split("//s+")
    # each_message =  re.split(r'[ ]',each_message[0])
    each_message = each_message[0].split()
    # message_element_product = each_message[3].strip()  # 默认商品名称是最后元素，直接提取

    print("----------------message_element_product----------------------")
    print(message_element_product)

    print("----------------each_message----------------------")
    print(each_message)

    exception_signal = judge_message_element(each_message, name_saved_file, message_element_product)

    each_message = []
    each_message_element = 0
    return each_message, each_message_element, exception_signal


# 模式四（四行标准输入）下的数据录入
def mode_four(each_message, name_saved_file):
    # eachline_length = 0  # 待检测行的行长
    message_element_product = each_message[3].strip()  # 默认商品名称是最后元素，直接提取

    print("----------------message_element_product----------------------")
    print(message_element_product)

    exception_signal = judge_message_element(each_message, name_saved_file, message_element_product)

    each_message = []
    each_message_element = 0
    return each_message, each_message_element, exception_signal


# 模式五（五行及五行以上标准输入）下的数据录入，第一行发货信息，剩下行
def mode_five(each_message, name_saved_file, each_message_element):
    # eachline_length = 0  # 待检测行的行长
    message_element_product = each_message[0].strip()  # 针对多用户输入模式，默认商品名称是开头元素，直接提取
    # each_message_element -= 1  # 取出了第一行商品信息，进入下一行，将each_message_element-1用于处理剩余行信息（默认每行信息代表一条下单信息）

    print("----------------message_element_product----------------------")
    print(message_element_product)

    input_message_count = 1  # 用于后续计数处理下单数量
    # end_signal = True
    while input_message_count != each_message_element:
        each_message_input = each_message[input_message_count].split()

        print("----------------each_message----------------------")
        print(each_message_input)

        exception_signal = judge_message_element(each_message_input, name_saved_file, message_element_product)
        input_message_count += 1
    #
    #
    # exception_signal = judge_message_element(each_message, name_saved_file, message_element_product)

    each_message = []
    each_message_element = 0
    return each_message, each_message_element, exception_signal
    #
