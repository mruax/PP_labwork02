name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))
address = input("Введите место вашего проживания: ")
country = input("Введите вашу страну проживания: ")
print(f"Уважаемый {name}!\nНа сегодняшний день Вы проживаете в стране {country}, в городе {address}, "
      f"и вы родились в {2023 - age}.")
