from abc import ABC, abstractmethod


class PersonObserver(ABC):
    @abstractmethod
    def person_born(self, person):
        pass

    @abstractmethod
    def person_died(self, person):
        pass


class PersonsRegistryObserver(PersonObserver):
    def __init__(self):
        self.people = []

    def person_born(self, person):
        self.people.append(person)

    def person_died(self, person):
        self.people.remove(person)

    def get_people_count(self):
        return len(self.people)


class PeshoPersonRegistryObserver(PersonObserver):
    def __init__(self):
        self.people = []

    def person_born(self, person):
        if person.first_name != 'Pesho':
            return
        self.people.append(person)

    def person_died(self, person):
        if person.first_name != 'Pesho':
            return
        self.people.remove(person)

    def get_people_count(self):
        return len(self.people)


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class PersonsSubject:
    def __init__(self):
        self.observers = []

    def born(self, person):
        [observer.person_born(person) for observer in self.observers]

    def add_observer(self, observer):
        self.observers.append(observer)


subj1 = PersonsSubject()
subj2 = PersonsSubject()

obs1 = PersonsRegistryObserver()
obs2 = PersonsRegistryObserver()
obs_pesho = PeshoPersonRegistryObserver()

observers = [obs1, obs2, obs_pesho]

subj1.add_observer(obs1)
subj1.add_observer(obs_pesho)

subj2.add_observer(obs1)
subj2.add_observer(obs2)
subj2.add_observer(obs_pesho)

subj1.born(Person('Gosho', 'Goshov'))

[print(obs.get_people_count()) for obs in observers]
subj2.born(Person('Pesho', 'Goshov'))

[print(obs.get_people_count()) for obs in observers]
#
# observers = [
#     PersonsRegistryObserver(),
#     PersonsRegistryObserver(),
# ]
#
#
# def notify(observers, event, person):
#     if event == 'born':
#         [observer.person_born(person) for observer in observers]
#     else:
#         [observer.person_born(person) for observer in observers]
#
#
# notify(observers, 'born', Person('Pesho', 'Peshov'))
#
# print(observers[0].get_people_count())
