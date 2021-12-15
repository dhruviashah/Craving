from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(number, number2):
	return number*number2

@register.filter(name='total')
def total(orders):
	order_sum=0
	for order in orders:
		order_sum += order.quantity*order.price
	return order_sum

