import json

import math
import pandas as pd
import scipy.stats as ss
# import numpy as np
import matplotlib.pyplot as plt

def analysis_correlation(resultfiles):
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as infile:
        json_data = json.loads(infile.read())
        # print(json_data)

######################################################################################################################
    tourspotvisitor_table = pd.DataFrame(json_data, columns=['count_foreigner', 'date', 'tourist_spot'])
    # print(tourspotvisitor_table)

    # 일자별 그룹핑 하여 방문객의 총합을 구한다
    temp_tourspotvisitor_table = pd.DataFrame(tourspotvisitor_table.groupby('date')['count_foreigner'].sum())
#######################################################################################################################

    results = []
    for filename in resultfiles['foreign_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data = json.loads(infile.read())

        foreignvisitor_table = pd.DataFrame(json_data, columns=['date', 'country_name', 'visit_count'])
        foreignvisitor_table = foreignvisitor_table.set_index('date')

        merge_table = pd.merge(temp_tourspotvisitor_table, foreignvisitor_table, left_index=True, right_index=True)
        # print(merge_table)

        # 데이터 전처리 - 시각화를 위한
        x = list(merge_table['visit_count'])
        y = list(merge_table['count_foreigner'])
        country_name = foreignvisitor_table['country_name'].unique().item(0)
        # r = ss.correlation_coefficient(x, y)
        r = ss.pearsonr(x, y)
        # 넘파이 코릴레이션을 제공하지만 자세한 사용법은 알아보고 할 것
        # r = np.corrcoef(x, y)[0]

        data = {'x': x, 'y' : y, 'country_name': country_name, 'r' : r}
        results.append(data)

        # merge_table['visit_count'].plot(kind='bar')
        # plt.show()
    print(results)
    return results



def analysis_correlation_by_tourspot(resultfiles):
    # 투어리스트 스팟 테이블 작성 ##########################################################################################
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as infile:
        json_data = json.loads(infile.read())
    # print(json_data)
    tourspotvisitor_table = pd.DataFrame(json_data, columns=['date', 'tourist_spot', 'count_foreigner'])
    # print(tourspotvisitor_table)
    ########################################################################################################################

    # 루프를 돌기위한 관광지 리스트 추출 ###################################################################################
    tourist_spot_list = tourspotvisitor_table['tourist_spot'].unique()
    ########################################################################################################################

    # 외국인 방문객의 월별 카운트 테이블 작성 ##############################################################################
    # 외국인 방문객의 spot 별 조인된 테이블을 담기위한 리스트 : tables $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    foreignvisitor_table_list = []
    for filename in resultfiles['foreign_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data = json.loads(infile.read())
        foreignvisitor_table = pd.DataFrame(json_data, columns=['date', 'country_name', 'visit_count']).sort_values(
            'date').set_index('date')
        # foreignvisitor_table.rename(columns={'visit_count': '{0}'.format(foreignvisitor_table['country_name'].unique()[0])}, inplace=True)
        # del foreignvisitor_table["country_name"]
        # print(foreignvisitor_table)
        foreignvisitor_table_list.append(foreignvisitor_table)
        # visit_count = foreignvisitor_table['visit_count'].get_values().tolist()
    ########################################################################################################################

    # 각 관광지별 월별 방문객 테이블 루프 안에서 외국인 방문객 테이블을 각각 조인하여 시각화를 위한 전처리 수행 ############
    # 시각화를 위한 데이터의 전처리 ########################################################################################
    resultSetList = []  # 이곳에 시각화에 사용될 데이터셋을 담을 것!
    # 필요한 데이터는 장소명, 나라명, coefficient

    for index, spot in enumerate(tourist_spot_list):
        temp_table = tourspotvisitor_table[tourspotvisitor_table['tourist_spot'] == spot].sort_values('date').set_index(
            'date')

        resultSet = {'tour_spot': spot}
        for foreignvisitor_table in foreignvisitor_table_list:
            merge_table = pd.merge(temp_table, foreignvisitor_table, left_index=True, right_index=True)
            # print(merge_table)

            # 상관계수에 필요한 데이터 추출 - 리스트로...###########################################################################
            count_foreigner = list(merge_table['count_foreigner'])
            visit_count = list(merge_table['visit_count'])
            ########################################################################################################################
            # 데이터 결과를 그래프로 나타내기 위해 필요한 나라이름, correlation coefficient 추출 ###################################
            r = correlation_coefficient(count_foreigner, visit_count)
            country_name = merge_table['country_name'].unique()[0]
            ########################################################################################################################
            # print(spot, country_name, r)

            # 결과를 딕셔너리에 업데이트 후 최종 리스트에 추가
            resultSet.update({'r_{0}'.format(country_name): r})
        resultSetList.append(resultSet)

    return resultSetList

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