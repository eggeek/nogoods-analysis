## Experiment

### Last week

Last week we got some results from experiment, however, those results are wrong, because the `spmf` library require all transactions are sorted by lexicographical.

### Steps

1. `./nogoods_gen.sh`: extract nogoods from log

2. `./tokenize.sh ` 

   * extract tokens from nogoods, saved in a dict
   * generate transactions by using the dict
   * `./tokenize.sh -l` regard literal as token
   * `./tokenize.sh -i` regard identifier as token

3. `./mining.sh`: perform itemset mining and rule mining algorithm on transaction

   * $sup=0.68$, $conf=0.8$


* `./mining.sh -i` mining identifier transaction
   * `./mining.sh -l` mining literal transaction

4. `./summarize.sh`: remoe itemset/rule which already covered by other itemset/rule

   * `./summarize.sh -i`
   * `./sumarize.sh -l`

5. `./trans.sh`: replace item id by token

   * `./trans.sh -i`
   * `./trans.sh -l`

### Result

* identifier

  * 36 raw itemsets, 4 summarized

  * 16 raw rules, 5 summarized

  * identifier summary

    ```
    X_INTRODUCED_172_ X_INTRODUCED_169_ X_INTRODUCED_166_
    X_INTRODUCED_177_ X_INTRODUCED_3446_
    X_INTRODUCED_172_ X_INTRODUCED_169_ X_INTRODUCED_3446_
    X_INTRODUCED_177_ X_INTRODUCED_172_ X_INTRODUCED_169_
    ```

    ​

* literal

  * 130 raw itemsets, 4 summarized

  * 1144 raw rules, 4 summarized

  * literal summary

    ```
    X_INTRODUCED_172_>=4 X_INTRODUCED_169_>=4 X_INTRODUCED_166_>=4 X_INTRODUCED_172_==2 X_INTRODUCED_169_==2 X_INTRODUCED_166_==2
    X_INTRODUCED_177_>=4 X_INTRODUCED_177_==2 X_INTRODUCED_3446_<=0
    X_INTRODUCED_177_>=4 X_INTRODUCED_172_>=4 X_INTRODUCED_169_>=4 X_INTRODUCED_177_==2 X_INTRODUCED_172_==2 X_INTRODUCED_169_==2
    X_INTRODUCED_172_>=4 X_INTRODUCED_169_>=4 X_INTRODUCED_172_==2 X_INTRODUCED_169_==2 X_INTRODUCED_3446_<=0
    ```

### Notice

* identifier and literal have similar summary
  * does this means conflicts are caused by a set of specific value?
* `X_INTRODUCED_172_>=4 X_INTRODUCED_169_>=4 X_INTRODUCED_172_==2`
  * how?
  * ~~does this means the solver make decision in a poor order?~~
  * ~~or something goes wrong in path file~~
  * ~~or there is a bug in my script…~~ (I've verified)
* seems rule mining doesn't make a lot sense
  * I guess...
    * rule mining can reveal the inner structure of itemset
    * but such structures have been overwhelmed by  meaningless nogoods
* there is a threshold on $sup$
  * when $sup <= 0.66$, the itemset mining can't finish
  * when $sup > 0.66$, it only take 300ms
* the experiment only analyzed 10s log, but it tooks solver 30min to finish
  * analyzed different time interval may find different result
  * but different piece of log may have different $sup$ threshold