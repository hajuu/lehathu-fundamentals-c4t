class Print_str: #chữ đầu tiên phải viết hoa
    string="abc"

    def get_string(self):
        self.string=input("enter string: ")

    def print_string(self):
        print(self.string.upper())

str1=Print_str()
str1.get_string()
str1.print_string()
