import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from util.file_helper import FileReader

class CctvModel:
    def __init__(self):
        print(f'baseurl #### {baseurl}')
        self.reader = FileReader()

    def hook_process(self):
        print('----------- CCTV & POP ----------')
        cctv = self.get_cctv()
        pop = self.get_pop()
        
        print(f'CCTV Head: {cctv.head()}')
        print(f'POP Head: {pop.head()}')
        
        
        

    def get_cctv(self):
        reader = self.reader
        reader.context = os.path.join(baseurl,'data')
        reader.fname = 'cctv_in_seoul.csv'
        reader.new_file()
        cctv = reader.csv_to_dframe()
        cctv.rename(columns = {cctv.columns[0]: '구별'}, inplace = True)
        return cctv

    def get_pop(self):
        reader = self.reader
        reader.context = os.path.join(baseurl,'data')
        reader.fname = 'pop_in_seoul.xls'
        reader.new_file()
        pop = reader.xls_to_dframe(2, 'B,D,G,J,N')
        pop.rename(columns = {
            pop.columns[0]: '구별',
            pop.columns[1]: '인구수',
            pop.columns[2]: '한국인',
            pop.columns[3]: '외국인',
            pop.columns[4]: '고령자',
            }, inplace = True)
        print(f'POP Null Checker: {pop["구별"].isnull()}')
        pop.drop([26], inplace=True)
        return pop

    


if __name__ == '__main__':
    model = CctvModel()
    model.hook_process();
    
    