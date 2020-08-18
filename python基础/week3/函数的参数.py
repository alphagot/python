# __author:  xiaoxinpro13
# date:  2020/8/18

#   参数的顺序：关键参数，默认参数，*元组不定长参数，**字典不定长参数。
def print_info(name,job="IT",*args,**kwargs):
    print(name)
    print(job)
    for i in args:
        print(i)
    for i in kwargs:
        print(i,kwargs[i])


print_info("nan","IT",1,1,args="ss,ddd")
