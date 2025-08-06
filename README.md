mancer-ready OP IO schema:
 - IN DAT `controls_in_dat`
 - OUT DAT `controls_out_dat`
 - OUT TOP `out1`

controls_in_dat DAT schema:
| Key | Value |
|-----|-------|
| fader1 | float:value |

controls_out_dat DAT schema:
| Key | Value |
|-----|-------|
| fader1 | float:value |
| label_fader1_control | string:control_name |
| label_fader1_value | string:value |

MIDI encoder spec:
 - should the hardware encoders loop from 360 to 0 or have software stops?
 - should the MCU send MIDI positions (0-360) or decrement/increment messages?
