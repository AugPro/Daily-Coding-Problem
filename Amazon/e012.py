"""This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time."""


def main(N,X):
    if N<0:  return 0
    if N==0: return 1
    return sum((main(N-x,X) for x in X))

if __name__ == '__main__':
    assert main(4, {1,2})==5
    assert main(6, {1,3,5})==8  # 51 33 3111 15 1311 1131 1113 111111
