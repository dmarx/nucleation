"""Relations of the kind for which linear relational structure has been reported
(Hernandez et al., "Linearity of relation decoding in transformer language
models", 2023: country capital, city in country, country language), written as
context s, query q and one-token reply y, as in NOTE-746's s ^ q ^ y.

Pairs whose reply is not one token in a model's tokenizer are dropped at run
time, so the counts differ by model. The lists were written for this study
from general knowledge; ambiguous cases (several official languages, disputed
capitals) were left out.
"""

_CITY = {
    "France": ["Lyon", "Marseille", "Toulouse", "Nice", "Bordeaux", "Lille", "Strasbourg", "Nantes"],
    "Germany": ["Munich", "Hamburg", "Cologne", "Frankfurt", "Stuttgart", "Dresden", "Leipzig", "Bremen"],
    "Italy": ["Milan", "Naples", "Turin", "Florence", "Venice", "Bologna", "Genoa", "Palermo"],
    "Spain": ["Barcelona", "Seville", "Valencia", "Bilbao", "Malaga", "Granada", "Zaragoza"],
    "Japan": ["Osaka", "Kyoto", "Yokohama", "Nagoya", "Sapporo", "Kobe", "Hiroshima", "Fukuoka"],
    "China": ["Shanghai", "Guangzhou", "Shenzhen", "Chengdu", "Wuhan", "Nanjing", "Tianjin"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune", "Jaipur"],
    "Russia": ["Novosibirsk", "Kazan", "Omsk", "Samara", "Volgograd", "Yekaterinburg", "Vladivostok"],
    "Brazil": ["Salvador", "Recife", "Fortaleza", "Curitiba", "Manaus"],
    "Canada": ["Toronto", "Montreal", "Vancouver", "Calgary", "Edmonton", "Winnipeg", "Halifax"],
    "Mexico": ["Guadalajara", "Monterrey", "Tijuana", "Puebla", "Cancun", "Acapulco"],
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Hobart"],
}

_LANG = {
    "French": ["France", "Senegal", "Mali"],
    "Spanish": ["Spain", "Mexico", "Argentina", "Colombia", "Peru", "Chile", "Venezuela", "Cuba",
                "Ecuador", "Uruguay", "Guatemala", "Honduras"],
    "Portuguese": ["Portugal", "Brazil", "Angola", "Mozambique"],
    "German": ["Germany", "Austria"],
    "Italian": ["Italy"],
    "Japanese": ["Japan"],
    "Russian": ["Russia"],
    "Arabic": ["Egypt", "Saudi Arabia", "Jordan", "Iraq", "Syria", "Libya", "Yemen", "Oman", "Kuwait", "Qatar"],
    "Chinese": ["China", "Taiwan"],
    "Korean": ["South Korea", "North Korea"],
    "Dutch": ["the Netherlands", "Suriname"],
    "Greek": ["Greece"],
    "Turkish": ["Turkey"],
    "Polish": ["Poland"],
    "Swedish": ["Sweden"],
    "Thai": ["Thailand"],
    "Persian": ["Iran"],
    "English": ["Australia", "Jamaica", "New Zealand"],
}

_CAP = [("France", "Paris"), ("Germany", "Berlin"), ("Italy", "Rome"), ("Spain", "Madrid"), ("Japan", "Tokyo"),
        ("China", "Beijing"), ("Russia", "Moscow"), ("Egypt", "Cairo"), ("England", "London"), ("Greece", "Athens"),
        ("Austria", "Vienna"), ("Poland", "Warsaw"), ("Hungary", "Budapest"), ("Portugal", "Lisbon"),
        ("Ireland", "Dublin"), ("Norway", "Oslo"), ("Sweden", "Stockholm"), ("Finland", "Helsinki"),
        ("Denmark", "Copenhagen"), ("the Netherlands", "Amsterdam"), ("Belgium", "Brussels"), ("Turkey", "Ankara"),
        ("Iran", "Tehran"), ("Iraq", "Baghdad"), ("Syria", "Damascus"), ("Lebanon", "Beirut"), ("Kenya", "Nairobi"),
        ("Nigeria", "Abuja"), ("Thailand", "Bangkok"), ("Vietnam", "Hanoi"), ("Indonesia", "Jakarta"),
        ("the Philippines", "Manila"), ("South Korea", "Seoul"), ("Pakistan", "Islamabad"),
        ("Afghanistan", "Kabul"), ("Cuba", "Havana"), ("Peru", "Lima"), ("Chile", "Santiago"),
        ("Colombia", "Bogota"), ("Venezuela", "Caracas"), ("Canada", "Ottawa"), ("Australia", "Canberra"),
        ("Scotland", "Edinburgh"), ("Wales", "Cardiff"), ("Romania", "Bucharest"), ("Serbia", "Belgrade"),
        ("Switzerland", "Bern"), ("Saudi Arabia", "Riyadh"), ("Morocco", "Rabat"), ("Ghana", "Accra")]

RELATIONS = {
    "city_in_country": {"query": " is a city in the country of",
                        "pairs": [(c, " " + k) for k, cs in _CITY.items() for c in cs]},
    "country_language": {"query": "'s official language is",
                         "pairs": [(c, " " + k) for k, cs in _LANG.items() for c in cs]},
    "country_capital": {"query": "'s capital city is",
                        "pairs": [(c, " " + y) for c, y in _CAP]},
}
