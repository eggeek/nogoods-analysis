## Question

1. [sokoban](https://en.wikipedia.org/wiki/Sokoban)

   Can this game be solved by CP?

    Given a configuration of the game, determine whether it can be solved, or find a solution.

   * It seems hard to define the movement by CP language.

2. [Alien](https://polygon.codeforces.com/statements/previewAsPdf/alien-r9-en.pdf?lang=english&ccid=8bd4f1756db08900056c81de143fd507&session=ca3762eed44781da921575ccefd86a8e96cbbc58)

   1. brute-force search: exponential
   2. greedy + brute-force: $O(n^2\log(n))$ 
   3. greedy + symmetric + monotony: $O(n^2)$ / $O(n\log(n))$ (if use binary search)
   4. greedy + symmetric + monotony + specific order: $O(n)$ 

   What if I run in chuffed solver and analyze learnt log?

## Experiment

What have done:

* It took 30min to finish, with input pizza27.dnz, and nodes.csv has 17G.
* Running 10s will generate 6k lines log, but only one with nogood.
* When finished, we will get 10 million lines log and 4 million nogoods.
* a $literal$ is like $x\_INTRODUCED\_id\_\oplus num$
* a $clause$ is like $literal_1\ literal_2\ …\ literal_i$ 

Next:

* Map a $literal$ to a integer, as item id, and turn a $clause$ to a transaction
* Run data mining algorithm
* Translate outputs to $literal$ and $clause$

Probably, there are nothing interesting in output, because multiple $literal$ may in same meaning, and we should regard them as a same item.

So we may need $classify$.

How?

* $literal$ with same $id$ ?
* $literal$ with close $num$ ?
* $literal$ with similar domain?



A Guess:

We should consider both $num$ and $id$, because what I expect is find some genral things like
$$
how_i <= f(i, C)
$$
where $C$ is constant, and $f$ is a function, and $num = f(i,C)$.

For example, given: $l_1:x_1 \leq 3$, $l_2: x_2 \leq 4$, $l_3: x_3<=5$ , $l_4=x_4\leq7$ 

$l_1,l_2,l_3$ should be in same class and $l_4$ should in other class, because

$l_1,l_2,l_3$ are fit the same function $f(x)=x+2$ .



Now the problem is: given a sort of points in xy coordinate, classify them by their function expression.

Can this be solved by SVM?

  