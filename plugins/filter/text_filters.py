# (c) 2024, Andreas Kraftl <akraftl@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = '''
---
module: text_filters
short_description: Text transformation filters for Ansible.
description:
  - Provides a set of filters to perform common text transformations.
version_added: "1.0.0"
author: "Your Name"
options:
  to_upper:
    description:
      - Convert all characters in a string to uppercase.
    type: str
    required: True
  to_lower:
    description:
      - Convert all characters in a string to lowercase.
    type: str
    required: True
  reverse_text:
    description:
      - Reverse the order of characters in a string.
    type: str
    required: True
  remove_character:
    description:
      - Remove a character from a string at a specified position.
    options:
      text:
        description:
          - The text from which a character will be removed.
        type: str
        required: True
      position:
        description:
          - The 0-based position of the character to remove.
        type: int
        required: True
'''

EXAMPLES = '''
- name: Convert to uppercase
  debug:
    msg: "{{ 'hello' | training.example.to_upper }}"

- name: Convert to lowercase
  debug:
    msg: "{{ 'HELLO' | training.example.to_lower }}"

- name: Reverse text
  debug:
    msg: "{{ 'hello' | training.example.reverse_text }}"

- name: Remove character at position
  debug:
    msg: "{{ 'hello' | training.example.remove_character(1) }}"
'''

RETURN = '''
to_upper:
    description: The input string converted to uppercase.
    type: str
    returned: always
to_lower:
    description: The input string converted to lowercase.
    type: str
    returned: always
reverse_text:
    description: The input string with characters in reverse order.
    type: str
    returned: always
remove_character:
    description: The input string with the specified character removed.
    type: str
    returned: always
'''

from ansible.errors import AnsibleFilterError


def remove_character(text, position):
    """Entfernt einen Buchstaben aus dem Text an der angegebenen Position."""
    if not isinstance(text, str):
        raise AnsibleFilterError('remove_character erwartet einen String als ersten Parameter')
    if not (isinstance(position, int) and 0 <= position < len(text)):
        raise AnsibleFilterError('Die Position muss eine gültige ganze Zahl innerhalb der Textlänge sein')
    return text[:position] + text[position + 1:]


def to_upper(text):
    """Wandelt den gegebenen Text in Großbuchstaben um."""
    if not isinstance(text, str):
        raise AnsibleFilterError('to_upper erwartet einen String')
    return text.upper()


def to_lower(text):
    """Wandelt den gegebenen Text in Kleinbuchstaben um."""
    if not isinstance(text, str):
        raise AnsibleFilterError('to_lower erwartet einen String')
    return text.lower()


def reverse_text(text):
    """Kehrt die Reihenfolge der Zeichen im Text um."""
    if not isinstance(text, str):
        raise AnsibleFilterError('reverse_text erwartet einen String')
    return text[::-1]


class FilterModule(object):
    """Ansible Filter Plugin."""
    def filters(self):
        return {
            'to_upper': to_upper,
            'to_lower': to_lower,
            'reverse_text': reverse_text,
            'remove_character': remove_character
        }