


def discr_mean(x_f: dict) -> float:
    '''Returns the mean of the supplied discrete table of data(x) and frequency(f)'''
    '''discr_mean({2: 5, 3: 1}) -> '''
    return sum(x*f for x, f in zip(x_f, x_f.values()))/sum(x_f.values())


def cont_mean(ci_f: dict) -> float:
    '''Returns the mean of the supplied continuous table of:
       class intervals(ci) and frequency(f)'''
    '''cont_mean({(0,10): 5, (10,20): 1}) -> '''
    x = [(a+b)/2 for a,b in ci_f]
    return sum(x[i]*f[i] for i in range(len(x)))


def std_dev(): pass
