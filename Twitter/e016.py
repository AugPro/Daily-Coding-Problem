"""This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log.
i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible."""


class FixedSizeLog:
    """Used to store only the last {size} elements of a log
       Space complexity : O(size)
    """
    def __init__(self, size):
        self.size = size
        self.log = [None]* size
        self._cursor = 0

    def record(self, order_id):
        """Adds order_id to log
           Time complexity : O(1)
        """
        cursor = self._cursor
        self.log[cursor] = order_id
        self._cursor = cursor + 1 if cursor+1 != self.size else 0

    def get_last(self, index):
        """Returns the last ith element from the log
           only works for index smaller than self.size
           Time complexity : O(1)
        """
        return self.log[self._cursor - index] # Uses Python negative indexation


def test_log():
    log = FixedSizeLog(size=10)
    for i in range(20):
        log.record(i)
    assert log.get_last(5) == 15
