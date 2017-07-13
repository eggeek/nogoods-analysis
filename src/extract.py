#!/usr/bin/env python
import sys
import json
from collections import defaultdict
from model.parser import *

def extract_nogoods(path):
  """
  Assumption:
    header of *.csv is `occurence, reduction, nogood`
  """
  nogoods = []
  with open(path, "r") as f:
    for line in f:
      if line.strip() == 'occurrence, reduction, nogood':
        continue
      nogoods.append(line.split(',')[-1].strip())
  return nogoods


def dzn2json(content):
  return content


def literal_transform(l):
  """
  l:
    {
      'v': ,
      'op':,
      'num_label':,
      'idx_label':
    }
  """
  if l['idx_label'] is not None:
    return '%s[%s]%s%s' % (l['v'], l['idx_label'], l['op'], l['num_label'])
  else:
    return '%s%s%s' % (l['v'], l['op'], l['num_label'])


def extract_pattern(nogoods=[], data={}):
  """
  return json:
    {
      pattern: [
        {
          'values': {label: num, ...},
          'facts': [fact1, fact2, ...]
        },
        ...
      ],
      ...
    }
  """
  res = defaultdict(list)
  for nogood in nogoods:
    parsed = parse_nogood(nogood)
    pattern = ' '.join([literal_transform(i) for i in parsed])
    values = {}
    for j in parsed:
      if j['idx_label'] is not None:
        values[j['idx_label']] = j['idx']
      values[j['num_label']] = j['num']
    facts = []
    res[pattern].append({'values': values, 'facts': facts})
  return res


def work(csv_path="", dzn_path="", output_path=""):
  nogoods = extract_nogoods(csv_path)
  with open(dzn_path, "r") as f:
    content = f.readlines()
    data = dzn2json(content)
  pattern = extract_pattern(nogoods, data)
  with open(output_path, 'w') as f:
    json.dump(pattern, f, indent=2, sort_keys=True)

if __name__ == "__main__":
  work(*sys.argv[1:])
