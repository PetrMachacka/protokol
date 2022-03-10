radio.set_group(1)
radio.set_transmit_power(7)
radio.on_received_value(data_received)
remote_serial = radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
learn = 0
alarm = 0

data_list = []
# FOREVER
def on_forever():
    if learn == 1:
        pass
basic.forever(on_forever)
# I DON´T KNOW
def data_received(name, value):
    control.in_background(onIn_background)

radio.set_transmit_serial_number(True)
# LONG PRESS
def on_logo_event_longpressed():
    global learn
    learn == 1
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_event_longpressed)
# SHORT PRESS
def on_logo_event_pressed():
    global learn
    learn = 0
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)
# ALARM ON
def on_button_pressed_a():
    global alarm
    alarm = 1
    radio.send_value("name", 1)
input.on_button_pressed(Button.A, on_button_pressed_a)
# ALARM OFF
def on_button_pressed_b():
    global alarm
    alarm = 0
input.on_button_pressed(Button.B, on_button_pressed_b)
def onIn_background():
    music.play_tone(Note.C, 3000)   
control.in_background(onIn_background)