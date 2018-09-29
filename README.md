# sdc2fol
Try transfer NL-sentence to FOL from via stanford-parser

## reference
[nltk.tree illustration](https://kite.com/python/docs/nltk.tree.Tree) 

[Penn Treebank II illustration](https://gist.github.com/nlothian/9240750)
  
[Penn Treebank II tag set](https://www.clips.uantwerpen.be/pages/mbsp-tags)

[NLTK/3.3-documentation_Source-code-for-nltk.tree](https://www.nltk.org/_modules/nltk/tree.html)

[简单句的五种基本句型精析](https://www.hjenglish.com/juxing/p1206680/) 

## Basic Idea
1. parse过程分层进行;
2. clause_parser/phrase_parer各自处理对应层次的内容, 原则上互不涉入对方处理范围;
3. 对于不同层中普遍存在的"上/下"嵌套, 在各自层面分别处理: 需要各层次parser有比较清晰的调用方式;
4. parser的主要作用是根据子结构对象的类型做相应的特殊化处理过程, 返回合适的fol子字符串:因此处理xx层内容的xx_parser应该包含相应的xx_type函数对目标子结构分类, 并根据已知分类的子结构的结构特征个性化地调用下层parser处理下层子结构, 整合下层parser返回的结果并返回本层最终结果;
5. 对不同语法结构的分类解析主要体现在各层parser中， 对指定语句成分的抽取主要依靠extractor，目前的手段是对parse-tree进行有目的的遍历，并假设任务中树的结构足够简单直接且目标指向明确， 此部分对执行时间影响较大应该着重设计
6. 对句子结构的看法有两个角度:parse 中区分句子中各词的词性(pos), 而fol角度更倾向于只区分词在句中的成分, 因此代码中该部分初看有部分歧义;

## Target of Version
0.1.0:  
1. 初步设计代码框架;
2. 完成简单句五种基本类型的初步解析，可以解析简单例句;

0.1.1:  
1. 处理各层并列结构;
2. 处理嵌套结构;
    
