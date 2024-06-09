import pcbnew

# RUN: exec(open("/Users/ashleyr/RailLed/Hardware/RailLed/railled.py").read())

def addTrace(sx, sy, ex, ey, top_n_bot=True, width=0.3):
    b = pcbnew.GetBoard()
    t = pcbnew.PCB_TRACK(b)
    t.SetStart(pcbnew.wxPointMM(sx, sy))
    t.SetEnd(pcbnew.wxPointMM(ex, ey))
    t.SetWidth(int(width * 1e6))
    if top_n_bot:
        t.SetLayer(pcbnew.F_Cu)
    else:
        t.SetLayer(pcbnew.B_Cu)
    b.Add(t)

def addVia(x, y):
    b = pcbnew.GetBoard()
    v = pcbnew.PCB_VIA(b)
    v.SetPosition(pcbnew.wxPointMM(x, y))
    v.SetDrill(int(0.4 * 1e6))
    v.SetWidth(int(0.8 * 1e6))
    b.Add(v)

SQR = 12

LED_ORIGIN = 50
LED_PITCH = 5

b = pcbnew.GetBoard()


# Arrange LEDs
for i in range(SQR):
    o = (i * SQR)
    even = ((i % 2) == 0)
    for j in range(SQR):
        m = b.FindFootprintByReference(f"D{o+j}")
        if even:
            p = pcbnew.wxPointMM(LED_ORIGIN+(i*LED_PITCH),LED_ORIGIN+((SQR-j-1)*LED_PITCH))
        else:
            p = pcbnew.wxPointMM(LED_ORIGIN+(i*LED_PITCH),LED_ORIGIN+(j*LED_PITCH))
        m.SetPosition(p)
        m.Rotate(p, 900)

# Add Power rails for LEDs
#   - Not last row
for i in range(SQR):
    for j in range(SQR-1):
        if((i % 2) == 0):
            start_x = LED_ORIGIN + 1.13 + (i*LED_PITCH)
            start_y = LED_ORIGIN - 1.13 + (j*LED_PITCH)
        else:
            start_x = LED_ORIGIN + (i*LED_PITCH)
            start_y = LED_ORIGIN + (j*LED_PITCH)

        if((i % 2) == 0):
            end_x = start_x + 1.880
            end_y = start_y + 1.143
        else:
            end_x = start_x - 1.880
            end_y = start_y + 1.854
        #addTrace(start_x,start_y,end_x,end_y,True,0.3)


# Place the LED Drivers
for i in range(0,6):
    # Driver ICs
    m = b.FindFootprintByReference(f"U{i}")
    p = pcbnew.wxPointMM(LED_ORIGIN+(2*i*LED_PITCH)-1.2,LED_ORIGIN-13)
    m.SetPosition(p)
    # DECAPs
    m = b.FindFootprintByReference(f"C{i+1}")
    p = pcbnew.wxPointMM(LED_ORIGIN+(2*i*LED_PITCH)+6.3,LED_ORIGIN-14.6)
    m.SetPosition(p)
    m.Rotate(p, 900)
    # Current RES
    m = b.FindFootprintByReference(f"R{i+2}")
    p = pcbnew.wxPointMM(LED_ORIGIN+(2*i*LED_PITCH)+4,LED_ORIGIN-16.1)
    m.SetPosition(p)
    m.Rotate(p, -900)

# Place ALL the SMPS
for i in range(8,15):
    m = b.FindFootprintByReference(f"U{i}")
    p = pcbnew.wxPointMM(LED_ORIGIN-7.43+(2*(i-8)*LED_PITCH),LED_ORIGIN+64.2)
    m.SetPosition(p)
for i in range(0,7):
    m = b.FindFootprintByReference(f"L{i}")
    p = pcbnew.wxPointMM(LED_ORIGIN-10.63+(2*i*LED_PITCH),LED_ORIGIN+69.2)
    m.SetPosition(p)
