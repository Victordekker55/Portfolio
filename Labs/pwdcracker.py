import time
import random
import string

# Password Cracker

Password = (input("Enter your password: "))

word_pool = string.ascii_lowercase + string.digits
Guess_count = 0
start = time.time()
print("Welcome to the Password Cracker")

while True:
    Guess = ''.join(random.choice(word_pool) for _ in range(len((Password))))
    
    time.sleep(0.0001)
    print("Guess:", Guess)
    Guess_count += 1
    if Guess == Password:
        print("Your password is: " + Guess)
        break
    
    

end = time.time()
print("Guess count:", (Guess_count), " Time taken: {:.2f} seconds".format(end - start))

 