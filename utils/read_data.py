import json
import chardet


def read_data_function(file_name):
    """the function reads the file, automatically detects its encoding,
    and then returns its contents as a JSON object"""

    # Open the file in binary mode and read raw data:
    with open(file_name, 'rb') as file:
        raw_data = file.read()

    # Detect the encoding of the file using chardet
    result = chardet.detect(raw_data)
    encoding = result['encoding']

    # Open the file with the detected encoding
    with open(file_name, 'r', encoding=encoding) as file:
        data = json.load(file)
    return data


