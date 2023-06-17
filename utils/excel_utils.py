import openpyxl

from utils import helper

def read_xlsx_file(test_name):
    config = helper.read_config()
    if not config:
        return
    TESTS = config["TESTS"]
    test_data = TESTS['test_data']
    file_path = f'{test_data}{test_name}.xlsx'

    try:
        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active
    except Exception as e:
        raise RuntimeError(f'Error loading test data, exception: {str(e)}')
    headers = [cell.value for cell in sheet[1] if cell.value is not None]
    data = dict()
    for row in sheet.iter_rows(min_row=2, values_only=True):
        row_data = {}
        for header, value in zip(headers, row):
            if value is not None:  # Ignore empty cells
                row_data[header] = value
        if 'test_name' in row_data.keys():
            test_name = row_data['test_name']
            data[test_name] = row_data

    return data
