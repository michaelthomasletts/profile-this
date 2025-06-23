import os
from random import randint

from profile_this import profilethis

docs = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs"))


@profilethis(title="Profile for func", path=os.path.join(docs, "func.png"))
def func(n=10_000_000):
    return sum([randint(0, i + 1) for i in range(n)])


def test_profile_this():
    func()
