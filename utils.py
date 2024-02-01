def get_population(county_dict):
    population_dict={
        '2022': int(county_dict['2022 Population']),
        '2020': int(county_dict['2020 Population']),
        '2015': int(county_dict['2015 Population']),
        '2010': int(county_dict['2010 Population']),
        '2000': int(county_dict['2000 Population']),
        '1990': int(county_dict['1990 Population']),
        '1980': int(county_dict['1980 Population']),
        '1970': int(county_dict['1970 Population'])
    }
    
    keys = population_dict.keys()
    values = population_dict.values()

    return keys, values

def get_global_population(data, continent):
    if continent != '': data = list(filter(lambda x:x['Continent']== continent, data))

    countries = list(map(lambda x:x['Country/Territory'], data))
    percentages = list(map(lambda x:x['World Population Percentage'], data))

    return countries, percentages

def population_by_country(data, country):
    result = list(filter(lambda iten: iten['Country/Territory'] == country, data))
    
    return result
