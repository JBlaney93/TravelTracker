from models.user import User
from models.country import Country
from models.memory import Memory


from repositories import user_repository, country_repository, memory_repository

user_repository.delete_all()
country_repository.delete_all()
# city_repository.delete_all()

user1 = User('James')
user_repository.save(user1)

country1 = Country('Scotland', 'Glasgow, Edinburgh', True)
country_repository.save(country1)

memory1 = Memory(user1, country1, 'Heart of Scotland')
memory_repository.save(memory1)




# breakpoint()
# user_repository.select_all()

# breakpoint()
# user_repository.select_user_by_id(1)

