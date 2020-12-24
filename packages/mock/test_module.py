# -*- coding: utf-8 -*-

from mock import patch
from foo_module import some_func


def test_fun():
    with patch("foo_module.Foo") as mock:
        instance = mock.return_value
        instance.ins_func.return_value = "mock result"
        instance.labels = [1, 2, 3, 4, 5]

        result = some_func()
        assert result == "mock result"
