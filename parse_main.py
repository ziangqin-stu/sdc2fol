from utils.data import *
from utils.parse_util_level_1 import *
from utils.tree_service import *
from utils.sentences_level_1 import *





sentence = "He went on holiday."
tree = sentence2tree(sentence)
print(phrase_type(tree))
for child in tree:
    print(phrase_type(child))
for child in tree[0]:
    print(phrase_type(child))

res = parse_clause(tree)
print(res)
