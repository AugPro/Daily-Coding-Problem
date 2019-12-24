"""This problem was asked by Amazon.

Given an integer k and a string s, find the length of the
longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2,
the longest substring with k distinct characters is "bcb"."""


def main(word, k):
    temp = ""
    start = 0
    end = k
    while end <= len(word):
        sub = word[start:end]
        if len(set(sub)) <= k:
            temp = max(temp, sub, key=len)
            end += 1
        else:
            start += 1
    return temp



if __name__ == '__main__':
    assert main("abcba", 2) == "bcb"
    assert main("abcba", 3) == "abcba"
