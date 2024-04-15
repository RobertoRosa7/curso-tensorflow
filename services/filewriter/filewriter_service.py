# -*- coding: utf-8 -*-

import csv
import json
import os


class FileWriterService:
    path_default = os.path.join('storage')

    @staticmethod
    def fetch_local_cep(path: str):
        with open(path, 'r', encoding='utf-8') as json_file:
            data = json.loads(json_file.read())
            json_file.close()

        return data

    def save_csv(self, filename: str, data: str):
        """
        Version: 1.0.0
        Summary: This method is responsible to write a new file type csv

        Params: filename<string>, data<string>
        Return: None
        """
        with open(os.path.join(self.path_default, filename), 'w', encoding='utf-8') as csv:
            csv.writelines(data)
            csv.close()

    @staticmethod
    def save_csv_with_header(path: str, header: list, data) -> None:
        """
        Version: 1.0.0 Summary: This method is responsible to write a new file type csv with header, where parameter
        header is a list of names and data is the content

        Params: path<string>, header<list<string>>, data<any>
        Return: None
        """
        with open(path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)

            f.close()

    @staticmethod
    def write_json(json_array: list, path: str) -> None:
        """
        Version: 1.0.0
        Summary: This method is responsible to write a new file type json, and receive as parameter a list of
        data that'll be written and the path where directory

        Params: json_array<list>, path<string>
        Return: None
        """
        with open(path, 'w', encoding='utf-8') as json_file:
            json.dump(json_array, json_file, ensure_ascii=False, indent=4)
            json_file.close()

    @staticmethod
    def read_txt(path: str):
        """
        Version: 1.0.0
        Summary: This method is responsible to read file type txt, path is a directory where file is located

        Params: path<string>
        Return: list
        """
        with open(path, 'r', encoding='utf-8') as txt_file:
            data = list(map(lambda lines:
                            list(map(lambda line:
                                     str(line).replace('\n', '').strip(), lines.split('\t'))), txt_file))
            txt_file.close()
        return data

    @staticmethod
    def read_csv(path: str) -> list:
        """
        Version: 1.0.0
        Summary: This method is responsible to read file type csv and create a list to be written in json file
        path to directory where will be saved

        Params: path<string>
        Return: list
        """

        json_array = []
        with open(path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)  # load csv file data using csv library's dictionary reader

            for row in csv_reader:
                json_array.append(row)  # add this python dict to json array
            csv_file.close()

        return json_array
