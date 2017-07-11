int: n; % number of pizzas
set of int: PIZZA = 1..n;
array[PIZZA] of int: price;   % price of each pizza

int: m; % number of vouchers
set of int: VOUCHER = 1..m;
array[VOUCHER] of int: buy;   % buy this many to use voucher
array[VOUCHER] of int: free;  % get this many free

set of int: ASSIGN = -m .. m; % -i pizza is assigned to buy of voucher i
                              %  i pizza is assigned to free of voucher i
                              %  0 no voucher used on pizza

array[PIZZA] of var ASSIGN: how;
array[VOUCHER] of var bool: used;

% NOTE(maxim): if a voucher is used,
% the number of pizzas bought with a voucher >= number of pizzas required by the voucher
constraint forall(v in VOUCHER)(used[v] <-> sum(p in PIZZA)(how[p] = -v) >= buy[v]);

% NOTE(maxim): the number of pizzas bought with a voucher <= number of pizzas
% required by the voucher (if the voucher is used) NOTE(maxim): the same as above?
constraint forall(v in VOUCHER)(sum(p in PIZZA)(how[p] = -v) <= used[v]*buy[v]);

% NOTE(maxim): number of free pizzas got with a voucher do not exceed the specified number
constraint forall(v in VOUCHER)(sum(p in PIZZA)(how[p] = v) <= used[v]*free[v]);

% pizzas assigned to free are cheaper than pizzas assigned to buy
constraint forall(p1, p2 in PIZZA)((how[p1] < how[p2] /\ how[p1] = -how[p2]) 
                                   -> price[p2] <= price[p1]);

int: total = sum(price);
var 0..total: objective = sum(p in PIZZA)((how[p] <= 0)*price[p]);

array[PIZZA] of int: search_order = [ 8, 4, 7, 2, 1, 9, 6, 5, 3 ];

solve :: int_search(sort_by(how, search_order), input_order, indomain_max, complete) minimize objective;

output ["how = "++show(how)++",\nobjective = "++show(objective)++ "used = ", show(used), ",\n"];