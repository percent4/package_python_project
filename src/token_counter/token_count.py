# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: token_count.py
# @time: 2024/1/22 17:45
import tiktoken

from typing import List, Union


class TokenCounter(object):
    def __init__(self, model="gpt-3.5-turbo"):
        """
        :param model: name of model, type: string
        """
        self.model = model

    def count(self, _input: Union[List, str]) -> Union[List[int], int]:
        """
        :param _input: user input, type: str or List[str]
        :return: Return the number of tokens used by text, type int or List[int]
        """
        try:
            encoding = tiktoken.encoding_for_model(self.model)
        except KeyError:
            print("Warning: model not found. Using cl100k_base encoding.")
            encoding = tiktoken.get_encoding("cl100k_base")

        if isinstance(_input, list):
            token_count_list = []
            for text in _input:
                token_count_list.append(len(encoding.encode(text)))
            return token_count_list
        elif isinstance(_input, str):
            return len(encoding.encode(_input))
        else:
            raise NotImplementedError(f"not support data type for {type(_input)}, please use str or List[str].")
