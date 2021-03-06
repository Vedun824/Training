# Как думаете, что делает этот код? Сначала попробуйте в этом разобраться, не вводя код в оболочку Python, а затем проверьте свой ответ.

money = 2000
if money > 1000:
    print("Я богат!")
else:
    print("Я не богат!")
    print("Может, когда-нибудь потом…")

# 1. money = 2000 (переменная и присвоенное ей значение)
# 2-3. if money > 1000 (конструкция if с оператором > проверяющая значение присвоенное переменной money) и при совпадении
# или превышении этого значения выводящая результат указанный в конструкции.
# 4. else: конструкция (ложь) отвечающая за вывод результата при не совпадении проверки значения переменной в конструкции if

# Решение: В задаче результатом вывода будет print("Я богат!")


# Создайте конструкцию if, которая проверяет, соответствует ли заданная в переменной money сумма денег диапазону значений от 100 до 500
# или диапазону значений от 1000 до 5000.

money = 5001
if money == 100:
    print('я не богат')
elif money <= 500:
    print('Я всё же не богат')
elif money == 1000:
    print('я богат!')
elif money <= 5000:
    print('я всё же богат')
else:
    print('Ну чтож я средний класс в рф')
# Создание переменной money
# Использование конструкции if с использованием переменной и оператора == для указанного  стартового значения.
# Использование конструкции elif с использованием переменной и оператора <=  для окончательного значения.
# Решение: Использование конструкций (if-elif) P/s (решение дополнено мной через конструкцию (else) для более развёрнутого выражения.


# Создайте конструкцию if, которая проверяет, действительно ли количество бисквитов (которое задано в переменной twinkies) меньше 100
# или больше 500. Если это условие выполняется, пусть ваша программа
#напечатает сообщение «Слишком мало или слишком много».

twinkeis = 3000
if twinkeis < 100:
    print('Слишком мало')
elif twinkeis > 500:
    print('Слишком много')
# Решение: Практически аналогично варианту выше только в более коротком варианте.

# Создайте конструкцию if, которая печатает строку «Их слишком много», если количество ниндзя (заданное в переменной ninjas) меньше 50,
# печатает «Будет непросто, но я с ними разделаюсь», если это количество
# меньше 30, и печатает «Я одолею этих ниндзя!», если количество меньше 10. Проверьте, как ваш код работает с таким значением:

ninjas = 28
if ninjas < 50 and ninjas >= 30:
    print('Их слишком много')
elif ninjas < 30 and ninjas >= 10:
    print('Будет непросто,но я с ними разделаюсь')
elif ninjas < 10:
    print('Я одолею этих ниндзя')
# Решение присвoение переменной значения,использование  конструкции if с условием and. Попросить гронка дать задач
# c использованием условий and - or так-как практическое применение не сильно раскрыто.





