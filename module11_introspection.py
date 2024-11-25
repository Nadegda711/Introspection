from pprint import pprint


def introspection_info(obj):
    # Определяем тип объекта
    obj_type = type(obj).__name__

    # Получаем все атрибуты
    all_attributes = dir(obj)

    # Фильтруем атрибуты и методы
    attributes = [attr for attr in all_attributes if not attr.startswith("__")]
    attributes = [attr for attr in all_attributes if callable(getattr(obj, attr)) and not attr.startswith("__")]
    methods = [method for method in all_attributes if callable(getattr(obj, method)) and method.startswith("__")]

    # Получаем имя модуля
    module_name = __name__

    # Формируем и возвращаем словарь с информацией
    return {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module_name
    }
number_info = introspection_info(42)

print(number_info)
