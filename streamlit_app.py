
# 在terminal里输入： 
# streamlit run "/Users/qinxu/Visual Studio Code/Py files/重叠式检索.py"
# 可自动启动浏览器
  #Local URL: http://localhost:8504
  #Network URL: http://192.168.10.11:8504



import pandas as pd
from glob import glob
from collections import Counter
import re
import math
from re import findall
from dataclasses import dataclass
from tkinter import N
import streamlit as st
import altair as alt
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from collections import Counter
import base64


# Path = "/Users/qinxu/Jupyter_work/2022博士论文语料/日本学生作文801/*.txt"
# Filenames = glob(Path)
# Filenames= natsort.natsorted(Filenames)#文件名如果乱序，则需要用到这一行
# len(Filenames)

# dic = {}
# for Filename in Filenames:
#     with open(Filename, "r",encoding="UTF-8-sig") as f: #汉语文本读取若有“\ufeff”，则用"UTF-8-sig"（#文件为ANSI格式时，编码为"gbk"；文件为UTF-8格式时，编码为"utf-8"）
#         tokens = []
#         #1.将文本单词以空格进行切分,有标点
#         text = f.read() #分词语料用以下几行 （未分词语料用该行#file = f.read().replace("\n","").replace("\ufeff","").replace(" ","") ）
#         doc = text.strip().replace("\ufeff","").replace("\n","").replace("  "," ")  #将文本开头的"\ufeff"替换掉；将换行符\n替换掉 （有时将"/"替换为_,不然"/"会被识别为空格）   

#         #2.将文本单词以空格进行切分
#         Wordlst = doc.split()  #doc.split(" ")
        
#         wordlst = [token.split("/")[0] for token in Wordlst]  # 将上一步读取的含标点的文本，去掉标注。
        
#         #3在上一步的基础上，去掉标点符号
#         Wordlist = [token for token in Wordlst if token.split("/")[-1] not in ["w", "wkz", "wky" , "wyz" , "wyy", "wj", "ww",  "wt",  "wd", "wf", "wn", "wm", "ws",  "wp",  "wb", "wh"]]
#         wordlist = [token.split("/")[0] for token in Wordlist]  #将上一步读取的不含标点的文本，去掉标注。
        
#         #4.统计文本中的字数
#         file = "".join(wordlst).replace("\n","")           #将去掉标注的文本，去掉回车符和空格，变为有标点的纯本文;  
#         file_no标点 = "".join(wordlist).replace("\n","")    #去掉标注的文本，去掉回车符和空格和标点，变为无标点的纯本文。
#         字数含标点 = len(file)                               #文本长度含标点
#         字数不含标点 = len(file_no标点)                       #文本长度不含标点    
        
#         wordlist重叠式= [token for token in Wordlist if token.split("/")[-1] not in ["nt","nms", "t","m","mq","c","nz","x","nr","nrj","nrf","nr1","nr2","ns","nsf"]]
#         wordlist重叠式= [token.split("/")[0] for token in wordlist重叠式]
    

# # # # # # # 将doc文本以完整句子进行切分  "。/wj|？/ww|！/wt|……/ws"
#         完整句子= re.split('wj|ww|wt|ws',doc) #以完整句子进行切分
#         句子去标注去空格=[]
#         for i in 完整句子:
#             wi = i.split()
#             wii=[token.split("/")[0] for token in wi] #去掉标注
#             wiii= ("".join(wii))
#             句子去标注去空格.append(wiii) 
        
#         句子去标注有空格=[]
#         for i in 完整句子:
#             qi = i.split()
#             qii=[token.split("/")[0] for token in qi] #去掉标注
#             qiii= (" ".join(qii))
#             句子去标注有空格.append(qiii) 

# #### ## ## 特殊形式的四字成语：在不含标点、去掉标注的分词列表中检索
#    #### 1.AABB式（高高兴兴、慌慌张张、祖祖辈辈）: pattern = r'((.)\2(.)\3)'
#         patternAABB式 = r'((.)\2(.)\3)'
#         AABB式=[]
#         for x in wordlist重叠式:
#             for i in re.finditer(patternAABB式,x):
#                 t=i.group()
#                 AABB式.append(t)  
#         AABB式频度=len(AABB式) 

