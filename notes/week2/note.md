## What is learning?
* [Clause Learning in SAT](https://www.cs.princeton.edu/courses/archive/fall13/cos402/readings/SAT_learning_clauses.pdf)

    A process to detect *confilic clause*, extract `reason` information and `confilict` information.

* Conflict Clause

> an assignment to a subset  of variable from the problem that never be part of solution


## How to use learnt clause?
In `Learning from Learning Solvers`.
Given clause like:
> {mark[6] >= 38, mark[5] <= 35, mark[4] <= 34}
> {makr[5] >= 18, mark[4] <= 15, mark[3] <= 14}
> ...

How to find pattern automatically, find something like:
> {mark[i] >= n, mark[i+1] >= n+1, mark[i+2] >= n+3}


## Lazy clause generation
* Translate CSP to SAT
* Generate clauses in run time
* Trade off between strength of the information inferred and efficiency
    * Question: how does lazy clause generation make impact on strength?

## How to use itemset minging

1. Encode `SAT` or `CSP` by itemset problem (refer [*On SAT Models Enumeration in Itemset Mining*](https://arxiv.org/pdf/1506.02561.pdf))
2. Design evaluate function
3. Measure the quality of learnt data ( refer *Predicting Learnt Clauses Quality in Modern SAT Solvers*)
4. Select the best threshold
