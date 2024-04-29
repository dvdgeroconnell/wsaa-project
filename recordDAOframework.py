# recordDAOframework.py
#
# Create a DAO framework for development and test purposes.
# This will provide the REST server with a set of stubs to interact with.
#
# David O'Connell
#

# Create the class
class RecordDAO:

    # Get all records         
    def get_all_records(self):
        return [{"id":1,"title":"The Dark Side of the Moon","artist":"Pink Floyd","year":1973,"genre":"Prog"}]
    
    # Find a record by ID
    def find_record_by_id(self, id):
        return {"id":id,"title":"The Dark Side of the Moon","artist":"Pink Floyd","year":1973,"genre":"Prog"}
    
    # Create a record
    def create_record(self, record):
        return(record)
    
    # Update a record with an ID of 'id'
    def update_record(self, id, record):
        return(record)
    
    # Delete a record with an ID of 'id'  
    def delete_record(self, id):
        return True

# Create an instance of the class   
recordDAO = RecordDAO()

# Define a set of tests to execute if this module is run as main 
if __name__ == "__main__":
    record = {"id":1,"title":"The Dark Side of the Moon","artist":"Pink Floyd","year":1973,"genre":"Prog"} 
    print ("test get_all_records()")
    print (f"\t{recordDAO.get_all_records()}")
    print ("test find_record_by_id()")
    print (f"\t{recordDAO.find_record_by_id(1)}")
    print ("test create_record()")
    print (f"\t{recordDAO.create_record(record)}")
    print ("test update_record()")
    print (f"\t{recordDAO.update_record(1,record)}")
    print ("test delete_record()")
    print (f"\t{recordDAO.delete_record(1)}")