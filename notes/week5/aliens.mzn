array[int] of int: feels;

int: n = length(feels);

var 0..n: A;
var 0..n: B;
var 0..n: C;

array[int] of var 0..n: population = [A,B,C];

array[1..n] of var 1..3: planet;

array[1..n, 1..3] of var 0..max(feels): a;

constraint forall (i in 1..n) (a[i,1]+a[i,2]+a[i,3]=feels[i]);

constraint forall (i in 1..n) (a[i,planet[i]] = population[planet[i]]);

include "globals.mzn";

constraint forall (i in 1..3) (count(planet,i) = population[i]);

constraint forall (i in 1..n, j in 1..3) (a[i,j] <= population[j]);

constraint forall (i in 1..n) (planet[i] = 1 -> a[i,3] = 0);
constraint forall (i in 1..n) (planet[i] = 3 -> a[i,1] = 0);

solve maximize max (i in 1..n) (a[i,1]);

output [show2d(a)++"\n"++show(planet)++"\n"++show(population)++"\n"];
