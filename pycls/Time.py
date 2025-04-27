class Time:
    def __init__(self,h,m,s):
        self.h = h
        self.m = m
        self.s = s
    
    def __add__(self,other):
        h = self.h + other.h
        h = h%12
        m = self.m + other.m
        if(m > 60):
            m = m % 60
            h = h+1
        s = self.s + other.s
        if(s > 60):
            s = s % 60
            m = m+1

        print(f"{h}:{m}:{s}")

        
time1 = Time(10, 20, 45)
time2 = Time(2, 15, 20)


sumtime = time1 + time2



