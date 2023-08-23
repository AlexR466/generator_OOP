from faker import Faker

from Archivator import Archivator
from Saver import SaverCSV, SaverXLSX


def make_fake_data(number_of_strings):
    data = []
    fake = Faker("ru_RU")
    for row in range(int(number_of_strings)):
        new_row = [fake.name(),
                   fake.city(),
                   fake.street_address(),
                   fake.postcode(),
                   fake.job(),
                   fake.phone_number(),
                   fake.hostname(),
                   fake.ascii_free_email(),
                   fake.uri(),
                   fake.company(),
                   fake.city()]
        data.append(new_row)
    print('Фейковые данные созданы')
    return data


def saver(format_file: str, path: str, data: list):
    # лучше отдельным классом
    if format_file == 'xlsx':
        SaverXLSX().save_to_file(path, data)
    elif format_file == 'csv':
        SaverCSV().save_to_file(path, data)


def archive_data(path, file_name):
    Archivator().make_archieve(path, file_name)


def split(arc_name, arc_format, archieve_size):
    Archivator().split_archieve(arc_name, arc_format, archieve_size)
