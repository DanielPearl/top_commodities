class MapDataStructure:

    def __init__(self, headers):
        self.header = headers
        self.rows = []

    def add_row(self, row):
        if len(row) == len(self.header):
            self.rows.append(row)
        #else

    def generate_data(self):
        result = []
        result.append(self.header)
        for row in self.rows:
            result.append(row)
        return result