for i in range(0,7):
    m = b.FindFootprintByReference(f"C{12 + (3*i)}")
    p = pcbnew.wxPointMM(LED_ORIGIN-7+(2*i*LED_PITCH),LED_ORIGIN+58)
    m.SetPosition(p)
for i in range(0,7):
    m = b.FindFootprintByReference(f"C{10 + (3*i)}")
    p = pcbnew.wxPointMM(LED_ORIGIN-9.5+(2*i*LED_PITCH),LED_ORIGIN+58)
    m.SetPosition(p)
    m.Rotate(p, 1800)
for i in range(0,7):
    m = b.FindFootprintByReference(f"R{11 + (4*i)}")
    p = pcbnew.wxPointMM(LED_ORIGIN-12.5+(2*i*LED_PITCH),LED_ORIGIN+63.5)
    m.SetPosition(p)
for i in range(0,7):
    m = b.FindFootprintByReference(f"R{12 + (4*i)}")
    p = pcbnew.wxPointMM(LED_ORIGIN-11+(2*i*LED_PITCH),LED_ORIGIN+61.5)
    m.SetPosition(p)
    m.Rotate(p, 1800)
for i in range(0,7):
    m = b.FindFootprintByReference(f"C{11 + (3*i)}")
    p = pcbnew.wxPointMM(LED_ORIGIN-11+(2*i*LED_PITCH),LED_ORIGIN+60)
    m.SetPosition(p)
    m.Rotate(p, 1800)
for i in range(0,7):
    m = b.FindFootprintByReference(f"R{13 + (4*i)}")
    p = pcbnew.wxPointMM(LED_ORIGIN-5.5+(2*i*LED_PITCH),LED_ORIGIN+61)
    m.SetPosition(p)
    m.Rotate(p, 900)
for i in range(0,7):
    m = b.FindFootprintByReference(f"R{14 + (4*i)}")
    p = pcbnew.wxPointMM(LED_ORIGIN-5.5+(2*i*LED_PITCH),LED_ORIGIN+64)
    m.SetPosition(p)
    m.Rotate(p, 900)
m = b.FindFootprintByReference(f"R0")
p = pcbnew.wxPointMM(35.536,108.458)
m.SetPosition(p)
m.Rotate(p, 1800)
m = b.FindFootprintByReference(f"R1")
p = pcbnew.wxPointMM(35.536,109.982)
m.SetPosition(p)
m.Rotate(p, 1800)
m = b.FindFootprintByReference(f"C0")
p = pcbnew.wxPointMM(35.536,111.506)
m.SetPosition(p)
m.Rotate(p, 1800)


# Place MCU
m = b.FindFootprintByReference("U6")
p = pcbnew.wxPointMM(25,45)
m.SetPosition(p)

m = b.FindFootprintByReference("C8")
p = pcbnew.wxPointMM(22.3774,46.0128)
m.SetPosition(p)
m.Rotate(p, 900)

m = b.FindFootprintByReference("C7")
p = pcbnew.wxPointMM(22.3774,47.3964)
m.SetPosition(p)
m.Rotate(p, -900)

m = b.FindFootprintByReference("R8")
p = pcbnew.wxPointMM(22.3774,51.7666)
m.SetPosition(p)
m.Rotate(p, 900)

m = b.FindFootprintByReference("C9")
p = pcbnew.wxPointMM(22.3774,53.0098)
m.SetPosition(p)
m.Rotate(p, -900)



# Place the LED Driver VIAs
for i in range(0,6):
    for j in range(8):
        for k in range(2):
            x = LED_ORIGIN+(2*i*LED_PITCH)+2
            if(k == 1):
                x += 1
            y = (LED_ORIGIN-13) + 2 + j
            addVia(x,y)

