from shuffle import *
def shuffle_test():
    # check whether the estimated p is statistically different than 1/2 via z test
    s = [0,1]
    est = [0] * 100
    for i in range(100):
        for j in range(10000):
            result = shuffle(s)
            if result[0] == 0:
                est[i] += 1
        est[i] = est[i]/10000
    mean = sum(est)/100
    for i in range(100):
        est[i] = (est[i]-mean)**2
    std = (sum(est)/100)**(0.5)
    assert abs((mean-0.5)/std) <= 1.96
    print('shuffle works.')
shuffle_test()