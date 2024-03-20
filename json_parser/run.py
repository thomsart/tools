import os
import argparse

from jsonparser import JsonParser


# the parser
parser = argparse.ArgumentParser()
parser.add_argument("file", help="the json to parse")
parser.add_argument("action", choices=["get_vwk", "get_kwv", "get_dwkv"], help="The methods to use")
args = parser.parse_args()


if __name__ == '__main__':

    # the variables to declare
    folder = "jsons"
    path = os.path.abspath(folder)
    # print("The path => " + path)

    input_key = "Which key you want to search ?\n"
    input_value = "Which value you want to search ?\n"

    # If we want to parse all files in jsons
    if args.file == "all_files":
        result = {}
        key = "modified_date" # input("Key:\n") # 
        value = "2019-09-25T00:00:00Z" # input("Value:\n")

        for file in os.listdir(folder):

            data = JsonParser(json_name=file)
            opened_data = data.read()

            if args.action == "get_vwk":
                data.get_value_with_key(item=opened_data, key=key)

            elif args.action == "get_kwv":
                data.get_key_with_value(item=opened_data, value=value)

            elif args.action == "get_dwkv":
                data.get_dict_with_key_value(item=opened_data, key=key, value=value)

            result[file] = data.return_results()

        print(result)

    else:

        data = JsonParser(json_name=args.file + ".json")
        opened_data = data.read()
        key = input(input_key)
        value = input(input_value)

        if args.action == "get_vwk":
            data.get_value_with_key(item=opened_data, key=key)

        elif args.action == "get_kwv":
            data.get_key_with_value(item=opened_data, value=value)

        elif args.action == "get_dwkv":
            data.get_dict_with_key_value(item=opened_data, key=key, value=value)

        datas = data.return_results()
        print(datas)

    # # exemple pour lancer un module
    # elif args.action == "update_consumptions":
    #     exec(open("app/operators_api/orange/update_data.py"))