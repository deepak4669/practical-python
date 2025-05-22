# bounce.py
#
# Exercise 1.5
curr_height = 100.0 # 100 meters
num_bounces = 0

while num_bounces<10:
    # Bounces
    curr_height = round(0.6*curr_height, 4)
    num_bounces += 1

    print(num_bounces, curr_height)




