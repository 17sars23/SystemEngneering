# システム工学特論課題
単一始点最短路問題(SSSP)を解くDijkstraの実装

### 環境
 python3
 
### プログラムの詳細
**dijkstra.py**
非負辺重み付き有向グラフを入力とし，指定された始点と終点の最短経路と最短距離を出力する

- route_test.py：非負辺重み付き有向グラフのデータ

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

- n：ノード数
- min：辺重みの最小値
- max：辺重みの最大値


```makeRoutefile.py
$ python3 makeRoutefile.py n min max

```