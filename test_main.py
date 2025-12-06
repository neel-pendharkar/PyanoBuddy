from main import NoteSequenceGenerator

from scales import scales
from keys import keys 

def test_generate_note_sequence():
    note_sequences=[]
    trainer = NoteSequenceGenerator()
    for i in range(10):
        key = 'C#'
        scale = 'MAJOR'
        note_sequence = trainer.generate_note_sequence('C#', 'MAJOR', 5)
        note_sequences.append(note_sequence)
        assert len(note_sequence)==6
        assert note_sequence[0] == keys[key]
        for note in note_sequence:
            assert note - keys[key] in scales[scale]
    assert len([list(t) for t in dict.fromkeys(tuple(x) for x in note_sequences)]) > 1
    