#         ## 1.AABB式句子提取
#         AABB式type=list(set(AABB式))
#         AABB式句子=[]
#         for d in AABB式type:
#             dd=".*"+d+".*"
#             for x in 句子去标注去空格:
#                 for i in re.finditer(dd,x):
#                     #print(i.group()+str(i.span()))
#                     n = i.group()
#                     AABB式句子.append(n)
#         AABB式句子去重=list(set(AABB式句子))
#         AABB式句数 = len(AABB式句子去重)         

#   #### 2.AABC式（念念不忘、多多益善、惴惴不安）: pattern = r'((.)\2..)'
#         patternAABC式 = r'((.)\2..)'
#         AABC式=[]
#         for x in wordlist重叠式:
#             for i in re.finditer(patternAABC式,x):
#                 n = i.group()
#                 AABC式.append(n)
#         AABC式 = [x for x in AABC式 if x not in AABB式] #去掉ABCC词语中的AABB类词语
#         AABC式频度 = len(AABC式)

#         ## 2.AABC式句子提取
#         AABC式type=list(set(AABC式))
#         AABC式句子=[]
#         for d in AABC式type:
#             dd=".*"+d+".*"
#             for x in 句子去标注去空格:
#                 for i in re.finditer(dd,x):
#                     #print(i.group()+str(i.span()))
#                     n = i.group()
#                     AABC式句子.append(n)
#         AABC式句子去重=list(set(AABC式句子))
#         AABC式句数 = len(AABC式句子去重) 


#  #### 3.ABAB式（彼此彼此、意思意思、恭喜恭喜）: pattern = r'((.)(.)\2\3)'
#         patternABAB式 = r'((.)(.)\2\3)'
#         ABAB式=[]
#         for x in wordlist重叠式:
#             for i in re.finditer(patternABAB式,x):
#                 n = i.group()
#                 ABAB式.append(n)
#         ABAB式频度 = len(ABAB式)

#         ## 3.ABAB式句子提取
#         ABAB式type=list(set(ABAB式))
#         ABAB式句子=[]
#         for d in ABAB式type:
#             dd=".*"+d+".*"
#             for x in 句子去标注去空格:
#                 for i in re.finditer(dd,x):
#                     #print(i.group()+str(i.span()))
#                     n = i.group()
#                     ABAB式句子.append(n)
#         ABAB式句子去重=list(set(ABAB式句子))
#         ABAB式句数 = len(ABAB式句子去重) 



#   #### 4.ABAC式（百发百中、自由自在、十全十美、一生一世）: pattern = r'((.).\2.)'
#         patternABAC式 = r'((.).\2.)'
#         ABAC式=[]
#         for x in wordlist重叠式:
#             for i in re.finditer(patternABAC式,x):
#                 n = i.group()
#                 ABAC式.append(n)
#         ABAC式频度 = len(ABAC式)

#      ## 4.ABAC式句子提取
#         ABAC式type=list(set(ABAC式))
#         ABAC式句子=[]
#         for d in ABAC式type:
#             dd=".*"+d+".*"
#             for x in 句子去标注去空格:
#                 for i in re.finditer(dd,x):
#                     #print(i.group()+str(i.span()))
#                     n = i.group()
#                     ABAC式句子.append(n)
#         ABAC式句子去重=list(set(ABAC式句子))
#         ABAC式句数 = len(ABAC式句子去重) 



#   #### 5.ABBA式（一二二一）: pattern = r'((.)(.)\3\2)'
#         patternABBA式 = r'((.)(.)\3\2)'
#         ABBA式=[]
#         for x in wordlist重叠式:
#             for i in re.finditer(patternABBA式,x):
#                 n = i.group()
#                 ABBA式.append(n)
#         ABBA式频度 = len(ABBA式)

#     ## 5.ABBA式句子提取
#         ABBA式type=list(set(ABBA式))
#         ABBA式句子=[]
#         for d in ABBA式type:
#             dd=".*"+d+".*"
#             for x in 句子去标注去空格:
#                 for i in re.finditer(dd,x):
#                     #print(i.group()+str(i.span()))
#                     n = i.group()
#                     ABBA式句子.append(n)
#         ABBA式句子去重=list(set(ABBA式句子))
#         ABBA式句数 = len(ABBA式句子去重) 


