def check_permission(required_permission):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if required_permission not in user_permissions:
                raise PermissionError(f"У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
try:
    add_comment()
except PermissionError as e:
    print(f'PermissionError: {e}')
