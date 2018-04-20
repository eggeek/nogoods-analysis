#!/usr/bin/env python
import sys
import json
import os
from collections import defaultdict
from model import parser
from model import predicates

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
    try:
      parsed = parser.parse_nogood(nogood)
      pattern = ' '.join([literal_transform(i) for i in parsed])
      values = {}
      for j in parsed:
        if j['idx_label'] is not None:
          values[j['idx_label']] = j['idx']
        values[j['num_label']] = j['num']
      facts = predicates.gen_facts(values, data)
      res[pattern].append({'values': values, 'facts': facts})
    except Exception as e:
      print 'Nogood: %s' % nogood
      print e.message
      print 'The nogood has been ignored.'
  return res

def work(instance_path):
  instance_name = os.path.basename(instance_path)
  csv_path = instance_path.strip('/') + '/' + '%s.csv' % instance_name
  dzn_path = instance_path.strip('/') + '/' + '%s.dzn' % instance_name
  output_path = '../output/%s.json' % instance_name
  nogoods = extract_nogoods(csv_path)
  with open(dzn_path, "r") as f:
    content = f.readlines()
    data = parser.parse_dzn(content)
  pattern = extract_pattern(nogoods, data)
  with open(output_path, 'w') as f:
    json.dump(pattern, f, indent=2, sort_keys=True)

if __name__ == "__main__":
  work(*sys.argv[1:])
