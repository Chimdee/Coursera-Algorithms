def karatsuba_multiply(x, y):
    
    if len(str(x)) == 1 or len(str(x)) == 1:
        return x*y
    else:
        length = max(len(str(x)), len(str(x)))
        idx = length//2
            
        a = x // 10**idx
        b = x %  10**idx
        c = y // 10**idx
        d = y %  10**idx
        
        ac= karatsuba_multiply(a, c)
        bd= karatsuba_multiply(b ,d)
        ab_cd = karatsuba_multiply(a+b, c+d) 
        ad_bc = ab_cd - ac - bd
        
        out = 10**(2*idx)*ac + 10**(idx)*ad_bc + bd
    return out
