def create_object(field_names, class_name):
    valid_fields = [field for field in field_names if isinstance(field, str)]
    new_class = type(class_name, (object,), {})
    
    obj = new_class()
    
   
    for field in valid_fields:
        setattr(obj, field, 1)
    
    return obj



fields = ['name', 123, 'age', 'location', None]
class_name = 'Person'
obj = create_object(fields, class_name)


print(obj.__class__.__name__)  
print(vars(obj))  

    