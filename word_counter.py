#!/usr/bin/python

#
# Python script to word repitations in file.
#

word_counter = {}
file = open("test.txt","r")
for word in file.read().split():
    if word in word_counter:
        word_counter[word]+=1
    else:
        word_counter[word]=1

print word_counter