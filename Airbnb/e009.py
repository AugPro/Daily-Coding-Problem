"""This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?"""


def main(li):
    score = dict()
    for i,val in enumerate(li):
        score[i] = max(score.get(i-1,0),score.get(i-2,0)+val)
    return score[len(li)-1]


if __name__ == '__main__':
    assert main([2, 4, 6, 2, 5])==13
    assert main([5, 1, 1, 5])==10
