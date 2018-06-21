import analyze
import collect
import visualize
from config import CONFIG

if __name__ == '__main__':
    resultfiles = dict()

    #collect
    resultfiles['tourspot_visitor'] = collect.crawling_tourspot_visitor(
        district=CONFIG['district'],
        **CONFIG['common'])

    resultfiles['foreign_visitor'] = []
    for country in CONFIG['countries']:
        rf = collect.crawling_foreign_visitor(country, **CONFIG['common'])
        resultfiles['foreign_visitor'].append(rf)

    # print(resultfiles['foreign_visitor'])

    # analysis & visualize
    # result_analysis = analyze.analysis_correlation(resultfiles)
    # print(result_analysis)
    # visualize.graph_scatter(result_analysis)

    # 2. analysis & visualization
    result_analysis = analyze.analysis_correlation_by_tourspot(resultfiles)
    # print(result_analysis)
    visualize.graph_ex_last(result_analysis)