def introspection_info(obj):
    obj_type = type(obj).__name__

    all_attributes = dir(obj)

    attributes = [attr for attr in all_attributes if not attr.startswith("__")]
    methods = [method for method in all_attributes if callable(getattr(obj, method)) and method.startswith("__")]
    module_name = __name__

    return {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module_name
    }

number_info = introspection_info(42)
print(number_info)
