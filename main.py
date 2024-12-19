from file_extraction_service import  Extraction
from load_data import LoadData

def main():
    file_path = "employee_data.csv"
    table_name  = "employees"

    extractor = Extraction(file_path)
    if extractor is not None:
        print("Data extraction successful")

        loader = LoadData()
        try:
            loader.load_to_db(table_name, extractor.data)
        finally:
            loader.close_connection()
    else:
        print("ETL pipeline failure")

if __name__ == "__main__":
    main()
