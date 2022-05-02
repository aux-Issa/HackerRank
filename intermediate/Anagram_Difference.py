def find(word_a, word_b):
    chars = set()
    for char in word_a: 
        chars.add(char)
    for char in word_b: 
        chars.discard(char)
    return len(chars)
def getMinimumDifference(a, b):
    # Write your code here
    ans = []
    # lenのチェック
    
    for word_a,word_b in zip(a, b):
        if len(word_a)!=len(word_b):
            ans.append(-1)
        elif sorted(list(word_a))==sorted(list(word_b)):
            ans.append(0)
        else:
            ans.append(find(word_a, word_b))
    return ans


print(getMinimumDifference(['hoge','fuga','hogehoge', 'yarn','npm'],['geho','gafug','gehoyarn','bind','npm']))
