# -*- coding: utf-8 -*-
import random
import datetime
import logging
from django import template
from django.db.models import Count

register = template.Library()

def widget_categories_menu():
    categories = []
    #try:
        #from aquasite.apps.blog.models import Category
        #categories = Category.objects.all().order_by('sort', 'name').exclude(deleted=True)
    #except:
    #    logging.exception('Error in widget w_categories_menu')
    return {'categories': categories}

def widget_tags_menu():
    tags = []
    #try:
    #    from aquasite.apps.blog.models import Tag
    #    tags = Tag.objects.all().order_by('name').exclude(deleted=True)
    #except:
    #    logging.exception('Error in widget w_tags_menu')
    return {'tags': tags}

def widget_links_menu():
    return {}

register.inclusion_tag('widgets/categories.html')(widget_categories_menu)
register.inclusion_tag('widgets/tags.html')(widget_tags_menu)
register.inclusion_tag('widgets/links.html')(widget_links_menu)
