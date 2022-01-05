#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#그래프 matplotilb 를 사용
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import platform

#한글 폰트 사용시 마이너스 폰트 깨짐 해결
if platform.system() == 'Darwin': #맥
        plt.rc('font', family='AppleGothic') 
elif platform.system() == 'Windows': #윈도우
        plt.rc('font', family='Malgun Gothic') 
elif platform.system() == 'Linux': #리눅스 (구글 콜랩)
        plt.rc('font', family='Malgun Gothic') 

plt.rcParams['axes.unicode_minus'] = False 

