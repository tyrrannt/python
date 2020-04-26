from lesson8 import Warehouse84, OfficeEquipment84

sklad = Warehouse84('Основной склад')
sklad.read('nums.json')
items = OfficeEquipment84('ABS000001', 'Принтеры', 'Kyocera FS-1130 MFP', 'PM0001', '15')
sklad.profit(items.nomenclature, items.profit_wharehouse(), 25)
print(sklad)
items2 = OfficeEquipment84('ABS000002', 'Ноутбук', 'Lenovo Ideapad L340-17IRH Gaming', 'PM0002', '2.78')
sklad.profit(items2.nomenclature, items2.profit_wharehouse(), 5)
print(sklad)
sklad.profit(items.nomenclature, items.profit_wharehouse(), 50)
print(sklad)
sklad.cost(items.nomenclature, items.profit_wharehouse(), 75)
print(sklad)

sklad.save('nums.json')
