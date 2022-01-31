#   Nesting

capitals = {
    "India": "New Delhi",
    "Russia": "Moscow"
}

#   Nesting a list in Dictionary

travel_log = {
    "India": {"cities_visited": ["New Delhi", "Mumbai", "Chandigarh", "Varanasi", "Patna"], "total_visit": 10},
    "Russia": {"cities_visited": ["Moscow", "Leningrad"], "total_visit": 5},
}

#   Nesting Dictionary in a list

travel_log = [
    {
        "country": "India",
        "cities_visited": ["New Delhi", "Mumbai", "Chandigarh", "Varanasi", "Patna"],
        "total_visit": 10
     },
    {
        "country": "Russia",
        "cities_visited": ["Moscow", "Leningrad"],
        "total_visit": 5
    },
]
