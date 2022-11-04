# Murat Can Bastug and Gokce Unal
# Assignment 1 (Architectures for Big Data)

class interco_batch_uploader:
    cache_list = [...]  # Keeps the caches in order from the last used cache to the first used cache.

    def get_conn(self, server, DB, credential, port):
        """
        get_conn function connects to the related database using the parameters given by the user and returns the
        connection object. A reusable structure is provided to the customer by selecting the database to be connected
        with the parameters that will be given in the future.

        :param server: Server name
        :param DB: Database name
        :param credential: ID
        :param port: Port number

        :return: Connection object | false: for connection error
        """
        pass

    def write_data_to_cache(self, table, conditions, data):
        """
        write_data_to_cache changes the data and conditions of the cache at the end of the cache_list and puts it at the
        top of the list. It works O(1).

        :param table: Table which to get data
        :param conditions: Conditions to get data
        :param data: Data to be written
        """
        pass

    def get_data_from_cache(self, sql, table, conditions):
        """
        get_data_from_cache checks whether the desired data is currently kept in a cache and this data is up-to-date.
        Since each cache statically keep the data under which conditions, the control of all caches can be done in o(n).
        (n: number of caches). If any cache holds the desired data, the function returns this data, otherwise it
        returns -1.

        :param sql: Connection object to check up-to-date data
        :param table: Table which to get data
        :param conditions: Conditions to get data

        :return: Desired data | -1
        """
        pass

    def get_data(self, sql, table, columns, conditions, limit=-1):
        """
        get_data function request last six months Intercompany data which impacts on Company Balance Sheet from given
        database and returns incoming data with considering the requirements. Also the customer can also make different
        queries in the future using function parameters. By default, the limit is -1. If no limit is specified
        (limit is -1), the function returns all data that satisfies the conditions. It is connected our architecture
        being a technical basis for design.

        get_data first calls the get_data_from_cache function and checks whether there is data in any cache with the
        desired conditions and the data is up-to-date. If there is data in any cache, it is first brought to the
        beginning of the relevant cache cache_list. Then it is processed and returned according to the limit and columns
        information. If get_data_from_cache returns -1, data is read from OneStream. Then the write_data_to_cache
        function is run and the data is written to the cache that is the last item of cache_list with its conditions
        and add at the top of the cache_list.

        Using cache makes the architecture highly scalable. The customer can increase or decrease the number of caches
        according to his own data and needs.

        :param sql: Connection object
        :param columns: Columns which to get data | for all columns use '*'
        :param table: Table which to get data
        :param conditions: Conditions to get data
        :param limit: How many data can be retrieved | optional

        :return: Data from executed query
        """
        pass

    def write_data(self, sql, data, table, columns):
        """
        write_data function writes the data previously fetched from the database to the Historical Database. This
        function also provides ability to write external data that is not in the OneStream to the Historical Database.
        Even though this feature is not specified by the customers, it can be a useful feature to add missing data.

        :param sql: Connection object
        :param data: Data to be written
        :param table: Table which to insert data
        :param columns: Columns which to insert data | for all columns use '*'
        """
        pass

    def delete_data(self, sql, data, table, conditions):
        """
        delete_data function can delete unrelated or unwanted data from the Historical Database. It is an additional
        feature that our architecture provides.


        :param sql: Connection object
        :param data: Data to be deleted
        :param table: Table which to delete data
        :param conditions: Conditions to delete data
        """
        pass
