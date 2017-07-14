from collections import namedtuple

variable = namedtuple("variable", ['label', 'v'])

def eq(v1, v2, arr):
  try:
    if arr.v[v1.v] == arr.v[v2.v]:
      return True, '%s[%s]=%s[%s]' % (arr.label, v1.label, arr.label, v2.label)
    else:
      return False, ''
  except Exception:
    return False, ''

def eq2(v1, v2, *argv, **kw):
  if v1.v == v2.v:
    return True, '%s=%s' % (v1.label, v2.label)
  else:
    return False, ''

def neq(v1, v2, arr):
  try:
    if arr.v[v1.v] != arr.v[v2.v]:
      return True, '%s[%s]!=%s[%s]' % (arr.label, v1.label, arr.label, v2.label)
    else:
      return False, ''
  except Exception:
    return False, ''

def lt(v1, v2, arr):
  try:
    if arr.v[v1.v] < arr.v[v2.v]:
      return True, '%s[%s]<%s[%s]' % (arr.label, v1.label, arr.label, v2.label)
    else:
      return False, ''
  except Exception:
    return False, ''

def gt(v1, v2, arr):
  try:
    if arr.v[v1.v] > arr.v[v2.v]:
      return True, '%s[%s]>%s[%s]' % (arr.label, v1.label, arr.label, v2.label)
    else:
      return False, ''
  except Exception:
    return False, ''

functors = [eq, eq2, lt, gt]

def gen_facts(values={}, data={}):
  """
  values:
    { label: num, ... }
  data:
    { key: num, key: [num, num, ...], ... }
  """
  tuples = []
  for k1 in values.keys():
    for k2 in values.keys():
      if k1 > k2:
        tuples.append((k1, k2))
  facts = set()
  for i in tuples:
    a = variable(i[0], values[i[0]])
    b = variable(i[1], values[i[1]])
    for k, v in data.items():
      arr = variable(k, v)
      for p in functors:
        res, desc = p(a, b, arr)
        if res is True:
          facts.add(desc)
  return list(facts)