#   #### 6.ABCA式（天外有天、数不胜数、话里有话）: pattern = r'((.)..\2)'
#         patternABCA式 = r'((.)..\2)'
#         ABCA式=[]
#         for x in wordlist重叠式:
#             for i in re.finditer(patternABCA式,x):
#                 n = i.group()
#                 ABCA式.append(n)
#         ABCA式频度 = len(ABCA式)
#     ## 6.ABCA式句子提取
#         ABCA式type=list(set(ABCA式))
#         ABCA式句子=[]
#         for d in ABCA式type:
#             dd=".*"+d+".*"
#             for x in 句子去标注去空格:
#                 for i in re.finditer(dd,x):
#                     #print(i.group()+str(i.span()))
#                     n = i.group()
#                     ABCA式句子.append(n)
#         ABCA式句子去重=list(set(ABCA式句子))
#         ABCA式句数 = len(ABCA式句子去重) 



#    ####  7.ABBC式（不了了之、自欺欺人、以风风人）: pattern = r'(.(.)\2.)'
#         patternABBC式 = r'(.(.)\2.)'
#         ABBC式=[]
#         for x in wordlist重叠式:
#             for i in re.finditer(patternABBC式,x):
#                 n = i.group()
#                 ABBC式.append(n)
#         ABBC式频度 = len(ABBC式)

#      ## 7.ABBC式句子提取
#         ABBC式type=list(set(ABBC式))
#         ABBC式句子=[]
#         for d in ABBC式type:
#             dd=".*"+d+".*"
#             for x in 句子去标注去空格:
#                 for i in re.finditer(dd,x):
#                     #print(i.group()+str(i.span()))
#                     n = i.group()
#                     ABBC式句子.append(n)
#         ABBC式句子去重=list(set(ABBC式句子))
#         ABBC式句数 = len(ABBC式句子去重) 


#    ####  8.ABCB式（将心比心、出尔反尔、人云亦云）: pattern = r'(.(.).\2)'
#         patternABCB式 = r'(.(.).\2)'
#         ABCB式=[]
#         for x in wordlist重叠式:
#             for i in re.finditer(patternABCB式,x):
#                 n = i.group()
#                 ABCB式.append(n)
#         ABCB式频度 = len(ABCB式)
#      ## 8.ABCB式句子提取
#         ABCB式type=list(set(ABCB式))
#         ABCB式句子=[]
#         for d in ABCB式type:
#             dd=".*"+d+".*"
#             for x in 句子去标注去空格:
#                 for i in re.finditer(dd,x):
#                     #print(i.group()+str(i.span()))
#                     n = i.group()
#                     ABCB式句子.append(n)
#         ABCB式句子去重=list(set(ABCB式句子))
#         ABCB式句数 = len(ABCB式句子去重) 


#    ####  9.ABCC式（议论纷纷、人才济济、小心翼翼）: pattern = r'(..(.)\2)'
#         patternABCC式 = r'(..(.)\2)'
#         ABCC式=[]
#         for x in wordlist重叠式:
#             for i in re.finditer(patternABCC式,x):
#                 n = i.group()
#                 ABCC式.append(n)
#         ABCC式 = [x for x in ABCC式 if x not in AABB式] #去掉ABCC词语中的AABB类词语
#         ABCC式频度 = len(ABCC式)

#      ## 9.ABCC式句子提取
#         ABCC式type=list(set(ABCC式))
#         ABCC式句子=[]
#         for d in ABCC式type:
#             dd=".*"+d+".*"
#             for x in 句子去标注去空格:
#                 for i in re.finditer(dd,x):
#                     #print(i.group()+str(i.span()))
#                     n = i.group()
#                     ABCC式句子.append(n)
#         ABCC式句子去重=list(set(ABCC式句子))
#         ABCC式句数 = len(ABCC式句子去重) 



#    ####  10.ABCD式（热火朝天、五花八门、一言为定）: pattern = r'(....)'
#         patternABCD式 = r'(....)'
#         ABCD式=[]
#         for x in wordlist重叠式:
#             for i in re.finditer(patternABCD式,x):
#                 n = i.group()
#                 ABCD式.append(n)
                
#         特殊重叠式4字词语=AABB式+AABC式+ABAB式+ABAC式+ABBA式+ABCA式+ABBC式+ABCB式+ABCC式
#         ABCD式 = [x for x in ABCD式 if x not in 特殊重叠式4字词语]
#         ABCD式频度 = len(ABCD式)      

