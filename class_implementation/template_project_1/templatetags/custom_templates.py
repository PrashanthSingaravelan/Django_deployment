from django import template

register = template.Library()
@register.filter(name='cut')

def cut_func(value,arg):
    # value = "I am in"
    # arg   = 'in'        
    # replace() --> will replace the 'in' with the values passed
    #      here ''-->(i.e no value), so 'in' will be removed
    return value.replace(arg,'')

# register.filter('cut',cut_func) 

# 'cut' --> the function when we use the template tag
# cut_func --> the function that is present in this custom_templates.py