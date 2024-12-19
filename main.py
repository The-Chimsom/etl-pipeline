from file_extraction_service import  Extraction
from load_data import LoadData
from transform_data import TransformData

def main():
    file_path = "employee_data.csv"
    table_name  = "employees"

    extractor = Extraction(file_path)
    transformed_data = TransformData(extractor.data)
    if extractor is not None:
        print("Data extraction successful")

        loader = LoadData()
        try:
            loader.load_to_db(table_name, transformed_data.extracted_data)
        finally:
            loader.close_connection()
    else:
        print("ETL pipeline failure")

if __name__ == "__main__":
    main()
