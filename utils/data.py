ConjunctionList = ['SWITCH', 'UNION']


ClauseList = ['S', 'SBAR', 'SBARQ', 'SINV', 'SQ']
PhraseList = ['ADJP','ADVP', 'CONJP', 'FRAG', 'INTJ', 'LST', 'NAC', 'NP', 'NX', 'PP',
              'PRN', 'PRT', 'QP', 'RRC', 'UCP', 'VP', 'WHADJP', 'WHAVP', 'WHNP', 'WHPP', 'X']
WordList = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN',
            'NNS', 'NNP', 'NNPS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP',
            'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB']


NounList = ['NP', 'NN', 'NNS', 'NNP', 'NNPS', 'PRP']
VerbList = ['VP', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'MD']


beVerbList = ['am', 'is', 'are', 'were', 'was']
beVerbAbbreviationDict = {'\'s': 'is', '\'m': 'am', '\'re': 'are'}


notRBList = ['not', 'n\'t']
andRBList = ['and', 'nor', 'neither', 'either']
orRBList = ['or']

prepositionList = ['in', 'at', 'on']

clause_type = 'Clause'
phrase_type = 'Phrase '
word_type = 'Word'
