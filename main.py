import json
import csv
# Definition of class 
class DataTable:
    def __init__(self, data_path):
        self.data_path = data_path
        self.item = []
        self.category = []
        self.price = []
        self.load_data()
    def load_data(self):        
        with open(self.data_path, 'r') as file:
            data = json.load(file)
        self.item = [item['item'] for item in data]
        self.category = [item['category'] for item in data]
        self.price = [item['price'] for item in data]
        return data
    def creat_csv(self):
        with open('grocery_list.csv', 'w') as file:
            file.write('item,category,price\n')
            for i in range(len(self.item)):
                file.write(f'{self.item[i]},{self.category[i]},{self.price[i]}\n')
        return 'grocery_list.csv'  
    def add_item(self, item, category, price):
        self.item.append(item)
        self.category.append(category)
        self.price.append(price)
        return self.item, self.category, self.price
data_path = 'grocery_list.json'
# Create DataTable object
table = DataTable(data_path)
print(table.item)
print(table.category)
print(table.price)     
# add new item to grocery_list.json and grocery_list.csv
table.add_item('Banana', 'Fruits', 0.60)
table.creat_csv()
print(table.item)
print(table.category)
print(table.price)