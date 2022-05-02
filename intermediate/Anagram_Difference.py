# Given
# two strings, determine the minimum number of characters in either string that must be
# modified to make the two strings anagrams. If it is not possible to make the two strings
# anagrams, return -1.
# return int[n]

# determine how many times strings should be replaced so that a pair of strings can be anagrams
def count(word_a, word_b):
    # chars other than duplication are swappable，thus discarding duplication as follows
    word_a = list(word_a)
    word_b = list(word_b)
    for char in word_a: 
      if char in word_b: 
        word_b.remove(char)
    return len(word_b)

def getMinimumDifference(a, b):
    # Write your code here
    ans = []    
    for word_a,word_b in zip(a, b):
        # when len of them pair are not same, they cannot be anagrams
        if len(word_a)!=len(word_b):
            ans.append(-1)
        # when sorted chars are completely same, they must be anagrams
        elif sorted(list(word_a))==sorted(list(word_b)):
            ans.append(0)
        # when len of their pair are same, they can be anagrams by replacing each char
        else:
            ans.append(count(word_a, word_b))
    return ans


print(getMinimumDifference(['hoge','fuga','hogehoge', 'yarn','npm'],['geho','gafug','gehoyarn','bind','npm']))
