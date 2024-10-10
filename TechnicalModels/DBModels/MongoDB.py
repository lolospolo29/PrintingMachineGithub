from pymongo import MongoClient
from bson.objectid import ObjectId

from Interfaces.IDBService import IDBService


class DBService(IDBService):
    def __init__(self, db_name, uri):
        """
        Initialize the DbService with a MongoDB URI and database name.
        """
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def add(self, collection_name, data):
        # """
        # Add a new document to a collection.
        # param collection_name: The name of the collection.
        # param data: A dictionary representing the document to insert.
        # :return: The inserted document's ID.
        # """
        collection = self.db[collection_name]
        result = collection.insert_one(data)
        return str(result.inserted_id)

    def get(self, collection_name, document_id):
        """
        Retrieve a document by its ID.
        param collection_name: The name of the collection.
        param document_id: The document's unique ID (as a string).
        return: The document, or None if not found.
        """
        collection = self.db[collection_name]
        return collection.find_one({"_id": ObjectId(document_id)})

    def update(self, collection_name, document_id, updates):
        # """
        # Update an existing document in a collection.
        # param collection_name: The name of the collection.
        # param document_id: The document's unique ID (as a string).
        # param updates: A dictionary with the fields to update.
        # return: True if the update was successful, False otherwise.
        # """
        collection = self.db[collection_name]
        result = collection.update_one({"_id": ObjectId(document_id)}, {"$set": updates})
        return result.modified_count > 0

    def delete(self, collection_name, document_id):
        """
        Delete a document by its ID.
        param collection_name: The name of the collection.
        param document_id: The document's unique ID (as a string).
        return: True if the deletion was successful, False otherwise.
        """
        collection = self.db[collection_name]
        result = collection.delete_one({"_id": ObjectId(document_id)})
        return result.deleted_count > 0

    def deleteByQuery(self, collection_name, query):
        documents = self.find(collection_name, query)
        deleted_ids = []

        for document in documents:
            document_id = str(document['_id'])
            if self.delete(collection_name, document_id):
                deleted_ids.append(document_id)

    def delete_all(self, collection_name):
        """
        Delete all documents in the specified collection.

        param collection_name: The name of the collection.
        return: The number of documents deleted.
        """
        collection = self.db[collection_name]
        result = collection.delete_many({})

        # Return the count of deleted documents
        return result.deleted_count

    def find(self, collection_name, query):
        """
        Find documents in a collection based on a query.
        param collection_name: The name of the collection.
        param query: A dictionary representing the query (optional).
        return: A list of matching documents.
        """
        if query is None:
            query = {}
        collection = self.db[collection_name]
        return list(collection.find(query))

    def execute_raw_query(self, collection_name, query):
        """
        Execute a raw MongoDB query.
        param collection_name: The name of the collection.
        param query: A MongoDB query.
        return: The result of the query.
        """
        collection = self.db[collection_name]
        return list(collection.find(query))

    def close(self):
        """
        Close the MongoDB connection.
        """
        self.client.close()

    def deleteOldDocuments(self, collection_name, date_field, iso_date):
        """
        Delete documents older than a specified ISO date from the specified collection.

        :param collection_name: The name of the collection.
        :param date_field: The field name that contains the date.
        :param iso_date: The ISO date to compare against.
        :return: Number of deleted documents.
        """
        # Delete documents older than the specified ISO date
        collection = self.db[collection_name]
        result = collection.delete_many({
            date_field: {  # Use the provided date field
                '$lt': iso_date  # Less than the specified date
            }
        })

        return result.deleted_count  # Return the number of deleted documents

    def getDataWithinDateRange(self, collection_name, date_field, start_date, end_date):
        """
        Retrieve data within a specified date range from the specified collection.

        :param collection_name: The name of the collection.
        :param date_field: The field name that contains the date.
        :param start_date: The start date for the range (in ISO format).
        :param end_date: The end date for the range (in ISO format).
        :return: A list of documents within the specified date range.
        """
        # Query to get documents within the specified date range
        query = {date_field: {'$gte': start_date,
                              '$lte': end_date}}  # Greater than or equal to start_date and less than or equal to end_date
        collection = self.db[collection_name]
        return list(collection.find(query))

    @staticmethod
    def buildQuery(className, attribute, value):
        return {f"{className}.{attribute}": value}
