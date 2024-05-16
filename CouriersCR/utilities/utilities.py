import csv
from unidecode import unidecode
import os



def get_current_path():
    """
    Get the current OS path where the code is running.

    Returns:
        str: The current OS path.
    """
    return os.getcwd()

# Store the current path in a config file
config_file = '/Users/jorgebarquero/GitRepos/DS-TFM-JL/config.txt'
with open(config_file, 'w') as file:
    file.write(get_current_path())


def normalize_with_accents(data):
    """
    Normalize the given data by removing accents.

    Args:
        data (str): The data to be normalized.

    Returns:
        str: The normalized data.
    """
    return unidecode(data)

def read_csv_file(file_path):
    """
    Read a CSV file and normalize its contents.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        list: A list of lists containing the normalized data from the CSV file.
    """
    normalized_data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            normalized_row = [normalize_with_accents(data) for data in row]
            normalized_data.append(normalized_row)
    return normalized_data

def save_normalized_data(data):    
    output_file = file_path + 'Universidad/normalized/normalized_data.csv'
    #output_file = '/Users/jorgebarquero/GitRepos/DS-TFM-JL/Univ/normalized_data.csv'
    with open(output_file, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(normalized_data)
    print(f"Normalized data saved to {output_file}")


#TODO: pasarlo a un archivo de configuración 



# Estudiantes por cuatrimestre
file_path = get_current_path()
file_name = 'Universidad/raw/estudiantesporcuatrimestre.csv'

normalized_data = read_csv_file(file_path + file_name)

save_normalized_data(normalized_data)

# Save normalized data to a CSV file


print(normalized_data)


