import time
start = time.time()

def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "x", "y", "z"]
    max_count = 0
    max_al = array[0]
    
    for a in array:
        count = 0 #글자별로 저장해서 비교한다.
        for i in string:
            if a == i :
                count += 1
        if count > max_count :
            max_al = a
            max_count = count
    return max_al

result = find_max_occurred_alphabet
print("정답 = a 현재 풀이 값 =", find_max_occurred_alphabet("Hello my name is sparta"))
print("정답 = a 현재 풀이 값 =", find_max_occurred_alphabet("Sparta coding club"))
print("정답 = s 현재 풀이 값 =", find_max_occurred_alphabet("best of best sparta"))

print("time :", time.time() - start)