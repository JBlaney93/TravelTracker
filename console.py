from models.user import User
from models.country import Country
from models.city import City

from repositories import user_repository, city_repository, country_repository

user_repository.delete_all()

user1 = User('James')
user_repository.save(user1)
user2 = User('Ben')
user_repository.save(user2)



# breakpoint()
# user_repository.select_all()

# breakpoint()
# user_repository.select_user_by_id(1)

