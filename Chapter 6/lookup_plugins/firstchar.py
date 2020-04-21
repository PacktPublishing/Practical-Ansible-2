# (c) 2020, James Freeman <james.freeman@example.com>
# (c) 2012, Daniel Hokka Zakrisson <daniel@hozac.com>
# (c) 2017 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
    lookup: firstchar
    author: James Freeman <james.freeman@example.com>
    version_added: "2.9"
    short_description: read the first character of file contents
    description:
        - This lookup returns the first character of the contents from a file on the Ansible controller's file system.
    options:
      _terms:
        description: path(s) of files to read
        required: True
    notes:
      - if read in variable context, the file can be interpreted as YAML if the content is valid to the parser.
      - this lookup does not understand 'globing', use the fileglob lookup instead.
"""

EXAMPLES = """
- debug: msg="the first character in foo.txt is {{lookup('firstchar', '/etc/foo.txt') }}"

"""

RETURN = """
  _raw:
    description:
      - first character of content of file(s)
"""

from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display

display = Display()


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        ret = []
        for term in terms:
            display.debug("File lookup term: %s" % term)

            lookupfile = self.find_file_in_search_path(variables, 'files', term)

            display.vvvv(u"File lookup using %s as file" % lookupfile)
            try:
                if lookupfile:
                    contents, show_data = self._loader._get_file_contents(lookupfile)
                    ret.append(contents.rstrip()[0])
                else:
                    raise AnsibleParserError()
            except AnsibleParserError:
                raise AnsibleError("could not locate file in lookup: %s" % term)

        return ret
