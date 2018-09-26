from nlp_tools.stanford_parser import parser
from parser import *

import numpy

stanford_parser = parser.Parser()
sentence = 'I like dogs.'

dependencies = stanford_parser.parseToStanfordDependencies(sentence)
tokens, tree = stanford_parser.parse(sentence)
print(dependencies)

print(type(tokens), type(tree))
print(tokens)
print(tree)
