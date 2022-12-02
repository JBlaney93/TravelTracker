from models.user import User
from models.country import Country
from models.city import City

from repositories import user_repository, city_repository, country_repository

user_repository.delete_all()
country_repository.delete_all()
# city_repository.delete_all()

user1 = User('James')
user_repository.save(user1)

country1 = Country('Scotland', user1, 'Europe')
country_repository.save(country1)

city1 = City('Glasgow', country1, True)
city_repository.save(city1)





# breakpoint()
# user_repository.select_all()

# breakpoint()
# user_repository.select_user_by_id(1)

