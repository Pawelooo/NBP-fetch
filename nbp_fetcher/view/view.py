class View:

    def print_message(self, msg: str):
        print(msg)

    def get_value(self, msg):
        self.print_message(msg)
        return input()
