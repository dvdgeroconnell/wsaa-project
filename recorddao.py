# recordDAOframework.py
#
# Create a DAO framework for development and test purposes.
# This will provide the REST server with a set of stubs to interact with.
#
# David O'Connell
#

import mysql.connector
from mysql.connector import cursor
import mysqldbcfg as cfg

# Create the class
class RecordDAO:
    connection = ''
    cursor =     ''
    host =       ''
    user =       ''
    password =   ''
    database =   ''

    def __init__(self):
        self.host=cfg.mysqldb['host']
        self.user=cfg.mysqldb['user']
        self.password=cfg.mysqldb['password']
        self.database=cfg.mysqldb['database']

    def get_cursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def close_all(self):
        self.connection.close()
        self.cursor.close()
    
    # Get all records         
    def get_all_records(self):    
        cursor = self.get_cursor()
        sql_string="select * from records"
        cursor.execute(sql_string)
        results = cursor.fetchall()
        # returnArray = []
        for result in results:
            # This is temporary
            pass
            # print(result)
            # Taking out the convert to dictionary for now
            # returnArray.append(self.convertToDictionary(result))

        self.close_all()
        # return returnArray
        return(results)

    
    # Find a record by ID
    def find_record_by_id(self, id):
        cursor = self.get_cursor()
        print("retrieving record id =", id)
        sql_string="select * from records where id = %s"
        values = (id,)
        cursor.execute(sql_string, values)
        result = cursor.fetchone()
        #returnvalue = self.convertToDictionary(result)
        self.close_all()
        # return returnvalue
        return result
        

    # Create a record
    def create_record(self, record):

        cursor = self.get_cursor()
        sql_string="insert into records (title, artist, year, genre) values (%s,%s,%s,%s)"
        values = (record.get("title"), record.get("artist"), record.get("year"), record.get("genre"))
        cursor.execute(sql_string, values)

        self.connection.commit()
        new_id = cursor.lastrowid
        record["id"] = new_id
        self.close_all()
        return record


    # Update a record with an ID of 'id'
    def update_record(self, id, record):
        cursor = self.get_cursor()
        sql_string="update records set title= %s,artist=%s, year=%s, genre=%s where id = %s"
        print(type(record))
        values = (record.get("title"), record.get("artist"), record.get("year"), record.get("genre"),id)
        cursor.execute(sql_string, values)
        self.connection.commit()
        self.close_all()
        return(record)
    

    # Delete a record with an ID of 'id'  
    def delete_record(self, id):
        cursor = self.get_cursor()
        sql_string="delete from records where id = %s"
        values = (id,)
        cursor.execute(sql_string, values)
        self.connection.commit()
        self.close_all()
        print("Deleted record", id)

        return True

# Create an instance of the class   
recordDAO = RecordDAO()

# Define a set of tests to execute if this module is run as main 
if __name__ == "__main__":
    record = {"title":"London Calling","artist":"The Clash","year":1979,"genre":"Punk Rock"}
    record2 = {"title":"Foxtrot","artist":"Genesis","year":1973,"genre":"Prog Rock"} 

    print ("test get_all_records()")
    print (f"\t{recordDAO.get_all_records()}")
    print ("test find_record_by_id()")
    print (f"\t{recordDAO.find_record_by_id(2)}")
    print ("test create_record()")
    print (f"\t{recordDAO.create_record(record)}")
    print ("test update_record()")
    print (f"\t{recordDAO.update_record(1,record2)}")
    print ("test delete_record()")
    print (f"\t{recordDAO.delete_record(1)}")