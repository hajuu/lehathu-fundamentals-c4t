class Print_str:
    string="abc"

    def get_string(self,g):
        self.string=g

    def print_string(self):
        return print(self.string.upper())

str1=Print_str()
str1.get_string(input("enter string: "))
str1.print_string()
