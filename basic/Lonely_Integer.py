# Given an array of integers, where all elements but one occur twice, find the unique element.
# https://www.hackerrank.com/challenges/one-week-preparation-kit-lonely-integer/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two
def lonelyinteger(a):
    # Write your code here
    import collections
    a = collections.Counter(a)
    for key, val in a.items():
        if val == 1:
            return key