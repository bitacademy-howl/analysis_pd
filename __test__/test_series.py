import pandas as pd

price = [92600, 92400, 92100, 94300, 92300]
s = pd.Series(price)

print(s)

print(s[0], s[1])

# 리스트로 시리즈 생성
data = [92600, 92400, 92100, 94300, 92300]
index = ['2017-01-01', '2017-02-02', '2017-03-03', '2017-04-04', '2017-04-04']
s = pd.Series(data=data, index=index)
# print(s)

# s = pd.Series([92600, 92400, 92100, 94300, 92300], index=['2017-01-01', '2017-02-02', '2017-03-03', '2017-04-04', '2017-04-04'])

print(s['2017-03-03'])

# 스칼라 값으로 초기화 할때는 반드시 인덱스가 필요
s1 = pd.Series(7, index=['a', 'b', 'c', 'd'])
print(s1)

# 딕셔너리로 스칼라 생성
d = {'a' : 10, 'b' : 20, 'c' : 30}
s1 = pd.Series(d)
print(s1)

s1 = pd.Series(d, index=['A', 'B', 'C'])
print(s1)

s1 = pd.Series(d, index=['a', 'b', 'c', 'd'])
print(s1)

# 순회 (index, Value 라는 속성을 통해 접근이 가능하다.
for date in s.index:
    print(date, end=' ')
else:
    print()

# 시리즈의 연산
s1 = pd.Series([10, 20, 30], index=['A', 'B', 'C'])
s2 = pd.Series([10, 20, 30], index=['B', 'C', 'D'])

s3 = s1+s2
print(s3, type(s3))

s3 = s1-s2
print(s3, type(s3))

s3 = s1*s2
print(s3, type(s3))

s3 = s1/s2
print(s3, type(s3))

s3 = s1 * 3
print(s3, type(s3))

