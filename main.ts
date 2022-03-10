radio.setGroup(1)
radio.setTransmitPower(7)
radio.onReceivedValue(function data_received(name: string, value: number) {
    control.inBackground(onIn_background)
})
let remote_serial = radio.receivedPacket(RadioPacketProperty.SerialNumber)
let learn = 0
let alarm = 0
let data_list = []
//  FOREVER
basic.forever(function on_forever() {
    if (learn == 1) {
        
    }
    
})
//  I DON´T KNOW
radio.setTransmitSerialNumber(true)
//  LONG PRESS
input.onLogoEvent(TouchButtonEvent.LongPressed, function on_logo_event_longpressed() {
    
    learn == 1
})
//  SHORT PRESS
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_event_pressed() {
    
    learn = 0
})
//  ALARM ON
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    alarm = 1
    radio.sendValue("name", 1)
})
//  ALARM OFF
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    alarm = 0
})
function onIn_background() {
    music.playTone(Note.C, 3000)
}

control.inBackground(onIn_background)