#     ## 10.ABCD式句子提取
#         ABCD式type=list(set(ABCD式))
#         ABCD式句子=[]
#         for d in ABCD式type:
#             dd=".*"+d+".*"
#             for x in 句子去标注去空格:
#                 for i in re.finditer(dd,x):
#                     #print(i.group()+str(i.span()))
#                     n = i.group()
#                     ABCD式句子.append(n)
#         ABCD式句子去重=list(set(ABCD式句子))
#         ABCD式句数 = len(ABCD式句子去重)        

#         特殊重叠式4字词语_频度 = len(特殊重叠式4字词语)
        
#         dic[Filename] = file, AABB式,AABB式频度,AABB式句子去重,AABB式句数,AABC式,AABC式频度,AABC式句子去重,AABC式句数,ABAB式,ABAB式频度,ABAB式句子去重,ABAB式句数,ABAC式,ABAC式频度,ABAC式句子去重,ABAC式句数, ABBA式,ABBA式频度,ABBA式句子去重,ABBA式句数,ABCA式,ABCA式频度,ABCA式句子去重,ABCA式句数,ABBC式,ABBC式频度,ABBC式句子去重,ABBC式句数,ABCB式,ABCB式频度,ABCB式句子去重,ABCB式句数,ABCC式,ABCC式频度,ABCC式句子去重,ABCC式句数,ABCD式,ABCD式频度,ABCD式句子去重,ABCD式句数,特殊重叠式4字词语_频度
# df重叠式 = pd.DataFrame(dic,["原文","AABB式","AABB式频度","AABB式句子","AABB式句数","AABC式","AABC式频度","AABC式句子","AABC式句数",'ABAB式','ABAB式频度',"ABAB式句子","ABAB式句数","ABAC式","ABAC式频度","ABAC式句子","ABAC式句数","ABBA式",'ABBA式频度',"ABBA式句子","ABBA式句数","ABCA式","ABCA式频度","ABCA式句子去重","ABCA式句数",'ABBC式','ABBC式频度',"ABBC式句子","ABBC式句数","ABCB式","ABCB式频度","ABCB式句子","ABCB式句数","ABCC式","ABCC式频度","ABCC式句子","ABCC式句数","ABCD式","ABCD式频度","ABCD式句子","ABCD式句数","特殊重叠式4字词语_频度"])                      
# df重叠式.columns = [columns.split("/")[-1] for columns in df重叠式.columns]

# # 统计每种检索式的总频度sum
# freq_sum = df重叠式.apply(lambda x : x.sum(), axis=1) #axis=0,按列相加；axis=1，按行相加 
# df重叠式["sum_s"]=freq_sum 

# df重叠式 = df重叠式.T
# #df重叠式.to_csv("/Users/qinxu/Jupyter_work/2022博士论文语料/运行结果/20220501_df重叠式.csv")
# #df重叠式      


# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# # 取消警告：You are calling st.pyplot() without any arguments. After December 1st, 2020, we will remove the ability to do this as it requires the use of Matplotlib's global figure object, which is not thread-safe.
# st.set_option('deprecation.showPyplotGlobalUse', False)
# st.title("重叠式检索")
# df= df重叠式


df四字词语重叠式 = pd.read_csv("/Users/qinxu/Jupyter_work/2022博士论文语料/运行结果/20220508_四字词语重叠式.csv")
df四字词语重叠式=df四字词语重叠式.rename(columns={'Unnamed: 0':"Filename"})
df=df四字词语重叠式.set_index('Filename')


if st.sidebar.checkbox("Show Data"):
    st.write("#### 输入要查询的行数(Enter the number of rows to view)")
    rows = st.number_input("", min_value=0,value=5)
    if rows > 0:
        st.dataframe(df.head(rows))
        st.write(f'Total :  {df.shape[0]} rows × {df.shape[1]} columns')

