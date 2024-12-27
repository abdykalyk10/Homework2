import sqlite3

def work_db():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    while True:
        cursor.execute('SELECT id, title FROM cities')
        cities = cursor.fetchall()

        print('Вы можете отобразить список студентов по выбранному id города из перечня городов ниже,\n'
              'для выхода из программы введите 0:')
        for city in cities:
            print(city)

        user = input("Введите ID города или 0 для выхода: ")

        if user == '0':
            print('Программа завершена!')
            break

        try:
            city_id = int(user)
            cursor.execute('''
                SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
                FROM students
                JOIN cities ON students.city_id = cities.id
                JOIN countries ON cities.country_id = countries.id
                WHERE cities.id = ?
            ''', (city_id,))
            students = cursor.fetchall()

            if students:
                print('Список студентов:')
                for student in students:
                    print(student)
            else:
                print('Нет студента в выбранном городе')
        except ValueError:
            print('Введите корректный ID города')

    conn.close()

work_db()
