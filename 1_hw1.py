input = 20


def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number+1) : # 2~number+1
        for i in range(2,n): # 2~n-1
            if n % i == 0 : #나머지가 0이면 정수.
                break
        else : #break 가 한번도 발생하지 않았다면
            prime_list.append(n)
    return prime_list


result = find_prime_list_under_number(input)
print(result)