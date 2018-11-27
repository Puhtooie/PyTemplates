import pandas as pd
import os
#this is with the assumption that the floats and ints in the df are numpy


#push dictionary to pickle zip
def dictionary_to_pickle():
    dictionary_key.to_pickle('keys.pickle')
    for key in dictionary_key:
        dictionary[key].to_pickle(key+'.pickle')
    return print('data saved to pickle')
to_klines_pickle()


#read dictionary from pickle zip
def read_dictionary_pickle():
    dictionary_key= pd.read_pickle('keys.pickle')

    dictionary={key:pd.read_pickle(key+'.pickle') for key in dictionary_key}
    return [dictionary_key, dictionary]

stuff= read_dictionary_pickle()

dictionary_key = stuff[0]
dictionary = stuff[1]
del stuff

#delete pickled df
def delete_dictionary_pickle():
    dictionary_key= pd.read_pickle('keys.pickle')
    for key in dictionary_key:
        os.remove(key+'.pickle')
    os.remove('keys.pickle')
    return print('deleted pickled files')

################################################################################################################################################################

#push to dictionary hdf
def dictionary_to_hdf():
    dictionary_key.to_hdf('keys.h5', key='key', mode='w', complevel=5,fletcher32=True)
    for key in dictionary:
        dictionary[key].to_hdf('dictionary.h5', key=key, mode='a', complevel=5,fletcher32=True)
    return print('pushed to hdf5')
to_klines_hdf()

dictionatry_key= pd.read_hdf('key.h5', 'key')
dictionatry={key: pd.read_hdf('dictionatry.h5',key) for key in dictionatry}

#deleting is the samme as a pickle

################################################################################################################################################################
#expiriment with hickle and pytables to commit a np.array directly to hdf5 instead. Post time differences
#/to do ^
