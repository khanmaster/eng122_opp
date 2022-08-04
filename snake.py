# inherit reptile from Reptile class

from reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True

  #  def __use_tongue_to_smell(self):
   #     return "Protected - I can use my tongue to smell food"

    def _use_tongue_to_smell(self):
        try: # if
            return snake_object.__use_tongue_to_smell()

        except AttributeError: # elif  - else
            return "this is information is protected or hidden"

        #return "Protected - I can use my tongue to smell food"

snake_object = Snake()
#print(snake_object._use_tongue_to_smell())
print(snake_object._use_tongue_to_smell())


# exception handling with try: and except blocks


#print(snake_object.eat()) # this function is inherited from Animal
#print(snake_object.seek_heat()) # This function is inherited from Reptile class
#print(snake_object._use_tongue_to_smell())


# what type of errors & exceptions have you seen so far
# syntax error
# indentation Error - value errors - attribute error -



# Try:
    # print()
    # return
# except name_of_error:
#   print()
#   return

# finally:
#    print("better luck next time")














# create 2 more functions one with _ the other one with __
# execute them both - return message should explain Encapsulation break down - public - protected - private