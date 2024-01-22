# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: test_token_count.py
# @time: 2024/1/22 17:53
import unittest

from src.token_counter.token_count import TokenCounter


class TestTokenCounter(unittest.TestCase):
    def setUp(self):
        self.token_cnt = TokenCounter()

    def test_case1(self):
        text = "who are you?"
        tokens_cnt = self.token_cnt.count(_input=text)
        self.assertEqual(tokens_cnt, 4)

    def test_case2(self):
        texts = ["who are you?", "How's it going on?"]
        tokens_cnt = self.token_cnt.count(_input=texts)
        self.assertEqual(tokens_cnt, [4, 6])

    def test_case3(self):
        with self.assertRaises(NotImplementedError) as cm:
            self.token_cnt.count(_input=23)
        the_exception = cm.exception
        self.assertEqual(the_exception.__str__(), "not support data type for <class 'int'>, please use str or List[str].")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestTokenCounter('test_case1'))
    suite.addTest(TestTokenCounter('test_case2'))
    suite.addTest(TestTokenCounter('test_case3'))
    run = unittest.TextTestRunner()
    run.run(suite)
