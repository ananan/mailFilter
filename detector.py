#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/9 00:16
# @Author  : Peter Yang
# @Contact : 13yhyang1@gmail.com
# @File    : detector.py

import os
import re


class BayesMailDetector:
    """
    贝叶斯邮件分类器
    """
    def __init__(self, data_path):
        self.data_path = data_path
        self.regex = re.compile(r"[\w-]+|[\x80-\xff]{3}")


    def init_word_trie(self, filename):
        word_trie = {}
        try:
            with open(filename, 'r') as f:
                content = f.readlines()
        except IOError:
            return word_trie
        else:
            for word in content:
                for char in self.regex.findall(word):
                    word_trie[char] = word_trie[char] if word_trie.has_key(char) else {}
                    word_trie = word_trie[char]


    def load_model(self, model_path):
        pass

    def split_word(self, content):
        pass

    def split_word_by_jieba(self, content):
        pass


