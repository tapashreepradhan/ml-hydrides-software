# -*- coding: utf-8 -*-
"""
"""

import pandas as pd
from matminer.featurizers.composition import alloy
#from pymatgen import Composition

file_path = '/path/to/your/ML-HYDPARK_v0.0.4.csv'

df = pd.read_csv(file_path)

if 'Composition_Formula' in df.columns:
    # Initializing the featurizers
    miedema_featurizer = alloy.Miedema()
    #yang_featurizer = alloy.YangSolidSolution()
    #wen_featurizer = alloy.WenAlloys()

    # Applying the featurizers
    df = miedema_featurizer.featurize_dataframe(df, 'Composition_Formula')
    #df = yang_featurizer.featurize_dataframe(df, 'Composition_Formula')
    #df = wen_featurizer.featurize_dataframe(df, 'Composition_Formula')
    
    df.to_csv('/path/to/your/featurized_ML-HYDPARK_v0.0.4.csv', index=False)
    
    print("Featurization complete. CSV file with features has been saved.")
else:
    print("The column 'Composition_Formula' was not found in the CSV file.")

