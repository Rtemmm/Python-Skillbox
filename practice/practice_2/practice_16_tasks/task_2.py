class App:
    def __init__(self):
        self.routes = {}

    def callback(self, route):
        def decorator(func):
            self.routes[route] = func
            return func

        return decorator

    def get(self, route):
        return self.routes.get(route, None)


app = App()


@app.callback('//')
def example():
    print('Ожидаемый результат: пример функции, которая возвращает ответ сервера.')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
