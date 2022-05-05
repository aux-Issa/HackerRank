# https://www.hackerrank.com/challenges/one-week-preparation-kit-countingsort1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# easy: 15
def countingSort(arr):
    # Write your code here
    import collections
    hoge = collections.Counter(arr)
    ans = [0]*(100)
    for key, val in hoge.items():
        ans[key]=val
    return ans   