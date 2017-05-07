#! /usr/env python2


import imghdr
import uuid
import os

from flask import Flask, request, jsonify, send_from_directory, abort
from gevent.wsgi import WSGIServer
from urllib2 import urlopen, URLError

from engines.simple_engine import SimpleEngine


app = Flask(__name__)
host = '0.0.0.0'
port = 42528


directory = 'img'
if not os.path.exists(directory):
    os.mkdir(directory, 0o755)


@app.route('/img2emoji/simple', methods=['GET'])
def img2emoji_simple():
    simple_engine = SimpleEngine(emoji_data_dir='emoji_data', img_host=host, img_port=port)

    req_json = request.get_json()
    photo_url = req_json.get('photo')

    img_uuid = uuid.uuid4().hex
    filename = img_uuid

    try:
        response = urlopen(photo_url)
        with open(os.path.join(directory, filename), 'wb') as cache_file:
            cache_file.write(response.read())
    except URLError:
        return jsonify(errno=1, err_message='URL error')
    except IOError:
        return jsonify(errno=2, err_message='I/O error')

    if imghdr.what(os.path.join(directory, filename)) is None:
        return jsonify(errno=3, err_message='Corrupted image file')

    if imghdr.what(os.path.join(directory, filename)) not in ['jpeg', 'png']:
        return jsonify(errno=4, err_message='Unsupported image format')

    suffix = imghdr.what(os.path.join(directory, filename))

    return jsonify(emoji=simple_engine(img_uuid, suffix))


@app.route('/getImg', methods=['GET'])
def get_image():
    img_uuid = request.args.get('img_uuid')
    suffix = request.args.get('suffix')

    filename = img_uuid
    if os.path.exists(os.path.join(directory, filename)):
        return send_from_directory(directory, filename,
                                   as_attachment=True,
                                   attachment_filename='{img_uuid}.{suffix}'.format(img_uuid=img_uuid, suffix=suffix))
    else:
        return abort(404)


if __name__ == '__main__':
    app.debug = True
    http_server = WSGIServer((host, port), app)
    http_server.serve_forever()
