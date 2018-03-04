#codeing=utf-8
import csv
import datetime
import re



def input_data(data_path):
    # !/usr/bin/python3

    # 打开一个文件
    file = open(data_path, "r", encoding='UTF-8')

    try:
        for line in file:        # print(len(line))

            # line = filter(lambda ch: ch not in ' ', line)
            # line.strip()
            if not line.strip():
                continue
            else:
                # re.sub('\s', '', string)
                # re.sub('\s', '', line)
                # line.strip()
                # line = line.split(' ')

                print('-------------')
                print(type(line))
                # result = .join(line.split())
                print(line[0])
                # line_changed = line.split(' ')
                print(len(line))
            # if line.strip():

            print(line, end='')
    finally:
        file.close()    # 关闭打开的文件

def output_data():
    date = datetime.datetime.now()
    print("当前的日期和时间是 %s" % date)
    print("year-month-day 格式是  %s-%s-%s" % (date.year, date.month, date.day))
    # python2可以用file替代open
    with open("C:\\Users\\dby_freedom\\Desktop\\2018-3-2.csv", "a+") as csvfile:
        writer = csv.writer(csvfile)

        # 先写入columns_name
        writer.writerow(["收件人姓名","收件人电话","收件人地址","物品名称","价格","价格","	下单微信名称","下单时间"])
        # 写入多行用writerows
        writer.writerows([[0, 1, 3], [1, 2, 3], [2, 3, 4]])

if __name__ == '__main__':
    # 读取文件
    input_data("C:\\Users\\dby_freedom\\Desktop\\data_input.txt")
    # output_data()
