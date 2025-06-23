import os
from random import randint

from profile_this import ProfileThis


def func(n=10_000_000):
    return sum([randint(0, i + 1) for i in range(n)])


def test_profile_this():
    docs = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "docs")
    )
    profiler = ProfileThis()
    profiler.start()
    func()
    profiler.stop()
    profiler.plot(
        title="Profile for func",
        path=os.path.join(docs, "func.png"),
    )
