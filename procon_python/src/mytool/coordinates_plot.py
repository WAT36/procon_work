# -*- coding:utf-8 -*-

import sys
import matplotlib.pyplot as plt

#x1 y1
#x2 y2
#...
#の形式になっているテキストファイルを読み込み
#散布図にプロットするスクリプト

#コマンドラインからの引数
args = sys.argv

#ファイル名取得
filename = args[1]

#ファイルオープン
input_data = open(filename,"r")

#入力データをリスト化
input_lines = input_data.readlines()

startline = 1

for i in range(startline,len(input_lines)):
    list = input_lines[i].split()
    print(int(list[0]))
    print(int(list[1]))
    plt.plot(int(list[0]),int(list[1]),'ro')

plt.show()
