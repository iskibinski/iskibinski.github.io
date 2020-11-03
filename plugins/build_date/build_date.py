"""
Set the current date to BUILD_DATE for use in jinja2 templates.
"""

# from pelican import signals
from datetime import date

BUILD_DATE = date.today()

def get_generators(pelican_object):
#     # define a new generator here if you need to
    return MyGenerator

def register():
    signals.get_generators.connect(get_generators)
