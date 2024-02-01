import utils, read_csv, charts

data = read_csv.read_csv('data.csv')

def population_by_country():
    country = input("Type country: ")
    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values)

def global_population():
    continents = set(map(lambda x:x['Continent'], data))
    print(continents)
    continent = input("Which continent do you want to see the population of? (default is all): ").title()

    try:
        assert continent in continents, f"Continent: '{continent}' not found"
    except AssertionError as error:
        print(error)
        continent = ""
        
    labels, values = utils.get_global_population(data, continent)
    charts.generate_pie_chart(labels, values)

def run():
    global_population()

if __name__ == "__main__": run()