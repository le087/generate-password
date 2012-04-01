# -*- coding: utf-8 -*-
#------------------------------------------------------------
# генератор словарей
#------------------------------------------------------------
 
import string
import sys
import os
import re



def gen_dict_fsmb():
    """generate dictionary symbols
    
    Arguments:
    - `file`: source
    """

    dict_fsmb = {} # словарь первых двух символов
    key_dict = ''
    re_patt = re.compile('[A-Za-z]')
    try:
        openfile = open('/home/mak/devel/scripts/old_work/gen_pass/pereraboka.txt', 'r')
        file_r = openfile.readlines()
    except:
        print 'Файла не существует'
    #------------------------------------------------------------
    # генерим словарь вида {'gu': 7, 'gr': 20, 'ge': 7, 'ga': 8}
    #------------------------------------------------------------        
    for st in file_r:
        for smb in st:
            if smb == ' ':
                key_dict = ''
            if re_patt.findall(smb):
                key_dict = key_dict + smb.lower()
                if len(key_dict) == 2:
                    if dict_fsmb.has_key(key_dict):
                        dict_fsmb[key_dict] += 1
                    else:
                        dict_fsmb[key_dict] = 1
    openfile.close()
    return dict_fsmb

def gen_dict_othsmb():
    """generate dictionary other symbols
    """
    dict_othsmb = {} #словарь правил для остальных символов
    key_dict = ''
    re_patt = re.compile('[A-Za-z]')
    try:
        openfile = open('/home/mak/devel/scripts/old_work/gen_pass/pereraboka.txt', 'r')
        file_r = openfile.readlines()
    except:
        print 'Файла не существует'
    #------------------------------------------------------------
    # генерим словарь вида { 'ab':{'c':1, 'm':2}, 'bc':{'d':1} }
    #------------------------------------------------------------
    for st in file_r:
        for smb in st:
            if smb == ' ':
                key_dict = ''
            if re_patt.findall(smb):
                key_dict = key_dict + smb.lower()
                if len(key_dict) > 2:
                    d_smb = key_dict[-3:-1]
                    if dict_othsmb.has_key(d_smb):
                        if dict_othsmb[d_smb].has_key(smb):
                            dict_othsmb[d_smb][smb] += 1
                        else:
                            dict_othsmb[d_smb][smb] = 1
                    else:
                        dict_othsmb[d_smb] = { smb:1 }
    print dict_othsmb
                        
#    openfile.close()
#    return dict_othsmb
gen_dict_othsmb()

    
def get_passwd():
    """generate paswd
    """
    dict_words = gen_dict()

    dict_summ =    { 'a':0, 'b':0, 'c':0, 'd':0, 'e':0,
                     'f':0, 'g':0, 'h':0, 'i':0, 'j':0,
                     'k':0, 'l':0, 'm':0, 'n':0, 'o':0,
                     'p':0, 'q':0, 'r':0, 's':0, 't':0,
                     't':0, 'u':0, 'v':0, 'w':0, 'x':0,
                     'y':0, 'z':0 }
    for i in dict_words:
        for p in dict_words[i]:
            dict_summ[i] = dict_summ[i] + dict_words[i].index(p)