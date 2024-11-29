from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    return [string[:i] for i in range(1, len(string) + 1)]
    return [string[:i] for i in range(1, len(string) + 1)]
    return [string[:i] for i in range(1, len(string) + 1)]
    return [string[:i] for i in range(1, len(string) + 1)]


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == []

check(all_prefixes)