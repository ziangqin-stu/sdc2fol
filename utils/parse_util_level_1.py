import utils.tree_service
from utils.data import *
from nltk_parser import *


def children_label(tree):
    '''

    :param tree:
    :return: list<string> lable_name of tree's children
    '''
    children_label_list = []
    num = len(tree)
    for i in range(num):
        children_label_list.append(tree[i].label())
    return children_label_list


def core_verb_in_phrase(tree):
    '''

    :param tree:
    :return: <string>left-most terminal-verb in tree
    '''
    terminal_verbs = VerbList
    return left_most_terminal(tree, terminal_verbs)


def core_noun_in_phrase(tree):
    '''

    :param tree:
    :return: <string>left-most terminal-noun in tree
    '''
    terminal_nouns = NounList
    return left_most_terminal(tree, terminal_nouns)


def left_most_terminal(tree, return_range=None):
    '''
    DFS
    :param tree:
    :param range:
    :return: <string> left-most terminal name whoese parent was specified in return_range
    '''
    if return_range == None:
        leaf_list = tree.leaves()
        return leaf_list[0]
    else:
        stack = [tree]
        while stack:
            temp_tree = stack.pop()
            degree = len(temp_tree)
            if temp_tree.label() in return_range and temp_tree.height() == 2:
                return temp_tree.leaves()[0]
            elif degree > 0:
                for i in range(degree-1, -1, -1):
                    stack.append(temp_tree[i])
    return None


def phrase_type(tree):
    '''

    :param tree:
    :return: <string> phrase_type
    '''
    phrase_label = tree.label()
    children_label_list = children_label(tree)

    # skip different level
    if phrase_label == 'ROOT':
        return '[ROOT TREE IN PHRASE PARSING]'
    elif phrase_label in ClauseList:
        return '[CLAUSE LEVEL IN PHRASE PARSING]'
    elif phrase_label in WordList:
        return '[WORD LEVEL IN PHRASE PARSING]'
    # specify phrase type
    if phrase_label == 'VP':
        if children_label_list[0] in VerbList \
                and len(children_label_list) == 1:
            return 'Vi'
        elif children_label_list[0] in VerbList \
                and children_label_list[1] == 'ADVP' \
                and len(children_label_list) == 2:
            return 'Vi+ADV'
        elif children_label_list[0] in VerbList \
                and children_label_list[1] == 'PP' \
                and len(children_label_list) == 2:
            return 'Vi+PP'
        elif children_label_list[0] in VerbList \
                and children_label_list[1] == 'S' \
                and len(children_label_list) == 2:
                return 'Vi+INFIN'                       # infinitive situation may vary
        elif children_label_list[0] in VerbList \
                and children_label_list[1] == 'NP' \
                and len(children_label_list) == 2:
            return 'Vi+PARTI'
        elif children_label_list[0] == 'MD' \
                and children_label_list[1] == 'VP' \
                and len(children_label_list) == 2:
            return 'MD+VP'
        else:
            return '[UNKNOWN VP TYPE]'

    elif phrase_label == 'NP':
        if (len(children_label_list) == 1) or (children_label_list[0] == 'DT' and children_label_list[1] in NounList):
            return 'NN'
        elif(children_label_list[0] == 'DT' and children_label_list[1] == 'JJ' and children_label_list[2] in NounList):
            return 'JJ+NN'
        else:
            return  '[UNKNOWN NP TYPE]'

    # mark unknown phrase types
    return '[UNKNOWN PHRASE TYPE]'


def clause_type(tree):
    '''

    :param tree:
    :return: <string> clause_type
    '''
    clause_label = tree.label()
    children_label_list = children_label(tree)

    # skip different level
    if clause_label == 'ROOT':
        return '[ROOT TREE IN PHRASE PARSING]'
    elif clause_label in PhraseList:
        return '[PHRASE LEVEL IN PHRASE PARSING]'
    elif clause_label in WordList:
        return '[WORD LEVEL IN PHRASE PARSING]'

    # specify phrase type
    if clause_label == 'S':
        if len(children_label_list) == 2 and children_label_list[0] == 'NP' and children_label_list[1] == 'VP':
            return 'NP+VP'
        else:
            return '[UNKNOWN S TYPE]'
    else:
        return  '[UNKNOWN CLAUSE TYPE]'


def parse_clause(tree):
    fol = []
    temp_tree = tree[0]
    if clause_type(temp_tree) == 'NP+VP':
        actor = None
        action = None
        np_tree = temp_tree[0]
        vp_tree = temp_tree[1]
        if phrase_type(np_tree) == 'NN':
            actor = core_noun_in_phrase(np_tree)
        else:
            actor = '[UNKNOWN ACTOR]'

        if phrase_type(vp_tree) in ['Vi+ADV', 'Vi+PP']:
            action = core_verb_in_phrase(vp_tree)
            return action + '<' + actor + '>'s
        else:
            return '[UNKNOWN VP TYPE]'


    else:
        return '[UNPARSEABLE CLAUSE]'
