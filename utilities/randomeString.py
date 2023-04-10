import random
import string


# random and string are predefined module
def random_string_generator(size=5, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))





# chatgpt random string generator
# # define the length of the random string
# length = 10
#
# # generate a random string of lowercase letters and digits
# random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
#
# # print the random string
# print(random_string)
