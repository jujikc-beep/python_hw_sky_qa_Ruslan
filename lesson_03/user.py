class User:
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name

        def get_first_name(self):
            return self.first_name
        def get_last_name(self):
            return self.last_name
        def get_full_name(self):
            return self.first_name + " " + self.last_name

        def get_first_name1(self):
            print(self.first_name)
        def get_last_name1(self):
            print(self.last_name)
        def get_full_name1(self):
            print(f"{self.first_name} {self.last_name}")

            # Просто для себя двумя способами, ввернуть и напечать