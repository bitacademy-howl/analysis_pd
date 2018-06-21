from matplotlib import font_manager
import matplotlib as mpl
from matplotlib import pyplot as plt

font_filename = 'c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_filename).get_name()
print(font_name)
print ('설정파일 위치: ', mpl.matplotlib_fname())

font_list = font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
print(font_list)
# ttf 폰트 전체개수
print(len(font_list))


font_options = {'family': 'Malgun Gothic'}
print(font_options)
plt.rc('font', **font_options)
plt.rc('axes', unicode_minus=False)
