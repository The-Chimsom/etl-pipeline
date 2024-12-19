from db import  get_db_connection

class LoadData:
    def __init__(self):
        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()  if self.conn else None

    def load_to_db(self, table_name, data):
        if not self.conn:
            print("Database connection is not established")
            return
        try:
            for index, row in data.iterrows():
                placeholders = ", ".join(["%s"] * len(row))
                columns = ", ".join(data.columns)
                query = f"INSERT INTO {table_name} ({columns}) VALUES({placeholders})"

                self.cursor.execute(query, tuple(row))
            self.conn.commit()
            print(f"Inserted {len(data)} rows into {table_name}.")
        except Exception as e:
            print(f"Error inserting data{e}")


    def close_connection(self):
        """Close the database connection."""
        if self.cursor:
            self.cursor.close()
        if self.conn and self.conn.is_connected():
            self.conn.close()
            print("Database connection closed.")