if st.sidebar.checkbox("重叠式"):
    st.write("#### 选取要查询的重叠式: ")
    # columns = df.columns.tolist()
    # class_name = columns[5]
    # hue_name= columns[1] # JP2,JP3,CHN, 按水平分组，分配颜色
    plot_type = st.sidebar.selectbox("选取重叠式: ", ["AABB式","AABC式","ABAB式","ABAC式","ABBA式","ABCA式","ABBC式","ABCB式","ABCC式","ABCD式"])
    
    # columns = df.columns.tolist()
    # st.write(columns)

    if plot_type  == "AABB式":
        columns = ["原文","AABB式","AABB式频度","AABB式句子","AABB式句数"]
    if plot_type == "AABC式":
        columns = ["原文","AABC式","AABC式频度","AABC式句子","AABC式句数"]
    if plot_type == "ABAB式":
        columns = ["原文","ABAB式", "ABAB式频度", "ABAB式句子","ABAB式句数"]
    if plot_type == "ABAC式":
        columns = ["原文","ABAC式","ABAC式频度","ABAC式句子","ABAC式句数"]
    if plot_type == "ABBA式":
        columns = ["原文","ABBA式","ABBA式频度","ABBA式句子","ABBA式句数"]
    if plot_type == "ABCA式":
        columns = ["原文","ABCA式","ABCA式频度","ABCA式句子","ABCA式句数"]
    if plot_type == "ABBC式":
        columns = ["原文","ABBC式","ABBC式频度","ABBC式句子","ABBC式句数"]
    if plot_type == "ABCB式":
        columns = ["原文","ABCB式","ABCB式频度","ABCB式句子","ABCB式句数"]
    if plot_type == "ABCC式":
        columns = ["原文","ABCC式","ABCC式频度","ABCC式句子","ABCC式句数"]
    if plot_type == "ABCD式":
        columns = ["原文","ABCD式","ABCD式频度","ABCD式句子","ABCD式句数"]

    new_df=df[columns]
    st.dataframe(new_df)


####### 将生成的表格用于下载
    csv = new_df.to_csv(index=True)  #index=False
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{columns[1]}_result.csv">download</a>'
    st.markdown(f"{columns[1]}_result をダウンロードする {href}", unsafe_allow_html=True)


####### 提取要用的列
    重叠式句子去重_所有句子 = df.at['sum_s',columns[3]]
    重叠式句子去重所有句子 = str(重叠式句子去重_所有句子).replace(", ","\n\n").replace("[","").replace("]","").replace("'","")

    重叠式单词_频度=df.at['sum_s',columns[2]]
    重叠式句子去重所有句子数量=df.at['sum_s',columns[4]]

    某重叠式词语汇总1=df.at['sum_s',columns[1]]
    某重叠式词语汇总2=某重叠式词语汇总1.replace("[","").replace("]","").replace("'","").replace(" ","")
    某重叠式词语汇总3=某重叠式词语汇总2.split(',')
    某重叠式词语汇总=list(某重叠式词语汇总3)

    # st.write(某重叠式式词语汇总1)
    # st.write(某重叠式式词语汇总)
    # ddd=type(某重叠式式词语汇总)
    # st.write(ddd)


##### 绘制词云图
    if 某重叠式词语汇总1=='[]':
        某重叠式词语type=0
    else:
        某重叠式词语type=len(set(某重叠式词语汇总))


    count = Counter(某重叠式词语汇总)
    sorted_x = sorted(count.items(), key=lambda x: x[1], reverse=True)
    df_某重叠式词语 = pd.DataFrame(sorted_x,columns=['词汇','词频'])
    df重叠式词语=df_某重叠式词语.set_index('词汇')
   
    if st.checkbox(f"查看含{columns[1]}的词汇及频率"):
        st.write(f'###### 含{columns[1]}的词汇共出现 {某重叠式词语type} 种;  含{columns[1]}的词汇共出现 {重叠式单词_频度}次')
        #st.dataframe(df_某重叠式词语, width=None, height=500)
        st.table(df_某重叠式词语)
        # 使用st.dataframe(df), 显示可滚动/可排序/交互式表格。但会截断列.
        # 使用st.table(df), 显示静态表格,完整地显示表格：不截断，不滚动，只显示整个表格。


