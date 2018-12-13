# システム工学特論課題
単一始点最短路問題(SSSP)を解くDijkstraの実装

### 環境
 python3
 
### プログラムの詳細
**dijkstra.py**
非負辺重み付き有向グラフを入力とし，指定された始点と終点の最短経路と最短距離を出力する

- route_test.txt：非負辺重み付き有向グラフのテストデータ

```dijkstra.py
$ python3 dijkstra.py route_test.txt
>> Start: 0 (始点の番号)
>> Goal: 6 (終点の番号)
minimum_distance: 45

-------Graph--------
1 : 0 -> 1 (distance: 30 )
2 : 0 -> 2 (distance: 15 )
3 : 0 -> 3 (distance: 10 )
4 : 0 -> 3 -> 6 -> 4 (distance: 65 )
5 : 0 -> 2 -> 5 (distance: 35 )
[minimum_Path] 6 : 0 -> 3 -> 6 (distance: 45 )
```


**makeRoutefile.py**
実験用非負辺重み付き有向グラフのデータ(route.txt)をランダムに生成

- n：ノード数 (ex.7)
- min：辺重みの最小値 (ex.10)
- max：辺重みの最大値 (ex.50)


```makeRoutefile.py
$ python3 makeRoutefile.py 7 10 50
$ vi route.txt
7 8
0 3 20
0 2 11
0 1 11
1 6 25
1 4 49
1 5 27
3 5 21
5 6 18
```

`route.txt`の構成

```
N(ノード数) R(辺,エッジ数)
A1 B1 L1(点A1,点B1を結ぶ辺の重み)
A2 B2 L2
...
AR BR LR
```