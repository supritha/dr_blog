from flask import Blueprint


import json


blog = Blueprint('blog', __name__)


@blog.route('/v1/blogs', methods=['POST'])
def create_blog(user_id):
    pass


@blog.route('/v1/blogs', methods=['GET'])
def get_glog(user_id):
    pass