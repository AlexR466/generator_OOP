# import os
import os
import zipfile

from Constants import BYTES_IN_KB, PATH_FOR_ARCHIVES


class Archivator:

    def make_archieve(self, path, file_name):

        with zipfile.ZipFile(path, mode='w') as archive:
            archive.write(file_name)

    def split_archieve(self, arc_name, arc_format, archieve_size):
        number_of_archieve: int = 1
        bytes_in_archieve: int = 0
        with open(f'{PATH_FOR_ARCHIVES}{arc_name}.{arc_format}', 'rb') as src:
            while True:
                output_name = (f'{PATH_FOR_ARCHIVES}{arc_name}'
                               f'{str(number_of_archieve)}.{arc_format}')
                output = open(output_name, 'wb')
                while bytes_in_archieve < (int(archieve_size) * BYTES_IN_KB):
                    data = src.read(int(archieve_size) * BYTES_IN_KB)
                    if data == b'':
                        break
                    output.write(data)
                    bytes_in_archieve += len(data)
                    print('write', len(data), 'bytes to', output_name)
                else:
                    output.close()
                    number_of_archieve += 1
                    bytes_in_archieve = 0
                    continue
                output.close()
                break
        # Удаляем исходный архив
        os.remove(f'{PATH_FOR_ARCHIVES}{arc_name}.{arc_format}')
        # Формируем один архив
        # ТАм где хочется оставить комментарий - делай отдельный метод
        with zipfile.ZipFile(
            f'{PATH_FOR_ARCHIVES}{arc_name}.{arc_format}', mode='w'
        ) as archive:
            for cur in range(1, number_of_archieve+1):
                cur_name = (f'{PATH_FOR_ARCHIVES}{arc_name}{str(cur)}'
                            f'.{arc_format}')
                archive.write(cur_name)
                os.remove(cur_name)
        print('Процесс архивирования завершен.')
