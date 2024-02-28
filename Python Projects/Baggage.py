class Baggage:
    allowed_item = ('pen', 'book', 'coat', 'umbrella', 'gloves', 'jacket', 'food', 'wallet', 'keys', 'laptop', 'phone', 'chapstick', 'spectacles', 'calculator')
    def __init__(self, name, capacity=5):
        self.name = name
        self.capacity = capacity
        self.inventory = []
    def display_items(self):
        print(self.inventory)
    def add_item(self, item_object):
        if not isinstance(item_object, InvItem):
            return False, f'{item_object.name} is not part of the InvItem Class'
        if len(self.inventory) <= self.capacity:
            if item_object.name in Baggage.allowed_item:
                self.inventory.append(item_object.name)
                return True, f'{item_object.name} successfully added'
            else:
                return False, f'{item_object.name}, is not in the allowed list'
        else:
            return False, 'Item over capacity'
    def remove_item(self, item_object):
        if not isinstance(item_object, InvItem):
            return False, f'{item_object.name} is not part of the InvItem Class'
        if self.check_item(item_object):
            i = self.inventory.index(item_object.name)
            self.inventory.pop(i)
            return True, f'{item_object.name} removed successfully'
        else:
            return False, 'Item not in Baggage Class'
    def check_item(self, item_object):
        if not isinstance(item_object, InvItem):
            return False, f'{item_object.name} is not part of the InvItem Class'
        return item_object.name in self.inventory
class InvItem:
    def __init__(self, name):
        self.name = name
if __name__ == '__main__':
    # !/usr/bin/env python
    # coding: utf-8

    # In[ ]:

    # Copy and paste the following code following your class definitions
    # and run it to test your classes.

    # Global Executable code follows......................................

    input('Hit "Enter" to create "backpack1" object with name "My backpack1": \n')
    backpack = Baggage('My backpack1')
    backpack.display_items()

    input('Hit "Enter" to create some "InvItem" objects: \n')
    It1 = InvItem("book")
    It2 = InvItem("umbrella")
    It3 = InvItem("coat")
    It4 = InvItem("pen")
    It5 = InvItem("cap")
    It7 = InvItem("banana")
    print('Created for use in this script: ', It1.name, It2.name, It3.name, It4.name,
          It5.name, It7.name)

    input('\nT1. Hit "Enter" to add \n\t' + It1.name + '\n\t' + It2.name +
          '\n\t' + It4.name + '\nto ' + backpack.name + '\n')
    backpack.add_item(It1)
    backpack.add_item(It2)
    backpack.add_item(It4)
    backpack.add_item(It7)
    print(backpack.name, ' now has the following items: ')
    backpack.display_items()

    input('\nT2. "Enter" to see if ' + backpack.name + ' has ' + It1.name + '  Should see "True" ')
    print(backpack.check_item(It1))

    input('\nT3. "Enter" to see if ' + backpack.name + ' has ' + It7.name + '  Should see "False" ')
    print(backpack.remove_item(It7))

    input('\nT4. "Enter" to remove ' + It1.name + ', result: ' + backpack.remove_item(It1)[1])

    input('\nT5. "Enter" to add ' + It3.name + ',  result: ' + backpack.add_item(It3)[1])
    print('\nShould now have umbrella, pen, and coat in the following list...')
    backpack.display_items()

    input('\n\nT6. Creating new container with name "My satchel" - add 2 items to container to equal capacity ')
    satchel = Baggage('My satchel', capacity=2)
    satchel.add_item(It3)
    satchel.add_item(It4)
    print('\n', satchel.name, ' was created with the following items: ')
    satchel.display_items()

    input('\nT7. "Enter" to try to add a third item ' + It5.name + ' to force over-capacity condition ')
    result, message = satchel.add_item(It5)
    print(result, message)

    print('\n\nEnd of Lab#4 test script')
