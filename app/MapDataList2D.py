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
