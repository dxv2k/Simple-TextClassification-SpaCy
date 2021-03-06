import pandas as pd  
import spacy 

import argparse

data_path = './data/yelp_ratings.csv'

# def create_model(
#     model = spacy.blank('en'), # create empty model  
#     lang='en', 
#     config = {
#        "exclusive_classes": True, 
#        "architecture": "bow" 
#     }
#     labels = []
#  ): 

#     model 
#     return model 

def load_data(data_path, split = 0.85): 
    ''' 
    param: 
        data_path: data path in *.csv format  
        split:  split ratio is 0.85 
    return: 
        train_texts, 
        train_labels, 
        val_texts, 
        val_labels 
    ''' 
    data = pd.read_csv(data_path)
    # shuffle data 
    train_data =  data.sample(frac = 1, random_state = 42) 

    texts = train_data.text.values  
    labels = [ 
      {'POSITIVE':bool(val), 'NEGATIVE':bool(val)}  for val in train_data.sentiment.values 
    ] 
        
    split = int(len(train_data)*split) # split length perspective to data length 
    train_labels = [ {'cats': labels for label in labels[:split] }]
    val_labels = [ {'cats': labels for label in labels[split:] }]

    return texts[:split], train_labels, texts[split:], val_labels 

from spacy.util import minibatch 

def train(

): 
    loss = {} 
    return loss 

def predict(): 
    predicted_class = None 
    return predicted_class 

def evaluate():
    accuracy = 0 
    return accuracy

train_texts, train_labels, val_texts, val_labels = load_data(data_path) 
print(train_texts[:5] )
print('-----------------------------')
# print(train_labels[:2] )
# print(load_data(data_path))
