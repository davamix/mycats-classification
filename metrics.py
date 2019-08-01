import tensorflow as tf
import numpy as np

# MCC metric from binary class
def MCC_binary(y_true, y_pred):
    y_pred_pos = tf.keras.backend.round(tf.keras.backend.clip(y_pred, 0, 1))
    y_pred_neg = 1 - y_pred_pos

    y_pos = tf.keras.backend.round(tf.keras.backend.clip(y_true, 0, 1))
    y_neg = 1 - y_pos

    tp = tf.keras.backend.sum(y_pos * y_pred_pos)
    tn =tf.keras. backend.sum(y_neg * y_pred_neg)

    fp = tf.keras.backend.sum(y_neg * y_pred_pos)
    fn = tf.keras.backend.sum(y_pos * y_pred_neg)

    numerator = (tp * tn - fp * fn)
    denominator = tf.keras.backend.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))

    return numerator / (denominator + tf.keras.backend.epsilon())

# MCC metric for multiclass
# https://github.com/Cobord/FairnessMCC/blob/master/MatthewsCorrCoeff.py
def MCC_multi(confusionMatrix):
    (dim1,dim2)=confusionMatrix.shape
    if (dim1 != dim2):
        raise ValueError("Confusion Matrix must be square")
    
    numerator = 0
    denominator1 = 0
    denominator2 = 0
    
    for k in range(dim1):
        for l in range(dim1):
            for m in range(dim1):
                numerator+=confusionMatrix[k,k]*confusionMatrix[l,m]
                numerator-=confusionMatrix[k,l]*confusionMatrix[m,k]
    
    for k in range(dim1):
        temp1=0
        temp2=0
        for k2 in range(dim1):
            if (k2 != k):
                for l2 in range(dim1):
                    temp1+=confusionMatrix[k2,l2]
                    temp2+=confusionMatrix[l2,k2]
        
        denominator1+=np.sum(confusionMatrix[k,:])*temp1
        denominator2+=np.sum(confusionMatrix[:,k])*temp2
    
    return numerator/(np.sqrt(denominator1*denominator2))