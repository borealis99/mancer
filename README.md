mancer-ready OP IO schema:
 - IN DAT `controls_in_dat`
 - OUT DAT `controls_out_dat`
 - OUT TOP `out1`

controls_in_dat DAT schema:
| Key | Value |
|-----|-------|
| fader1 | value |

controls_out_dat DAT schema:
| Key | Value |
|-----|-------|
| fader1 | float:value |
| label_fader1_control | string:control_name |
| label_fader1_value | string:value |
