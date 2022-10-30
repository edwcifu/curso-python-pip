import utils
import read_csv
import charts
import pandas as pd

def run():
  '''
  data = read_csv.read_csv('./data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  '''
  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values

  charts.generate_pie_chart(countries, percentages)

  data = read_csv.read_csv('./data.csv')
  country = input('ingrese pais: ')

  result = utils.filter_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values, country['Country/Territory'])
  
if __name__ == '__main__':
  run()
  