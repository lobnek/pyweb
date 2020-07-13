from pyutil.web.application import create_server
from pyweb.blueprints.whoosh.api import blueprint as blue_whoosh
from pyweb.blueprints.post.api import blueprint as blue_post
from pyweb.blueprints.admin.api import blueprint as blue_admin
from pyweb.exts.exts import engine, cache
from whitenoise import WhiteNoise


def create_app():
    server = create_server(extensions=[engine, cache], static_folder="/static")

    server.register_blueprint(blue_whoosh, url_prefix="/whoosh")
    server.register_blueprint(blue_post, url_prefix="/engine")
    server.register_blueprint(blue_admin, url_prefix="/admin")

    # add whitenoise
    server.wsgi_app = WhiteNoise(server.wsgi_app, root='/static', prefix='assets/')

    return server