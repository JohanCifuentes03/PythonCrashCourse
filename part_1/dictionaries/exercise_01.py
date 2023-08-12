def getInfo(countries):
    for k, v in countries.items():
        print("-----------")
        print(f"\ncountry : {k.title()}")
        print(f"cities: ")
        for city in v:
            print(f"\t{city.title()}")
        print()


countries = {
    'colombia': ['bogota', 'cali', 'medellin'],
    'brasil': ['sao paulo', 'rio de janeiro'],
    'venezuela': ['caracas'],
    'mexico': ['ciudad de mexico', 'sinaloa', 'juarez']
}

getInfo(countries)
