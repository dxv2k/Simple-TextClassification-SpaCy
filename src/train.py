from spacy.util import minibatch
import pandas as pd 
import random 
import spacy 

def load_data(data_path, split = 0.7): 
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

def train(model, # NLP model from SpaCy in this case  
        train_data, 
        optimizer,  
        # num_epoch = 50, 
        batch_size = 8, 
): 
    loss = {} 
    random.shuffle(train_data)
    batches = minibatch(train_data, size = batch_size)
    for batch in batches: 
        print(batch)
        print('--------------------------------------------------')
        text, label = zip(*batch)
        print(text,label)
        print('--------------------------------------------------')
        model.update(text, label, sgd = optimizer, losses = loss)
    return loss 

    # for epoch in range(num_epoch): 
    #     random.shuffle(train_data)
    #     batches = minibatch(train_data, size = batch_size)
    #     for batch in batches: 
    #         print(batch)
    ##         print('--------------------------------------------------')
    #         text, label = zip(*batch)
    #         print(text,label)
    ##         print('--------------------------------------------------')
    #         model.update(text, label, sgd = optimizer, losses = loss)
    # return loss 


def predict(): 
    predicted_class = None 
    return predicted_class 

def save_model(): 
    return 

def load_model(): 
    return 

def evaluate():
    accuracy = 0 
    return accuracy

