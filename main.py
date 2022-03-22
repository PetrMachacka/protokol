radio.set_group(1)
radio.set_transmit_power(7)
radio.on_received_value(data_received)
radio.set_transmit_serial_number(True)
learn = 0
alarm = 0
data_list = [0]
send_learn = 0
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_event_longpressed)
input.on_button_pressed(Button.B, on_button_pressed_b)

# FOREVER
def on_forever():
    pass
# Main

def data_received(name, value):
    global data_list, alarm
    remote_serial = radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
    if learn == 1 and name == "send" and value == 1:
        if remote_serial not in data_list:
            data_list.append(remote_serial)
            print(data_list)
    if remote_serial in data_list and name == "alarm" and value == 1:
        music.play_tone(Note.C, 0)
    if remote_serial in data_list and name == "alarm" and value == 0:
        music.stop_all_sounds()




# LEARN
def on_logo_event_longpressed():
    global learn
    if learn == 0:
        learn = 1
    else:
        learn = 0
    print(learn)

# SEND_LEARN
def on_logo_event_pressed():
    radio.send_value("send", 1)

# ALARM ON
def on_button_pressed_a():

    radio.send_value("alarm", 1)

# ALARM OFF
def on_button_pressed_b():
    global alarm
    alarm = 0
    radio.send_value("alarm", 0)