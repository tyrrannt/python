#Задания 8.4 и 8.5 и 8.6 объединены в один

from lesson8 import Warehouse84, OfficeEquipment84

sklad = Warehouse84('Основной склад')
sklad.read('nums.json')
items = OfficeEquipment84('ABS000003', 'Сканер', 'HP ScanJet Pro 3500 f1', 'SM0001', '5.58')
sklad.profit(items.nom, items.profit_wharehouse(), 25)
print(sklad)
items2 = OfficeEquipment84('ABS000004', 'Проектор', 'Sony VPL-VW270ES', 'PP0002', '14')
sklad.profit(items2.nom, items2.profit_wharehouse(), 25)
print(sklad)
sklad.profit(items.nom, items.profit_wharehouse(), 5)
print(sklad)
sklad.cost(items.nom, items.profit_wharehouse(), 80)
print(sklad)
sklad.cost(items2.nom, items.profit_wharehouse(), 5)
print(sklad)

sklad.save('nums.json')
