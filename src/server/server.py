import sys
sys.path.append('..')
import ml.modelling.inference as inference
from wsgiref.simple_server import make_server
import falcon
import json

class GetInference:
    def on_get(self, request, response):
        """Handles GET requests"""
        json_data = request.bounded_stream.read()
        json_model = json.loads(json_data)

        result = inference.infer(json_model, pickle_path='../ml/modelling/pickles')

        response.body = json.dumps({'Prediction' : result})
        response.status = falcon.HTTP_200

if __name__ == '__main__':
    app = falcon.App()
    app.add_route('/GetInference', GetInference())

    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')
        httpd.serve_forever()
