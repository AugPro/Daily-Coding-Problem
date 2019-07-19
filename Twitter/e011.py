"""This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries."""

def main(li, pref):
    return {el for el in li if el.startswith(pref)}

if __name__ == '__main__':
    assert main({'dog','deer','deal'}, 'de')=={'deer','deal'}


"""
The scalable solution is definitely the one using a tree representing
the set of possibilities for easier search.

In this case it would look like:

       d
      / \
     og  e
        / \
       er  al

"""
