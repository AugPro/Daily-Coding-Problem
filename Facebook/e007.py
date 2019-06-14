"""This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed."""

def main(msg):
    if len(msg) in (0,1):
        return 1
    elif msg[:2]<='26':
        return main(msg[1:])+main(msg[2:])
    else:
        return main(msg[1:])


#This solution could be better if dynamic programming was implemented

if __name__ == '__main__':
    assert main('321')==2
    assert main('111')==3
    assert main('1215')==5
