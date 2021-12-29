#!/usr/bin/env python
# coding: utf-8

# In[2]:


PI = 3.14

print("text name : ", __name__)
def number_input():
    print("text name : ", __name__)
    output = input("숫자 입력 > ")
    return float(output)

def get_circum(radius):
    return radius * PI * 2

def get_circle_area(radius):
    return radius * radius * PI

if __name__ == "__main__":
    print("get_circum(10):",get_circum(10))
    print("get_circle_area(10):",get_circle_area(10))

