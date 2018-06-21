# 스칼라 값으로 초기화 할때는 반드시 인덱스가 필요
import json

import math
import pandas as pd
import scipy.stats as ss
import matplotlib.pyplot as plt

s1 = pd.Series(7, index=['a', 'b', 'c', 'd'])
print(s1)






resultfile = '../__results__/crawling/서울특별시_tourspot_2017_2017.json'
resultfiles = ['../__results__/crawling/일본(130)_foreignvisitor_2017_2017.json',
    '../__results__/crawling/미국(275)_foreignvisitor_2017_2017.json',
    '../__results__/crawling/중국(112)_foreignvisitor_2017_2017.json']

# 아래는 상관계수의 구현 코드...(사용해 볼것!) #########################################################################
def correlation_coefficient(x, y):
    n = len(x)
    vals = range(n)

    x_sum = 0.0
    y_sum = 0.0
    x_sum_pow = 0.0
    y_sum_pow = 0.0
    mul_xy_sum = 0.0

    for i in vals:
        mul_xy_sum = mul_xy_sum + float(x[i]) * float(y[i])
        x_sum = x_sum + float(x[i])
        y_sum = y_sum + float(y[i])
        x_sum_pow = x_sum_pow + pow(float(x[i]), 2)
        y_sum_pow = y_sum_pow + pow(float(y[i]), 2)

    try:
        r = ((n * mul_xy_sum) - (x_sum * y_sum)) / \
            math.sqrt(((n * x_sum_pow) - pow(x_sum, 2)) * ((n * y_sum_pow) - pow(y_sum, 2)))
    except ZeroDivisionError as e:
        r = 0.0

    return r
########################################################################################################################

# 투어리스트 스팟 테이블 작성 ##########################################################################################
with open(resultfile, 'r', encoding='utf-8') as infile:
    json_data = json.loads(infile.read())
# print(json_data)
tourspotvisitor_table = pd.DataFrame(json_data, columns=['date', 'tourist_spot','count_foreigner'])
print(tourspotvisitor_table)
########################################################################################################################

# 루프를 돌기위한 관광지 리스트 추출 ###################################################################################
tourist_spot_list = tourspotvisitor_table['tourist_spot'].unique()
########################################################################################################################

# 외국인 방문객의 월별 카운트 테이블 작성 ##############################################################################
# 외국인 방문객의 spot 별 조인된 테이블을 담기위한 리스트 : tables $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

foreignvisitor_table_list = []
for filename in resultfiles:
    with open(filename, 'r', encoding='utf-8') as infile:
        json_data = json.loads(infile.read())
    foreignvisitor_table = pd.DataFrame(json_data, columns=['date', 'country_name', 'visit_count']).sort_values('date').set_index('date')
    # foreignvisitor_table.rename(columns={'visit_count': '{0}'.format(foreignvisitor_table['country_name'].unique()[0])}, inplace=True)
    # del foreignvisitor_table["country_name"]
    # print(foreignvisitor_table)
    foreignvisitor_table_list.append(foreignvisitor_table)
    # visit_count = foreignvisitor_table['visit_count'].get_values().tolist()
########################################################################################################################

# 각 관광지별 월별 방문객 테이블 루프 안에서 외국인 방문객 테이블을 각각 조인하여 시각화를 위한 전처리 수행 ############
# 시각화를 위한 데이터의 전처리 ########################################################################################
resultSetList = [] # 이곳에 시각화에 사용될 데이터셋을 담을 것!
               # 필요한 데이터는 장소명, 나라명, coefficient

for index, spot in enumerate(tourist_spot_list):
    temp_table = tourspotvisitor_table[tourspotvisitor_table['tourist_spot'] == spot].sort_values('date').set_index('date')

    resultSet = {'tour_spot' : spot}
    for foreignvisitor_table in foreignvisitor_table_list:
        merge_table = pd.merge(temp_table, foreignvisitor_table, left_index=True, right_index=True)
        print(merge_table)

# 상관계수에 필요한 데이터 추출 - 리스트로...###########################################################################
        count_foreigner = list(merge_table['count_foreigner'])
        visit_count = list(merge_table['visit_count'])
########################################################################################################################
# 데이터 결과를 그래프로 나타내기 위해 필요한 나라이름, correlation coefficient 추출 ###################################
        r = correlation_coefficient(count_foreigner, visit_count)
        country_name = merge_table['country_name'].unique()[0]
########################################################################################################################
        print(spot, country_name, r)

# 결과를 딕셔너리에 업데이트 후 최종 리스트에 추가
        resultSet.update({'r_{0}'.format(country_name) : r})
    resultSetList.append(resultSet)

print(resultSetList)
# return resultSetList


def graph_ex_last(result_analysis):
    graph_table = pd.DataFrame(result_analysis, columns=['tour_spot', 'r_중국', 'r_일본', 'r_미국'])
    graph_table = graph_table.set_index('tour_spot')

    graph_table.plot(kind='bar')
    plt.show()

graph_ex_last(resultSetList)