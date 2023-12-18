# Machine Learning model

## Model Recomendation
This model uses cosine similarity and tf-idf from [scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html).


![Screenshot (932)](https://github.com/SaveMoneyCapstone/ML-Repo/assets/89589561/c87a41e4-afe1-425a-8cad-2e131cd71365)

This model uses the parameters of the column and then calculates it to be the mean.

- then the result_mean column is embedded with tf-idf to find each feature on the stock symbol.
![Screenshot (933)](https://github.com/SaveMoneyCapstone/ML-Repo/assets/89589561/c751aef4-c8cd-4616-9901-951b19501d3d)

- then calculate the cosine similarity between the embedded mean results with the technique in the cosine_similiarty function.
![Screenshot (936)](https://github.com/SaveMoneyCapstone/ML-Repo/assets/89589561/88047c7c-39ad-4bde-921d-07eb4a32ffdd)

the model has built in [functions](https://github.com/SaveMoneyCapstone/ML-Repo/blob/main/train.py) to be trained and saved in ```.bin``` format.

setup model built in function


open terminal
- ``` git clone https://github.com/SaveMoneyCapstone/ML-Repo.git ```
- ``` cd ML-Repo ```
- ``` python3 -m ensurepip ```
- ``` pipenv install ```
- ``` pipenv install --dev ```
- ``` pipenv run python train.py ```



## Model Forecasting
This model uses the [tensorflow](https://www.tensorflow.org/) library and tensorflow costum layer in the n-beast approach in the [paper](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Farxiv.org%2Fpdf%2F1905.10437.pdf) as an experiment model.

the forecasting model here uses an experimental approach of 6 models, with the baseline model being naive forecasting.

In this approach, with a baseline of naive forecasting mode, the model with the smallest ```mae, mse, rmse, mape, mase``` values and efficient paramter and hyperparameter sizes is ```model_8_cnn_lstm```

![Screenshot (937)](https://github.com/SaveMoneyCapstone/ML-Repo/assets/89589561/4b6eb01b-a0fc-4d90-a340-6d8bfd05a625)


![Screenshot (938)](https://github.com/SaveMoneyCapstone/ML-Repo/assets/89589561/3b249356-624a-489e-ac9e-58bce08bf9e8)

``` note: the save model for cnn_lstm is in the last notebook cell. ```


