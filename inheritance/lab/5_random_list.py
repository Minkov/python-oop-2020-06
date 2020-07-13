import random


class RandomList(list):

    def get_random_element(self):
        """
        Returns and removes a random element from the list
        """
        element_to_remove = random.choice(self)
        self.remove(element_to_remove)
        return element_to_remove


ll = RandomList([1, 2, 3, 4, 5, 6, 7])
print(ll)
print(ll.get_random_element())
print(ll)
