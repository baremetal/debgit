"""
Module for reprepro management
"""
from jinja2 import Template

class Section(object):
    """
    Class to create configuration sections.
    """
    def __init__(self, template_path):
        self.template_path = template_path

        self._template = None

    def render(self, section_name):
        """
        Use jinja to render a section from the specified template
        """

        template = Template(self.template)

        return template.render(section=section_name)

    @property
    def template(self):
        """
        Property to get the template contents.
        """

        if self._template:
            return self._template

        with open(self.template_path) as template_file:
            self._template = template_file.read()

        return self._template
