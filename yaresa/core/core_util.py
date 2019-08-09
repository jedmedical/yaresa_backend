__author__ = 'andrews'

def add_zeros(length,code):
    while(len(code)<length):
          code = "0"+code
    return  code

def get_object_or_none(model, **kwargs):
    try:
        result = model.objects.get(**kwargs)
    except model.DoesNotExist:
        result = None
    return result