# __author:  xiaoxinpro13
# date:  2020/8/18
import time


def action1(n):
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)

    with open('日志记录', "a") as f:
        f.write('%s , end action %s\n' % (time_current, n))


action1(1)
action1(2)
action1(3)