# Place LED VIAs and wire
for i in range(SQR):
    o = (i * SQR)
    even = ((i % 2) == 0)
    # Wire up
    for j in range(SQR-4):
        y = LED_ORIGIN+((SQR-j-1)*LED_PITCH)
        if even:
            x = LED_ORIGIN+2+(i*LED_PITCH)
        else:
            x = LED_ORIGIN-2+(i*LED_PITCH)
        addVia(x,y)
        if even:
            addTrace(x,y,x-2,y)
            end_x = x - 4 + (j/2)
            addTrace(x,y,end_x,y,False)
            end_y = (LED_ORIGIN-13) + 2 + j
            addTrace(end_x,y,end_x,end_y,False)
            addTrace(end_x,end_y,end_x+4-(j/2),end_y,False)
        else:
            addTrace(x,y,x+2,y)
            end_x = x + 4 - (j/2)
            addTrace(x,y,end_x,y,False)
            end_y = (LED_ORIGIN-13) + 2 + j
            addTrace(end_x,y,end_x,end_y,False)
            addTrace(end_x,end_y,end_x-4+(j/2),end_y,False)
    # Wire VLED down
    y = LED_ORIGIN-1.55
    x = LED_ORIGIN+(i*LED_PITCH)
    if even:
        addTrace(x-1.7,y,x-1.7,y+58,width=1)
        addTrace(x-1.7,y+58,x+6.6,y+58,width=1)
    else:
        addTrace(x+1.7,y,x+1.7,y+58,width=1)
    for j in range(SQR):
        y = LED_ORIGIN-1.6+((SQR-j-1)*LED_PITCH)
        if even:
            addTrace(x,y,x-1.7,y,width=0.8)
        else:
            addTrace(x,y,x+1.7,y,width=0.8)

# Place Headers
for i,j in enumerate(["J1","J0","J2"]):
    m = b.FindFootprintByReference(j)
    p = pcbnew.wxPointMM(25,120-(18*i))
    m.SetPosition(p)
    m.Rotate(p, 900)
m = b.FindFootprintByReference("J3")
p = pcbnew.wxPointMM(25,120-(18*2)-(3*2.54))
m.SetPosition(p)
m.Rotate(p, 900)

# Place UART Res
m = b.FindFootprintByReference("R10")
p = pcbnew.wxPointMM(40,120-(18*2)-(3*2.54))
m.SetPosition(p)
m.Rotate(p, 1800)
m = b.FindFootprintByReference("R9")
p = pcbnew.wxPointMM(40,120-(18*2)-(4*2.54))
m.SetPosition(p)
m.Rotate(p, 1800)

# Place LDO
m = b.FindFootprintByReference("U7")
p = pcbnew.wxPointMM(43,90)
m.SetPosition(p)
m.Rotate(p, 900)

pcbnew.Refresh()

