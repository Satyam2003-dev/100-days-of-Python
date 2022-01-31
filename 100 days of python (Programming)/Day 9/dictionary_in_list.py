
travel_log = [
    {
        "country": "India",
        "cities_visited": ["New Delhi", "Mumbai", "Chandigarh", "Varanasi", "Patna"],
        "total_visit": 10
     },
    {
        "country": "Russia",
        "cities_visited": ["Moscow", "Leningrad", "Saint Petersburg"],
        "total_visit": 5
    },
]

def add_new_country(country_visited, cities_visited,total_visit):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities_visited"] = cities_visited
    new_country["total_visits"] = total_visit
    travel_log.append(new_country)

add_new_country("Japan", ["Tokyo"], 2)
print(travel_log)
