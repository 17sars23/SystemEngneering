# -*- coding: utf-8 -*-
#StudentNumber:2180104019
#author:Juna Kawagishi

import random
import sys

adj = [[]] # 隣接リスト

#隣接リストを作成 -------------------------------------------
#辺の総数(r)に達するまで各ノードに連結相手を1つ決めるサイクルを回すことで連結性を保証
#----------------------------------------------------------
def setAdjacentList(n,r):
    global adj
    adj = [[] for i in range(n)]

    while r > 0:
        for i in range(n):
            a = random.randrange(n)
            if not a in adj[i] and a != i: #重複を除去
                adj[i].append(a)
                adj[a].append(i)

            if sum(len(k) for k in adj) >= r:
                break
        else:
            continue;
        break



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

    n, min, max = map(int, argvs[1:])
    r = random.randrange(2*n, n*(n-1),2) #辺の数はn~nC2までに制限

    outputfilePath = "route.txt"
    f = open(outputfilePath, "w")
    f.write(str(n) + " " + str(int(0.5*r)) + "\n")

    #隣接リスト作成
    setAdjacentList(n,r)

    #output
    for a, v in enumerate(adj):
        for b in v:
            if a < b:
                weight = random.randrange(min, max)
                f.write(str(a) + " " + str(b) + " " + str(weight) + "\n")
            else:
                continue;

    f.close()