#def addVia(x, y):
#    b = pcbnew.GetBoard()
#    v = pcbnew.PCB_VIA(b)
#    v.SetPosition(pcbnew.wxPointMM(x, y))
#    v.SetDrill(int(0.4 * 1e6))
#    v.SetWidth(int(0.8 * 1e6))
#    b.Add(v)
#
#def addTrace(sx, sy, ex, ey, top_n_bot=True, width=0.3):
#    b = pcbnew.GetBoard()
#    t = pcbnew.PCB_TRACK(b)
#    t.SetStart(pcbnew.wxPointMM(sx, sy))
#    t.SetEnd(pcbnew.wxPointMM(ex, ey))
#    t.SetWidth(int(width * 1e6))
#    if top_n_bot:
#        t.SetLayer(pcbnew.F_Cu)
#    else:
#        t.SetLayer(pcbnew.B_Cu)
#    b.Add(t)
#
#name="x_uart_tx"
#
#with open(f'/Users/ashleyr/RTL-to-PCB/{name}.pcb', 'r+') as f:
#    pcb = f.read()
#
#with open(f'/Users/ashleyr/RTL-to-PCB/{name}.place', 'r+') as f:
#    place = f.read()
#
#
#lines = pcb.split('\n')
#size = len(lines)
#
#top = []
#via = []
#bot = []
#places = []
#for y,line in enumerate(pcb.split('\n')):
#    top.append([])
#    via.append([])
#    bot.append([])
#    for x,pos in enumerate(line.split(",")):
#        l = pos.split(":")
#        top[y].append(int(l[0]))
#        via[y].append(int(l[1]))
#        bot[y].append(int(l[2]))
#
#for y in range(size):
#    for x in range(size-1):
#        if (top[y][x] == top[y][x+1]) and (top[y][x] != -1):
#            addTrace(x,y,x+1,y,True)
#
#for x in range(size):
#    for y in range(size-1):
#        if (bot[y][x] == bot[y+1][x]) and (bot[y][x] != -1):
#            addTrace(x,y,x,y+1,False)
#
#for x in range(size):
#    for y in range(size):
#        if (via[y][x] != -1):
#            addVia(x,y)
#
#
#b = pcbnew.GetBoard()
#places = []
#for y,line in enumerate(place.split('\n')):
#    places.append([])
#    for x,name in enumerate(line.split(",")):
#        if name != "":
#            # Place the cell
#            m = b.FindFootprintByReference(name)
#            xs = (x * 15) + 2
#            ys = (y * 15) + 7
#            m.SetPosition(pcbnew.wxPointMM(xs,ys))
#
#            if name[0] in ["N","D"]:
#                # Input A track
#                addTrace(xs,ys,xs+1,ys,True)
#                addTrace(xs+1,ys,xs+1,ys-0.6,True)
#                addVia(xs+1,ys-0.6)
#                addTrace(xs+1,ys-0.6,xs+1,ys-3,False)
#
#                # Input B track
#                addTrace(xs,ys+0.65,xs+3,ys+0.65,True)
#                addTrace(xs+3,ys+0.65,xs+4,ys-0.6,True)
#                addVia(xs+4,ys-0.6)
#                addTrace(xs+4,ys-0.6,xs+4,ys-3,False)
#
#                # Output B track
#                addTrace(xs+2,ys+1.3,xs+4,ys+1.3,True)
#                addVia(xs+4,ys+1.3)
#                addTrace(xs+4,ys+1.3,xs+4,ys+3.9,False)
#
#                # VCC
#                addTrace(xs-1.5,ys-0.3,xs-1.5,ys-1.8,True)
#                addTrace(xs+2.2,ys,xs+2.2,ys-1.8,True)
#
#                # GND
#                addTrace(xs-1.5,ys+1.3,xs-1.5,ys+2.5,True)
#                addTrace(xs,ys+1.3,xs,ys+2.5,True)
#
#            elif name[0] == "I":
#                addTrace(xs,ys,xs+4,ys,True)
#                addVia(xs+4,ys)
#                addTrace(xs+4,ys,xs+4,ys+3.9,False)
#
#            elif name[0] == "O":
#                addTrace(xs,ys,xs+2,ys,True)
#                addVia(xs+2,ys)
#                addTrace(xs+2,ys,xs+1,ys,False)
#                addTrace(xs+1,ys,xs+1,ys-3,False)
#
#
#
#
#for y,line in enumerate(place.split('\n')):
#    start = -1
#    end = -1
#    for x,name in enumerate(line.split(",")):
#        if name != "":
#            if name[0] in ["D","N"]:
#                if start == -1:
#                    start = x
#                end = x
#    if end != -1:
#        # Horizontal
#        addTrace((start * 15)+0.6,(y*15)+5.2,size+3,(y*15)+5.2,True,1);
#        addTrace(-3,(y*15)+9.5,(end * 15)+2,(y*15)+9.5,True,1);
## Vertical
#addTrace(-3,9.5,-3,(y*15)+9.5,True,1);
#addTrace(size+3,5.2,size+3,(y*15)+5.2,True,1);
#
#
#pcbnew.Refresh()

