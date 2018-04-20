## Experiment

* Nogood rank

  * Is it possible:

    `a` caused 1k nogoods, and `b` caused `a`?

  * if so, should `b` 's rank higher than `a`?

  * do we need use `Page Rank` or something similar?

    guess: probably make thing much more complicated and not helpful.

* Implementation

  * $s_1$ and $s_2$ are in summarized itemsets, how to generate complement transaction?
    * $\{t - union(s_1, s_2) | t \in transactions\}$
    * $\{t - s_1 | t \in transactions\} \cup \{t-s_2 | t \in transactions\}$



### Result

*   tokenize by `literal` or `identifier` have similar result

    probably means nogoods have involved specific variable with specific value

* different data mining algorithms:

    using apriori / apriori_close can get different itemset/rules, but summary are similar

* complement itemsets

    * apirori

        ```
        count  49299.000000
        mean      86.179375
        std       79.459914
        min       10.000000
        25%       11.000000
        50%       18.000000
        75%      171.000000
        max      189.000000
        ```

        ​

    * apriori_close

        ```
        count  47789.000000
        mean      87.102367
        std       79.567451
        min       10.000000
        25%       12.000000
        50%       16.000000
        75%      171.000000
        max      187.000000
        ```

        ​

* try to perform itemset mining on complement itemsets

    * apriori

        * there is a threshold $t$ on $sup$, about 0.69
        * $\ge t$ , no itemsets
        * $\lt t$, would generate more than 100G itemsets, almost involved each transaction
        * guess: most of transactions are combination of a sort of `smaller` itemsets. 

    * apriori_close

        ```
        3 #SUP: 26446
        17 #SUP: 27237
        3 4  #SUP: 25875
        13 14  #SUP: 28406
        ```

        ​

* summary itemsets over 10s log and total log are similar

## Nogoods review

* $s = l_1 \lor l_2 \lor … \lor l_k$ is a nogoods

  * $s$ must be true, otherwise we would end up with $failure$.
  * there are no implication like $l_1 => l_i$ or $l_1 => \lnot l_i$ , because of `1UIP`.

* $s$ in summarized itemsets, means there are a sorts of nogoods in form:

  $s \lor clause_1$, $s \lor clause_2$ , … $s \lor clause_m$

  * can those be a hint for solver? e.g.
    * make decision on variable in $s$ first, so that solver can satisfy more constraints.


```
X_INTRODUCED_177_==2 X_INTRODUCED_177_>=4 X_INTRODUCED_172_==2 X_INTRODUCED_172_>=4
X_INTRODUCED_172_==2 X_INTRODUCED_172_>=4 X_INTRODUCED_169_==2 X_INTRODUCED_169_>=4 X_INTRODUCED_3421_<=0
```

1st itemset can be interpreted as

```
how[178]==2 || how[178]>=4 || how[173]==2 || how[173]>=4
```

notice that 

```
buy = [3,2,3,2];
free = [5,7,5,7];
```

we can replace `>=` by `==`

```
how[178]==2 || how[178]==4 || how[173]==2 || how[173]==4
```

why `price[178]`, `price[173]` and `price[170]` are so special?