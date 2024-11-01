# lib/owner_pet.py

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # Class variable to store all Pet instances

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        
        # Validate pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type.")
        
        self.owner = owner
        Pet.all.append(self)  # Add the instance to the all list

    def set_owner(self, owner):
        if not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner.")
        self.owner = owner


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # Private attribute to store pets

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet.")
        pet.set_owner(self)  # Set the owner of the pet
        self._pets.append(pet)  # Add pet to the owner's list

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)

# Example Usage (You can put this under `if __name__ == "__main__":`)
if __name__ == "__main__":
    owner1 = Owner("Alice")
    pet1 = Pet("Buddy", "dog")
    pet2 = Pet("Mittens", "cat")
    
    owner1.add_pet(pet1)
    owner1.add_pet(pet2)
    
    print(f"{owner1.name}'s pets:")
    for pet in owner1.get_sorted_pets():
        print(f"{pet.name} ({pet.pet_type})")