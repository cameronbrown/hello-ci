"""Fake utilitites for testing testing"""


def add_two(num):
    """Add two to num"""
    return num + 2


def add_three(num):
    """Add three to num"""
    return num + 3


def add_four(num):
    """Add four to num"""
    return num + 4


def add_five(num):
    """Add five to num"""
    num += 1
    num += 1
    num += 1
    num += 1
    num += 1
    return num
