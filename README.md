# sdc2fol
Try transfer NL-sentence to FOL from via stanford-parser

## reference
- [nltk.tree illustration](https://kite.com/python/docs/nltk.tree.Tree) 

- [Penn Treebank II illustration](https://gist.github.com/nlothian/9240750)
  
- [Penn Treebank II tag set](https://www.clips.uantwerpen.be/pages/mbsp-tags)

- [NLTK/3.3-documentation_Source-code-for-nltk.tree](https://www.nltk.org/_modules/nltk/tree.html)

- [简单句的五种基本句型精析](https://www.hjenglish.com/juxing/p1206680/) 

## Basic Idea
1. parse过程分层进行;
2. clause_parser/phrase_parer各自处理对应层次的内容, 原则上互不涉入对方处理范围;
3. 对于不同层中普遍存在的"上/下"嵌套, 在各自层面分别处理: 需要各层次parser有比较清晰的调用方式;
4. parser的主要作用是根据子结构对象的类型做相应的特殊化处理过程, 返回合适的fol子字符串:因此处理xx层内容的xx_parser应该包含相应的xx_type函数对目标子结构分类, 并根据已知分类的子结构的结构特征个性化地调用下层parser处理下层子结构, 整合下层parser返回的结果并返回本层最终结果;
5. 对不同语法结构的分类解析主要体现在各层parser中， 对指定语句成分的抽取主要依靠extractor，目前的手段是对parse-tree进行有目的的遍历，并假设任务中树的结构足够简单直接且目标指向明确， 此部分对执行时间影响较大应该着重设计
6. 对句子结构的看法有两个角度:parse 中区分句子中各词的词性(pos), 而fol角度更倾向于只区分词在句中的成分, 因此代码中该部分初看有部分歧义;

## Plan of Version
0.1.0:  
1. 初步设计代码框架;
2. 完成简单句五种基本类型的初步解析，可以解析简单例句;

0.1.1:  
1. 处理各层并列结构;
2. 处理嵌套结构;
3. 处理否定结构;

## 关于嵌套
1. 语句中的嵌套是在句子子结构中包含其他句子子结构的现象；
2. 因为当前程序中将句子分为字句(clause)和短语(phrase)两个层次解析, 因此这种分化隐含4种嵌套类型: 
    + clause-clause嵌套; 
        > + 这是clause中包含clause的情况; 
        > + 如包含若干个独立字句的并列句中可能存在"S-[S, CC, S]"结构
        > + 这部分已经在clause层次处理, 方法是先遍历原始node并记录嵌套的clause层次到table中, 用"NP-NNP-KR_XX"结构替代嵌套字句来解析浅层node结构，再分别按深度和层次顺序替换被记录在table中的嵌套nodes; 
        > + 对"NP-NNP-KR_XX"结构的处理方法会影响本层次的嵌套处理代码, 而对该结构的处理往往出现在phrase层次.
    + clause-phrase嵌套
        > + 这是clause中包含phrase的情况, 是最为普遍的情况; 
        > + clause层次到word层次必然经过phrase层次, 换言之, clause结构的子结构只能是clause结构或者phrase结构, phrase结构的子结构只能是phrase结构或者word结构;
        > + 这部分的处理对应clause_parser中根据phrase子结构的类型选择运行不同的处理代码的过程, 这里phrase_parser要向上提供自己的ingredient\< list\>服务;
    + phrase-clause嵌套
        > + 这是phrase中包含clause的情况, 稍微复杂的句子中经常出现;
        > + 如宾语从句嵌套在动词短语结构下呈现出"VP-[VBP, SBAR]"结构.
        > + 该层次的嵌套潜在包含由下向上的调用, 需要规范这种调用接口(服务)与其上层的服务接口, 使二者能够兼容.
    + phrase-phrase嵌套
        > + 这是prase中包含phrase的情况, 经常出现在复杂的VP中;
        > + 因为Stanford Parser结构中VP-tree包含了很多信息, 因此大部分予语义信息以phrase结构被包含在VP-tree中, 如主谓宾句型中的宾语多以NP-phrase的形式嵌套在谓语的VP-phrase中;
        > + 当前认为这种嵌套结构只存在于特定的句型中(如带有情态动词的VP-VP嵌套), 对寻找sdc的主要成分不会带来递归嵌套式的影响, 因此不需要对这种嵌套做标记替换操作;
        > + 该层次的嵌套潜在地调用自身, 需要规范这种调用接口(服务)与面向向上层的服务接口, 使二者能够兼容.
3. 目前代码中的嵌套处理比较模糊(之前的嵌套处理缺失), 仅有第二种嵌套被处理, 其他种类的嵌套没有被妥善处理, 嵌套机制并没有被显示独立出来, 各层次parser的服务接口形式也没有被设计出来, 这是下一步改进的重点工作. 
