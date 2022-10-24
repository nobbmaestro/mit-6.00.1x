"""Final Exam, Problem 5.

Implement a function that meets the specifications below.

def cipher(map_from, map_to, code):
    \"\"\" map_from, map_to: strings where each contain
                          N unique lowercase letters.
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where
        each key is a letter in map_from at index i and the corresponding
        value is the letter in map_to at index i.
        decoded is a string that contains the decoded version
        of code using the key_code mapping. \"\"\"
    # Your code here

For example,
  - cipher("abcd", "dcba", "dab") returns (order of entries in dictionary may not be the same)
    ({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')

Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.
"""


def coder(key_code, code):
    """Auxillary function for cipher()."""
    decoded = ""
    for letter in code:
        decoded += key_code[letter]

    return decoded


# pylint: disable=C0103
def cipher(map_from, map_to, code):
    """Get cipher dictionary.

    key_code: is a dictionary with N keys mapping str to str where
    each key is a letter in map_from at index i and the corresponding
    value is the letter in map_to at index i.

    decoded: is a string that contains the decoded version
    of code using the key_code mapping.

    Args:
        map_from, map_to (str): each contain N unique lowercase letters.
        code (str): (assume it only contains letters also in map_from)

    Returns:
        tupl: cantains keys (key_code, decoded).
    """
    key_code = {}

    for k, v in enumerate(map_from):
        key_code[v] = map_to[k]

    return key_code, coder(key_code, code)
