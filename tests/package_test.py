# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: package_test.py
# @time: 2024/1/22 21:08
from token_counter.token_count import TokenCounter

text = "who are you?"
print(TokenCounter().count(_input=text))

texts = ["who are you?", "Python is fun!", "苹果手机"]
print(TokenCounter().count(_input=texts))
