from memorious.views.assets import assets, compile_assets  # noqa
from memorious.views.base import blueprint as base


def mount_app_blueprints(app):
    app.register_blueprint(base)
    compile_assets(app)
