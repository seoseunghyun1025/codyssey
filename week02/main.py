# main.py
# 2025-03-19

FILE_NAME = 'week02/Mars_Base_Inventory_List.csv'


def get_data_from_csv():
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            data = file.read().splitlines()
            return [line.split(',') for line in data]
    except Exception as e:
        print(f"Error: {e}")
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
        print(f"Error: {e}")
    return []


if __name__ == '__main__':
    inventory_list = get_data_from_csv()
    print(inventory_list)
    sorted_inventory = get_flammability_values(inventory_list)
