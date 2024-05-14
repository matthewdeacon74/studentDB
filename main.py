# create student lists
names = ['Larry', 'Curly', 'Moe', 'Homer', 'Harry', 'Hermione', 'Ron']
home_towns = ["Porcupine Crest", "Nyuknyuk", "Wyiota", "Springfield", "Godric's Hollow", "London", "The Burrow"]
favorite_food = ['pizza', 'cheeseburgers', 'steak', 'beer', 'chocolate frogs', 'lasagne', 'corned beef sandwiches']

valid_id = False
while valid_id == False:
    student_query=int(input(f'Which student ID number do you wish to look up (1-{len(names)}]? '))
    student_index = 0
    if student_query <= len(names) and student_query > 0:
        valid_id = True
        student_index = student_query - 1
        print(f'Student {student_query} is named {names[student_index]}')
    else:
        print("That's not a valid ID.")

# with valid ID, prompt for food or hometown
valid_category = False
while valid_category == False:
    category = input("Would you like the student's Home Town ('h') or Favorite Food ('f')? ").lower()
    if category == 'h' or category == 'f':
        valid_category = True
    else:
        print("That's not a valid search type. 'f' or 'h' only, please.")

if category == 'h':
    print(f"{names[student_index]}'s home town is {home_towns[student_index]}")
if category == 'f':
    print(f"{names[student_index]}'s favorite food is {favorite_food[student_index]}")
