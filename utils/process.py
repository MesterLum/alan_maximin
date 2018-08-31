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
        self.get_max_or_min(1)

    def get_data_table(self):
        for data in self.table:
            yield data

    """
        *operation 1 = maximin
        *operation 2 = maximax
    """

    def get_max_or_min(self, operation = 1):
        

        if operation == 1:
            len_table_values = len(self.table[0]['values']) -1
            new_table_maximin = self.get_sub_table_with_index(len_table_values)
            if (DEBUG):
                print('Longitud: {}'.format(len_table_values+1))
            
            #Sort Values for ordenate and taked value-max
            new_table_maximin.sort(reverse=True)
            print(new_table_maximin)


    """
        *This method recived sub-list and return JSON with results indexs
    
    """
    def get_results_with_index(self, list, sub_table):
        list_data = []
        for value in list:




    """
        *This method return sub-table
    
    """

    def get_sub_table_with_index(self, index):
        sub_table = []
        for data in self.get_data_table():
            sub_table.append(data['values'][index])
            if (DEBUG):
                print('Value push in sub-table: {} in index: {}'.format(data['values'][index], index))

        return sub_table

