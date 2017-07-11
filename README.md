## Structure

* input: instance folders, each folder contains: `*.csv, *.mzn, *.dzn`, for example:

```
#!

  ├── input
  │   ├── pizza_search1a
  │   │   ├── pizza_search1a.csv
  │   │   ├── pizza_search1a.dzn
  │   │   └── pizza_search1a.mzn
  │   └── pizza_search1b
  │       ├── pizza_search1b.csv
  │       ├── pizza_search1b.dzn
  │       └── pizza_search1b.mzn
```

* src

## Assumptions

* header of `*.csv` is: `occurence, reduction, nogood`
* nogoods are in format: `A[num] op num` or `V op num `, where:
  * `A` is array (e.g. `how[]`)
  * `num` is concrete numeric value or `true/false`
  * `V` is variable (e.g. `objective`)
  * `op` is operator: `>=, >, <=, <, =, !=`
* only consider fact in format: `A[num] op A[num]` and `num op num`