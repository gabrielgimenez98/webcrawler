#encoding: utf-8
from web_crawler_main import conta_palavra
import pytest

#teste para ver se conta_palavra retorna o valor certo
url = 'https://python-forum.io/Thread-How-to-find-a-specific-word-in-a-webpage-and-How-to-count-it'
palavra = 'code'

assert 38 == conta_palavra(url,palavra)