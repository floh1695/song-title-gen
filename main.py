#!/usr/bin/python3

import pathlib
import random
import requests
import sys

nouns_source = 'http://www.desiquintans.com/downloads/nounlist/nounlist.txt'
nouns_file = pathlib.Path('./.words.nouns.csv')

noun_separator = ','

def nouns_exist():
  return nouns_file.exists()

def non_empty_iter(iter):
  return len(iter) > 0

def fetch_nouns():
  results = requests.get(nouns_source)
  nouns = results.text.split('\n')
  filtered_nouns = filter(non_empty_iter, nouns)

  noun_data = noun_separator.join(filtered_nouns)
  nouns_file.write_text(noun_data)

def get_nouns():
  noun_data = nouns_file.read_text()
  nouns = noun_data.split(noun_separator)
  return nouns

def main(verbose=False):
  if not nouns_exist():
    fetch_nouns()

  nouns = get_nouns()
  if verbose:
    noun_count = len(nouns)
    print(f'count of nouns: {noun_count}')
  chosen_nouns = random.sample(nouns, 3)
  print(' '.join(chosen_nouns))

if __name__ == '__main__':
  args = sys.argv
  verbose = '-v' in args
  main(verbose=verbose)
