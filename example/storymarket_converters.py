from __future__ import absolute_import

from .models import ExampleStory
import django_storymarket.converters

def story_to_storymarket(api, obj):
    return {
        "type": "text",
        "subt_type": api.sub_types.filter(type='text',is_default=True)[0],
        "title": obj.headline,
        "author": "jacobian",
        "org": api.orgs.get(12),
        "category": api.subcategories.get(12),
        "content": obj.body,
    }

django_storymarket.converters.register(ExampleStory, story_to_storymarket)