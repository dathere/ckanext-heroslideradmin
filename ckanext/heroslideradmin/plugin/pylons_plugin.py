# encoding: utf-8
import ckan.plugins as plugins


class MixinPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IRoutes, inherit=True)

    # IRoutes
    def before_map(self, map):
        ctrl = 'ckanext.heroslideradmin.controller:HeroSliderAdminController'
        map.connect(
            'hero_slider_admin',
            '/ckan-admin/hero_slider_admin',
            action='hero_slider_admin',
            ckan_icon='picture',
            controller=ctrl
        )
        return map