##### 显示重叠式词语
    def gen_wordcloud(wordfreqs):
        from pyecharts import options as opts
        from pyecharts.charts import WordCloud
        from streamlit_echarts import st_pyecharts
        from pyecharts.globals import ThemeType

        wc1 = (
            WordCloud(init_opts=opts.InitOpts(theme=ThemeType.DARK))
            .add(series_name="词云图", data_pair=wordfreqs, word_size_range=[10, 50], shape = 'circle')
            .set_global_opts(
                title_opts=opts.TitleOpts(title=" ", title_textstyle_opts=opts.TextStyleOpts(font_size=30)),
                tooltip_opts=opts.TooltipOpts(is_show=True),
                ))
        return st_pyecharts(wc1)


    st.title('数据分析')
    st.write('\n\n\n\n')
    wc = st.button(label='词云图')
    st.balloons()
    gen_wordcloud(sorted_x)



#############另一种绘制词云方式：圆形
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud
    font_path = 'System/Library/Fonts/STHeiti Medium.ttc' # STHeiti Light.ttc
    plt.rcParams['figure.figsize'] = [5, 5]

    #产生一个以(150,150)为圆心,半径为120的圆形mask
    x, y = np.ogrid[:300, :300]
    mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
    mask = 255 * mask.astype(int)#155：方形
   
    #colormap="copper"/viridis/Spectral/PiYG/PRGn/coolwarm/gist_heat/bone # Set the text color 
    wordcloud = WordCloud(font_path=font_path,background_color="white", mask=mask, contour_width=0.05, 
                        contour_color="black", max_font_size=50, min_font_size=5,random_state=45,
                        colormap="pink",max_words=1000, scale=5,width=30,height=30)#scale=5，这个数值越大，产生的图片分辨率越高，字迹越清晰。可以调到64试试

    wordcloud.generate_from_frequencies(df重叠式词语['词频'])   
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off") #将x轴和y轴坐标隐藏
    #plt.title("AABB式",font=dict(family='times new roman'),fontweight='bold',fontsize=40)
    #plt.savefig('/Users/qinxu/Jupyter_work/2022博士论文语料/代词词云图1') #图模糊可以在最后导出写一个plt.savefig('文件名',dpi=数字)，数字越大越清楚,dpi=1000
    plt.show()
    wc = st.button(label='圆形词云图')
    if wc == True:
        st.pyplot()



##### 显示含重叠式词语的句子
    if st.checkbox(f"查看含{columns[1]}单词的所有句子"):
        st.write(f'***含{columns[1]}单词的句子共 :  {重叠式句子去重所有句子数量} 条*** \n\n{重叠式句子去重所有句子}')







