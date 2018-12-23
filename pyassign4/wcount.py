"""wcount.py: count words from an Internet file.

__author__ = "Rui Yuchen"
__pkuid__  = "1800011803"
__email__  = "1800011803@pku.edu.cn"
"""

import sys
from urllib.request import urlopen
from collections import Counter
def wcount(lines, topn=10):
     """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    lines = lines.lower()
    replst=[',','.','!','?',':',';','\r','\n','\\r','\\n','/','—','"','(',')','_','--',"'s","'re","'ll","'ve"]
    """将标点符号、缩进、缩写等替换掉，利于切片"""
    for i in replst:
        lines = lines.replace(i," ")
    w=lines.split()
    """切片后得到单词列表"""
    count = Counter(w)
    """用counter进行统计"""
    if topn<=len(count):
        ans = count.most_common(topn)
        """统计排名前topn的单词"""
    else:
        ans = count.most_common(len(count))
        """单词种类不足topn，全部输出"""
    for i in ans:
        for j in i:
            print(j,end=' ')
        print('\n')
        """换行输出结果"""
def main():
    try:
        doc = urlopen(sys.argv[1])
    except Exception as er:
        e=str(er)
        """返回几种错误类型"""
        if e == '<urlopen error [Errno 11001] getaddrinfo failed>':
            print('网络连接错误 ')
        if e == 'HTTP Error 404: Not Found':
            print('未找到URL')       
        if 'unknown url type' in e:
            print('URL类型错误') 
    docstr = doc.read()
    doc.close()
    docu=str(docstr)
    """获得用户输入的网址并将其转换为字符串"""
    if len(sys.argv) == 2:
        """用户只输入网址时默认统计前10单词"""
        wcount(docu)       
    else:
        """用户输入网址和topn后正常统计"""
        topn=int(sys.argv[2])
        wcount(docu,topn)
if __name__=="__main__":
    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
        """当用户无输入时进行提示"""
    else:
        main()
