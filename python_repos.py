import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# Создание вызова API и сохранение ответа
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)

# Сохранение ответа API в переменной
response_dict = r.json()
print('Total repositories:', response_dict['total_count'])

# Анализ информации о репозиториях
repo_dicts = response_dict['items']
print('Repositories returned:', len(repo_dicts))
print("\nSelected information about each repository:")

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        }
    plot_dicts.append(plot_dict)

# Построение визуализации
my_style = LS('#333366', base_style=LCS)
# Настройки конфигурации диаграммы
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 14
my_config.truncate_label = 15 # сокращает длинные имена проектов
my_config.show_y_guides = False # скрываем горизонтальные линии на графике
my_config.width = 1000 # ширина для более эффективного исп/ия места в браузере

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-starred Python projects on GitHub'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
