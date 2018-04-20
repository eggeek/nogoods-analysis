* In I-Graph, is a vertex a literal of clause?

  For example, in right-angled triangle search problem, how to find nogoods when $x=3, y=5$?

* When does the I-Graph build?

  * when encounter a conflict?
  * when new constraints have been added?
  * ...

* `prof_learn`

  * non-learning solver execute learning solver's history, so that we can evaluate the actual effect of learnt clause while ignore the time cost on learning.



* Why DM doesn't work (guess)
  * noise
  * need algebra, not nogoods.
  * what is automatic proof?
* [Automatic Generation of Implied Constraints](http://ccg.doc.gold.ac.uk/papers/charnley_ecai06.pdf)
