
## ==============================================================
## 함수의 결과값은 언제나 하나이다.
## ==============================================================

# 예시 
def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(3,4)
print(result) 
# 튜플값 하나인 (7, 12)로 돌려준다. 

result1, result2 = add_and_mul(3,4)
print(result1, result2)
# 각각 7, 12

 