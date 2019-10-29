from app import app
from flask import jsonify, request
from app.models.Errors import ImageTooSmallError, InvalidImageTypeError
from app.models.ImageConverter import ImageConverter
from PIL import Image
import base64
import io

image_converter = ImageConverter()

@app.route('/image', methods=['POST'])
def convert_image():
  try:
      json_object = request.get_json()
      base64_string = json_object['data'].split(",")[1]
      image_data = base64.b64decode(base64_string)
      image = Image.open(io.BytesIO(image_data))
      scale = json_object['scale'] if 'scale' in json_object else 0.5
      cols = json_object['columns'] if 'columns' in json_object else 80
      inversed = json_object['inversed'] if 'inversed' in json_object else False
      aimg = image_converter.covertImageToAscii(image, cols, scale, inversed, True)
      new_image = ""
      for row in aimg:
          new_image += row + '\n'

      return jsonify({'image':  new_image,
                      'image-type': image.format })
  except ImageTooSmallError:
    return jsonify({'status': 'error', 'type': 'ImageTooSmallError'})
  except InvalidImageTypeError:
    return jsonify({'status': 'error', 'type': 'InvalidImageError'})
  except:
    return jsonify({'status': 'error', 'type': 'UndefinedError'})