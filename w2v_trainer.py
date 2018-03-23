# -*- coding: utf-8 -*-
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')
from gensim.corpora import WikiCorpus


SYS_DIR = "/root/lab/27py/ipynb/w2v/zhwiki/"
FWikiZip = SYS_DIR + "zhwiki-20180301-pages-articles.xml.bz2"  
FWiki    = SYS_DIR + "source.xml"                                           
FWikiSeg = SYS_DIR + "source2.xml"
FModel   = SYS_DIR + "word2vec.model" 



def WikiExtract():
    wiki_corpus = WikiCorpus(FWikiZip, lemmatize = False, dictionary={})    
    texts_num = 0
    
    with open(FWiki,'w') as output:
        for text in wiki_corpus.get_texts():
            output.write(' '.join(text) + '\n')
            texts_num += 1
            if texts_num % 10000 == 0:
                print ("Already processing %d articles" % texts_num)


import jieba
import codecs

def ZhSplit():
    jieba.set_dictionary(SYS_DIR+'dict.txt.big')

    # load stopwords set
    stopword_set = set()
    with codecs.open(SYS_DIR+'stopwords.txt','r','utf-8') as stopwords:
        for stopword in stopwords:
            stopword_set.add(stopword.strip('\n'))

    output = codecs.open(FWikiSeg, 'w','utf-8')
    with codecs.open(FWiki, 'r','utf-8') as content :
        for texts_num, line in enumerate(content):
            line = line.strip('\n')
            words = jieba.cut(line, cut_all=False)
            for word in words:
                if word not in stopword_set:
                    output.write(word + ' ')
            output.write('\n')

            if (texts_num + 1) % 10000 == 0:
                print (u"Complete %d lines spliting" % (texts_num + 1))
    output.close()

import time
from gensim.models import word2vec

def WikiTrain():
    sentences = word2vec.LineSentence(FWikiSeg)
    model = word2vec.Word2Vec(sentences, size=250)
    model.save(FModel)
    

if __name__ == '__main__':
    # print "Start processing...."                 
    # # WikiExtract()
    # # print "Result in " + FWiki
    # ZhSplit()          
    # print "Result in " + FWikiSeg

    print "Start training...." 
    tStart  = time.asctime( time.localtime(time.time()) )
    WikiTrain()
    tFinish = time.asctime( time.localtime(time.time()) )
    print tStart
    print tFinish



