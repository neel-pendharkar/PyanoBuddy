import random

from scales import scales
from keys import keys

class NoteSequenceGenerator:
    def generate_note_sequence(self, key, scale, length):
        note_choices = random.choices(scales[scale], k=length)
        return [keys[key]]+[keys[key] + choice for choice in note_choices]
