# imports for encoders
import board
import digitalio
from rainbowio import colorwheel

import adafruit_seesaw.digitalio
import adafruit_seesaw.neopixel
import adafruit_seesaw.rotaryio
import adafruit_seesaw.seesaw

# imports for MIDI
import time
import usb_midi
import adafruit_midi
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
from adafruit_midi.control_change import ControlChange

# initialize encoders
import busio
i2c = busio.I2C(board.SCL, board.SDA)
seesaw = adafruit_seesaw.seesaw.Seesaw(i2c, 0x49)

# Note: We still create the encoder objects for switch functionality if needed
encoders = [adafruit_seesaw.rotaryio.IncrementalEncoder(seesaw, n) for n in range(4)]
switches = [adafruit_seesaw.digitalio.DigitalIO(seesaw, pin) for pin in (12, 14, 17, 9)]
for switch in switches:
    switch.switch_to_input(digitalio.Pull.UP)  # input & pullup!

# initialize MIDI
midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0) # MIDI channel is out_channel - 1

# Current MIDI CC values for each encoder (0-127)
current_cc_values = [64, 64, 64, 64]  # Start at center position
switches_pressed = [False, False, False, False] 

print("Encoder Delta MIDI Controller Ready")

while True:
    # Check encoder deltas directly from seesaw
    for n in range(4):
        delta = seesaw.encoder_delta(n)
        if delta != 0:
            print(f"Encoder {n} delta: {delta}")
            
            # Update the current CC value based on delta
            # Scale delta for smoother control (adjust multiplier as needed)
            cc_change = delta * -6  # Multiply for faster response, negate for positive rotation
            current_cc_values[n] += cc_change
            
            # Clamp to valid MIDI CC range (0-127)
            current_cc_values[n] = max(0, min(127, current_cc_values[n]))
            
            # Send MIDI CC message
            # Using CC numbers 1, 2, 3, 4 (you can adjust these)
            cc_number = n + 70
            midi.send(ControlChange(cc_number, current_cc_values[n]))
            
            print(f"Encoder {n} -> CC{cc_number}: {current_cc_values[n]}")
    
    # Check switches (optional - you can remove this if not needed)
    for n, switch in enumerate(switches):
        if (not switch.value) != switches_pressed[n]:  # Switch pressed (active low due to pullup)
            pressed = not switch.value
            print(f"Switch {n} now {pressed}")
            cc_number = n + 90
            midi.send(ControlChange(cc_number, 127*pressed))
            switches_pressed[n] = pressed
            print(f"Switches: {switches_pressed}")
    
    time.sleep(0.01)  # Small delay to prevent overwhelming the loop