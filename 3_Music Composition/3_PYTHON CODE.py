import numpy as np 
from music21 import instrument, note, stream, chord 
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import LSTM, Dropout, Dense, Activation 
from tensorflow.keras.utils import to_categorical 
import random 
 
# Generate dummy note sequences for demonstration 
def generate_dummy_notes(n=1000): 
    pitch_names = ['C', 'D', 'E', 'F', 'G', 'A', 'B'] 
    octaves = [3, 4, 5] 
    return [random.choice(pitch_names) + str(random.choice(octaves)) for _ in range(n)] 
 
notes = generate_dummy_notes() 
 
# Map notes to integers 
pitchnames = sorted(set(notes)) 
note_to_int = {note: number for number, note in enumerate(pitchnames)} 
 
# Prepare sequences 
sequence_length = 100 
network_input = [] 
network_output = [] 
 
for i in range(len(notes) - sequence_length): 
    seq_in = notes[i:i + sequence_length] 
    seq_out = notes[i + sequence_length] 
    network_input.append([note_to_int[char] for char in seq_in]) 
    network_output.append(note_to_int[seq_out]) 
 
n_patterns = len(network_input) 
n_vocab = len(pitchnames) 
 
X = np.reshape(network_input, (n_patterns, sequence_length, 1)) 
X = X / float(n_vocab) 
8 
 
y = to_categorical(network_output) 
# Build the model 
model = Sequential([ 
    LSTM(256, input_shape=(X.shape[1], X.shape[2]), return_sequences=True), 
    Dropout(0.3), 
    LSTM(256), 
    Dense(256), 
    Dropout(0.3), 
    Dense(n_vocab), 
    Activation('softmax') 
]) 
model.compile(loss='categorical_crossentropy', optimizer='adam') 
 
# Train the model (for demo, only 1 epoch) 
model.fit(X, y, epochs=1, batch_size=64) 
 
# Generate music 
start = np.random.randint(0, len(network_input)-1) 
pattern = network_input[start] 
output_notes = [] 
 
for _ in range(100): 
    prediction_input = np.reshape(pattern, (1, len(pattern), 1)) 
    prediction_input = prediction_input / float(n_vocab) 
 
    prediction = model.predict(prediction_input, verbose=0) 
    
    index = np.argmax(prediction) 
    result = pitchnames[index] 
    output_notes.append(note.Note(result)) 
 
    pattern.append(index) 
    pattern = pattern[1:] 
# Create MIDI stream 
midi_stream = stream.Stream(output_notes) 
midi_stream.write('midi', fp='generated_music.mid') 
print("MIDI file saved as 'generated_music.mid'")