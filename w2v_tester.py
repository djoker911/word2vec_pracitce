# -*- coding: utf-8 -*-
import jieba
import codecs
import time
from gensim.models import word2vec
from gensim import models

SYS_DIR = "/root/lab/27py/ipynb/w2v/zhwiki/"
FWikiZip = SYS_DIR + "zhwiki-20180301-pages-articles.xml.bz2"  
FWiki    = SYS_DIR + "source.xml"                                           
FWikiSeg = SYS_DIR + "source2.xml"
FModel   = SYS_DIR + "word2vec.model"

model = models.Word2Vec.load(FModel) 
  
    
def Test(type, t1, t2, t3):    
    try:
        if type == 1:
            print("Test1: 輸入一個詞，則去尋找前個該詞的相似詞")
            print("相似詞 排序")
            print(t1)
            for item in model.wv.most_similar(t1,topn = 5):
                print item[0], item[1]
        elif type == 2:
            print("Test2: 輸入兩個詞，則去計算兩個詞的餘弦相似度")
            print("計算 Cosine 相似度")
            print(t1+" and "+t2)
            res = model.wv.similarity(t1, t2)
            print(res)
        elif type == 3:
            print("Test3: 輸入三個詞，進行類比推理")
            print(t1 + " : " + t3 + u"，如" + t2 + u" : ")
            res = model.wv.most_similar([t1, t2], [t3], topn= 10)
            for item in res:
                print(item[0]+","+str(item[1]))
        else:
            res = model.wv.most_similarity(positive=[t1, '國王'], negative=['男人'], topn= 3)
            for item in res:
                print(item[0]+","+str(item[1]))
            

        print("----------------------------")

    except Exception as e:
        print(repr(e))

if __name__ == '__main__':
    print("提供 3 種測試模式\n")
    # Test(1, u'香蕉', u'', u'') 
    Test(1, u'國王', u'', u'')
    # Test(1, u'hell', u'', u'')
    # Test(1, u'iron', u'', u'')

    # Test(2, u'hell', u'heaven', u'')
    # Test(2, u'皮卡丘', u'老鼠', u'')
    Test(2, u'猴子', u'猩猩', u'') 

    Test(3, u'國王', u'皇后', u'男人')
    # Test(3, u'國王', u'男人', u'皇后')
    # Test(3, u'魔王', u'聖女', u'信長') 