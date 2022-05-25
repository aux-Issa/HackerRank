# https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# review is required
# 25分: 遅い
def timeConversion(s):
    # Write your code here
    l =  s.split(':')

    if "".join(s[-2:]) == 'PM':
        l[-1] = l[-1].strip('AMPM')
        l[0] = int(l[0])
        l[0] = '12'  if l[0] == 12 else str(l[0] + 12)
    if "".join(s[-2:]) == 'AM':
        l[-1] = l[-1].strip('AMPM')
        if l[0] == '12':
           l[0] = '00' 
    
    return (":".join(l))