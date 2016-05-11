class MapDataStructure:

    def __init__(self):
        self.rows = []

    def add_row(self, row):
        self.rows.append(row)

    def generate_js_list(self):
        result = []
        for row in self.rows:
            result.append(row)
        return result

    def generate_dict(self, country, item, year):
        temp_dict = {}
        temp_dict["country"] = country
        temp_dict["item"] = item
        temp_dict["year"] = year
        return temp_dict

    def generate_choices(self, query):
        pass
