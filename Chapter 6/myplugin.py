from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
  lookup: myplugin
  author: Daniel Oh
  version_added: "1.1"
  short_description: read a file stream
  description:
    - This plugin will return contents of a certain file.
  options:
    _terms:
       description: path(s) of files to read
       required: True
"""

from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase

class LookupModule(LookupBase):
  def run(self, terms, variables=None, **kwargs):

    returndata = []

    for singleterm in terms:
      lookupfile = self.find_file_in_search_path(variables, 'files', singleterm)
      try:
        if lookupfile:
          contents, show_data = self._loader._get_file_contents(lookupfile)
          returndata.append(contents.rstrip())
        else:
          raise AnsibleParserError()
      except AnsibleParserError:
        raise AnsibleError("Can't find a file: %s" % singleterm)
    return returndata


