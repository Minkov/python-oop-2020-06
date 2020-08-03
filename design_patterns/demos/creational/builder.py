from demos.utils.print_attrs import IPrintAttributes


class Animal(IPrintAttributes):
    def __init__(self, name, age, species, weight):
        self.name = name
        self.age = age
        self.species = species
        self.weight = weight


class AnimalsBuilder:
    mandatory_attributes = {
        'name': str,
        'age': int,
        'species': str,
    }

    optional_attributes = {
        'weight': float,
    }

    def __init__(self):
        self.__attrs_dict = {}
        self.__reset()

    def set_name(self, name):
        self.__attrs_dict['name'] = name
        return self

    def set_age(self, age):
        self.__attrs_dict['age'] = age
        return self

    def set_species(self, species):
        self.__attrs_dict['species'] = species
        return self

    def set_weight(self, weight):
        self.__attrs_dict['weight'] = weight
        return self

    def build(self):
        self.__validate()
        result = Animal(**self.__attrs_dict)
        self.__reset()
        return result

    def __reset(self):
        for (key, pair) in self.mandatory_attributes.items():
            self.__attrs_dict[key] = None

        for (key, pair) in self.optional_attributes.items():
            self.__attrs_dict[key] = None

    def __validate(self):
        missing_attrs = [key for (key, value) in self.mandatory_attributes.items() if self.__attrs_dict[key] is None]
        if missing_attrs:
            raise ValueError(f'The following attributes are missing: {",".join(missing_attrs)}')


print(Animal('Gosho', 3, 'kuche', 123))

builder = AnimalsBuilder()
builder.set_name('Pesho')
builder.set_age(4)
builder.set_species('cat')
builder.set_weight(2)
print(builder.build())

print(builder
      .set_name('Pesho')
      .set_age(4)
      .set_species('cat')
      .set_weight(2)
      .build())
