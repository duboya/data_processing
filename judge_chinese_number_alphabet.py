# coding:utf8

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

