# Experiment Report

## Prepare

* SPMF (open source data mining library) : http://www.philippe-fournier-viger.com/spmf/ 
* MiniZinc(open source constraint modeling language): http://www.minizinc.org/
* Experiment repo: https://eggeek_edu@bitbucket.org/eggeek_edu/5108.git

## Guide

1. generate `*.path`: `./mzn2fzn {mzn file} {dzn file} --keep-paths`

  `path` file could link identifier like `X_INTRODUCED_1` to a piece of source code in model file (`*.mzn`), so that we can find the corresponding vairable.

2. `nogoods_gen.sh`

   * `./nogoods_gen.sh {log file}`: extract nogoods from log
   * output
     * `out/nogoods/nogoods`: all extracted nogoods
     * `out/nogoods/nogoods_ids`:  in format `id,{nogood}`
     * `out/nogoods/nogoods_info`: in format `id,nid1, nid2, ...`, nogood `id` is caused by `nid1, nid2, ...`
     * `out/nogoods/nogood_rank`: in format `nid, count`
     * `out/nogoods/ids`: id of nogood


3. `tokenize.sh`: 
* extract tokens from nogoods, saved in a dict
* generate transactions by using the dict
* `./tokenize.sh < out/nogoods/nogoods`

* output: `out/literal`, in format `id,litera`

6. `mining.sh`: `./mining.sh` perform mining algorithm on dataset
   * output
     * `out/res/literal_itemset.txt`
     * `out/res/literal_rules.txt`
7. `summarize.sh`: remove itemset/rule which already covered by other itemset/rule
   * output
     * `out/summary/literal_rules.txt`
     * `out/summary/literal_itemset.txt`
8. `trans.sh`: replace item id by token
   * output
     * `out/res/literal_cp_itemset.txt`
     * `out/res/literal_cp_rules.txt`
     * `out/summary/literal_cp_rules.txt`
     * `out/summary/literal_cp_itemset.txt`

We also examined:

* association rules for literal (regard `X_INTRODUCED_i>=j` as an item)
* itemset and association rules for identifier (regard `X_INTRODUCED_i` as an item)
* complement itemset (remove frequent itemset from transactions)

but those are either uninteresting or smilar to results of literal itemset, so we would ignore them.

## Experiment 1 (analyze partial log)

* Instance: 
  * model: `freepizza.mzn`
  * data: `pizza27.dzn`
* Input: partial log (run 10s, size: 67M).

Perform all steps in guide sections, but `nogoods_gen.sh` won't sort nogoods.

### Result

```python
# summarized itemset
X_INTRODUCED_172_>=4 X_INTRODUCED_169_>=4 X_INTRODUCED_166_>=4 X_INTRODUCED_172_==2 X_INTRODUCED_169_==2 X_INTRODUCED_166_==2
X_INTRODUCED_177_>=4 X_INTRODUCED_177_==2 X_INTRODUCED_3446_<=0
X_INTRODUCED_177_>=4 X_INTRODUCED_172_>=4 X_INTRODUCED_169_>=4 X_INTRODUCED_177_==2 X_INTRODUCED_172_==2 X_INTRODUCED_169_==2
X_INTRODUCED_172_>=4 X_INTRODUCED_169_>=4 X_INTRODUCED_172_==2 X_INTRODUCED_169_==2 X_INTRODUCED_3446_<=0
```
* There is a threhold on $sup$
  * when $sup <= 0.66$, itemset mining can't finish
  * when $sup > 0.66$, it only takes 300ms
* The experiment only anlyzed 10s log, but it tooks solver 30min to finish
  * analyzed different time interval may find different result
  * different piece of log may have different $sup$ threhold



## Experiment 2 (analyze full log)

* Instance:
  * model: `freepizza.mzn`
  * data: `pizza27.dzn`
* Input: all execution log (run 30 min, size: 17G)

To reduce the size of data, we will sort nogoods by influence and choose top 50000, where influence is counted by how many other nogoods are directly influenced by it. Other steps are same.

### Result

 ```python
# summarized itemset
X_INTRODUCED_172_==2 X_INTRODUCED_172_>=4 X_INTRODUCED_169_==2 X_INTRODUCED_169_>=4 X_INTRODUCED_3446_<=0
X_INTRODUCED_172_<=0 X_INTRODUCED_169_<=0 X_INTRODUCED_172_==2 X_INTRODUCED_172_>=4 X_INTRODUCED_169_==2 X_INTRODUCED_169_>=4
X_INTRODUCED_172_==2 X_INTRODUCED_172_>=4 X_INTRODUCED_169_==2 X_INTRODUCED_169_>=4 X_INTRODUCED_166_==2 X_INTRODUCED_166_>=4
X_INTRODUCED_177_==2 X_INTRODUCED_177_>=4 X_INTRODUCED_172_==2 X_INTRODUCED_172_>=4 X_INTRODUCED_169_==2 X_INTRODUCED_169_>=4 X_INTRODUCED_3421_<=0
 ```

* full log result is similar to partial log
* those literal in itemset are not special: we could find the corresponding variable name from `*.path` file.

Those facts suggest that itemsets in result may not because of their meaningfulness, instead, may just because of the search order.

Besides, the way of sorting is intuitive, consider a case: $a$ caused $ b$ and $b$ caused other 1k nogoods, which one has higher priority?

## Experiment 3 (random search )

To get ride of strong bias in search order, we've randomly generated 3 search order for a small instance.

Nogoods are provided by Maxim (with simplification), so we can skip `nogoods_gen.sh`

Nogoods:

* `search1.txt`
* `search2.txt`
* `search3.txt`

### Result

```python
# search 1
X_INTRODUCED_96_>=1 X_INTRODUCED_98_>=1
X_INTRODUCED_79_>=1 X_INTRODUCED_77_>=1
X_INTRODUCED_67_>=1 X_INTRODUCED_59_>=1 X_INTRODUCED_57_>=1
# search 2
objective>=204
X_INTRODUCED_47_<=0
X_INTRODUCED_96_>=1 X_INTRODUCED_90_>=1 X_INTRODUCED_106_>=1
X_INTRODUCED_134_>=1 X_INTRODUCED_128_>=1 X_INTRODUCED_144_>=1
X_INTRODUCED_57_>=1 X_INTRODUCED_67_>=1 X_INTRODUCED_51_>=1
X_INTRODUCED_115_>=1 X_INTRODUCED_125_>=1 X_INTRODUCED_109_>=1
X_INTRODUCED_115_>=1 X_INTRODUCED_109_>=1 X_INTRODUCED_121_>=1
X_INTRODUCED_87_>=1 X_INTRODUCED_77_>=1 X_INTRODUCED_71_>=1
# search 3
X_INTRODUCED_109_>=1
X_INTRODUCED_63_>=1 X_INTRODUCED_51_>=1 X_INTRODUCED_59_>=1
X_INTRODUCED_102_>=1 X_INTRODUCED_98_>=1 X_INTRODUCED_90_>=1
X_INTRODUCED_71_>=1 X_INTRODUCED_83_>=1 X_INTRODUCED_79_>=1
```

As we can see, itemsets in different search order could be very different.