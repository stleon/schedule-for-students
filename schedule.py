#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re
from datetime import datetime, time, date

def Find(pat, text):
        match = re.findall(pat, text)
        if match:
                s = {}
                for x in match:
                        if int(x[0]) not in s: s[int(x[0])]=[]
                        s[int(x[0])].append((x[1], int(x[2]), int(x[3]), x[4], x[5], x[6]))     
                return s
        
def SheduleOut(i):
        print i[0], i[1], i[2], i[5]

def ShedulePrint(user_date, sch):
        try:
                date = datetime.strptime(user_date, '%d-%m-%Y')
                if date.isoweekday() in sch:
                        list_date = user_date.split('-')
                        week =1+ date.isocalendar()[1] - datetime.strptime('01-09-'+list_date[2], '%d-%m-%Y').isocalendar()[1]
                        even_week = 2 if week%2==0 else 1 
                        print week, u'неделя'
                        for i in sch[date.isoweekday()]:
                                if i[3]== '*' and (i[4]==str(even_week) or i[4]=='*'):
                                        SheduleOut(i)
                                elif str(week) in i[3].split(' '):
                                        SheduleOut(i)
                else:
                        print u'Выходной'
        except TypeError:
                print u'Файл пуст или в нем есть ошибки'

def main():
        try:
                f = open('schedule.txt', 'rU')
                text = f.read() 
                f.close()
                ShedulePrint(sys.argv[1], 
                Find("(\d)\s([\w.]+)\s(\d+)\s(\d+)\s'(.+)'\s'(.)'\s(\d{2}:\d{2})", text))
        except (IndexError, ValueError):
                print u'Введите дату dd-mm-yyyy'
        except IOError:
                print u'Файл не найден'

if __name__=='__main__':
        main()
