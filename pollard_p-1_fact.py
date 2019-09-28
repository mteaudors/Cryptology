


def gcd(a,b):
    """ Compute the gcd of a and b using the Euclidean algorithm
    
    Arguments:
        a {integer} -- first integer 
        b {integer} -- second integer
    """

    if b>a:
        c = a
        a = b
        b = c
    
    return a if b == 0 else gcd(b , a%b)


def fact_p_minus_1(N , a , limit):
    val = a
    for i in range(1 , limit):
        val = (val**i)%N
        
        d = gcd(val-1,N)
        if d!=1 and d!=N:
            return d,int(N/d)

    return 0,0
    

N = [299,1403,2993]

for n in N:
    p,q = fact_p_minus_1(n , 2 , 10)    
    print(n , " = " , p , "*" , q)