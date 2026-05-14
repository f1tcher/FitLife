"""Программа для расчёта ИМТ и Нормы воды в день"""

WATER_PER_KG = 30  # Константа мл воды на кг
ML_TO_L = 1000  # Константа миллилитров в литре
DASHES_COUNT = 15  # Константа количества прочерков в отчёте

print('Здравствуйте, вы запустили тестовую версию FitLife')


def is_number(user_input):
    """Функция для проверки ввёл ли пользователь число"""
    try:
        user_input = float(user_input)
        return True
    except ValueError:
        return False


user_name = input('Введите пожалуйста ваше имя: ').lower().title()
user_age = input('А теперь возраст (числом): ')
while not is_number(user_age):
    user_age = input('Укажите пожалуйста возраст числом: ')
user_age = int(user_age)


user_weight = input('Введите пожалуйста ваш вес '
                    '(в кг, числом в формате [0.00]): ')
while not is_number(user_weight.replace(',', '.')):
    user_weight = input('Укажите пожалуйста вес числом: ')
user_weight = float(user_weight.replace(',', '.'))

user_height = input('Теперь рост (в метрах, '
                    'числом в формате [0.00]): ')
while not is_number(user_height.replace(',', '.')):
    user_height = input('Укажите пожалуйста рост числом: ')
user_height = float(user_height.replace(',', '.'))


bmi = round(user_weight / (user_height ** 2), 1)
water_ml = user_weight * WATER_PER_KG

water_l = round(water_ml / ML_TO_L, 1)


age_suffix = ('г.' if (user_age % 10 in range(1, 5)
                       and not 11 <= user_age % 100 <= 14)
              else 'л.')

print('-' * DASHES_COUNT, 'Отчёт', '-' * DASHES_COUNT)
print(f'Пользователь: {user_name} ({user_age} {age_suffix})')
print(f'Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l} л. в день')
print()
print('Расчет окончен. Будьте здоровы!')
