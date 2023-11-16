import ckan.plugins.toolkit as toolkit


def hero_slider_update(context, data_dict):
    return {'success':  False}

@toolkit.auth_allow_anonymous_access
def hero_slider_list(context, data_dict):
    return {'success': True}
