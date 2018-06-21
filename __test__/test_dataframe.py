import pandas as pd

# 데이터 프레임 만들기
# series 두개를 헙쳐서...

list1 = [1,2,3]
index1 = ['a', 'b', 'c']

list2 = [10,20,30,40]
index2 = ['a', 'b', 'c', 'd']

d = {
'one' : pd.Series(data=list1, index=index1),
'two' : pd.Series(data=list2, index=index2)
}

df = pd.DataFrame(d)
print(df)

# list와 dict 를 사용하여 데이터 프레임 생성
data = [
    {'name' : '둘리', 'age':10, 'phone':'010-1111-1111'},
    {'name' : '마이클', 'age':30, 'phone':'010-222-2222'},
    {'name' : '도우넛', 'age':20, 'phone':'010-3333-3333'},
]

df = pd.DataFrame(data)
print(df)

df2 = pd.DataFrame(df, columns=['name', 'phone'])

print(df2)

# 데이터 추가 (열 추가)
df2['height'] = [150, 160, 170]
print(df2)

# 인덱스 선택
df3 = df2.set_index('name')
print(df3)

# 컬럼 선택
s = df2['name'].get_values().tolist()
print('컬럼선택 : ', s, type(s))

# merge
df4 = pd.DataFrame([{'sido' : '서울'}, {'sido' : '부산'}, {'sido' : '전주'}])
print(df4, type(df4))

# 디폴트 인덱스를 가지고 병합하기 (일종의 데이터 추가 by merge)
df5 = pd.merge(df2, df4, left_index=True, right_index=True)
print(df5)

# merge & join
df1 = pd.DataFrame({
    '고객번호': [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    '이름': ['둘리', '도우너', '또치', '길동', '희동', '마이콜', '영희']})

df2 = pd.DataFrame({
    '고객번호': [1001, 1001, 1005, 1006, 1008, 1001],
    '금액': [10000, 20000, 15000, 5000, 100000, 30000]})

# 공통 열(고객번호)를 기준으로 데이터를 찾아서 합친다.
# 이 때, 기본적으로 양쪽 데이터프레임에 모두 키가 존재하는
# 데이터만 병합. (inner join 방식)

df3 = pd.merge(df1, df2)
print(df3)

# outer join : 명시된 키에 관한 모든 데이터를 포함하도록 join 하는 방식

# full outer join : 양쪽 모두의 데이터를 포함
df3 = pd.merge(df1, df2, how='outer')
print(df3)

# left outer join : 왼쪽의 전체 데이터를 기준으로 join
df3 = pd.merge(df1, df2, how='left')
print(df3)

# right outer join, 오른쪽 전체 데이터를 기준으로 join
df3 = pd.merge(df1, df2, how='right')
print(df3)

#
df1 = pd.DataFrame({'성별': ['남자', '남자', '여자'],
                    '연령': ['미성년자', '성인', '미성년자'],
                    '매출1': [1, 2, 3]})

df2 = pd.DataFrame({'성별': ['남자', '남자', '여자', '여자'],
                    '연령': ['미성년자', '미성년자', '미성년자', '성인'],
                    '매출2': [4, 5, 6, 7]})

# 기준을 명시하지 않았을 경우 공통된 컬럼을 기준으로 병합하게 된다.
df3 = pd.merge(df1, df2)
print(df3)
# 위와 동일한 코드
df3 = pd.merge(df1, df2, on=['성별', '연령'])
print(df3)

# 
df3 = pd.merge(df1, df2, on=['성별'])
print(df3)

