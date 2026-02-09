import json
# Definition of class 
class DataTable:
    def __init__(self, data_path):
        self.data_path = data_path
        self.item = []
        self.category = []
        self.price = []
        if data_path.endswith('.json'):
            self.from_json(data_path)
        elif data_path.endswith('.csv'):
            self.from_csv(data_path)
    def from_json(self, data_path):
        """
        Loads data from a JSON file and populates the instance attributes.

        Args:
            data_path (str): The path to the JSON file.

        Returns:
            list: The data loaded from the JSON file.
        """
        item = []
        category = []
        price = []
        with open(self.data_path, 'r') as file:
            data = json.load(file)
        for row in data:
            self.item.append(row['item'])
            self.category.append(row['category'])
            self.price.append(row['price'])
        return data
    
    def from_csv(self, data_path):
        """
        Loads data from a CSV file and populates the instance attributes.

        Args:
            data_path (str): The path to the CSV file.

        Returns:
            list: The data loaded from the CSV file.
        """
        item = []
        category = []
        price = []
        with open(self.data_path, 'r') as file:
            data = file.readlines()
        for row in data[1:]: 
            item.append(row.split(',')[0])
            category.append(row.split(',')[1])
            price.append(float(row.split(',')[2].strip()))
        self.item = item
        self.category = category
        self.price = price
        return data

# Create DataTable object
data_path = 'grocery_list.csv'
table = DataTable(data_path)

print(table.item)
print(table.category)
print(table.price)