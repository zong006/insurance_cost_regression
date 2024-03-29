import tensorflow as tf
from tensorflow.keras import models, layers

def neural_net(X_train, y_train):

    model = models.Sequential([
            layers.Dense(30, activation='softplus', input_dim=X_train.shape[1]),
            layers.Dropout(0.2),  
            layers.Dense(50, activation='softplus'), 
            layers.Dropout(0.2),
            layers.Dense(30, activation='softplus'), 
            layers.Dropout(0.2),
            layers.Dense(1, activation='linear')  
            ])
    optimizer = tf.optimizers.Adam(learning_rate=0.01)

    model.compile(optimizer=optimizer, loss='mean_squared_error')
    model.fit(X_train, y_train, epochs=100, batch_size=20, verbose=0, validation_split=0.2)
    return model

def randomforest_regression(X_train, y_train):
    from sklearn.ensemble import RandomForestRegressor

    model = RandomForestRegressor(n_estimators=100, random_state=42, criterion='squared_error')
    y_train = y_train.ravel()
    model.fit(X_train, y_train)
    
    return model



