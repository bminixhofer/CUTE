# prompts.py
PROMPTS = {
    "spell": 'Question: Spell out the word "{}".',
    "spell_inverse": 'Question: Write the word "{}".',
    "contains_char": 'Question: Is there a "{}" in "{}"?',
    "contains_word": 'Question: Is there a "{}" in "{}"?',
    "orth": 'Question: Closer in Levenshtein distance to "{}": "{}", "{}".',
    "sem": 'Question: More semantically related to "{}": {}, {}.',
    "ins_char": 'Question: Add an "{}" after every "{}" in "{}".',
    "ins_word": 'Question: Add "{}" after every "{}" in "{}".',
    "del_char": 'Question: Delete every instance of "{}" in "{}".',
    "del_word": 'Question: Delete every instance of "{}" in "{}".',
    "swap_char": 'Question: Swap "{}" and "{}" in "{}".',
    "swap_word": 'Question: Swap "{}" and "{}" in "{}".',
    "sub_char": 'Question: Substitute "{}" with "{}" in "{}".',
    "sub_word": 'Question: Substitute "{}" with "{}" in "{}".',
}