import rainbowhat
import time

TIMEOUT = 4 # Timeout in MS

rgb = [100,0,0]

#c = 261
d = 294
e = 329
f = 349
g = 392
a = 440
b = 493
c = 523

states = [
    [10,0,0, "Reed", a],
    [0,10,0, "Gren", b],
    [0,0,10, "Blue", c]
]

counts = [0,0,0]

#for note in [a,a,g,g,a,a,g,None,f,f,e,e,d,d,c,None,g,g,f,f,e,e,d,None,c,c,g,g,a,a,g,None,f,f,e,e,d,d,c,None]:
#    rainbowhat.buzzer.note(note,0.3,0.9)

@rainbowhat.touch.press()
def test(index):
    temp = rainbowhat.weather.temperature()
    pres = rainbowhat.weather.pressure()

    print("Touch: {}, Temp: {}, Pres: {}".format(index, temp, pres))

    r, g, b, text, note = states[index]

    counts[index] += 1

    rainbowhat.lights.rgb(r, g, b)
    rainbowhat.rainbow.set_all(r, g, b)
    rainbowhat.rainbow.show()
    rainbowhat.display.print_str(text)
    rainbowhat.display.show()
    rainbowhat.buzzer.note(note,0.30)

@rainbowhat.touch.release()
def test(index):
    print("Release:", index)

msg = ('I/-\\I/-\\O' * 2) + str(rainbowhat.weather.temperature())
offset = 0

def text():
    global offset

    rainbowhat.display.clear()
    rainbowhat.display.print_str(msg[offset:offset+4])
    rainbowhat.display.write_display()

    offset += 1
    if offset > len(msg) - 4:
        offset = 0

for x in range(len(msg)-4):
    text()
    time.sleep(0.1)

rainbowhat.display.print_float(rainbowhat.weather.temperature())
rainbowhat.display.show()




start = time.time()

while True:
    time.sleep(0.01)

    if counts[0] == 2 and counts[1] == 2 and counts[2] == 2:
        rainbowhat.display.print_str("OKAY")
        rainbowhat.display.show()
        break

    if time.time() - start > TIMEOUT:
        for x in [c,b,a,g,f,e,d]:
            rainbowhat.buzzer.note(x,0.1)
            time.sleep(0.2)

        rainbowhat.display.print_str("FAIL")
        rainbowhat.display.show()
        break
