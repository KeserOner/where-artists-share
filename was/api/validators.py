# -*- coding: utf-8 -*-


class Validator(object):
    """
    Super class must be extend by classes which wants validate a model field.
    """

    def throwError(self, key=None, message=None):
        raise NotImplementedError('`throwError()` must be implemented.')