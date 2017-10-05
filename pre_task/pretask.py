# -*- coding: utf-8 -*-
import codecs
import os
import sys
reload(sys) 
sys.setdefaultencoding('GBK') 

#1.读取文件
def  readfile(filepath):
    f = codecs.open(filepath, 'r', "utf-8") #打开文件
    lines = f.readlines()
    word_list = []
    for line in lines:
        line = line.strip()
        words = line.split(" ") #用空格分割
        word_list.extend(words)
    return word_list
#2.构造四个字的二元词组
def  two_word(wordlist):
    i = 0
    twoword = []
    fourletter =[]
    while i < len(wordlist)-1:
      if len(wordlist[i]) == 2 and len(wordlist[i+1]) == 2:
         twoword.append(wordlist[i] + wordlist[i+1])
      i = i +1
    #print twoword
    return twoword
# #3.清洗格式
# def  format(word_original):
#     fmt = '，。！？'
#     format_wordlist = []
#     for word in word_original:
#        for char in word :
#          #if str(char) not in str(fmt):
#             format_wordlist.append(word)

#     return format_wordlist


#4.统计频率
def  count_number(format_list):
    word_dict = {}
    for word in format_list:
        if word_dict.has_key(word):
            word_dict[word] = word_dict[word] + 1
        else:
            word_dict[word] = 1
    #排序
    sorted_dict = sorted(word_dict.iteritems(), key=lambda d: d[1], reverse=True)
    return sorted_dict

    

def print_to_csv(combined_wordlist, to_file_path):
    nfile = open(to_file_path,'w+')
    for list_tuple in  combined_wordlist[0:10]:
        
          nfile.write("%s,%d\n" % (list_tuple[0],list_tuple[1]))
    nfile.close()

def main():
    singleword = readfile('happiness_seg.txt')

    doubleword = two_word(singleword)

    dict_and_frequence = count_number(doubleword)

    print_to_csv(dict_and_frequence,'test.csv')


if __name__ == '__main__':
    main()
