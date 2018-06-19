import json
import pandas as pd
import scipy.stats as ss
# import numpy as np

def analysis_correlation(resultfiles):
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as infile:
        json_data = json.loads(infile.read())
        # print(json_data)

    tourspotvisitor_table = pd.DataFrame(json_data, columns=['count_foreigner', 'date', 'tourist_spot'])
    print(tourspotvisitor_table)

    # 일자별 그룹핑 하여 방문객의 총합을 구한다
    temp_tourspotvisitor_table = pd.DataFrame(tourspotvisitor_table.groupby('date')['count_foreigner'].sum())

    results = []
    for filename in resultfiles['foreign_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data = json.loads(infile.read())

        foreignvisitor_table = pd.DataFrame(json_data, columns=['date', 'country_name', 'visit_count'])

        foreignvisitor_table = foreignvisitor_table.set_index('date')

        merge_table = pd.merge(temp_tourspotvisitor_table, foreignvisitor_table, left_index=True, right_index=True)
        print(merge_table)

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

    return results