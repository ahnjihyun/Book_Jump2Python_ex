## ==============================================================
## 파일 읽기
## (파일 객체) = open( (파일 이름), (파일 열기 모드) )
## ==============================================================
## 파일 열기 모드
## r : 읽기모드 - 파일을 읽기만 할 때 사용
## w : 쓰기모드 - 파일에 내용을 쓸 때 사용(기존에 있던 내용 날라감)
## a : 추가모드 - 파일의 마지막에 새로운 내용을 추가할 때 사용
## ==============================================================


# 파일 생성 
f = open('fileName.txt', 'w')
# 열려있는 파일 객체를 닫아준다. 파일을 닫지 않은 상태에서 다시 열면 파일을 읽을 수 없다.
f.close() 



## ==============================================================
## 프로그램 외부에 저장된 파일을 읽는 여러 가지 방법
## ==============================================================

## 1.readline()함수 
f = open('file1.txt', 'r')
while 1:
    line = f.readline() # readline()은 더 이상 읽을 줄이 없을 경우 None을 출력한다
    if not line: break
    print(line)
f.close()

## 2.readlines()함수
f = open('file2.txt', 'r')
lines = f.readlines() # readlines()는 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다 ['line1', 'line2',...]
for line in lines:
    print(line)
f.close()

## 3.read()함수
f = open('file3.txt', 'r')
data = f.read() # read()는 파일의 전체 내용을 문자열로 돌려준다
print(data)
f.close()


## ==============================================================
## with문과 함께 사용하기 - 명시적으로 close()하지 않아도 됨
## ==============================================================

# Before
f = open('test.txt', 'w')
f.write('hello world')
f.close()

# After
with open('test.txt', 'w') as f:
    f.write('hello world')
