import mido, random
from time import sleep, time
import rtmidi
import argparse

from NoteSequenceGenerator import NoteSequenceGenerator

class Looper():
    def __init__(self):
        self._out_port = mido.open_output(mido.get_output_names()[0])
        self._in_port = mido.open_input(mido.get_input_names()[0])
        self._notes = [60]
        self._note_count = 4
        self._timer = 5
        self._max_note_count = 1
        self._generator = NoteSequenceGenerator()
    
    def _play_note(self):
        for note in self._notes:
            self._out_port.send(mido.Message('note_on', note=note, velocity=100))
            sleep(0.2)
            self._out_port.send(mido.Message('note_off', note=note))

    def _listen_for_note(self):
        start_time = time()
        
        matched = []
        while time() - start_time < self._timer:  
            for msg in self._in_port.iter_pending():
                if msg.type == 'note_on' and msg.velocity > 0:
                    matched.append(msg.note)
                    if len(matched) == self._note_count:
                        break
            if matched == self._notes:
                return True
        print('Time up')
        return False
    
    def run_loop(self, key = 'C', scale = 'MAJOR'):
        self._streak = 0
        while True:
            if(self._streak > 20):
                self._streak = 0
                self._max_note_count +=1
                print(f'Streak reached! Max count is now {self._max_note_count}')

            key = key
            scale = scale
            self._note_count = random.choice(range(1,self._max_note_count+1))
            
            self._notes = self._generator.generate_note_sequence(key, scale, self._note_count)
            match = False
            while not match:
                self._play_note()
                match = self._listen_for_note()
                if match:
                    print(f"✅ Correct")
                    self._streak += 1
                else:
                    print("❌ Wrong note, listen again!\n")
                    self._streak = 0
                print(f'Streak: {self._streak}')
                
                sleep(0.5)
def main():        
    args = parse_args()
    looper = Looper()
    looper.run_loop(args.key, args.scale)
    
def parse_args():
    parser = argparse.ArgumentParser(
        description="PyanoBuddy. Connect your piano and play what's playing."
    )
    parser.add_argument(
        "--key",
        help="Key to practice. Eg. C",
        default = 'C'
    )
    parser.add_argument(
        "--scale",
        help="Scale to practice Eg. POWER_CHORD",
        default = 'POWER_CHORD'
    )
    return parser.parse_args()

if __name__=='__main__':
    main()