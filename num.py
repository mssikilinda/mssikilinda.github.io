# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 12:54:56 2023

@author: Acer
"""

#!/usr/bin/env python3
import cgi
import html
form = cgi.FieldStorage()
text1 = form.getfirst("NUM_1", "пустое поле")
text2 = form.getfirst("NUM_2", "пустое поле")
text1 = html.escape(text1)
text2 = html.escape(text2)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <title>Обработка числа</title>
            <style> 
                body { font-family: Arial, Helvetica, sans-serif; 
                       background: #ebe8e8;
                       text-align: center;
                }

                .headd { background: #B0E0E6; /* Цвет фона */
                         outline: 2px solid #000; /* Чёрная рамка */
                         border: 3px solid #fff; /* Белая рамка */
                         border-radius: 5px; /* Радиус скругления */
                }
            </style>
        </head>
        <body>
        <div class="headd">
            <h2> Калькулятор чисел в заданном BCD-коде 
                с визуализацией арифметических действий.</h2>
        </div> <!--Конец верхушки-->
        <div class="main">""")
print("<h2>Набраны числa: {} и {}</h2>".format(text1, text2))
TEXT = [text1, text2]
n = 0
for t in list(TEXT):
    n = n + 1
    Y_1 = []
    sign = 0
    if t[0] == '-':
        sign = 1
        t = str(t)[1:]
    flag = str(t).find('.')
    if flag == -1:
        X = [int(a) for a in str(t)]
        X_1 = [format(a, 'b') for a in list(X)]
        X_2 = [str(a) for a in list(X_1)]
        Y = []
        for a in list(X_2):
            if len(a) == 1:
                a = '000' + a
            elif len(a) == 2:
                a = '00' + a
            elif len(a) == 3:
                a = '0' + a
            Y.append(a)
    else:
        T = str(t).split('.')
        Y = []
        for a in list(T):
            X = [int(b) for b in str(a)]
            X_1 = [format(b, 'b') for b in list(X)]
            X_2 = [str(b) for b in list(X_1)]
            for c in list(X_2):
                if len(c) == 1:
                    c = '000' + c
                elif len(c) == 2:
                    c = '00' + c
                elif len(c) == 3:
                    c = '0' + c
                Y.append(c)
        Y.insert(flag, '.')
    if sign == 1:
        Y.insert(0, '-')
    Y_1 = ' '.join(Y)
    print("<h2> Число {} в BCD-коде: {}<h2>".format(n, Y_1))
print("""</div> <!--Конец действий-->
      </body>
      </html>""")
