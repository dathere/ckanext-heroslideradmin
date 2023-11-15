# encoding: utf-8
import ckan.plugins as plugins
import ckanext.heroslideradmin.commands.cli as cli
import ckanext.heroslideradmin.views as views


class MixinPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IClick)
    plugins.implements(plugins.IBlueprint)

    # IClick
    def get_commands(self):
        return cli.get_commands()

    # IBlueprint
    def get_blueprint(self):
        return views.get_blueprints()
