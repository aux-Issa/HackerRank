# https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one&h_r=next-challenge&h_v=zen
# easy:6分

def miniMaxSum(arr):
    ans=[]
    # Write your code here
    arr.sort()
    ans.append(sum(arr[:4]))
    ans.append(sum(arr[-4:]))
    print(*ans)