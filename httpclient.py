import json

from kivy.network.urlrequest import UrlRequest


class HttpClient:
    def get_pizzas(self, on_complete, on_error):
        url = "https://therealpizzamamadjango.herokuapp.com/api/GetPizzas"

        def data_received(req, result):
            data = json.loads(result)
            pizzas_dict = []
            for i in data:
                pizzas_dict.append(i["fields"])
            print("data received")
            if on_complete:
                on_complete(pizzas_dict)

        def data_error(req, error):
            print("data error")
            if on_error:
                on_error(str(error))
        def data_failure(req, result):
            print("data failure")
            if on_error:
                on_error("SERVER ERROR" + str(req.resp_status))

        req = UrlRequest(url, on_success=data_received, on_error=data_error, on_failure=data_failure)
