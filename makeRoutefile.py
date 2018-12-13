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
            elif i==m+1:
                src, dst = map(int,line.split())
            else:
                s,t,w = map(int,line.split())
                G[s][t] = w
                G[t][s] = w


#問B2&3.5:ダイクストラ本体の関数 ---------------------------------
def solve():
    global G,fixed,via

    print("Start:",src,"\nGoal:",dst)

    q = queue.PriorityQueue()
    q.put((0,src,0))

    while len(fixed) != len(G):
        w,x,v = q.get()
        if x == dst: print("minimum_distance:",w) #終点までの最短距離を出力
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
    非負辺重み付き有向グラフのデータが格納されたroute.txtを作成する
    >> python3 makeRourefile.py n(ノード数) min(重みの最小値) max(重みの最大値)

    ▽作成するデータ(route.txt)の構成
    N(ノード数) R(辺,エッジ数)
    A1 B1 L1(点A1,点B1を結ぶ辺の重み)
    A2 B2 L2
    ...
    AR BR LR
    """

    argvs = sys.argv
    argc = len(argvs)

    if argc != 4:
        print("Enter the n, min and max.")
        sys.exit()

    n, min, max = argvs[1:]
    print(n,min,max)
