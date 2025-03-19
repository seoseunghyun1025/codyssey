# main.py
# 2025-03-19

FILE_NAME = 'Mars_Base_Inventory_List.csv'


def get_data_from_csv():
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            return file.read().splitlines()

    except Exception as e:
        print(e)

    return []


if __name__ == '__main__':
    inventory_list = get_data_from_csv()
    print(inventory_list)
