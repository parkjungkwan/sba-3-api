import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from util.file_helper import FileReader

class CctvModel:
    def __init__(self):
        print(f'baseurl #### {baseurl}')
        self.reader = FileReader()


    def get_cctv(self):
        reader = self.reader
        reader.context = os.path.join(baseurl,'data')
        reader.fname = 'cctv_in_seoul.csv'
        reader.new_file()
        cctv = reader.csv_to_dframe()
        print(f'{cctv.head()}')


if __name__ == '__main__':
    cctv = CctvModel()
    cctv.get_cctv()
    