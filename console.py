from models.user import User
from models.country import Country
from models.memory import Memory


from repositories import user_repository, country_repository, memory_repository

user_repository.delete_all()
country_repository.delete_all()
memory_repository.delete_all()

user1 = User('James')
user_repository.save(user1)
user2 = User('Brendan')
user_repository.save(user2)

country1 = Country('Australia', 'Sydney, Brisbane, Melbourne', True)
country_repository.save(country1)
country2 = Country('Japan', 'Tokyo, Osaka, Kyoto', False)
country_repository.save(country2)

memory1 = Memory(user1, country1, 'Sydney: Tried to go surfing with my mate Frank, got rolled by a small wave, smashed and dragged to the shore. Really fun would try again.')
memory_repository.save(memory1)
memory2 = Memory(user1, country2, 'Amazing')
memory_repository.save(memory2)



