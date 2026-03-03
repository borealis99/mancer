mancer-ready OP IO schema:
 - IN DAT `controls_in_dat`
 - OUT DAT `controls_out_dat`
 - OUT TOP `out1`

controls_in_dat DAT schema:
| Key | Value |
|-----|-------|
| hex0 | string: (hex color) |
| hex1 | string: (hex color) |
| beat | float:beat 0 <= x <= 1 |
| fader0 | float:value |
| fader1_click | float:value |
| button0 | float:value |

controls_out_dat DAT schema:
| Key | Value |
|-----|-------|
| fader0 | float:value |
| label_fader0_control | string:control_name |
| label_fader0_value | string:value |

MIDI Spec:
 - MCU will log encoder positions between 0 and 127.
 - MCU will not increment below 0 or above 127.
 - MCU will not loop the value range when incrementing past 0 or 127.
 - Encoders will send 0-127 on MIDI Channel 1 CC 70-79.
 - Encoder clicks will send 0 or 127 on MIDI Channel 1 CC 90-99.
 - Buttons will send 0 or 127 on MIDI Channel 1 CC 110-119.
 - MCU can receive new encoder positions (0-127) on encoder channels.
 - MCU will ignore messages sent to the button channels.

MIDI ALT Spec:
 - Buttons will send a momentary 127 on the encoder channels.

TD Patch Spec:
 - A 0->1 pulse on faderx_click will reset that parameter to a default value specified elsewhere in the patch.
