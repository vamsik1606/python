print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))

if height >= 120:

  print("You can ride the rollercoaster!")

  age = int(input("How old are you? "))

  if 12 <= age <= 18:

    print("Your ticket costs $7!")

  elif age < 12:

    print("Your ticket costs $5!")

  else:

    print("Your ticket costs $12!")

else:

    print("Sorry, you can't ride the rollercoaster for now!")