import re

from django.utils.safestring import mark_safe
from django import template

register = template.Library()


@register.filter
def placeholder(value, token):
	value.field.widget.attrs["placeholder"] = token
	return value	

@register.filter
def add_class(value, css_class):
	class_re = re.compile(r'(?<=class=["\'])(.*)(?=["\'])')
	string = str(value)
	match = class_re.search(string)
	if match:
		m = re.search(r'^%s$|^%s\s|\s%s\s|\s%s$' % (css_class, css_class, 
													css_class, css_class), match.group(1))
		print (match.group(1))
		if not m:
			return mark_safe(class_re.sub(match.group(1) + " " + css_class, 
										  string))
	else:
		return mark_safe(string.replace('>', ' class="%s">' % css_class))
	return value

@register.filter
def getDays(dictionary,key):
	print(dictionary)
	print(key)
	tdelta=dictionary.get(key)
	print("tdelta: "+ str(tdelta))
	return tdelta.days
@register.filter
def getHours(dictionary,key):
	tdelta=dictionary.get(key)
	return tdelta.seconds//3600

@register.filter
def getMinutes(dictionary,key):
	tdelta=dictionary.get(key)
	return (tdelta.seconds//60)%60

@register.filter
def getSeconds(dictionary,key):
	tdelta=dictionary.get(key)
	return (tdelta.seconds)%60
