import csv

import xlsxwriter as ex


class Saver:
    pass


class SaverXLSX(Saver):

    def save_to_file(self, path, data):
        workbook = ex.Workbook(path)
        worksheet = workbook.add_worksheet()
        row = 0
        for list in data:
            worksheet.write_row(row, 0, list)
            row += 1
        workbook.close()
        print(f'Файл {path} создан')


class SaverCSV(Saver):
    def save_to_file(self, path, data):
        with open(path, 'w') as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerow(row)
        print(f'Файл {path} создан')
