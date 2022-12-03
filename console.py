from models.user import User
from models.country import Country
from models.memory import Memory


from repositories import user_repository, country_repository, memory_repository

user_repository.delete_all()
country_repository.delete_all()
memory_repository.delete_all()

user1 = User('James')
user_repository.save(user1)

country1 = Country('Scotland', 'Glasgow, Edinburgh', True)
country_repository.save(country1)
country2 = Country('England', 'Manchester, Leeds, Newcastle', True)
country_repository.save(country2)

memory1 = Memory(user1, country1, 'Heart of Scotland')
memory_repository.save(memory1)
memory2 = Memory(user1, country2, 'Amongst the worst places that I have ever been, not good')
memory_repository.save(memory2)



