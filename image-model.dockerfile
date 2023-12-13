FROM tensorflow/serving:2.14.0


COPY model-forecast_tf-serving/model_cnn_lstm /models/model_cnn_lstm/1 

ENV MODEL_NAME="model_cnn_lstm"