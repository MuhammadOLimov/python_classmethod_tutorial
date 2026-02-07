import json

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
data_path = 'grocery_list.json'
print(DataTable(data_path).load_data())
print(DataTable(data_path).item)
print(DataTable(data_path).category)
print(DataTable(data_path).price)



#     def load_data(self):
#         with open(self.data_path, 'r') as file:
#             data = json.load(file)
#         self.item = [1,2,3]
#         self.category = [2,3,4]
#         self.price = [4,5,6]

#         return data



        


# # Create DataTable object
# data_path = 'grocery_list.json'
# table = DataTable(data_path)
# print(table.data_path)
# print(table.item)
# print(table.category)
# print(table.price)

