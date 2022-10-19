#!/usr/bin/python3
"""A module for a locked class"""


class LockedClass:
    """A locled class"""
    def __setattr__(self, attribute, value):
        """intercepts atrrs creatio """
        if attribute == "first_name":
            return
        raise AttributeError("'Locked'")
