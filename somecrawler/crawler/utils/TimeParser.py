__author__ = 'j'
from enum import Enum
def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)

monthDutch = enum(JANUARI=1, FEBRUARI=2, MAART=3, APRIL=4, MEI=5, JUNI=6,
             JULI=7, AUGUSTUS=8, SEPTEMBER=9, OKTOBER=10,NOVEMBER=11, DECEMBER=12)
print monthDutch.MAART