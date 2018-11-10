# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 20:22:24 2018
@author: Javier Soon 
ID:      80436654
Professor: Diego Aguirre
T.A.:      Manoj Saha

Description: Give a word file list, input the list in either a 
AVL Tree or a Red Black Tree after which search for a word and if the word 
exists in the list return the number of anagrams for that word.
Next find the largest number of anagrams in the file/tree.

"""
#import Node
import AVLTree
#import RBTNode
import RedBlackTree
# use a file reader
count = 0
count1 = 0


def read_file(file):
    print('Opening file words.txt')
    f = open(file)
#    print(f.read())
    return f
    
   
def print_anagrams(user_search_word, english_words, prefix=""):
    global count
    
    if len(user_search_word) <= 1:
        str1 = prefix + user_search_word
#        print(len(str1))    # prints the word that it just did an anagram for (repeats are included)
        if english_words.search(str1):  # looks for str in the tree
            count += 1
            print(prefix + user_search_word)
            
    else:
        for i in range(len(user_search_word)):
            cur = user_search_word[i: i + 1]
            before = user_search_word[0: i]  # letters before cur
            after = user_search_word[i + 1:]  # letters after cur
            
            if cur not in before:  # Check if permutations of cur have not been generated.
               print_anagrams(before + after, english_words, prefix + cur)   
    return count

def print_anagrams2(user_search_word, english_words, prefix=""):
    global count
    will = [2]
    
    if len(user_search_word) <= 1:
        str1 = prefix + user_search_word
#        print(len(str1))    # prints the word that it just did an anagram for (repeats are included)
        if english_words.search(str1):  # looks for str in the tree
            count += 1
            
    else:
        for i in range(len(user_search_word)):
            cur = user_search_word[i: i + 1]
            before = user_search_word[0: i]  # letters before cur
            after = user_search_word[i + 1:]  # letters after cur
            
            if cur not in before:  # Check if permutations of cur have not been generated.
               print_anagrams2(before + after, english_words, prefix + cur)   
    will.append(count)
    will.append(user_search_word)
    return will

def max_ana(english_words, words_file):
    max = -1
    max_word = " "
    i = 0
    
    with open (words_file, "r") as list:
        for i in list:
            j = 0
            line = i.split()
            count_a = print_anagrams2(line[j], english_words)
            
            if max < count_a[0]:
                max = count_a[0]
                max_word = count_a[1]
                
    print('This is the largest anagram word is: ' + max_word)
#    print(' with ' + max +' anagrams')
        
        

def user_in(user_input, words_file):
    
#    print(user_input == "AVL")     #USED TO DEBUG
    if user_input == 'AVL':
        AVL_list = read_file(words_file)
        english_words = AVLTree.AVLTree()
        
        for i in AVL_list:
#            a = i.split()
            english_words.insert(AVLTree.Node(i))
            
#        print_ascend (english_words.root)   #used to debug
        return english_words
      
    elif user_input == 'RBT':
        RBT_list = read_file(words_file)
        english_words = RedBlackTree.RedBlackTree()
        
        for i in RBT_list:
#            a = i.split
            english_words.insert(i)
            
#        print_ascend (english_words.root)   #used to debug
        return english_words
      
    else:
        print ('Invalid entry')
        print('Must be either AVL or RBT')
    
    
def user(user_input, words_file):
    if user_input == 'AVL':
         user_search = input('What word do you want to find: ')
         return user_search
    
    elif user_input == 'RBT':
         user_search = input('What word do you want to find: ')
         return user_search
     
    else:
        return None
    

def print_ascend(tree):
    global count1
    if tree is None:
        return
    print_ascend(tree.left)
    count1 = count1 + 1
    print_ascend(tree.right)
    return count1
    
    
def main():
    
    words_file = 'words.txt'#= input ('What file do you want to use: ')
    user_input = input('What type of tree do you want to use: AVL or RBT: ')        # asks tree type
    english_words = user_in(user_input, words_file) # makes the tree type be called english_words
    user_search_word= user(user_input, words_file) # asks for the word that they want to check for

#    searchword = english_words.search(user_search_word)
#    print_ascend(english_words.root)
#    print(searchword.key)
    
# =============================================================================
#     
#     
# =============================================================================
#    print_anagrams(user_search_word, english_words)
#    print('end')
    
#    count = print_anagrams2(user_search_word, english_words)   
#    print(count)
    
    max_ana(english_words, words_file)
        
main()