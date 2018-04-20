## Question

* Limitation of CP solver

  - can a solver deal with any computing problem?

* Can solver realize

  * symmetric constraint

    seems possible, can be learnt from nogoods.

  * a greedy strategy

    seems impossible, information hide behind *solutions*, not *conflicts*.

* What should be `transaction`

  * nogoods?
  * solutions?

* Can we learn from solutions?

## Association rule mining

* Confidence

  `confidence` is a threshold of rule, while `support` is a threshold of itemset

  * rule 
    * $A => B$ , $A$ and $B$ are itemset
  * $confidence(A=>B) = sup({A, B})/sup(A) = P(B|A)$  

* Generate rules from frequent itemset

  * $x$ is a itemset, and $s \subset x, s \neq \emptyset$
    $$
    rules(x) = \{s=>(x-s) | sup(x)/sup(s) >= min\_conf\}
    $$





* What about generating rules from non-frequent itemset ?

  for example, if `a` in basket and `b` in basket then `c` in basket, but only with `a` or `b`, won't cause `c` in basket.

  * Is such rule useless? or is it too expansive to generate? or it's laid in another problem domain.

  ​

  ​

* Lift
  $$
  lift(A->B) = \frac{sup(A,B)}{sup(A)  sup(B)} = \frac{P(B|A)}{P(B)}
  $$
  ​

  * $confidence$ can be misleading, so we also take $P(B)$ into consider.

  * The range of $lift$ should in range of $[0, \infty]$

    What can we learn, if:

    * $lift$ is very small
      * $P(B|A)$ is much smaller than $P(B)$, does this means $A->\neg B$ ?
    * $lift$ is very large
      * $P(B|A)$ is much larger than $P(B)$, the rule is strong
    * $lift \approx 1$
      * does this means: there is no rule between $A$ and $B$ ?

  * Problems

    * when $P(B)$ is naturally large, even $P(B|A) = 1$ , $lift$ can't be a large number

    * symmetric
      $$
      lift(A->B) = \frac{sup(A,B)}{sup(A)sup(B)} = lift(B->A)
      $$
      ​

      does it means $lift$ can only find rule like $iff$ ?



* Conviction
  $$
  conv(A->B) = \frac{sup(A)sup(\neg B)}{sup(A, \neg B)} = \frac{1}{lift(A->\neg B)}
  $$
  ​

  notice that
  $$
  conv(A->B) = conv(\neg B->A)
  $$
  does this means that a rule $A->B$ can also be expressed as $\neg B -> A$ ? (really weird)

* Leverage of a Rule (Piatetsky‐Shapiro)
  $$
  PS(A->B) = sup(A, B) - sup(A) sup(B)
  $$
  why we need this?

* python lib: https://github.com/bartdag/pymining

* java lib: http://www.philippe-fournier-viger.com/spmf/
