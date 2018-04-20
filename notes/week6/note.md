## Experiment

What have done:

* logs are from `pizza27.dzn`, running 10s


* some clauses are frequently, but they are something like:

  * `x1<=0 x2<=0 x3<=0 ...`

* some log lines are not in right format:

  > …X_INTRODUCED\_673_<=0 X_INTRODUCED_677_<=0 X

  end with `X`

  * this happend at last line

    Guess because the logger didn't finish writing when it was killed

* low sup, high conf

  * sup=0.2, con=0.9

  The number of sup is over than 4k, probably we have too much transactions.

* about 20 rules.

  * 4 rules are in form $A, B, C \implies D$
  * other rules are in form $A,B \implies C$

* Dont know the exactly meaning, need transalte to variable name.

* How to measure the qualify of rules?

  ​

What going to do:

* Try 3s, 6s, …, 20s log, 30s log, ...

  * some interesting facts  (probably) :

    * we need reduce `sup` threshold with time increase

    * more rules with similar format.

      for example, rule $A,B \implies C$ on $v_1$ may also occur on $v_2, v_3…v_k$ 

* Try different input

  * may find some similar rules, those maybe general rules over the problem.

* Try different modeling

  * may find different rules
  * may also include general rules



Does better model include more/less nogoods?

Does better model include more/less rules?

## Paper



> Further, static methods sometimes disagree with the search
>
> strategy [11], that is, they might select a representative that is not among the
>
> solutions that the search would have found rst, or might add constraints with
>
> poor propagation for the particular search strategy used.



Does this means, redundant constraint may damp the performance?



> … since they always agree with the search strategy

What does `search strategy` mean?



Let $\sigma$ be a symmetry of the problem.

> $\neg (d1 \land d2 \land … d_k) \implies \neg(\sigma(d1) \land \sigma(d2) … \sigma(dk))$

Does it means $\sigma(d) = d$ ?

Can we generate $2^k$ nogoods? Will those be helpful?



> The problem is split by making dierent decisions $d_i$ down each branch

Does solver naturally perform binary search?

Can solver perform binary search on set of variable? For example:

​	There is monotony in $v_1+v_2+v_3$ , the solver will perform binary search on $v_1+v_2+v_3$ and perform a normal search to find value of $v_1$, $v_2$ and $v_3$.



* Logical formulas: implies

  > If pigs fly, then your account won’t get hacked.

What does it mean, when we talking about the true/false of a `implies statement`.

For example, I can write down a `iff statement` as a mathematical theorem. It can be proofed either true or false. However, if I write down a `implies statement` ...