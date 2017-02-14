import jinja2

from yapylib.settings import JINJA2_ENV


def render_template(tpl, **context):
    template = JINJA2_ENV.get_template(tpl)
    rv = template.render(context)
    return rv
