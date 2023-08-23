import logging

from Constants import (ARC_FORMATS, FILE_FORMATS, PATH_FOR_ARCHIVES,
                       PATH_FOR_FILES)
from func import archive_data, make_fake_data, saver, split

logging.basicConfig(
    format='%(levelname)s - %(module)s - %(asctime)s - %(message)s',
    level=logging.INFO,
    filename='logs/app.log',
)


class Interface:

    def get_input_data_of_file(self):
        logging.info('Получаем данные файла от пользователя.')
        print('Привет, давай сгенерируем файл с данными!')

        self.name_file: str = input('Введи имя генерируемого файла: ')
        if self.name_file == '':
            logging.info('Ошибка! Введено пустое имя файла.')
            raise ValueError('Необходимо ввести название файла.')

        self.format_file: str = input('Введи формат генерируемого файла: ')
        if self.format_file not in FILE_FORMATS:
            logging.info(f'Ошибка! Формата "{self.format_file}" нет в базе.')
            raise KeyError('Такого формата нет в базе')

        self.number_of_strings = input('Введи количество строк данных: ')
        try:
            int(self.number_of_strings)
        except ValueError:
            logging.info('Ошибка! Вместо числа введено:'
                         f' {self.number_of_strings}.')
            raise ValueError('Необходимо ввести целое число')

        self.full_file_name: str = (
            f'{PATH_FOR_FILES}{self.name_file}.{self.format_file}'
            )

    def get_input_data_for_archive(self):
        logging.info('Получаем данные архива от пользователя.')
        print('Теперь создадим архив нашего файла!')
        self.arc_name = input('Введи имя архива или оставь это поле пустым: ')
        if self.arc_name == '':
            self.arc_name = f'archive_of_{self.name_file}'

        self.arc_format = input('Введи формат архива: ')
        if self.arc_format not in ARC_FORMATS:
            logging.info(f'Ошибка! Формата "{self.arc_format}" нет в базе.')
            raise KeyError('Такого формата нет в базе')
        self.archieve_name: str = (
            f'{PATH_FOR_ARCHIVES}{self.arc_name}.{self.arc_format}'
        )

        self.choice_split = input('Разделить архив на тома? yes/no: ')
        if self.choice_split == ('yes'):
            self.archieve_size = input('Введи предельный размер тома архива: ')
            try:
                int(self.archieve_size)
            except ValueError:
                logging.info('Ошибка! Вместо числа введено:'
                             ' {self.archieve_size}.')
                raise ValueError('Необходимо ввести целое число')

    def generate_data(self):
        logging.info('Запуск генератора фейковых данных.')
        self.choice: str = input('Сгенерировать фейковые данные (yes/no)? ')
        if self.choice == 'yes':
            self.data = make_fake_data(self.number_of_strings)
        logging.info('Создание фейковых данных завершено.')
        return self.data

    def save_file(self):
        logging.info('Сохраняем данные в файл.')
        saver(self.format_file, self.full_file_name, self.data)
        logging.info(f'Файл {self.full_file_name} создан.')

    def make_archive(self):
        logging.info(f'Создаем архив файла.{self.full_file_name}.')
        archive_data(self.archieve_name, self.full_file_name)
        logging.info(f'Создан архив {self.archieve_name}.')

    def split_archive(self):
        logging.info(f'Создаем многотомный архив {self.archieve_name}.')
        split(self.arc_name, self.arc_format, self.archieve_size)
        logging.info(f'Создан многотомный архив {self.archieve_name}.')

    def main(self):
        self.get_input_data_of_file()
        self.generate_data()
        self.save_file()
        self.get_input_data_for_archive()
        if self.choice_split == 'yes':
            self.split_archive()
        else:
            self.make_archive()
        logging.info('Работа программы завершена.')


def main():
    Interface().main()


main()
print('done')
