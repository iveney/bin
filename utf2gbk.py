#!/usr/bin/env python
# convert the UTF8 encoded UTF8 string back to UTF8

import sys
import os
import unicodedata

for name in sys.argv[1:]:
    try:
        new_name = unicodedata.normalize("NFC", name.decode('utf8'))
        new_name = new_name.encode('latin-1').decode('gbk')
        new_name_utf8 = new_name.encode('utf8')
        if name != new_name_utf8:
            print "%s -> %s" % (name, new_name_utf8)
            os.rename(name, new_name)
    except:
        print "Ignoring %s" % name
