# (c) 2020, James Freeman <james.freeman@example.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
def improve_automation(a):
       return a.replace("Puppet", "Ansible")
class FilterModule(object):
       '''improve_automation filters'''
       def filters(self):
           return {'improve_automation': improve_automation}
