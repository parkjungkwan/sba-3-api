import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from config import basedir

class Crime:
    def __init__(self):
        pass

    def read_file(self):
        basedir = os.path.dirname(os.path.abspath(__file__))
        cctv_seoul = pd.read_csv(os.path.join(basedir,'model','data','cctv_in_seoul','cctv_in_seoul.csv'))
        print(cctv_seoul.head())

        print(cctv_seoul.sort_values(by='소계',ascending=True))

        print('#'*50)

        crime_seoul = pd.read_csv(os.path.join(basedir,'model','data','crime_in_seoul','.model/data/crime_in_seoul.csv'))
        print(crime_seoul.head())

if __name__ == '__main__':
    t = Crime()
    t.read_file()
    