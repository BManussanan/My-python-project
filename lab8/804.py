def read_hour():
    h = int(input('Enter hour: '))
    return h
def read_minute() :
    m = int(input('Enter minute: '))
    return m
def read_second() :
    s = int(input('Enter second: '))
    return s
def to_seconds(h, m, s):
    summ = (h*3600)+(m*60)+s
    return summ
def time_elapsed(start, finish):
    total = finish-start
    hr = total//3600
    mi = (total%3600)//60
    se = total%60
    return f'{hr} hours {mi} minutes {se} seconds.'
def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)

print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()
print('Elapsed time is', time_elapsed(start_time, finish_time))