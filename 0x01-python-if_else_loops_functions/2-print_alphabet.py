#!/usr/bin/python3

for i in range (97,123):
    print(''.join('{} '.format(chr(i)) for i in range(97, 123)), end="")