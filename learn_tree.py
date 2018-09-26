from nltk_parser import sentence2tree
from nltk_parser import draw_tree

sent = "I like apple."
tree = sentence2tree(sent)

print(tree)
print(type(tree))
