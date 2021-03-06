import sys
import os
from datetime import datetime
import random
from functools import partial
from pygame import mixer
from tkinter import *


class FastNumbers:
    def __init__(self):
        """Инициализация переменных, подготовка к запуску приложения."""
        root.title('Быстрые цифры')
        root.resizable(width=False, height=False)
        mixer.init()

        # Получение пути для сохранения данных о прогрессе
        path = os.path.dirname(os.getenv('APPDATA')) + '\\Local\\FastNumbers'
        try:
            os.mkdir(path)
        except OSError:
            pass
        self.info_path = path + '\\info.txt'

        # Запись данных о прогрессе при запуске игры в первый раз
        if not os.path.isfile(self.info_path):
            with open(self.info_path, 'w', encoding='utf-8') as f:
                f.write('coins = 300\n')
                f.write('record_super_easy = 9:99:99.999999\n')
                f.write('record_easy = 9:99:99.999999\n')
                f.write('record_medium = 9:99:99.999999\n')
                f.write('record_hard = 9:99:99.999999\n')
                f.write('record_super_hard = 9:99:99.999999\n')
                f.write('theme_num = black\n')
                f.write('theme_bg = white\n')
                f.write('theme1 = Выбрано\n')
                f.write('theme2 = Купить!\n')
                f.write('theme3 = Купить!\n')
                f.write('theme4 = Купить!\n')
                f.write('theme5 = Купить!\n')
                f.write('theme6 = Купить!\n')

        # Считывание данных о прогрессе
        info_list = []
        with open(self.info_path, 'r', encoding='utf-8') as f:
            for line in f:
                info_list.append(line.strip().split(' = '))
        self.coins = int(info_list[0][1])
        self.record_super_easy = info_list[1][1]
        self.record_easy = info_list[2][1]
        self.record_medium = info_list[3][1]
        self.record_hard = info_list[4][1]
        self.record_super_hard = info_list[5][1]
        self.theme_num = info_list[6][1]
        self.theme_bg = info_list[7][1]
        self.theme1 = info_list[8][1]
        self.theme2 = info_list[9][1]
        self.theme3 = info_list[10][1]
        self.theme4 = info_list[11][1]
        self.theme5 = info_list[12][1]
        self.theme6 = info_list[13][1]

        # Инициализация изображений
        self.bg_img = PhotoImage(file=self.resource_path('img\\bg_img.gif'))
        self.img1 = PhotoImage(file=self.resource_path('img\\theme1.gif'))
        self.img2 = PhotoImage(file=self.resource_path('img\\theme2.gif'))
        self.img3 = PhotoImage(file=self.resource_path('img\\theme3.gif'))
        self.img4 = PhotoImage(file=self.resource_path('img\\theme4.gif'))
        self.img5 = PhotoImage(file=self.resource_path('img\\theme5.gif'))
        self.img6 = PhotoImage(file=self.resource_path('img\\theme6.gif'))

    def resource_path(self, relative_path):
        """Возвращает путь к файлу."""
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath('.')
        return os.path.join(base_path, 'resourсes', relative_path)

    def save_info(self):
        """Сохраняет информацию о прогрессе."""
        with open(self.info_path, 'w', encoding='utf-8') as f:
            f.write(f'coins = {self.coins}\n')
            f.write(f'record_super_easy = {self.record_super_easy}\n')
            f.write(f'record_easy = {self.record_easy}\n')
            f.write(f'record_medium = {self.record_medium}\n')
            f.write(f'record_hard = {self.record_hard}\n')
            f.write(f'record_super_hard = {self.record_super_hard}\n')
            f.write(f'theme_num = {self.theme_num}\n')
            f.write(f'theme_bg = {self.theme_bg}\n')
            f.write(f'theme1 = {self.theme1}\n')
            f.write(f'theme2 = {self.theme2}\n')
            f.write(f'theme3 = {self.theme3}\n')
            f.write(f'theme4 = {self.theme4}\n')
            f.write(f'theme5 = {self.theme5}\n')
            f.write(f'theme6 = {self.theme6}\n')

    def clear(self):
        """Очищает экран, удаляя все виджеты."""
        for i in root.pack_slaves():
            i.destroy()
        for i in root.grid_slaves():
            i.destroy()

    def play_sound(self, filename):
        """Воспроизводит звуковой файл."""
        mixer.music.load(self.resource_path('sounds\\' + filename))
        mixer.music.play()

    def MAIN(self):
        """Создает главнй экран приложения."""
        root.title('Быстрые цифры')
        self.clear()

        Label(image=self.bg_img).grid(row=0, column=0, rowspan=7)
        Button(text='Играть!', font='arial 20', bg='orange', command=self.GAME_SETTINGS).grid(row=0, column=0, rowspan=7)
        Button(text='Магазин', width=8, font='arial 20', bg='blue', fg='white', command=self.STORE).grid(row=2, column=1)
        Button(text='Рекорды', width=8, font='arial 20', bg='blue', fg='white', command=self.RECORDS).grid(row=3, column=1)
        Button(text='Титры', width=8, font='arial 20', bg='blue', fg='white', command=self.CREDITS).grid(row=4, column=1)

    def CREDITS(self):
        """Создает окно с титрами."""
        root.title('Титры')
        self.clear()

        Label(text='Автор идеи, дизайнер и программист:\nМуратов Михаил Александрович',
              font='arial 16', justify='left').pack()
        Button(text='Вернуться', font='arial 12', bg='grey', command=self.MAIN).pack()

    def RECORDS(self):
        """Создает окно с рекордами."""
        root.title('Рекорды')
        self.clear()

        bad = '9:99:99.999999'
        Label(text=f'Очень легко: {self.record_super_easy if self.record_super_easy != bad else "нет"}\n' +
                   f'Легко: {self.record_easy if self.record_easy != bad else "нет"}\n' +
                   f'Средне: {self.record_medium if self.record_medium != bad else "нет"}\n' +
                   f'Сложно: {self.record_hard if self.record_hard != bad else "нет"}\n' +
                   f'Очень сложно: {self.record_super_hard if self.record_super_hard != bad else "нет"}',
              font='arial 16', justify='left').pack()
        Button(text='Вернуться', font='arial 12', bg='grey', command=self.MAIN).pack()

    def STORE(self):
        """Создает окно с магазином.
        Магазин предназначен для покупки цветовых схем игрового поля.

        """
        def buy_themes(i):
            """Осуществляет покупку игровой темы."""
            themes = [row[2] for row in themes_list[1:]]
            thms = [self.theme1, self.theme2, self.theme3, self.theme4, self.theme5, self.theme6]
            if (themes[i]['text'] == 'Купить!' and self.coins >= 500) or themes[i]['text'] == 'Куплено':
                if themes[i]['text'] == 'Купить!':
                    self.coins -= 500
                    balance['text'] = f'Ваш баланс: {self.coins}'
                themes[i]['text'] = 'Выбрано'
                themes[i]['bg'] = 'yellow'
                thms[i] = 'Выбрано'
                self.theme_num = colors[i][0]
                self.theme_bg = colors[i][1]
                p = -1
                for j in themes[:i] + themes[i+1:]:
                    p += (2 if p == i else 1)
                    if j['text'] == 'Выбрано':
                        j['text'] = 'Куплено'
                        j['bg'] = 'grey'
                        thms[p] = 'Куплено'
                self.theme1, self.theme2, self.theme3, self.theme4, self.theme5, self.theme6 = thms
            self.save_info()

        root.title('Магазин')
        self.clear()

        balance = Label(text=f'Ваш баланс: {self.coins}', font='arial 14', bg='grey')
        balance.grid(row=0, column=0, sticky='nw')
        Button(text='Вернуться', font='arial 12', bg='grey', command=self.MAIN).grid(row=0, column=1, sticky='ne')
        Label(text='МАГАЗИН', font='arial 20', fg='yellow', bg='blue').grid(row=1, column=0, columnspan=2)
        frame1 = Frame(root, bg='black', bd=5)
        frame2 = Frame(root, bg='black', bd=5)
        frame1.grid(row=2, column=0)
        frame2.grid(row=2, column=1)

        # Создание списка виджетов с данными об объектах покупки
        themes_list = [None]
        themes_names = [None, self.theme1, self.theme2, self.theme3, self.theme4, self.theme5, self.theme6]
        img_names = [None, self.img1, self.img2, self.img3, self.img4, self.img5, self.img6]
        colors = [['black', 'white'], ['white', 'blue'], ['yellow', 'purple'], ['yellow', 'green'], ['green', 'beige'], ['orange', 'black']]
        for i in range(1, 7):
            theme, img = themes_names[i], img_names[i]
            themes_list.append([Label(frame1 if i < 4 else frame2, bg='black', fg='orange', justify='left', font='arial 12',
                                      text=f'{i}. Тема №{i}\n' + ('Тема по умолчанию     ' if i == 1 else 'Стоимость: 500 монет')),
                                Label(frame1 if i < 4 else frame2, image=img),
                                Button(frame1 if i < 4 else frame2, text=theme, command=partial(buy_themes, i-1),
                                       bg=('yellow' if theme == 'Выбрано' else ('grey' if theme == 'Куплено' else 'white')))])
            for j in themes_list[i]:
                j.pack()

    def GAME_SETTINGS(self):
        """Создает окно с выбором параметров игры."""
        def choice_seq(sequence):
            nonlocal seq

            seq = sequence
            if seq == 1:
                p1['bg'], p2['bg'] = 'yellow', 'white'
            else:
                p1['bg'], p2['bg'] = 'white', 'yellow'
            for i in root.grid_slaves():
                i['state'] = NORMAL

        root.title('Настройки игрового режима')
        self.clear()

        seq = 1
        Label(text='Выбирите порядок чисел: ', font='arial 20').grid(row=0, column=0, columnspan=5)
        p1 = Button(text='Обычный', font='arial 16', command=lambda: choice_seq(1))
        p2 = Button(text='Обратный', font='arial 16', command=lambda: choice_seq(-1))
        p1.grid(row=1, column=0)
        p2.grid(row=1, column=1)
        Label(text='Выбирите режим игры: ', font='arial 20').grid(row=2, column=0, columnspan=5)
        Button(text='Очень легко', width=11, font='arial 16', state=DISABLED, command=lambda: self.GAME('очень легко', seq)).grid(row=3, column=0)
        Button(text='Легко', width=11, font='arial 16', state=DISABLED, command=lambda: self.GAME('легко', seq)).grid(row=3, column=1)
        Button(text='Средне', width=11, font='arial 16', state=DISABLED, command=lambda: self.GAME('средне', seq)).grid(row=3, column=2)
        Button(text='Сложно', width=11, font='arial 16', state=DISABLED, command=lambda: self.GAME('сложно', seq)).grid(row=3, column=3)
        Button(text='Очень сложно', width=11, font='arial 16', state=DISABLED, command=lambda: self.GAME('очень сложно', seq)).grid(row=3, column=4)
        Label(text='Правила игры:', font='arial 20').grid(row=4, column=0, columnspan=5)
        Label(text='В игре вы будите последовательно нажимать на цифры,\n'
                   'разбросанные по полю в случайном порядке.\n'
                   'Над полем будет показана цифра, которую нужно найти.\n'
                   'Дойдите до последнего числа как можно быстрее,\n'
                   'чтобы набрать больше монет.'
                   '\nУдачной игры!',
              font='arial 16').grid(row=5, column=0, columnspan=5)

    def GAME(self, type, seq):
        """Создает окно с игровым полем, осуществляет игровой процесс.

        Аргументы:
          type - сложность игры (от "очень легко" до "очень сложно")
          seq - последовательность чисел (1 - прямая, -1 - обратная)

        """
        def play_again():
            """Запускает новую игру, сохраняя изначальные параметры."""
            if type == 'очень легко':
                self.record_super_easy = record
            elif type == 'легко':
                self.record_easy = record
            elif type == 'средне':
                self.record_medium = record
            elif type == 'сложно':
                self.record_hard = record
            else:
                self.record_super_hard = record
            self.GAME(type, seq)

        def create_matrix():
            """Создает матрицу со случайно перемешанными числами."""
            random.shuffle(numbers)
            k = 0
            for i in range(matrix_size):
                matrix.append([])
                for j in range(matrix_size):
                    matrix[i].append(numbers[k])
                    k += 1

            # Отображение чисел на игровом поле
            for i in range(matrix_size):
                for j in range(matrix_size):
                    x1 = i * cell_size + 2
                    x2 = j * cell_size + 2
                    y1 = x1 + cell_size
                    y2 = x2 + cell_size
                    field.create_rectangle(x1, x2, y1, y2)
                    field.create_text(x1 + cell_size / 2, x2 + cell_size / 2,
                                      text=str(matrix[i][j]),
                                      fill=self.theme_num,
                                      font='arial 32' if type == 'очень легко' else ('arial 24' if type == 'легко' else 'arial 16'))

        def win():
            """Создает окно с информациее о победе."""
            nonlocal score, record

            game_time = datetime.now() - start_time
            root.title('Результаты')
            self.clear()
            self.play_sound('win.mp3')

            score = str(game_time)
            if score < record:
                record = score
            self.coins += current_coins

            results_widget['text'] = 'Победа!\n' + \
                                     f'Ошибки: {errors}\n' + \
                                     f'Итоговое время: {score}\n' + \
                                     f'Рекордное время ({type}): {record}\n' + \
                                     f'+{current_coins} монет\n'
            results_widget.pack()
            play_again_widget.pack()
            Button(text='Выход', bg='grey', font='arial 24', command=self.MAIN).pack()

            if type == 'очень легко':
                self.record_super_easy = record
            elif type == 'легко':
                self.record_easy = record
            elif type == 'средне':
                self.record_medium = record
            elif type == 'сложно':
                self.record_hard = record
            else:
                self.record_super_hard = record
            self.save_info()

        def click(event):
            """Обрабатывает нажатия по игровому полю."""
            nonlocal next_num, score, record, errors, current_coins

            self.play_sound('click.mp3')

            x, y = event.x, event.y
            i, j = x // cell_size, y // cell_size

            if matrix[i][j] == next_num:
                if type == 'легко':
                    x1 = i * cell_size + 2
                    x2 = j * cell_size + 2
                    y1 = x1 + cell_size
                    y2 = x2 + cell_size
                    field.create_rectangle(x1, x2, y1, y2, fill=self.theme_bg)
                next_num += seq
                current_coins += 2
                if (matrix[i][j] == matrix_size ** 2) if seq == 1 else (matrix[i][j] == 1):
                    win()
                else:
                    next_num_widget['text'] = f'Следующее число: {next_num}'
            elif not ((matrix[i][j] < next_num) if seq == 1 else (matrix[i][j] > next_num)):
                self.play_sound('err.wav')
                errors += 1
                # current_coins -= 2

        def run_timer():
            """Отображает игровое время."""
            time = str(datetime.now() - start_time)[:-7]
            if time:
                timer['text'] = f'Время: {time}'
            root.after(1000, run_timer)

        root.title('Игра: ' + type)
        self.clear()

        # Инициализация переменных, необходимых для игры
        if type == 'очень легко':
            record = self.record_super_easy
            matrix_size = 5
        elif type == 'легко':
            record = self.record_easy
            matrix_size = 7
        elif type == 'средне':
            record = self.record_medium
            matrix_size = 10
        elif type == 'сложно':
            record = self.record_hard
            matrix_size = 12
        else:
            record = self.record_super_hard
            matrix_size = 15
        cell_size = 80 if type == 'очень легко' else (60 if type == 'легко' else 40)#40
        field_size = cell_size * matrix_size
        matrix = []
        numbers = list(range(1, (matrix_size ** 2) + 1))
        next_num = 1 if seq == 1 else matrix_size * matrix_size
        score = '9:99:99.999999'
        current_coins, errors = 0, 0

        Button(text='Выход', bg='grey', font='arial 24', command=self.MAIN).grid(row=0, column=0)
        timer = Label(text='Время: 0:00:00', bg='grey', font='arial 24')
        timer.grid(row=0, column=1)
        next_num_widget = Label(text=f'Следующее число: {next_num}', font='arial 20')
        next_num_widget.grid(row=1, column=0, columnspan=2)
        field = Canvas(root, width=field_size + 1, height=field_size + 1, bg=self.theme_bg)
        field.grid(row=2, column=0, columnspan=2)
        results_widget = Label(text='', font='arial 20')
        play_again_widget = Button(text='Играть снова', bg='red', font='arial 24', command=play_again)

        create_matrix()
        start_time = datetime.now()
        run_timer()
        field.bind('<1>', click)


root = Tk()
game = FastNumbers()
game.MAIN()
root.mainloop()
