import openpyxl

test_prefix = 'C:\\Users\\aazaizh\\PycharmProjects\\RestApiAutomation\\tests_data'


def read_xlsx_file(test_name):
    file_path = f'{test_prefix}\\{test_name}.xlsx'
    try:
        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active
    except Exception as e:
        raise RuntimeError(f'Error loading test data, exception: {str(e)}')
    headers = [cell.value for cell in sheet[1]]
    data = dict()
    for row in sheet.iter_rows(min_row=2, values_only=True):
        row_data = {}
        for header, value in zip(headers, row):
            if value is not None:  # Ignore empty cells
                row_data[header] = value
        test_name = row_data['test_name']
        data[test_name] = row_data

    return data
