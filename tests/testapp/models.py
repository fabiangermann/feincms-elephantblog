# -*- coding:utf-8 -*-

from __future__ import absolute_import, unicode_literals

from elephantblog.models import Entry
from feincms.content.richtext.models import RichTextContent

Entry.register_regions(
    ('main', 'Main content area'),
)
Entry.register_extensions('feincms.module.extensions.translations',)
Entry.create_content_type(RichTextContent, cleanse=False, regions=('main',))
