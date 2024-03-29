#!/usr/bin/env python

import sys
import os.path

# This is a tiny script to help you creating a CSV or txt file from a face
#  |-- README
#  |-- s1
#  |   |-- 1.pgm
#  |   |-- ...
#  |   |-- 10.pgm
#  |-- s2
#  |   |-- 1.pgm
#  |   |-- ...
#  |   |-- 10.pgm
#  ...
#  |-- s40
#  |   |-- 1.pgm
#  |   |-- ...
#  |   |-- 10.pgm
#
list_file=open('list.txt','w')

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print "usage: create_csv <base_path>"
        sys.exit(1)

    BASE_PATH=sys.argv[1]
    SEPARATOR=" "

    label = 0
    for dirname, dirnames, filenames in os.walk(BASE_PATH):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                abs_path ="%s/%s" % (subject_path, filename)
                print '%s%s%d' % (abs_path, SEPARATOR, label)
		list_file.writelines('%s%s%d' % (abs_path, SEPARATOR, label))
		list_file.write('\n')
            label = label + 1
