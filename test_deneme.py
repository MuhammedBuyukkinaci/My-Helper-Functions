# This test code was written by the `hypothesis.extra.ghostwriter` module
# and is provided under the Creative Commons Zero public domain dedication.

import temp
from hypothesis import given, strategies as st

# TODO: replace st.nothing() with an appropriate strategy


@given(x=st.nothing())
def test_fuzz_pop_list(x):
    temp.pop_list(x=x)

