from models.user import User
from models.country import Country
from models.city import City

from repositories import user_repository, city_repository, country_repository

user_repository.delete_all()
country_repository.delete_all()

user1 = User('James')
user_repository.save(user1)
user2 = User('Ben')
user_repository.save(user2)

country1 = Country('Scotland', 'English', 'Europe')
country_repository.save(country1)
country2 = Country('England', 'English', 'Europe')
country_repository.save(country2)
country3 = Country('France', 'French', 'Europe')
country_repository.save(country3)
country4 = Country('Spain', 'Spanish', 'Europe')
country_repository.save(country4)




# breakpoint()
# user_repository.select_all()

# breakpoint()
# user_repository.select_user_by_id(1)

