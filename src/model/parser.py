import re

pat_von = re.compile('([a-zA-Z0-9\_\[\]]+)(>=|<=|>|<|!=|==|=)(\-?\d+\.?\d*|true|false)')
pat_idx = re.compile('\[(\d+)\]')

def to_numeric(s):
  if s == 'true':
    return True
  elif s == 'false':
    return False
  else:
    try:
      return int(s)
    except Exception:
      return s

def gen_label(num):
  label = ''
  if num == 0:
    label = 'A'
  else:
    while num:
      label += chr(num % 26 + ord('A'))
      num /= 26
  return label

def parse_literal(txt):
  """
  txt: 'how[4]=-3' or 'used[3]=false or objective<=1'
  return
  {
    'original': 'used[3]=false'
    'v': 'used',
    'idx': 3,
    'op': '='
    'num': 'false'
    'key': 'used[_]=_'
  }
  """
  comps = pat_von.findall(txt)
  if len(comps) != 1:
    raise Exception('Parsing Error:' + txt)
  v, op, num = comps[0]
  idx = pat_idx.findall(v)
  idx = to_numeric(idx[0]) if len(idx) == 1 else None
  num = to_numeric(num)
  v = pat_idx.sub('', v)
  key = '%s%s%s' % (v, op, '_')
  return dict(v=v, idx=idx, op=op, num=num, key=key)

def parse_nogood(nogood):
  """
  nogood: 'how[4]=-3 objective>=198 how[9]=-3 how[6]=-3 how[5]=-3 how[6]>0 used[3]=false'
  return
  [
    {
      'original': 'used[3]=false',
      'v': 'used',
      'idx': 3,
      'op': '=',
      'num': 'false',
      'key': 'used[_]=_',
      'idx_label': 'A',
      'num_label': 'B'
    },
    ...
  ]
  """
  txt = nogood.strip()
  literals = [parse_literal(i) for i in txt.split()]
  literals.sort(key=lambda x: x['key'])
  res = []
  cnt = 0
  for i in literals:
    idx_label = None
    num_label = None
    if i['idx'] is not None:
      idx_label = gen_label(cnt)
      cnt += 1
    num_label = gen_label(cnt)
    cnt += 1
    i['idx_label'] = idx_label
    i['num_label'] = num_label
    res.append(i)
  return res

def parse_dzn(content):
    res = {}
    for line in content:
        name, raw_var = map(lambda x: x.strip(), line.strip(';\n').split('='))
        # var is list
        if '[' in raw_var:
            var = [int(i) for i in raw_var[1:-1].strip().split(',')]
        # var is a number
        else:
            var = int(raw_var)
        res[name] = var
    return res
