# Process an input
# Basic logic to test

# ++++ SCENARIO ++++
# I have a class to operate odd-even checker and exponential (power == 2)
# Because of using clase, always make sure to attach "self." to make unique instances simultaneously
class isOdd():
    def __init__(self, input:int):
        self.input = input
    
    def check_is_odd(self):
        if self.input % 2 == 0:
            return "It is an even number"
        else:
            return "It is an odd number"
    
    def square_power(self, power=2):
        helper_square = self.input ** power
        return helper_square

# ===== CHECK ====
# In current module, is it work
if __name__ == "__main__":
    number_a = isOdd(5)
    if number_a.check_is_odd() != "It is an even number":
        print(False)
    else:
        number_a.square_power()
