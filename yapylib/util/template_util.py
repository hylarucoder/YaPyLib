import jinja2

loader = jinja2.FileSystemLoader(searchpath="template")
JINJA2_ENV = jinja2.Environment(loader=loader)


def render_template(tpl, **context):
    template = JINJA2_ENV.get_template(tpl)
    rv = template.render(context)
    return rv
