while True:
    N = input("Please enter an integer n, n > 2: ")
    if N.isdigit():
        N=int(N)
        prime_list = list()
        for digit in range(2, N):
            flag = True    
            for i in range(2, int(digit ** 0.5 + 1)):
                if digit % i == 0:
                    flag = False
                    break
            if flag:
                prime_list.append(digit)
        print("All the prime numbers smaller than", N, "are:")
        count=0
        for a in prime_list:
            print(a, end=' ')
            count=count+1
            if count %8==0:
                print()
        break
    else:
        print('please try to enter an integer again:')
