#!/usr/bin/python3
"""A module for a locked class"""


class LockedClass:
    """A locled class"""
    def __setattr__(self, attribute, value):
        """intercepts atrrs creatio """
        if attribute != "first_name":
            msg = "'LockedClass' object has no attribute 'last_name'"
            raise AttributeError(msg)
        else:
            self.__dict__[attribute] = value
