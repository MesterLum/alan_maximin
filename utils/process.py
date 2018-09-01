"""
    *La tabla obtiene los datos por el constructor y al tomar los datos
    hay respectivos modulos para maximin y esas madres

"""
from .constants import DEBUG
class Process:

    def set_table(self, table):
        self.table = table

    def __str__(self):
        return 'Process'

    """
        !(value_p / 100) > 0 and < 1:
            return {'value': 0}
    
    """

    def get_optimist_pesimist(self, value_p):
        value_q = 1 - value_p
        if not ((value_p / 100) > 0 and (value_p / 100) < 1):
            return {'value': 0}

        accum_values = []
        for value in self.__get_data_table():
            values_sort = sorted(value['values'])
            extrems_accum = (values_sort[0] * value_q) + (values_sort[len(values_sort) -1] * value_p)
            accum_values.append(extrems_accum)

        if (DEBUG):
            print(accum_values)

        return self.__get_results_with_index(sorted(accum_values, reverse=True)[0],accum_values)
        
    def get_results_minimax(self):
        pass
        """
        new_table = []
        
        for index in range(len(self.table[0]['values'])):
            mini_table = [0] * len(self.table[0]['values'])
            for sub_index in range(len(self.table)):
                #print(self.table[sub_index]['values'][index])
                mini_table[index] = self.table[sub_index]['values'][index]
            print(mini_table)"""
                

            #for index in range(len(data['values'])):
        #print(new_table)

    

    def __get_index_for_sub_table(self, sub_table, value_max):
        for index in range(len(sub_table)):
            if value_max == sub_table[index]:
                return index

    def get_results_maximin(self):
        return self.__get_max_or_min(1)
    
    def get_results_maximax(self):
        return self.__get_max_or_min(2)

    def get_results_laplace(self):
        values_accum = self.__accum_values()
        return self.__get_results_with_index(sorted(values_accum, reverse=True)[0], values_accum)
        
    def __accum_values(self):
        values_accum = []
        for data in self.__get_data_table():
            accum = 0
            for values in data['values']:
                accum = accum + values
            values_accum.append(accum / len(data['values']))
        return values_accum

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

