stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 1}
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print('- ' + str(k) + ': ' + str(v))
        item_total += v
    print('Total number of items: ' + str(item_total))

def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] in inventory:
            inventory[addedItems[i]] = inventory[addedItems[i]] + 1 # +1 of the same items
        else:
            inventory.setdefault(addedItems[i], 1) # new items set to 1
    return inventory # adds to the inventory

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)