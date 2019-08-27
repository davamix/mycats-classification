from tensorflow.keras.applications.xception import Xception
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, BatchNormalization, Dropout, Activation, Flatten, LeakyReLU

import efficientnet.keras as efn


def build_xception(height, width, depth, include_top=False, weights='imagenet'):
    xception_model = Xception(weights=weights, 
                              include_top=include_top, 
                              input_shape = (height, width, depth))

    model = Sequential()
    model.add(xception_model)

    model.add(Flatten())
    model.add(Dense(512))
    model.add(LeakyReLU())
    model.add(BatchNormalization())
    model.add(Dropout(0.4))
    
    model.add(Dense(256))
    model.add(LeakyReLU())
    model.add(BatchNormalization())
    model.add(Dropout(0.4))

    model.add(Dense(128))
    model.add(LeakyReLU())
    model.add(BatchNormalization())
    model.add(Dropout(0.4))


    model.add(Dense(2))
    model.add(Activation("softmax"))

    xception_model.trainable = False

    return model

def build_efficientnet(height, width, depth, include_top=False, weights='imagenet'):
    efficientnet_model = efn.EfficientNetB0(weights=weights, 
                                            include_top=include_top,
                                           input_shape=(height, width, depth))

    model = Sequential()
    model.add(efficientnet_model)
    model.add(GlobalAveragePooling2D())
    model.add(Dropout(0.5))
    model.add(Dense(2))
    model.add(Activation("softmax"))

    return model