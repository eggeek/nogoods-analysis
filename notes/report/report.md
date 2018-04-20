# Data mining techniques for analysing clause learning solvers

## Abstract

Learnt clause is an constraint added by solver during the search. It can prevent solver from explore conflict subtrees which are already encountered, so that improved performance of search. However, the performance  is not only depend on solver, but also on model. A naive model may not able to reveal deep structure of the problem, and has bad performance. Usually, improving model involves a lot of user's effort. In order to relieve such effort, we try to apply data mining techniques on learnt clauses, to see whether this combination can automatically reveal deep structures of the problem and improve model.

## Literature review

* literature review of cp
  * background of cp
    - learning
    - learnt clause
    - lazy clause generation (?)
  * **prof_learning**
    * how to manually analyze nogoods
    * how to count reduced search


* literature review of data mining

  * apriori algorithm

  * rule mining

    *summarize formulas, in what motivation, benefit what kind of dataset...*

  * improvement: by using inverted table or big data tools (e.g. Hive)

    Briefly speaking, itemset mining is computing $sup$, where $sup$ measure the number of cover of a itemset. The difficultly of this work is from set searching. Apriori algorithm achieve this function by using `hashtree` . However, in big data scenario, `inverted index` is more suitable. 

* **combine cp and data mining**

  * what are transactions
  * what does itemset imply
  * what does rule imply

## Experiment

* simply introduce `chuffed` solver and `spmf` data mining library
* experiment on 10s log
  * what we've found
  * what do those mean
  * problems and solution
    * limitations of the experiment
    * `sup` threshold
    * solution
* experiment on entire log for input `pizza27.dzn`
* further  improvement
  * use Hadoop

## Conclusion



## Reference

