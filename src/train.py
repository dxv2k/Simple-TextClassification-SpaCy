import pandas as pd 



def load_data(data_path, split = 0.85): 
    ''' 
    param: 
        data_path, data_path in *.csv format  
        split = 0.85 split ratio between train set and validation set 
    return: 
        train_texts, 
        train_labels, 
        val_texts, 
        val_labels 
    ''' 
    data = pd.read_csv(data_path)
    # shuffle data 
    train_data =  data.sample(frac = 1, random_state = 42) 

    texts = train_data.stars.values  
    labels = [ 
      {'POSITIVE':bool(val), 'NEGATIVE':bool(val)}  for val in train_data.sentiment.values 
    ] 
        
    split = int(len(train_data)*split) # split length perspective to data length 
    train_labels = [ {'cats': labels for label in labels[:split] }]
    val_labels = [ {'cats': labels for label in labels[split:] }]

    return texts[:split], train_labels, texts[split:], val_labels 

def train(): 
    loss = {} 
    return loss 

def predict(): 
    predicted_class = None 
    return predicted_class 

def evaluate():
    accuracy = 0 
    return accuracy

