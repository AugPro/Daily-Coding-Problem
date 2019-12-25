"""This problem was asked by Facebook.

Given a stream of elements too large to store in memory,
pick a random element from the stream with uniform probability."""
from random import random


def uniform_pick(gen):
    res = None
    for i, elt in enumerate(gen):
        if random() < 1/(i+1):
            res = elt
    return res

def test_uniform():
    nb = 10
    tries = 10**5
    picks = {i:0 for i in range(nb)}
    for i in range(tries):
        picks[uniform_pick(range(nb))] += 1
    for value in picks.values():
        assert round(value/tries, 2) == round(1/nb, 2)
