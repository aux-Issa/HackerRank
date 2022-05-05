# https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one
# easy: 10分
def plusMinus(arr):
    count_positive, count_negative, count_zero = 0.000000, 0, 0
    # Write your code here
    for i in range(n):
        if arr[i] > 0:
            count_positive += 1
        elif arr[i] < 0:
            count_negative += 1
        else: 
            count_zero += 1    
    print('{:.06f}'.format(count_positive/n))
    print('{:.06f}'.format(count_negative/n))
    print('{:.06f}'.format(count_zero/n))
