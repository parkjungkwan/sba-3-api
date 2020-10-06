import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from util.file_helper import FileReader

class CrimeModel:
    def __init__(self):
        print(f'baseurl #### {baseurl}')
        self.reader = FileReader()


    def get_crime(self):
        reader = self.reader
        reader.context = os.path.join(baseurl,'data')
        reader.fname = 'crime_in_seoul.csv'
        reader.new_file()
        crime = reader.csv_to_dframe()
        print(f'{crime.head()}')


if __name__ == '__main__':
    crime = CrimeModel()
    crime.get_crime()
    