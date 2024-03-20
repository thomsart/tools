import json


class JsonParser():
    """
    This class have the responsability to make more easier the parsing of
    Json files with some methods. Instanciate the class for each json file.
    """

    def __init__(self, json_name=str):
        self.json = json_name
        self.result = []


    def read(self):
        """
        As it said it return an opened json.
        """

        with open('jsons/' + self.json, "r") as file:
            self.json = json.load(file)

        return self.json


    def get_value_with_key(self, item=any, key=str) -> any:
        """
        This method allows to retrieve the value of a given key in a json file.
        """

        if isinstance(item, dict):
            if key in item:
                self.result.append({key: item[key]})

            for each_value in item.values():
                self.get_value_with_key(each_value, key)

        elif isinstance(item, list):
            for each_item in item:
                self.get_value_with_key(each_item, key)

        else:
            return None


    def get_key_with_value(self, item=any, value=any) -> str:
        """
        This method allows to retrieve the key of a given value in a json file.
        """

        if isinstance(item, dict):
            for each_key, each_value in item.items():
                # We have to keep in mind that maybe the value in the json is -
                # something else than a string
                if each_value == value or each_value == eval(value):
                    self.result.append({each_key: each_value})

                self.get_key_with_value(each_value, value)

        elif isinstance(item, list):
            for each_item in item:
                self.get_key_with_value(each_item, value)

        else:
            return None


    def get_dict_with_key_value(self, item=any, key=str, value=any) -> dict:
        """
        This method allows to retrieve the complete dict which contains
        a specific pair of key/value in a json file.
        """

        if isinstance(item, dict):
            if key in item:
                if item[key] == value:
                    self.result.append(item)

            for each_value in item.values():
                self.get_dict_with_key_value(each_value, key, value)

        elif isinstance(item, list):
            for each_item in item:
                self.get_dict_with_key_value(each_item, key, value)

        else:
            return None


    def display_results(self):
        """
        This method display the datas in the terminal.
        """

        if self.result == []:
            return print('No datas')

        for el in self.result:
            print('-----------------------------------------------------------------')
            print(el)
        print('-----------------------------------------------------------------')


    def return_results(self) -> list[any]:
        """
        This methods returns the results in list.
        """

        return self.result