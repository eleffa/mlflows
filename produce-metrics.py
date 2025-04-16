from mlflow import log_metric
from random import choice

metrics_name= ['cpu','ram','disk']
percentages=[i for i in range(0,100)]

for i in range(40):
    log_metric(choice(metrics_name), choice(percentages))