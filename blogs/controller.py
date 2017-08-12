from .model import Schema, create_new, get_list


def create(data):
	schema = Schema()
	data = schema.validate(data)

	data.update(schema.get_defaults())
	return create_new(data)


def get(data):
	page = int(data.get('page', 0))
	count = int(data.get('count', 10))
	return get_list(page, count)