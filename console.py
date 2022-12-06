from models.user import User
from models.country import Country
from models.memory import Memory


from repositories import user_repository, country_repository, memory_repository

user_repository.delete_all()
country_repository.delete_all()
memory_repository.delete_all()

user1 = User('James Blaney')
user_repository.save(user1)
user2 = User('Brendan McLaughlin')
user_repository.save(user2)
user3 = User('Josh Peck')
user_repository.save(user3)
user4 = User('Dan Kingman')
user_repository.save(user4)
user5 = User('Adam Blaney')
user_repository.save(user5)

country1 = Country('Australia', 'Sydney, Brisbane, Melbourne', True)
country_repository.save(country1)
country2 = Country('Vietnam', 'Ho Chi Minh City, Hoi An, Hanoi', True)
country_repository.save(country2)
country3 = Country('Japan', 'Tokyo, Osaka, Kyoto', True)
country_repository.save(country3)
country4 = Country('America', 'New York, San Francisco, Las Vegas', True)
country_repository.save(country4)
country5 = Country('Czech Republic', 'Prague', False)
country_repository.save(country5)

memory1 = Memory(user1, country1, 'Sagittis orci a scelerisque purus semper eget duis. Mauris pharetra et ultrices neque ornare. Commodo viverra maecenas accumsan lacus vel facilisis volutpat est. Diam maecenas sed enim ut sem viverra aliquet eget. Penatibus et magnis dis parturient montes nascetur. Arcu ac tortor dignissim convallis. Orci a scelerisque purus semper eget duis at tellus. Vestibulum lectus mauris ultrices eros in cursus turpis massa tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames. Sed adipiscing diam donec adipiscing tristique risus nec. At ultrices mi tempus imperdiet. Ornare lectus sit amet est placerat in egestas erat. Felis bibendum ut tristique et egestas. Adipiscing elit duis tristique sollicitudin nibh sit amet commodo. Morbi enim nunc faucibus a. Sed euismod nisi porta lorem mollis aliquam.')
memory_repository.save(memory1)
memory2 = Memory(user1, country2, 'Ut tristique et egestas quis ipsum. Ullamcorper malesuada proin libero nunc consequat interdum varius. Ante in nibh mauris cursus mattis molestie. Enim facilisis gravida neque convallis a cras semper. Sapien nec sagittis aliquam malesuada bibendum. Scelerisque felis imperdiet proin fermentum leo. Scelerisque viverra mauris in aliquam sem fringilla ut morbi tincidunt. Nec sagittis aliquam malesuada bibendum arcu. Tempus egestas sed sed risus pretium quam vulputate dignissim.')
memory_repository.save(memory2)
memory3 = Memory(user1, country3, 'Velit aliquet sagittis id consectetur purus. Vitae aliquet nec ullamcorper sit amet risus nullam eget. Tortor posuere ac ut consequat semper viverra nam. Non odio euismod lacinia at quis risus. Mi ipsum faucibus vitae aliquet nec. Semper viverra nam libero justo laoreet sit amet. Enim nunc faucibus a pellentesque sit amet porttitor eget. Justo donec enim diam vulputate ut pharetra. Auctor elit sed vulputate mi. Duis at tellus at urna condimentum mattis pellentesque id nibh. Enim sed faucibus turpis in eu mi bibendum neque. Amet venenatis urna cursus eget.')
memory_repository.save(memory3)
memory4 = Memory(user1, country4, 'At quis risus sed vulputate odio ut enim. Purus sit amet luctus venenatis. Dui faucibus in ornare quam viverra orci sagittis eu. At lectus urna duis convallis convallis tellus id. Porttitor eget dolor morbi non arcu. Feugiat vivamus at augue eget arcu dictum varius duis at. Tristique nulla aliquet enim tortor.')
memory_repository.save(memory4)

memory5 = Memory(user2, country1, 'Faucibus a pellentesque sit amet porttitor eget dolor morbi non. Ornare quam viverra orci sagittis eu volutpat odio facilisis. Magna etiam tempor orci eu lobortis elementum nibh. Sed risus pretium quam vulputate dignissim suspendisse in est. Dictum varius duis at consectetur lorem donec massa sapien faucibus. Dolor morbi non arcu risus. Mattis pellentesque id nibh tortor id aliquet lectus. Sit amet cursus sit amet dictum sit amet justo. Nunc pulvinar sapien et ligula ullamcorper. Sem integer vitae justo eget magna fermentum iaculis eu.')
memory_repository.save(memory5)

memory6 = Memory(user3, country1, 'Pharetra magna ac placerat vestibulum lectus mauris ultrices eros in. Sed enim ut sem viverra aliquet eget sit amet tellus. Auctor elit sed vulputate mi sit amet. Ut enim blandit volutpat maecenas volutpat blandit aliquam etiam. Massa sed elementum tempus egestas sed. Praesent semper feugiat nibh sed pulvinar proin. Volutpat ac tincidunt vitae semper quis. Amet est placerat in egestas erat imperdiet. Ut venenatis tellus in metus vulputate eu scelerisque felis imperdiet.')
memory_repository.save(memory6)
memory7 = Memory(user3, country2, 'Est pellentesque elit ullamcorper dignissim cras tincidunt lobortis. A condimentum vitae sapien pellentesque. Massa eget egestas purus viverra accumsan in nisl nisi scelerisque. Risus ultricies tristique nulla aliquet enim.')
memory_repository.save(memory7)
memory8 = Memory(user3, country4, 'At erat pellentesque adipiscing commodo. Dolor purus non enim praesent elementum facilisis leo. Eu feugiat pretium nibh ipsum consequat nisl vel. Feugiat pretium nibh ipsum consequat nisl vel. Nulla aliquet porttitor lacus luctus accumsan tortor posuere ac ut. Tortor pretium viverra suspendisse potenti nullam ac tortor.')
memory_repository.save(memory8)

memory9 = Memory(user4, country2, 'Feugiat pretium nibh ipsum consequat nisl vel. Nulla aliquet porttitor lacus luctus accumsan tortor posuere ac ut. Tortor pretium viverra suspendisse potenti nullam ac tortor. Tristique senectus et netus et. Tristique et egestas quis ipsum suspendisse. Quis risus sed vulputate odio ut enim blandit volutpat maecenas. Sit amet commodo nulla facilisi nullam vehicula. Egestas tellus rutrum tellus pellentesque eu tincidunt.')
memory_repository.save(memory9)
memory10 = Memory(user4, country4, 'Ornare lectus sit amet est placerat in egestas erat. Proin libero nunc consequat interdum varius sit. Mi eget mauris pharetra et ultrices neque ornare aenean. Ultrices in iaculis nunc sed. Dictum at tempor commodo ullamcorper a lacus vestibulum sed. Enim sed faucibus turpis in eu mi bibendum neque. Nam aliquam sem et tortor consequat. Commodo quis imperdiet massa tincidunt.')
memory_repository.save(memory10)

memory11 = Memory(user5, country3, 'Malesuada fames ac turpis egestas sed tempus urna. Feugiat scelerisque varius morbi enim nunc faucibus. Tempor orci dapibus ultrices in iaculis nunc sed augue lacus. Amet mattis vulputate enim nulla aliquet porttitor lacus luctus accumsan. Aliquam sem et tortor consequat id porta nibh venenatis cras. Id nibh tortor id aliquet lectus proin nibh. Sem viverra aliquet eget sit. Consectetur libero id faucibus nisl tincidunt eget nullam. Fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate sapien nec. Enim nulla aliquet porttitor lacus luctus accumsan tortor. Lacus viverra vitae congue eu.')
memory_repository.save(memory11)



