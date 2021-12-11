# 백준의 1158번 요세푸스 문제

# N명으로 이루어진 원이 있고 한명씩 순서대로 1~N까지의 숫자를 가진다.
# 처음 k번째에 있던 숫자 n1을 가진 사람을 빼고, 
# 빠진 사람이 있던 위치에서부터 다시 k번째 있는 사람을 뺀다.
# 이때 빠진 사람들의 숫자를 차례대로 <> 안에 쌓은게 "요세푸스 순열" 이다.

N = 5000
K = 1

N_list = list(range(1,N+1)) #[1,2,3,4,5,6,7]
result = []
idx = K-1

while N != 0 :
    if N == 1 :
        result += N_list
        break
    elif N < K :
        idx = (K%N)-1
    result.append(N_list[idx])
    N_list =  N_list[idx+1:N] + N_list[0:idx]
    N -= 1

text_result = []

for r in result :
    text_result.append(str(r))

print('<'+','.join(text_result)+'>')
    
# 틀려서 원인이 뭔지 생각해봐야함..

        
        
    