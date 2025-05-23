# main.py
# 2025-03-19

INPUT_FILE_NAME = 'week02/Mars_Base_Inventory_List.csv'
OUTPUT_FILE_NAME_CSV = 'week02/Mars_Base_Inventory_danger.csv'
OUTPUT_FILE_NAME_BIN = 'week02/Mars_Base_Inventory_List.bin'
SUCCESS = f'Data successfully saved to {OUTPUT_FILE_NAME_CSV}'
SEPARATOR = ','

ERROR_MESSAGES = {
    FileNotFoundError: 'File not found >> {}',
    PermissionError: 'Permission denied >> {}',
    Exception: 'Unknown error >> {}',
}


def get_data_from_csv():
    try:
        with open(INPUT_FILE_NAME, 'r', encoding='utf-8') as file:
            data = file.read().splitlines()
            return [line.split(SEPARATOR) for line in data]
    except Exception as e:
        error_message = ERROR_MESSAGES.get(
            type(e), ERROR_MESSAGES[Exception]
        ).format(INPUT_FILE_NAME)
        print(error_message)
    return []


def get_flammability_values(data):
    try:
        header, *content = data
        flammability_index = header.index('Flammability')

        flammability_values = [
            (float(row[flammability_index]), row) for row in content
        ]

        sorted_flammability_values = sorted(
            flammability_values, key=lambda x: x[0], reverse=True
        )

        return [row[1] for row in sorted_flammability_values]
    except Exception as e:
        error_message = ERROR_MESSAGES.get(
            type(e), ERROR_MESSAGES[Exception]
        ).format("Flammability values processing")
        print(error_message)
    return []


def filter_flammability_above_0_7(sorted_inventory):
    try:
        filtered_inventory = [
            row for row in sorted_inventory if float(row[4]) >= 0.7
        ]

        return filtered_inventory
    except Exception as e:
        error_message = ERROR_MESSAGES.get(
            type(e), ERROR_MESSAGES[Exception]
        ).format("Filtering by threshold")
        print(error_message)
    return []


def save_to_csv(data):
    try:
        with open(OUTPUT_FILE_NAME_CSV, 'w', encoding='utf-8') as file:
            header = [
                'Substance',
                'Weight (g/cm³)',
                'Specific Gravity',
                'Strength',
                'Flammability',
            ]
            file.write(SEPARATOR.join(header) + '\n')
            for row in data:
                file.write(SEPARATOR.join(row) + '\n')
    except Exception as e:
        error_message = ERROR_MESSAGES.get(
            type(e), ERROR_MESSAGES[Exception]
        ).format(OUTPUT_FILE_NAME_CSV)
        print(error_message)


def save_to_binary_file(data):
    try:
        with open(OUTPUT_FILE_NAME_BIN, 'wb') as file:
            for row in data:
                row_data = ','.join(row)
                row_bytes = row_data.encode('utf-8')
                length = len(row_bytes)

                file.write(length.to_bytes(4, 'big'))
                file.write(row_bytes)
        print(SUCCESS)
    except Exception as e:
        error_message = ERROR_MESSAGES.get(
            type(e), ERROR_MESSAGES[Exception]
        ).format(OUTPUT_FILE_NAME_BIN)
        print(error_message)
    return []


def print_from_binary_file():
    try:
        with open(OUTPUT_FILE_NAME_BIN, 'rb') as file:
            while True:
                length_bytes = file.read(4)
                if not length_bytes:
                    break

                length = int.from_bytes(length_bytes, 'big')
                row_bytes = file.read(length)
                row_data = row_bytes.decode('utf-8')

                print(row_data)
    except Exception as e:
        error_message = ERROR_MESSAGES.get(
            type(e), ERROR_MESSAGES[Exception]
        ).format(OUTPUT_FILE_NAME_BIN)
        print(error_message)
    return []


if __name__ == '__main__':
    inventory_list = get_data_from_csv()
    print(inventory_list)
    sorted_inventory = get_flammability_values(inventory_list)
    filtered_inventory = filter_flammability_above_0_7(sorted_inventory)
    print(filtered_inventory)
    save_to_csv(filtered_inventory)
    save_to_binary_file(filtered_inventory)
    print_from_binary_file()
