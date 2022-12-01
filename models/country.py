class Country:
    
    def __init__ (self, name, language, continent, id=None):
        self.name = name
        self.language = language
        self.continent = continent
        self.cities = []
        self.id = id


# self.cities left out of constructor as we are declaring it as an empty list to be populated
# is this correct?