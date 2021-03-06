# -*- coding: utf-8 -*-
#StudentNumber:2180104019
#author:Juna Kawagishi

import queue
import sys

G = [{}]
fixed = {} #各点への最短距離を格納するリスト
via = [[]] #各点への最短経路を格納するリスト
src, dst = 0, 0 #始点，終点

def setNode(n):
  global G,via
  G = [{} for i in range(n)]
  via = [[] for i in range(n)]


#問B1&3.5:データを格納する関数 ----------------------------------
def setData(inputDataTextfile):
    global G, src, dst

    with open(inputDataTextfile) as f:
        for i,line in enumerate(f):
            if i==0:
                n,m = map(int,line.split())
                setNode(n)
            #elif i==m+1:
                #src, dst = map(int,line.split())
            else:
                s,t,w = map(int,line.split())
                G[s][t] = w
                G[t][s] = w


#問B2&3.5:ダイクストラ本体の関数 ---------------------------------
def solve():
    global G,fixed,via
    min_d = 1000000

    q = queue.PriorityQueue()
    q.put((0,src,src))

    while len(fixed) != len(G):
        w,x,v = q.get()
        if x == dst:
            if min_d < w: continue;
            min_d = w
            print("minimum_distance:",min_d) #終点までの最短距離を出力
        if x in fixed: continue;

        fixed[x] = w
        via[x].append(v)
        via[x].append(x)
        for y in G[x]:
            if (y in fixed) == False:
                q.put((w + G[x][y], y, x))


#問B3&3.5:ダイクストラの計算結果をわかりやすく表示 -------------------
def showGraph():

    print("\n-------Graph--------")
    for pre,num in via:
        if num == dst: print("[minimum_Path] ", end="")

        if pre == src:
            if num == src: continue;
            print(num,":",pre,"->",num,"(distance:",fixed[num],")")
        else:
            path = [num]
            while pre != src:
                path.insert(0,pre)
                pre, _ = via[pre]

            print(num, ":", src, end="")
            for i in path:
                print(" ->", i, end="")
            print(" (distance:",fixed[num],")")



if __name__ == "__main__":

    """
    コマンドライン引数に非負辺重み付き有向グラフのデータが格納されたroute.txtをとる
    >> python3 dijkstra.py route.txt

    ▽入力データ(route.txt)の中身
    N(ノード数) R(辺,エッジ数)
    A1 B1 L1(点A1,点B1を結ぶ辺の重み)
    A2 B2 L2
    ...
    AR BR LR
    #S(始点) T(終点)
    """

    argvs = sys.argv
    argc = len(argvs)

    if argc != 2:
        print("Specify graph data as an argument.")
        sys.exit()

    #入力テキストデータをもとに格納
    setData(argvs[1])

    #問3.5:始点と終点の指定
    print("Start:", end="")
    src = int(input())
    print("Goal:", end="")
    dst = int(input())

    #ダイクストラの実装
    solve()

    #ダイクストラの結果をわかりやすく表示
    showGraph()
