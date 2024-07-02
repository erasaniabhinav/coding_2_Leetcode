# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code"


# s = "leetcode"
# wordDict = ["leet","code"]

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]


for i in wordDict:
    if i in s:
        print(False)