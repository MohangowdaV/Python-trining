"""
Given a query string s and a list of all possible words, return all words that have s as a prefix.

Example 1:

Input:
s = “de”
words = [“dog”, “deal”, “deer”]

Output:
[“deal”, “deer”]

Explanation:
Only deal and deer begin with de.

Example 2:

Input:
s = “b”
words = [“banana”, “binary”, “carrot”, “bit”, “boar”]

Output:
[“banana”, “binary”, “bit”, “boar”]

Explanation:
All these words start with b, except for “carrot”.

Write your code bellow

"""
  

s=input("enter the s")
words = []
res = []
n = int(input("enter the value of n"))
for i in range(0,n):
    ele = input()
    words.append(ele)

for item in words:
    if item.startswith(s):
       res.append(item)
print(res)
