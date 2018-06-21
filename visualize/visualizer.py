import matplotlib.pyplot as plt
import pandas as pd

def graph_scatter(result_analysis):
    fig, subplots = plt.subplots(1, len(result_analysis), sharey=True)

    # index = 0 와 같은 초기화 및 내부에서 i++ 할 필요가 없다.
    for index, result in enumerate(result_analysis):
        subplots[index].set_xlabel('{0}인 입국자수'.format(result['country_name']))

        index == 0 and subplots[index].set_ylabel('관광지 입장객 수')
        subplots[index].set_title('r={:.5f}'.format(result['r'][0]))
        subplots[index].scatter(result['x'], result['y'], color='black', s=6)
    plt.subplots_adjust(wspace=0)
    plt.show()



def graph_ex_last(result_analysis):

    graph_table = pd.DataFrame(result_analysis, columns=['tour_spot', 'r_중국', 'r_일본', 'r_미국'])
    graph_table = graph_table.set_index('tour_spot')

    graph_table.plot.bar()
    # graph_table.plot(kind='bar')

    plt.xticks(rotation=20)
    plt.title('Correlation Coefficient of Countries & Attractions', fontsize=15)
    plt.show()