
def add(n1, n2):
    return n1 + n2

def add3(n1, n2, n3):
    return n1 + n2 + n3

def add4(n1, n2, n3, n4):
    return n1 + n2 + n3 + n4


'''
* 위치 가변 인수
- 함수를 호출할 때는 함수 정의시에 지정한 인수의 개수만큼
값을 전달해야 합니다.

- 하지만 가변 인수를 사용하면 하나의 인수로 여러 개의 값을
받아서 처리할 수 있습니다.

- 위치 가변인수는 함수 정의부에서 인수를 선언할 때
인수 앞에 * 기호를 붙여 선언하며, 이런 경우에 여러 개의 
데이터를 튜플로 묶어서 함수 내부로 전달합니다.

'''
def calc_total(*nums): 
    print(type(nums))
    total = 0
    for n in nums:
        total += n

    return total

print(calc_total(5, 7, 9, 3, 12))

def calc_points(*points, name):
    print(f'{name} 학생의 성적을 계산합니다...')

    total = 0
    for p in points:
        total += p
    return total / len(points)
    
# 가변 인수와 일반 인수를 동시에 사용할 때는
# 일반 인수를 반드시 키워드 인수 방식으로 전달해야 합니다.
result = calc_points(94, 88, 40, 50, 44, name='군범이')
print(f'평균: {result:0.1f}점')

'''
# 키워드 가변 인수

- 함수가 여러개의 키워드 인수를 받을 수 있게 해 주는 가능.
- 키워드 가변 인수를 선언해서 여러 값을 받으면 함수 내부로 사전이 전달됨.
'''

def print_info(**kwargs):
    print(type(kwargs))
    for k in kwargs:
        print(f'{k}: {kwargs[k]}')


print_info(name='김철수', age=30, city='서울')