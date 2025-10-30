from flask import Flask
from flask.json.provider import DefaultJSONProvider
from model import db
from route import blueprints
import config

class CustomJSONProvider(DefaultJSONProvider):
    def dumps(self, obj, **kwargs):
        kwargs.setdefault("ensure_ascii", False)
        return super().dumps(obj, **kwargs)

    def loads(self, s, **kwargs):
        return super().loads(s, **kwargs)

app = Flask(__name__)
app.json = CustomJSONProvider(app)
app.config.from_object(config)
db.init_app(app)

with app.app_context():
    db.create_all()

for bp in blueprints:
    app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)