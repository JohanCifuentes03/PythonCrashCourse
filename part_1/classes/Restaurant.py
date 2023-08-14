class Restaurant:
    restaurant_name = ''
    cuisine_type = ''

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")


restaurants = []
restaurant = Restaurant("johan's pizza", 'pizza')
restaurant2 = Restaurant('gloton', 'burger')
restaurant3 = Restaurant('samaritano', 'sushi')
restaurants.append(restaurant)
restaurants.append(restaurant2)
restaurants.append(restaurant3)

for res in restaurants:
    res.describe_restaurant()