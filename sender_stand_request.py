import configuration
import requests
import data

#Создание заказа
def CREATE_ORDER_PATH_NEW():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body)


# Получение номера заказа

def NUMBER_TRACK(CREATE_TRACK_PATH):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_TRACK_PATH+str(CREATE_TRACK_PATH))


