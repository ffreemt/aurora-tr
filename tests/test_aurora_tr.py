"""
Test aurora_tr.

run `rye run pytest`
"""
import os
from aurora_tr import aurora_tr


def test_aurora_tr():
    """Test aurora_tr."""
    _ = aurora_tr()
    assert _.startswith("aurora")
