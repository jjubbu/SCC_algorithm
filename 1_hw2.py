import time
start = time.time()
A = "0011"

# 내 코드
def Reverse (a) :
    count = 0
    zero = a.count("0")
    
    if zero == 0 or zero == len(a) :
        return 1
    
    i = 0
    while i < len(a) :
        if a[i-1] != a[i] :
            count += 1
        i += 1
        
    return count

# 답안
input = "00110011"
def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == '0':
                count_to_all_one += 1
            if string[i + 1] == '1':
                count_to_all_zero += 1

    return min(count_to_all_one, count_to_all_zero)

# result = find_count_to_turn_out_to_all_zero_or_all_one(input)
result = Reverse(A)

print(result)
print("time :", time.time() - start)


# 답 똑같이 나오고 걸리는 시간도 비슷함. (time 세번씩 찍어보기..)
# 내 코드의 경우 모든 숫자가 같은 경우만 예외로 if문 처리 하고 그 외에는 '앞뒤 숫자가 다를때' count 를 하나씩 올라가게함.
# 이때 첫번째 숫자는 앞숫자가 없기에 count에 기본으로 1이 더해진다.
# 모든 숫자가 같은 경우를 제외하고 count는 무조건 짝수이며 count를 2로 나누면 문제에서 요청한 답을 낼 수 있다.

# 강의에서 보여준 답의 경우 앞뒤숫자가 다를때 뒤의 숫자가 0일때와 1일때를 나누어 저장하고
# 둘 중 작은 수를 return 한 것.

# 내 코드와 강의 답안의 차이점은 내 코드는 0 1 분리를 안하고 count를 2로 나누었지만 
# 강의 답안은 0 1 분리하여 작은 횟수를 출력한것!
# 분리 하고 후처리를 덜할지, 분리하지 않고 후처리를 할지의 차이..인듯.



