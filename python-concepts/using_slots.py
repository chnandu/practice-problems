#!/usr/bin/python

# Using __slots__ to limit the attributes on an instance.
# __slots__ would prevent creating and allocating storage for default class attributes and also
# would prevent adding undefined attributes

# This will be useful only with new-style class definition according to the documentation

import cPickle
import sys
from pprint import pprint

class Foo(object):
    def __init__(self, str_):
        self.str_ = str_

    def set_new_attrib(self, val):
        self.new_attr = val

class Bar(object):
    __slots__ = ['str_']
    def __init__(self, str_):
        self.str_ = str_

    def set_new_attrib(self, val):
        self.new_attr = val

    def __getstate__(self):
        return self.str_

    def __setstate__(self):
        self.str_ = state

if __name__ == "__main__":
    ab = Foo("Test String")
    print("Setting 'new_attr' on Foo instance")
    ab.set_new_attrib(10)
    res = {"instance": str(ab),
           "attribs": dir(ab),
           "size": sys.getsizeof(ab),
           "memory_approx": sys.getsizeof(cPickle.dumps(ab)),
    }
    pprint(res, indent=4)

    xy = Bar("Test String")
    print("Setting 'new_attr' on Bar instance")
    try:
        xy.set_new_attrib(10)
    except AttributeError:
        print(":( Could not set new attribute because of __slots__")
    res = {"instance": str(xy),
           "attribs": dir(xy),
           "size": sys.getsizeof(xy),
           "memory_approx": sys.getsizeof(cPickle.dumps(xy)),
    }
    pprint(res, indent=4)
