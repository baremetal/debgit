from jinja2 import Template

class Section(object):
    def __init__(self, template_path):
        self.template_path = template_path

        self._template = None

    def render(self, section_name):
        template = Template(self.template)

        return template.render(section=section_name)

    @property
    def template(self):
        if self._template:
            return self._template

        with open(self.template_path) as fh:
            self._template = fh.read()

        return self._template
