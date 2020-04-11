#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 15:52:26 2020

@author: bijayamanandhar
"""

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
       
        len_s = len(S) - 1
        len_t = len(T) - 1
       
        while len_s>=0 or len_t>=0:
            s_backspaces = 0
            while len_s>=0 and (s_backspaces>0 or S[len_s]=='#'):
                if S[len_s] == '#':
                    s_backspaces = s_backspaces + 1
                else:
                    s_backspaces = s_backspaces - 1
                   
                len_s = len_s - 1
               
            t_backspaces = 0
            while len_t>=0 and (t_backspaces>0 or T[len_t]=='#'):
                if T[len_t] == '#':
                    t_backspaces = t_backspaces + 1
                else:
                    t_backspaces = t_backspaces - 1
                   
                len_t = len_t - 1
               
            if len_s>=0 and len_t>=0:
                if S[len_s] != T[len_t]:
                    return False
                else:
                    len_s = len_s - 1
                    len_t = len_t - 1
            else:
                if len_s>=0 or len_t>=0:
                    return False
               
        return len_s<0 and len_t<0
               
# write code here
        
Input = [["ab#c", "ad#c"], 
         ["ab##", "c#d#"], 
         ["a##c", "#a#c"],
         ["a#c", "b"]]
       
if __name__ == '__main__':
    
    Result = Solution()
    
    for i in range(len(Input)):
        print(Result.backspaceCompare(Input[i][0], Input[i][1]))

    
    
    
    
    
    