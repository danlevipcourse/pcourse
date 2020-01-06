from collections import defaultdict, Counter
from contextlib import contextmanager
import pickle
import os
import shelve

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print(d.items())


# Ex1 keydefaultdict
class keydefaultdict(defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        self[key] = value = self.default_factory(key)
        return value


s = [7, 8, '8']
d = keydefaultdict(int)
for k in s:
    d[k]
print(d.items())

# Ex4 CharCounter
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1


def char_count(charString, most_common):
    cnt = Counter(charString)
    return dict(cnt.most_common(most_common))


print(char_count("abbcccdddd", 2))


def word_count(wordString, most_common):
    cnt = Counter(wordString.split(" "))
    return dict(cnt.most_common(most_common))


print(word_count("How much wood can a woodchuck chuck if a woodchuck would chuck wood", 2))


# Ex6 implement a dB

class DB(object):
    def __init__(self, path):
        self._path = path
        self._dict = {}
        self.open()

    def open(self):
        try:
            with open(self._path, 'rb') as fid:
                self._dict = pickle.loads(fid.read())
        except IOError as e:
            self._dict = {}
        except EOFError as e:
            os.remove(self._path)

    def close(self):
        with open(self._path, 'wb') as fid:
            fid.write(pickle.dumps(self._dict))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __getitem__(self, item):
        return self._dict[item]

    def __setitem__(self, key, value):
        self._dict[key] = value
        self.close()


with DB(path='db.txt') as db:
    db['a'] = 10
    db['b'] = [1, 2, 3]

db = DB(path='db.txt')
print(db['a'])
print(db['b'])
db.close()
