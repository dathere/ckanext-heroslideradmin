import datetime
import uuid
import json

from six import text_type
import sqlalchemy as sa
from sqlalchemy.orm import class_mapper
try:
    from sqlalchemy.engine.result import RowProxy
except:
    from sqlalchemy.engine import Row as RowProxy
import ckan.model as model


try:
    from ckan.plugins.toolkit import BaseModel
except ImportError:
    # CKAN <= 2.9
    from ckan.model.meta import metadata
    from sqlalchemy.ext.declarative import declarative_base


def _make_uuid():
    return text_type(uuid.uuid4())


class Hero_Slider(model.DomainObject, BaseModel):

    __tablename__ = 'hero_slider'
    id = sa.Column(sa.UnicodeText, primary_key=True, default=_make_uuid)
    image_url_1 = sa.Column(sa.UnicodeText, default=u'')
    hero_text_1 = sa.Column(sa.UnicodeText, default=u'')
    image_url_2 = sa.Column(sa.UnicodeText, default=u'')
    hero_text_2 = sa.Column(sa.UnicodeText, default=u'')
    image_url_3 = sa.Column(sa.UnicodeText, default=u'')
    hero_text_3 = sa.Column(sa.UnicodeText, default=u'')
    image_url_4 = sa.Column(sa.UnicodeText, default=u'')
    hero_text_4 = sa.Column(sa.UnicodeText, default=u'')
    image_url_5 = sa.Column(sa.UnicodeText, default=u'')
    hero_text_5 = sa.Column(sa.UnicodeText, default=u'')
    created = sa.Column(sa.DateTime, default=datetime.datetime.now())
    modified = sa.Column(sa.DateTime, default=datetime.datetime.now())

    @classmethod
    def get_hero_images(self):
        query = model.Session.query(self).autoflush(False)
        return query.first()


def table_dictize(obj, context, **kw):
    '''Get any model object and represent it as a dict'''
    result_dict = {}

    if isinstance(obj, RowProxy):
        fields = obj.keys()
    else:
        ModelClass = obj.__class__
        table = class_mapper(ModelClass).mapped_table
        fields = [field.name for field in table.c]

    for field in fields:
        name = field
        if name in ('current', 'expired_timestamp', 'expired_id'):
            continue
        if name == 'continuity_id':
            continue
        value = getattr(obj, name)
        if name == 'extras' and value:
            result_dict.update(json.loads(value))
        elif value is None:
            result_dict[name] = value
        elif isinstance(value, dict):
            result_dict[name] = value
        elif isinstance(value, int):
            result_dict[name] = value
        elif isinstance(value, datetime.datetime):
            result_dict[name] = value.isoformat()
        elif isinstance(value, list):
            result_dict[name] = value
        else:
            result_dict[name] = text_type(value)

    result_dict.update(kw)

    ##HACK For optimisation to get metadata_modified created faster.

    context['metadata_modified'] = max(result_dict.get('revision_timestamp', ''),
                                       context.get('metadata_modified', ''))

    return result_dict
