#-*- coding: utf-8 -*-
'''
结巴的使用
'''
import jieba
import jieba.analyse

text = '我想和你做爱做的事情'
full_text = jieba.cut(text,cut_all=True)
default_text =  jieba.cut(text)
search_text = jieba.cut_for_search(text)

'''
for i in default_text:
    print i
生成了迭代器generator，for 循环遍历或者使用list(jieba.cut())转换成list
'''
print "全模式:","/".join(full_text)
print "精确模式:","/".join(default_text)
print "搜索引擎模式:","/".join(search_text)

textAnalyze = "我爱广州"
tags = jieba.analyse.extract_tags(textAnalyze,1)
print "关键词抽取:","/".join(tags)

#新词识别 “杭研”并没有在词典中,但是也被Viterbi算法识别出来了
seg_list = jieba.cut("他来到了网易杭研大厦")
print u"[新词识别]: ", "/ ".join(seg_list)

#导入自定义词典前
testText = '佛郎机、娜美和路飞是动漫海贼王里面的主角'
text_list = jieba.cut(testText, cut_all=False)
print u"导入自定义词典之前[精确模式]: ", "/ ".join(text_list)
#导入自定义词典
jieba.load_userdict("../data/jieba_1.txt")
text_list = jieba.cut(testText, cut_all=False)
print u"[精确模式]: ", "/ ".join(text_list)

'''
基本方法：jieba.analyse.extract_tags(sentence, topK)
需要先import jieba.analyse，其中sentence为待提取的文本，
topK为返回几个TF/IDF权重最大的关键词，默认值为20
'''
tags = jieba.analyse.extract_tags(testText, topK=3)
print u"关键词:"
print " ".join(tags)



