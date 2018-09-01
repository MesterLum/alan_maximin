"""
    *La tabla obtiene los datos por el constructor y al tomar los datos
    hay respectivos modulos para maximin y esas madres

"""
from .constants import DEBUG
class Process:

    def __init__(self, table):
        self.table = table

    def __str__(self):
        return 'Process'

    def get_results_maximin(self):
        return self.__get_max_or_min(1)
    
    def get_results_maximax(self):
        return self.__get_max_or_min(2)

    def __get_data_table(self):
        for data in self.table:
            yield data

    """
        *operation 1 = maximin
        *operation 2 = maximax
    """

    def __get_max_or_min(self, operation = 1):
        

        if operation == 1:
            len_table_values = len(self.table[0]['values']) -1
            new_table_maximin = self.__get_sub_table_with_index(len_table_values)
            if (DEBUG):
                print('__get_max_or_min- Longitud: {}'.format(len_table_values+1))
            
            #Sort Values for ordenate and taked value-max
            return self.__get_results_with_index(sorted(new_table_maximin, reverse=True)[0], new_table_maximin)

        elif operation == 2:
            new_table_maximin = self.__get_sub_table_with_index(0)
            return self.__get_results_with_index(sorted(new_table_maximin, reverse=True)[0], new_table_maximin)


    """
        *This method recived sub-list and return JSON with results indexs
    
    """
    def __get_results_with_index(self, value, table_old):
        list_data = []
        for index in range(len(table_old)):
            if (DEBUG):
                print('__get_results_with_index- value: {} Index: {}'.format(table_old[index], index))

            if (table_old[index] == value):
                list_data.append(self.table[index])
        return list_data




    """
        *This method return sub-table
    
    """

    def __get_sub_table_with_index(self, index):
        sub_table = []
        for data in self.__get_data_table():
            sub_table.append(data['values'][index])
            if (DEBUG):
                print('__get_sub_table_with_index- Value push in sub-table: {} in index: {}'.format(data['values'][index], index))

        return sub_table

