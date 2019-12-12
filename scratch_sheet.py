#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 17:51:37 2019

@author: patrickbenitez
"""

from collections import defaultdict

work_dict  = defaultdict(int)
key_text = 'lskjdfhlqwueklsdfhqwpeoriuasdfljgcxkdsfjh'
text_len = len(key_text)

for k in key_text:
    work_dict[k] += 1
    
print(work_dict.items())

work_dict.keys()
work_dict.values()
work_dict.items()

for k,v in work_dict.items():
    print("Key:", k, " Value:", v)