"""This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place."""

def main(li):
    li=set(li)
    start = 1
    while True:
        if start not in li:
            return start
        start+=1
    pass


if __name__ == '__main__':
    assert main([3, 4, -1, 1])==2
    assert main([1, 2, 0])==3
