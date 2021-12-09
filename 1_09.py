A = [0, 3, 5, 6, 1, 2, 4]

# 내코드
def Big (a) :
    result = 0
    for aa in a :
        if aa <= 1 :
            result += aa
            continue
        if aa > 1 and result == 0 :
            result = 1
        result *= aa
    return result

# 같이 풀어보기
def find_max_plus_or_multiply(array):
    multiply_sum = 0
    for number in array:
        if number <= 1 or multiply_sum <= 1:
            multiply_sum += number
        else:
            multiply_sum *= number
    return multiply_sum

# 내 코드의 개선해야 할 점 ::
# 초기 합계가 0 이면 곱해야할수도 그냥 더하고나서 그 이후부터 곱하게 만들면 됨.
# 이러면 continue 안써두 된다는것~!

result = Big
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))