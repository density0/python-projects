def city_country(city, country, *pop):

    location = f"{city}, {country}"
    for pops in pop:

        location = f"{location} - population {pops}"

    return location
