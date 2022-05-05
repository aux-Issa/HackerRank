# https://www.hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two&h_r=next-challenge&h_v=zen
# easy: 20分
def diagonalDifference(arr):
    # Write your code here
    sum1 = 0
    sum2 = 0
    for i in range(len(arr)):
        sum1 += arr[i][i]
        # print(sum1)
        sum2 += arr[i][n-1-i]
        print(sum2)
        
    else:
        return abs(sum1-sum2)
            