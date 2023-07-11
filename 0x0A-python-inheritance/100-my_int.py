#!/usr/bin/python3


class MyInt(int):
    """Inherits from int"""
    def __eq__(self, other):
        """inverts == to != and vice versa"""
        return super().__ne__(other)

    def __ne__(self, other):
        """inverts != to == and vice versa"""
        return super().__eq__(other)
