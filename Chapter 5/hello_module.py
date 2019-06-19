#!/usr/bin/python

ANSIBLE_METADATA = {'metadata_version': '1.1',
                   'status': ['preview'],
                   'supported_by': 'community'}
DOCUMENTATION = '''
module: my_custom_module
short_description: This is my custom module
version_added: "1.0"
description:
  - "This is a description what my first module is"
options:
  option_name:
    description:
      - Some details of this option
    required: true or false
'''

EXAMPLES = '''
- name: Print instant messages
  modulename:
    name: hi custom module
'''

RETURN = '''
message:
  description: The message that the module prints
  type: str
'''

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec = dict(
            name      = dict(required=True)
        )
    )
    response = "hello"
    module.exit_json(changed=True, message=response)


if __name__ == '__main__':
    main()
