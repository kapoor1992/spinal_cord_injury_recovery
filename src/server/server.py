from wsgiref.simple_server import make_server

import falcon
import json

class GetSampleResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        result_dict = dict()
        result_dict["score"] = "value1"
        result_dict["description"] = "value2"
        result_dict["color"] = "value3"
        resp.body = json.dumps(result_dict)

class PostSampleResource:
    def on_post(self, req, resp):
        """Handles POST requests"""
        raw_json = req.bounded_stream.read()
        #print(raw_json)
        req_dict = json.loads(raw_json)
        print(req_dict)
        result_dict = dict()
        result_dict["score"] = "E"
        result_dict["description"] = "Total recovery possible"
        result_dict["color"] = "Green"
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(result_dict)

# falcon.App instances are callable WSGI apps...
# in larger applications the app is created in a separate file
app = falcon.App()

# Resources are represented by long-lived class instances
sample_get = GetSampleResource()
sample_post = PostSampleResource()

app.add_route('/sample_get', sample_get)
app.add_route('/sample_post', sample_post)

if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()
