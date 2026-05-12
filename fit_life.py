# 1. Знакомство
print('Здравствуйте, вы запустили тестовую версию FitLife')  # Приветствие


def is_number(user_input):
    """Создал функцию для проверки ввёл ли пользователь число"""
    try:
        user_input = float(user_input)
        return True
    except ValueError:
        return False


# Запрашиваю имя пользователя и привожу к нижнему регистру
user_name = input('Введите пожалуйста ваше имя: ').lower()
user_age = input('А теперь возраст (числом): ')  # Запрашиваю возраст
# И проверяю, ввёл ли пользователь число, иначе прошу ввести числом
while not is_number(user_age):
    user_age = input('Укажите пожалуйста возраст числом: ')
user_age = int(user_age)

# 2. Сбор данных
user_weight = input('Введите пожалуйста ваш вес '
                    '(в кг, числом в формате [0.00]): ')  # Запрашиваю вес
while not is_number(user_weight):
    user_weight = input('Укажите пожалуйста вес числом: ')
user_weight = float(user_weight)

user_height = input('Теперь рост (в метрах, '
                    'числом в формате [0.00]): ')  # Запрашиваю рост
while not is_number(user_height):
    user_height = input('Укажите пожалуйста рост числом: ')
user_height = float(user_height)

# 3. Логика расчетов
WATER_PER_KG = 30  # Константа мл воды на кг
ML_TO_L = 1000  # Константа миллилитров в литре

# Рассчитываю ИМТ и норму воды по формулам
bmi = round(user_weight / (user_height ** 2), 1)
water_ml = user_weight * WATER_PER_KG

# Привожу мл в л для более понятного вывода
water_l = round(water_ml / ML_TO_L, 1)

# 4. Вывод красивого результата
# Добавил проверку возраста, чтобы указать правильный суффикс
age_suffix = ('г.' if (user_age % 10 in range(1, 5)
                       and not 11 <= user_age % 100 <= 14)
              else 'л.')

print('-' * 15, 'Отчёт', '-' * 15)
print(f'Пользователь: {user_name.title()} ({user_age} {age_suffix})')
print(f'Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l} л. в день')
print()
print('Расчет окончен. Будьте здоровы!')
