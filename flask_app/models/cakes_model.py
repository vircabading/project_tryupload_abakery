# import the function that will return an instance of a connection ////////
from typing import Dict
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


TARGETDATABASE = 'cake_db'                                       # Designates the database we are using
TABLENAME = "cakes"                                                     # Designates the table we are using

# //// CAKES CLASS ///////////////////////////////////////////////////
class Cakes:
    def __init__( self , data ):                                        # Constructor function
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.specifications = data['specifications']
        self.category = data['category']
        self.img_src = data['img_src']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # //// FLASH ///////////////////////////////////////////////////////////


    # //// CREATE //////////////////////////////////////////////////////////


        
    # //// RETRIEVE /////////////////////////////////////////////////////////

    # **** Get All Class Method *******************************************
    # @Returns: a list of instances of the class
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM " + TABLENAME + ";"
        results = connectToMySQL(TARGETDATABASE).query_db(query)        # Call the connectToMySQL function with the target db
        list_of_instances = []                                          # Initialize an empty list where we can store instances of the class
        for class_instance in results:                                  # Iterate over the db results and create instances of the cls objects
            list_of_instances.append( cls(class_instance) )             # Add each instance of the class to the list of instances
        return list_of_instances

    # **** Get All BY CATEGORY Class Method ****************************
    # @Returns: a list of instances of the class
    @classmethod
    def get_all_by_category(cls, data:dict):
        query = "SELECT * FROM cakes WHERE category = %(category)s;"
        print("in get all by category || query =", query)
        results = connectToMySQL(TARGETDATABASE).query_db(query, data)        # Call the connectToMySQL function with the target db
        list_of_instances = []                                          # Initialize an empty list where we can store instances of the class
        for class_instance in results:                                  # Iterate over the db results and create instances of the cls objects
            list_of_instances.append( cls(class_instance) )             # Add each instance of the class to the list of instances
        return list_of_instances

    # **** Get All BY SEARCH ITEM Class Method ****************************
    # @Returns: a list of instances of the class
    @classmethod
    def get_all_by_search_item(cls, data:dict):
        query = "SELECT * FROM cakes WHERE cakes.name LIKE %(searchitem)s;"
        print("in get all by category || query =", query)
        results = connectToMySQL(TARGETDATABASE).query_db(query, data)        # Call the connectToMySQL function with the target db
        list_of_instances = []                                          # Initialize an empty list where we can store instances of the class
        for class_instance in results:                                  # Iterate over the db results and create instances of the cls objects
            list_of_instances.append( cls(class_instance) )             # Add each instance of the class to the list of instances
        return list_of_instances
    
    # //// UPDATE //////////////////////////////////////////////////////////



    # //// DELETE //////////////////////////////////////////////////////////

