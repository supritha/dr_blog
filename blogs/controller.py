from .model import Schema, create_new, get_list


def create(data):
	data = Schema().validate(data)
	create_new(data)


def get(count):
	return get_list(count)