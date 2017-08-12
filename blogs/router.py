from flask import Blueprint
from flask import jsonify
from flask import request, Response

import json
import blogs.controller


blog = Blueprint('blog', __name__)


@blog.route('/v1/blogs', methods=['POST'])
def create_blog():
	data = request.get_json()
	status = blogs.controller.create(data)
	return jsonify({'status': status})


@blog.route('/v1/blogs', methods=['GET'])
def get_blog():
	data = request.get_json()
	return blogs.controller.get(data)