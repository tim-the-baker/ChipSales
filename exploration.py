import pandas as pd
import numpy as np

TRANS_DATA_FILE = r'data\QVI_transaction_data.xlsx'
PURCHASE_BEHAVIOR_FILE = r'data\QVI_purchase_behaviour.csv'

if __name__ == '__main__':
    trans_data = pd.read_excel(TRANS_DATA_FILE)

    print(trans_data.head())