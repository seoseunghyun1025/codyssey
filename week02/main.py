# main.py
# 2025-03-19

INPUT_FILE_NAME = 'week02/Mars_Base_Inventory_List.csv'
OUTPUT_FILE_NAME = 'week02/Mars_Base_Inventory_danger.csv'


def get_data_from_csv():
    try:
        with open(INPUT_FILE_NAME, 'r', encoding='utf-8') as file:
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


def filter_flammability_above_0_7(sorted_inventory):
    try:
        filtered_inventory = [
            row for row in sorted_inventory if float(row[4]) >= 0.7
        ]

        return filtered_inventory
    except Exception as e:
        print(f"Error: {e}")
    return []


def save_to_csv(data):
    try:
        with open(OUTPUT_FILE_NAME, 'w', encoding='utf-8') as file:
            header = [
                "Substance",
                "Weight (g/cm³)",
                "Specific Gravity",
                "Strength",
                "Flammability",
            ]
            file.write(','.join(header) + '\n')
            for row in data:
                file.write(','.join(row) + '\n')
        print(f"Data successfully saved to {OUTPUT_FILE_NAME}")
    except Exception as e:
        print(f"Error saving to CSV: {e}")
    return []


if __name__ == '__main__':
    inventory_list = get_data_from_csv()
    print(inventory_list)
    sorted_inventory = get_flammability_values(inventory_list)
    filtered_inventory = filter_flammability_above_0_7(sorted_inventory)
    print(filtered_inventory)
    save_to_csv(filtered_inventory)
