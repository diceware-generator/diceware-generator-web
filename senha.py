#!/usr/bin/python3
import random, sys

w = [s.split()[0] for s in open(sys.path[0]+'/dicionario-pt-low.txt')]
print(' '.join(random.SystemRandom().choice(w) for i in range(6)))