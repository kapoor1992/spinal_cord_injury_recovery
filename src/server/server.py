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

class PostInference:
    def on_post(self, req, resp):
        """Handles POST requests"""
        raw_json = req.bounded_stream.read()
        print(raw_json)
        json_model = json.loads(raw_json)
        result = inference.infer(json_model, pickle_path='../ml/modelling/pickles')

        resp.status = falcon.HTTP_200
        resp.body = json.dumps({'Prediction' : result})

if __name__ == '__main__':
    app = falcon.App()
    app.add_route('/GetInference', GetInference())
    app.add_route('/PostInference', PostInference())

    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')
        httpd.serve_forever()
