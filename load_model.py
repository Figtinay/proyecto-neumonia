import tensorflow as tf

def model_fun():
    # cargar el modelo
    model_cnn = tf.keras.models.load_model('conv_MLP_84.h5')
    return model_cnn