#  词云图举例
if st.checkbox("#### 词云图举例"):
    from pyecharts import options as opts
    from pyecharts.charts import WordCloud

    words = [
        ("火箭", 10000),
        ("勇士库里", 8888),
        ("在你写这个教程之前，我已经会用了", 6181),
        ("哈登", 6386),
        ("金州拉文", 5055),
        ("杜兰特", 6467),
        ("戳眼", 2244),
        ("NBA", 1868),
        ("季后赛", 1484),
        ("约老师", 1112),
        ("利拉德", 865),
        ("双卡双待", 847),
        ("字母歌MVP", 5582),
        ("卡哇伊", 555),
        ("猛龙", 550),
        ("大帝", 462),
        ("西蒙斯不投三分", 366),
        ("JB", 360),
        ("科尔垃圾", 282),
        ("格林公式", 273),
        ("欧文", 2650),
    ]


    def wordcloud_base(word):
        from pyecharts.charts import WordCloud
        from streamlit_echarts import st_pyecharts
        c = (
            WordCloud()
                .add("", word, word_size_range=[20, 50], shape="diamond", word_gap=10)
                .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud-shape-diamond"))
        )
        return st_pyecharts(c) 


    st.title('数据分析2')
    st.write('\n\n\n\n')
    wc = st.button(label='词云图2')
    wordcloud_base(words)

    word2 = [
        ("生活资源", "999"),
        ("供热管理", "888"),
        ("供气质量", "777"),
        ("生活用水管理", "688"),
        ("一次供水问题", "588"),
        ("交通运输", "516"),
        ("城市交通", "515"),
        ("环境保护", "483"),
        ("房地产管理", "462"),
        ("城乡建设", "449"),
        ("社会保障与福利", "429"),
        ("社会保障", "407"),
        ("文体与教育管理", "406"),
        ("公共安全", "406"),
        ("公交运输管理", "386"),
        ("出租车运营管理", "385"),
        ("供热管理", "375"),
        ("市容环卫", "355"),
        ("自然资源管理", "355"),
        ("粉尘污染", "335"),
        ("噪声污染", "324"),
        ("土地资源管理", "304"),
        ("物业服务与管理", "304"),
        ("医疗卫生", "284"),
        ("粉煤灰污染", "284"),
        ("占道", "284"),
        ("供热发展", "254"),
        ("农村土地规划管理", "254"),
        ("生活噪音", "253"),
        ("供热单位影响", "253"),
        ("城市供电", "223"),
        ("房屋质量与安全", "223"),
        ("大气污染", "223"),
        ("房屋安全", "223"),
        ("文化活动", "223"),
        ("拆迁管理", "223"),
        ("公共设施", "223"),
        ("供气质量", "223"),
        ("供电管理", "223"),
        ("燃气管理", "152"),
        ("教育管理", "152"),
        ("医疗纠纷", "152"),
        ("执法监督", "152"),
        ("设备安全", "152"),
        ("政务建设", "152"),
        ("县区、开发区", "152"),
        ("宏观经济", "152"),
        ("教育管理", "112"),
        ("社会保障", "112"),
        ("生活用水管理", "112"),
        ("物业服务与管理", "112"),
        ("分类列表", "112"),
        ("农业生产", "112"),
        ("二次供水问题", "112"),
        ("城市公共设施", "92"),
        ("拆迁政策咨询", "92"),
        ("物业服务", "92"),
        ("物业管理", "92"),
        ("社会保障保险管理", "92"),
        ("低保管理", "92"),
        ("文娱市场管理", "72"),
        ("城市交通秩序管理", "72"),
        ("执法争议", "72"),
        ("商业烟尘污染", "72"),
        ("占道堆放", "71"),
        ("地上设施", "71"),
        ("水质", "71"),
        ("无水", "71"),
        ("供热单位影响", "71"),
        ("人行道管理", "71"),
        ("主网原因", "71"),
        ("集中供热", "71"),
        ("客运管理", "71"),
        ("国有公交（大巴）管理", "71"),
        ("工业粉尘污染", "71"),
        ("治安案件", "71"),
        ("压力容器安全", "71"),
        ("身份证管理", "71"),
        ("群众健身", "41"),
        ("工业排放污染", "41"),
        ("破坏森林资源", "41"),
        ("市场收费", "41"),
        ("生产资金", "41"),
        ("生产噪声", "41"),
        ("农村低保", "41"),
        ("劳动争议", "41"),
        ("劳动合同争议", "41"),
        ("劳动报酬与福利", "41"),
        ("医疗事故", "21"),
        ("停供", "21"),
        ("基础教育", "21"),
        ("职业教育", "21"),
        ("物业资质管理", "21"),
        ("拆迁补偿", "21"),
        ("设施维护", "21"),
        ("市场外溢", "11"),
        ("占道经营", "11"),
        ("树木管理", "11"),
        ("农村基础设施", "11"),
        ("无水", "11"),
        ("供气质量", "11"),
        ("停气", "11"),
        ("市政府工作部门（含部门管理机构、直属单位）", "11"),
        ("燃气管理", "11"),
        ("市容环卫", "11"),
        ("新闻传媒", "11"),
        ("人才招聘", "11"),
        ("市场环境", "11"),
        ("行政事业收费", "11"),
        ("食品安全与卫生", "11"),
        ("城市交通", "11"),
        ("房地产开发", "11"),
        ("房屋配套问题", "11"),
        ("物业服务", "11"),
        ("物业管理", "11"),
        ("占道", "11"),
        ("园林绿化", "11"),
        ("户籍管理及身份证", "11"),
        ("公交运输管理", "11"),
        ("公路（水路）交通", "11"),
        ("房屋与图纸不符", "11"),
        ("有线电视", "11"),
        ("社会治安", "11"),
        ("林业资源", "11"),
        ("其他行政事业收费", "11"),
        ("经营性收费", "11"),
        ("食品安全与卫生", "11"),
        ("体育活动", "11"),
        ("有线电视安装及调试维护", "11"),
        ("低保管理", "11"),
        ("劳动争议", "11"),
        ("社会福利及事务", "11"),
        ("一次供水问题", "11")]


    st.title('数据分析3')
    st.write('\n\n\n\n')
    wc = st.button(label='词云图3')
    wordcloud_base(word2)
