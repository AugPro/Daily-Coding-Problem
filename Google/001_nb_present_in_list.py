"""This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?"""

def main(li,k):
    visited = set()
    for n in li:
        if k-n in visited:
            return True
        visited.add(n)
    else:
        return False


if __name__ == '__main__':
    assert main([10, 15, 3, 7],17)
