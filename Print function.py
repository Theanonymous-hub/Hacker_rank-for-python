#The included code stub will read an integer,n, from STDIN. Without using any string methods, try to print the following:
#Note that "...." represents the consecutive values in between.
#code
if __name__ == '__main__':
    n = int(input())
    print(*range(1, n+1), sep='')
