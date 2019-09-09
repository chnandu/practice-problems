#!/usr/bin/python

# Generate all permutations of given string


def _generate_perms(s, prefix=""):
    """Generate permutations of given string

    :param s: String
    :param prefix: Prefix to add on both sides of string to generate possible combinations
    :returns: Returns the list of all generated permutations
    """
    if len(s) == 1:
        if prefix:
            return [s+prefix, prefix+s]
        else:
            return [a]

    perms = _generate_perms(s[:-1], s[-1])
    result = []
    if prefix:
        for p in perms:
            i = 0
            while i <= len(p):
                result.append(p[:i]+prefix+p[i:])
                i += 1
    else:
        result = perms

    return result

def all_perms(s):
    """Generate all permutations of given string

    :param s: Given string
    :returns: Returns the list of all permutations of given string
    """
    import pdb; pdb.set_trace()
    return _generate_perms(s)

if __name__ == "__main__":
    inputs = ["abc", "abcd", "xyz"]
    for s in inputs:
        print("%s ---> %s" % (s, all_perms(s)))
