import os
from nltk.parse.stanford import StanfordParser

def sentence2tree(sent):
    result = list(eng_parser.parse(sent.split()))
    return result[0]


def draw_tree(tree):
    tree.draw()


os.environ["CLASSPATH"] = r"C:\Users\qinziang\Documents\Tools\nlp_tools\StanfordNLP\jars"
os.environ["STANFORD_MODELS"] = "C:(我的路徑)/StanfordNLP/StanfordNLP/models"

eng_parser = StanfordParser()