while True:
    a=input('enter the left side of the interval:')
    b=input('enter the right side of the interval:')
    n=input('enter the number of sub-intervals:')
    c=input('which trigonometric function?please enter sin,cos or tan:')
    if a.replace('.','',1).isdigit() and b.replace('.','',1).isdigit() and n.isdigit() and c in ('sin','cos','tan'):
        a=eval(a)
        b=eval(b)
        a=min(a,b)
        b=max(a,b)
        n=eval(n)
        from math import sin
        from math import cos
        from math import tan
        if c=='sin':
            i=1
            result=0
            while i<=n:
                d=(b-a)/n*sin(a+(b-a)/n*(i-0.5))
                result=result+d
                i=i+1
            print('The numerical integration is:',result)
        if c=='cos':
            i=1
            result=0
            while i<=n:
                d=(b-a)/n*cos(a+(b-a)/n*(i-0.5))
                result=result+d
                i=i+1
            print('The numerical integration is:',result)
        if c=='tan':
            i=1
            result=0
            while i<=n:
                d=(b-a)/n*tan(a+(b-a)/n*(i-0.5))
                result=result+d
                i=i+1
            print('The numerical integration is:',result)
        break
    else:
        print('please check your input and try again, note that a and b must be number, n must be integer, and the function can only be written as sin, cos and tan')
