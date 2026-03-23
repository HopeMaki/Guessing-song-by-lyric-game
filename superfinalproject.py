from tkinter import*
import random
from tkinter import messagebox
import sys 
def maindata():
    root = Tk()
    root.title("เกมทายเพลง")
    root.geometry("1024x768")
    root.option_add('*font', 'tahoma 10 bold')
    #abuout da background
    frame = Frame(root)
    frame.config(background="cyan")
    frame.place(width=1024, height=768, x=0, y=0)
    photo=PhotoImage(file="bg.gif")
    label1 = Label(frame, image=photo)
    label1.place(width=1024, height=768,x = 0, y = 0) 
    #commandplay
    def choosetype():
        root.destroy()
        choosetype=Tk()
        choosetype.title("เกมทายเพลง")
        choosetype.geometry("1024x768")
        #background
        frame = Frame(choosetype)
        frame.config(background="cyan")
        frame.place(width=1024, height=768, x=0, y=0)
        photo2=PhotoImage(file="choosetype.gif")
        label1 = Label(frame, image=photo2)
        label1.place(width=1024, height=768,x = 0, y = 0)
        #gamepart
        def folksongpart():
            choosetype.destroy()
            folksongpart=Tk()
            folksongpart.title("เกมทายเพลง")
            folksongpart.geometry("1024x768")
            #background
            frame = Frame(folksongpart)
            frame.config(background="cyan")
            frame.place(width=1024, height=768, x=0, y=0)
            photo2=PhotoImage(file="bg2.gif")
            label1 = Label(frame, image=photo2)
            label1.place(width=1024, height=768,x = 0, y = 0)
            def pick_random_key_from_dict(folksong: dict):
                keys = list(folksong.keys())
                random_key = random.choice(keys)
                return random_key
            def checkans():
                answer=entry.get()
                if answer==songname:
                    folksongpart.destroy()
                    correctans=Tk()
                    correctans.title("เกมทายเพลง")
                    correctans.geometry("1024x768")
                    #background
                    frame = Frame(correctans)
                    frame.config(background="cyan")
                    frame.place(width=1024, height=768, x=0, y=0)
                    photocor=PhotoImage(file="correctans.gif")
                    label1 = Label(frame, image=photocor)
                    label1.place(width=1024, height=768,x = 0, y = 0)
                    #command
                    def exit():
                        correctans.destroy()
                    def playagain():
                        correctans.destroy()
                        maindata()
                    #button
                    bpa= Button(frame, text="เล่นอีกครั้ง",font='Garuda 30 bold' ,command=playagain,bg="#00C5A7")
                    bpa.place(width=230, height=120,x=77, y=591)
                    bexit = Button(frame, text="ออก",font='Garuda 30 bold' ,command=exit,bg="#00C5A7")
                    bexit.place(width=230, height=120,x=717, y=591)
                    correctans.mainloop()
                else:
                    folksongpart.destroy()
                    wrongans=Tk()
                    wrongans.title("เกมทายเพลง")
                    wrongans.geometry("1024x768")
                    #background
                    frame = Frame(wrongans)
                    frame.config(background="cyan")
                    frame.place(width=1024, height=768, x=0, y=0)
                    photowro=PhotoImage(file="wrongans.gif")
                    label1 = Label(frame, image=photowro)
                    label1.place(width=1024, height=768,x = 0, y = 0)
                    #command
                    def exit():
                        wrongans.destroy()
                    def showans():
                        showans = Message(frame, text=songname, width=600,font='Garuda 30 bold' , 
                    anchor=CENTER,bg="white")
                        showans.place(width=600, height=190,x=212, y=288)
                    def playagain():
                        wrongans.destroy()
                        maindata()
                    #button
                    bpa= Button(frame, text="เล่นอีกครั้ง",font='Garuda 30 bold' ,command=playagain,bg="#00C5A7")
                    bpa.place(width=230, height=120,x=77, y=591)
                    bexit = Button(frame, text="ออก",font='Garuda 30 bold' ,command=exit,bg="#00C5A7")
                    bexit.place(width=230, height=120,x=717, y=591)
                    bans= Button(frame, text="เฉลย",font='Garuda 30 bold' ,command=showans,bg="#00C5A7")
                    bans.place(width=230, height=120,x=397, y=591)
                    wrongans.mainloop()

            folksong = {'แก้มน้องนางนั้นแดงกว่าใคร':[	'ฝากดวงใจ\n พี่ลอยล่องไปบนนภา\n สุดขอบฟ้า หัวใจพี่จะไปถึง'],
            'จ่าหน้าซองถึงน้องพี่':[	'รักของพี่นี้\n มีให้เธอในวันนั้น\n ถึงวันนี้ยังอยู่ ฝากบอกดวงดาวให้เธอ'],
            'อ้ายนี้ยังกอยอยู่':[	'แม่หญิงเมืองกรุง\nมาป๊ะมาปรุงเนื้อเวียงเชียงใหม่\n เดี๋ยวนะเดี๋ยวเน้อหัวใจ\nมันเป็นจะไดเต้นแฮงแต้ ๆ'],
            'อะไรเอ่ยสวยกว่า..ทะเล':[	'ช่วงเวลานี้ช่างดีจัง ได้นั่งชายฝั่งมองทะเล\n อากาศสดใสและโพล้เพล้\n นั่งมองทะเลข้าง ๆ เธอ'],
            'ภาษารักไม่บอกรัก':[	'เธอไม่เอ่ยรักฉันเลยสักคำ\n แต่เธอแสดงด้วยการกระทำ\n เมื่อก่อนน้อยใจเธอเองด้วยซ้ำ'],
            'ฉันเป็นแมลง':[	'เป็นดั่งดอกไม้\n กลิ่นหอมยั่วใจ\n คอยล่อแมลงตัวใดบินหลงเข้าไปไม่อาจถอน'],
            'หนีห่าง':[	'นั่งมองดูดวงดาว\n ฉันมองเห็นเธอสุกสกาว\n ส่องแสงเรืองรองนับกลางใจ'],
            'ภาพฝันในจักรวาล':[	'เธอคือภาพฝันในจักรวาลของฉัน\n ดวงดาวส่องแสงวับวาวเมื่อพบเจอ'],
            'ใจรัก':[	'เมื่อดวงใจมีรักมอบแด่ใครซักคน\n หมดทุกห้องหัวใจขอให้เธอมั่นใจรักจริง'],
            'ใครงามเลิศในปฐพี':[	'บางสิ่งนั้น ฉันเคยว่าดีพอผ่านนานปี\n ก็มีอื่นใดมาทดแทน']}
            songname = pick_random_key_from_dict(folksong)
            #print(random_key)
            hint = folksong[songname]
            message3 = Message(frame, text=hint, width=600,font='Garuda 30 bold' , 
            anchor=CENTER,bg="#00C5A7")
            message3.place(width=600, height=190,x=212, y=288)
            entry = Entry(folksongpart, width= 25,font=20)
            entry.place(x=352, y=553)
            Button(folksongpart, text= "Click to Check", command= checkans).place(x=700, y=553)
            folksongpart.mainloop()
        def forlifepart():
            choosetype.destroy()
            forlifepart=Tk()
            forlifepart.title("เกมทายเพลง")
            forlifepart.geometry("1024x768")
            #background
            frame = Frame(forlifepart)
            frame.config(background="cyan")
            frame.place(width=1024, height=768, x=0, y=0)
            photo2=PhotoImage(file="bg2.gif")
            label1 = Label(frame, image=photo2)
            label1.place(width=1024, height=768,x = 0, y = 0)
            def pick_random_key_from_dict(forlife: dict):
                keys = list(forlife.keys())
                random_key = random.choice(keys)
                return random_key
            def checkans():
                answer=entry.get()
                if answer==songname:
                    forlifepart.destroy()
                    correctans=Tk()
                    correctans.title("เกมทายเพลง")
                    correctans.geometry("1024x768")
                    #background
                    frame = Frame(correctans)
                    frame.config(background="cyan")
                    frame.place(width=1024, height=768, x=0, y=0)
                    photocor=PhotoImage(file="correctans.gif")
                    label1 = Label(frame, image=photocor)
                    label1.place(width=1024, height=768,x = 0, y = 0)
                    #command
                    def exit():
                        correctans.destroy()
                    def playagain():
                        correctans.destroy()
                        maindata()
                    #button
                    bpa= Button(frame, text="เล่นอีกครั้ง",font='Garuda 30 bold' ,command=playagain,bg="#00C5A7")
                    bpa.place(width=230, height=120,x=77, y=591)
                    bexit = Button(frame, text="ออก",font='Garuda 30 bold' ,command=exit,bg="#00C5A7")
                    bexit.place(width=230, height=120,x=717, y=591)
                    correctans.mainloop()
                else:
                    forlifepart.destroy()
                    wrongans=Tk()
                    wrongans.title("เกมทายเพลง")
                    wrongans.geometry("1024x768")
                    #background
                    frame = Frame(wrongans)
                    frame.config(background="cyan")
                    frame.place(width=1024, height=768, x=0, y=0)
                    photowro=PhotoImage(file="wrongans.gif")
                    label1 = Label(frame, image=photowro)
                    label1.place(width=1024, height=768,x = 0, y = 0)
                    #command
                    def exit():
                        wrongans.destroy()
                    def showans():
                        showans = Message(frame, text=songname, width=600,font='Garuda 30 bold' , 
                    anchor=CENTER,bg="white")
                        showans.place(width=600, height=190,x=212, y=288)
                    def playagain():
                        wrongans.destroy()
                        maindata()
                    #button
                    bpa= Button(frame, text="เล่นอีกครั้ง",font='Garuda 30 bold' ,command=playagain,bg="#00C5A7")
                    bpa.place(width=230, height=120,x=77, y=591)
                    bexit = Button(frame, text="ออก",font='Garuda 30 bold' ,command=exit,bg="#00C5A7")
                    bexit.place(width=230, height=120,x=717, y=591)
                    bans= Button(frame, text="เฉลย",font='Garuda 30 bold' ,command=showans,bg="#00C5A7")
                    bans.place(width=230, height=120,x=397, y=591)
                    wrongans.mainloop()
            forlife={'ขอนไม้กับเรือ':	['โดดเดี่ยวเดียวดายในท้องเล\nลมพัดลมเพลอยมาไกล\nเป็นแค่ขอนไม้ไม่มีทิศทาง'],
    'หนอนผีเสื้อ':	['แค่ใช้น้ำค้างเพื่อพอประทัง\nตายังมองชื่นชมแค่เพียงดอกไม้\nไม่เคยคิดมองตัวเอง'],
    'ขวัญใจพี่หลวง':	['ทุกคืนทุกวันเวลารอเธอกลับ หวนคืนที่เดิมที่เธอจากลานี่ห้าปีกว่าก็ยังไม่เห็นแม้เงา'],
    '11 ร.ด.':	['งูพิษ งูเห่า ที่เขาว่าร้าย\n เป็นต้องชิดซ้าย เมื่อได้เจอเธอ\n เสือ สิงห์ กระทิงป่าที่เคยได้เจอ'],
    'กลับกลาย':	['เพราะทุก ๆ อย่างรอบข้างเราเคลื่อนไหว\nเพราะทุกๆอย่างทำคนรอบข้างเราเปลี่ยนไป'],
    'เสมอ':	['หลีกหนีไม่พ้นไม่หลงทาง\nทางเก่าซ้ำซ้ำไม่พ้นเดิมเดิม'],
    'ลมเพลมพัด':	['พี่สร้างศิลปะ\nศิลศิลศิล\nศิลปะเนื้อตัวมอมแมมผมยาวรุงรัง'],
    'วณิพก':	['จึงมาเป็นวณิพกพเนจร\n เที่ยวเร่ร่อน\n ร้องเพลงแลกเศษเงิน'],
    'เวลคัมทูไทยแลนด์':	['ทอมทอมแวร์ยูโกลาสไนท์ไอเลิฟเมืองไทย \nไอไลค์พัฒพงศ์'],
    'ยายสา':	['ยืนรอความหวังกับท้องทะเลที่ว่างเปล่า\nตั้งแต่ค่ำยันเช้าก็ไม่เห็นหน้าเธอ\nยังอยู่ตรงนี้ยังรอคอยเธออยู่เสมอ']
    }
            songname = pick_random_key_from_dict(forlife)
            #print(random_key)
            hint = forlife[songname]
            message3 = Message(frame, text=hint, width=600,font='Garuda 30 bold' , 
            anchor=CENTER,bg="#00C5A7")
            message3.place(width=600, height=190,x=212, y=288)
            entry = Entry(forlifepart, width= 25,font=20)
            entry.place(x=352, y=553)
            Button(forlifepart, text= "Click to Check", command= checkans).place(x=700, y=553)
            forlifepart.mainloop()
        def hiphoppart():
            choosetype.destroy()
            hiphoppart=Tk()
            hiphoppart.title("เกมทายเพลง")
            hiphoppart.geometry("1024x768")
            #background
            frame = Frame(hiphoppart)
            frame.config(background="cyan")
            frame.place(width=1024, height=768, x=0, y=0)
            photo2=PhotoImage(file="bg2.gif")
            label1 = Label(frame, image=photo2)
            label1.place(width=1024, height=768,x = 0, y = 0)
            def pick_random_key_from_dict(hiphop: dict):
                keys = list(hiphop.keys())
                random_key = random.choice(keys)
                return random_key
            def checkans():
                answer=entry.get()
            def checkans():
                answer=entry.get()
                if answer==songname:
                    hiphoppart.destroy()
                    correctans=Tk()
                    correctans.title("เกมทายเพลง")
                    correctans.geometry("1024x768")
                    #background
                    frame = Frame(correctans)
                    frame.config(background="cyan")
                    frame.place(width=1024, height=768, x=0, y=0)
                    photocor=PhotoImage(file="correctans.gif")
                    label1 = Label(frame, image=photocor)
                    label1.place(width=1024, height=768,x = 0, y = 0)
                    #command
                    def exit():
                        correctans.destroy()
                    def playagain():
                        correctans.destroy()
                        maindata()
                    #button
                    bpa= Button(frame, text="เล่นอีกครั้ง",font='Garuda 30 bold' ,command=playagain,bg="#00C5A7")
                    bpa.place(width=230, height=120,x=77, y=591)
                    bexit = Button(frame, text="ออก",font='Garuda 30 bold' ,command=exit,bg="#00C5A7")
                    bexit.place(width=230, height=120,x=717, y=591)
                    correctans.mainloop()
                else:
                    hiphoppart.destroy()
                    wrongans=Tk()
                    wrongans.title("เกมทายเพลง")
                    wrongans.geometry("1024x768")
                    #background
                    frame = Frame(wrongans)
                    frame.config(background="cyan")
                    frame.place(width=1024, height=768, x=0, y=0)
                    photowro=PhotoImage(file="wrongans.gif")
                    label1 = Label(frame, image=photowro)
                    label1.place(width=1024, height=768,x = 0, y = 0)
                    #command
                    def exit():
                        wrongans.destroy()
                    def showans():
                        showans = Message(frame, text=songname, width=600,font='Garuda 30 bold' , 
                    anchor=CENTER,bg="white")
                        showans.place(width=600, height=190,x=212, y=288)
                    def playagain():
                        wrongans.destroy()
                        maindata()
                    #button
                    bpa= Button(frame, text="เล่นอีกครั้ง",font='Garuda 30 bold' ,command=playagain,bg="#00C5A7")
                    bpa.place(width=230, height=120,x=77, y=591)
                    bexit = Button(frame, text="ออก",font='Garuda 30 bold' ,command=exit,bg="#00C5A7")
                    bexit.place(width=230, height=120,x=717, y=591)
                    bans= Button(frame, text="เฉลย",font='Garuda 30 bold' ,command=showans,bg="#00C5A7")
                    bans.place(width=230, height=120,x=397, y=591)
                    wrongans.mainloop()

            hiphop={'มีแค่เรา':   ['เธอไปกับใครตั้งกี่คน มึงก็ยังทนอยู่ เมียมึงอย่างซุก แม่งอย่างซน มึงว่ามึงเอาอยู่'], 
            'เป็นไรไหม':    ['เธอรู้ดีว่าต้องเจอคนใจร้าย เธอเป็น Good Girl แต่เขาไม่ใช่ Goog Guy'],
            'ครั้งสุดท้าย':	['ขอบคุณนะ แต่พอแล้ว กับความเศร้า ที่มืดมน ฉันเจ็บช้ำ Im so sad ที่เห็นเธออยู่ด้วยกัน'],
            'MORNING':	['แสงมันลอดออกมาจากม่านมาผ่านกระทบลงตรงเตียง มองเห็นหมอนที่นอนที่เราสองเคยได้นอนเคียง'],
            'เสือสิ้นลาย':	['เล่นแต่บทผู้ร้าย ร้าย ร้าย แต่ตอนนี้เป็นเสือสิ้นลาย You Look into My Eyes สาบานให้ตาย ตาย ตาย'],
            'เป็นได้ทุกอย่าง':	['ก็เป็น Wikipedia ตอนที่เธอเกิดอยากรู้อะไร เป็น Google Map ตอนที่เธออยากจะไปที่ไหนต่อไหน'],
            'วายร้าย':	['เธอมีโลกของเธอฉันมีโลกของฉัน คงจะไม่มีวันที่เราจะได้รักกัน นิยายขายดีก็ต้องมีวายร้ายและฉันก็รู้ดี'],
            'Very Very Small':	['เคยยืนรอเธอบน BTS ฉันไม่ได้คิดเรื่อง sex แค่เดินเข้าโรงเรียนด้วยกัน'],
            'ธาตุทองซาวด์':	['อีกี้นี้มันเป็นสก้อย ไปกับผู้บ่อย ผู้พาไป skrt อีกี้ชอบไป skrt แต่เปลี่ยนผู้บ่อย สงสัยไม่เวิร์ก'],
            'Microphone':   ['และนี่ชื่ออะไร What is your name และนี่คุณเป็นใคร Tell me tell me baby']}
            songname = pick_random_key_from_dict(hiphop)
            #print(random_key)
            hint = hiphop[songname]
            message3 = Message(frame, text=hint, width=600,font='Garuda 30 bold' , 
            anchor=CENTER,bg="#00C5A7")
            message3.place(width=600, height=190,x=212, y=288)
            entry = Entry(hiphoppart, width= 25,font=20)
            entry.place(x=352, y=553)
            Button(hiphoppart, text= "Click to Check", command= checkans).place(x=700, y=553)
            hiphoppart.mainloop()
        def lukthungpart():
            choosetype.destroy()
            lukthungpart=Tk()
            lukthungpart.title("เกมทายเพลง")
            lukthungpart.geometry("1024x768")
            #background
            frame = Frame(lukthungpart)
            frame.config(background="cyan")
            frame.place(width=1024, height=768, x=0, y=0)
            photo2=PhotoImage(file="bg2.gif")
            label1 = Label(frame, image=photo2)
            label1.place(width=1024, height=768,x = 0, y = 0)
            def pick_random_key_from_dict(lukthung: dict):
                keys = list(lukthung.keys())
                random_key = random.choice(keys)
                return random_key
            def checkans():
                answer=entry.get()
                if answer==songname:
                    lukthungpart.destroy()
                    correctans=Tk()
                    correctans.title("เกมทายเพลง")
                    correctans.geometry("1024x768")
                    #background
                    frame = Frame(correctans)
                    frame.config(background="cyan")
                    frame.place(width=1024, height=768, x=0, y=0)
                    photocor=PhotoImage(file="correctans.gif")
                    label1 = Label(frame, image=photocor)
                    label1.place(width=1024, height=768,x = 0, y = 0)
                    #command
                    def exit():
                        correctans.destroy()
                    def playagain():
                        correctans.destroy()
                        maindata()
                    #button
                    bpa= Button(frame, text="เล่นอีกครั้ง",font='Garuda 30 bold' ,command=playagain,bg="#00C5A7")
                    bpa.place(width=230, height=120,x=77, y=591)
                    bexit = Button(frame, text="ออก",font='Garuda 30 bold' ,command=exit,bg="#00C5A7")
                    bexit.place(width=230, height=120,x=717, y=591)
                    correctans.mainloop()
                else:
                    lukthungpart.destroy()
                    wrongans=Tk()
                    wrongans.title("เกมทายเพลง")
                    wrongans.geometry("1024x768")
                    #background
                    frame = Frame(wrongans)
                    frame.config(background="cyan")
                    frame.place(width=1024, height=768, x=0, y=0)
                    photowro=PhotoImage(file="wrongans.gif")
                    label1 = Label(frame, image=photowro)
                    label1.place(width=1024, height=768,x = 0, y = 0)
                    #command
                    def exit():
                        wrongans.destroy()
                    def showans():
                        showans = Message(frame, text=songname, width=600,font='Garuda 30 bold' , 
                    anchor=CENTER,bg="white")
                        showans.place(width=600, height=190,x=212, y=288)
                    def playagain():
                        wrongans.destroy()
                        maindata()
                    #button
                    bpa= Button(frame, text="เล่นอีกครั้ง",font='Garuda 30 bold' ,command=playagain,bg="#00C5A7")
                    bpa.place(width=230, height=120,x=77, y=591)
                    bexit = Button(frame, text="ออก",font='Garuda 30 bold' ,command=exit,bg="#00C5A7")
                    bexit.place(width=230, height=120,x=717, y=591)
                    bans= Button(frame, text="เฉลย",font='Garuda 30 bold' ,command=showans,bg="#00C5A7")
                    bans.place(width=230, height=120,x=397, y=591)
                    wrongans.mainloop()
            lukthung={'ผู้สาวขาเลาะ' : ['เพียงแค่จอบแนมซอมเบิ่งอ้ายอยู่ไกลๆ หัวใจน้องนี้ก็มีแฮง ฮู้ว่าอ้ายมีเขา น้องกะสิบ่ขอแข่ง'],
            'คำแพง' : ['เขามีความหมายกับเจ้า เจ้ามีความหมายต่ออ้าย เจ้าให้เขาหมดใจหมดกาย'] ,
            'ไม่มีข้อแม้ตั้งแต่เริ่มต้น' : ['อยากให้อ้ายเป็นแค่ที่พักใจ หรือเป็นอะไรก็ได้ทั้งนั้น ถึงแม้ว่าเราจะอยู่ด้วยกัน'],
            'มหาลัยวัวชน' : ['ตื่นเช้าเดินตามยาวหนน จูงวัวชน คนกับวัว น้องสาวคงไม่รู้ตัว ว่าทำเด็กแลวัวนั้นหวั่นไหว'] ,
            'ให้เคอรี่มาส่งได้บ่' : ['เป็นตาฮักปานนี่ ให้เคอรี่มาส่งได้บ่ สั่งซื้อไสหนอ ยี่ห้ออีหยัง'] ,
            'ขอใจเธอแลกเบอร์โทร' : ['เบอร์โทรอื่นจะได้ยินเสียงรอสาย แบบแบบแบบว่าให้รอ แต่เบอร์นี้จะได้ยินเสียงใจบอกว่า'],
            'กอดเสาเถียง' : ['น้ำตาตก ลงโจก จักโบก มันจังสิพอ พอสิฆ่า คนจั่งมึง ให้ตายไปจากใจ เคียดให้คัก ๆ เบิดเหล้าจักว่าจักไหม'] ,
            'ปี้จนป่น' : ['ถึงหน้าตาไม่ดีแต่ฉันก็มีหัวใจ หัวใจของฉันให้เธอไปจนหมด'] ,
            'ความคิดถึงกำลังเดินทาง' : ['ความคิดถึง กำลังเดินทาง สัญญาณใจเธอ ว่างเยอะม๊ายช่วยวางลับสายที'] ,
            'โนบรา - โนราห์' : ['แล้วพี่ก็ลืม พี่ก็ลืมโนราห์ ไปเจอะสาวโนบรา สาวโนราห์เลยจ๋อยอยู่ดงสายเดี่ยว']}
            songname = pick_random_key_from_dict(lukthung)
            #print(random_key)
            hint = lukthung[songname]
            message3 = Message(frame, text=hint, width=600,font='Garuda 30 bold' , 
            anchor=CENTER,bg="#00C5A7")
            message3.place(width=600, height=190,x=212, y=288)
            entry = Entry(lukthungpart, width= 25,font=20)
            entry.place(x=352, y=553)
            Button(lukthungpart, text= "Click to Check", command= checkans).place(x=700, y=553)
            lukthungpart.mainloop()
        def poppart():
            choosetype.destroy()
            poppart=Tk()
            poppart.title("เกมทายเพลง")
            poppart.geometry("1024x768")
            #background
            frame = Frame(poppart)
            frame.config(background="cyan")
            frame.place(width=1024, height=768, x=0, y=0)
            photo2=PhotoImage(file="bg2.gif")
            label1 = Label(frame, image=photo2)
            label1.place(width=1024, height=768,x = 0, y = 0)
            def pick_random_key_from_dict(pop: dict):
                keys = list(pop.keys())
                random_key = random.choice(keys)
                return random_key
            def checkans():
                answer=entry.get()
                if answer==songname:
                    poppart.destroy()
                    correctans=Tk()
                    correctans.title("เกมทายเพลง")
                    correctans.geometry("1024x768")
                    #background
                    frame = Frame(correctans)
                    frame.config(background="cyan")
                    frame.place(width=1024, height=768, x=0, y=0)
                    photocor=PhotoImage(file="correctans.gif")
                    label1 = Label(frame, image=photocor)
                    label1.place(width=1024, height=768,x = 0, y = 0)
                    #command
                    def exit():
                        correctans.destroy()
                    def playagain():
                        correctans.destroy()
                        maindata()
                    #button
                    bpa= Button(frame, text="เล่นอีกครั้ง",font='Garuda 30 bold' ,command=playagain,bg="#00C5A7")
                    bpa.place(width=230, height=120,x=77, y=591)
                    bexit = Button(frame, text="ออก",font='Garuda 30 bold' ,command=exit,bg="#00C5A7")
                    bexit.place(width=230, height=120,x=717, y=591)
                    correctans.mainloop()
                else:
                    poppart.destroy()
                    wrongans=Tk()
                    wrongans.title("เกมทายเพลง")
                    wrongans.geometry("1024x768")
                    #background
                    frame = Frame(wrongans)
                    frame.config(background="cyan")
                    frame.place(width=1024, height=768, x=0, y=0)
                    photowro=PhotoImage(file="wrongans.gif")
                    label1 = Label(frame, image=photowro)
                    label1.place(width=1024, height=768,x = 0, y = 0)
                    #command
                    def exit():
                        wrongans.destroy()
                    def showans():
                        showans = Message(frame, text=songname, width=600,font='Garuda 30 bold' , 
                    anchor=CENTER,bg="white")
                        showans.place(width=600, height=190,x=212, y=288)
                    def playagain():
                        wrongans.destroy()
                        maindata()
                    #button
                    bpa= Button(frame, text="เล่นอีกครั้ง",font='Garuda 30 bold' ,command=playagain,bg="#00C5A7")
                    bpa.place(width=230, height=120,x=77, y=591)
                    bexit = Button(frame, text="ออก",font='Garuda 30 bold' ,command=exit,bg="#00C5A7")
                    bexit.place(width=230, height=120,x=717, y=591)
                    bans= Button(frame, text="เฉลย",font='Garuda 30 bold' ,command=showans,bg="#00C5A7")
                    bans.place(width=230, height=120,x=397, y=591)
                    wrongans.mainloop()
            pop={'เจ็บจนพอ' : ['เฝ้าอดทนมาทุกครั้ง เจ็บก็ยอมอยู่อย่างนั้น เพราะหวังว่าสักวันนึงเธอคงเห็นใจ'],
        'ภาพจำ' : ['ที่ตรงนั้นก็กลายเป็นเขา เข้ามาแทนที่คำว่าเรา ไม่มีแล้วคืนวันที่ฉันได้อยู่ใกล้เธอ'] ,
        'พูดไม่คิด' : ['เอาข้าวเอาของ เขวี้ยงออกนอกห้อง แต่ไม่กล้าลบรูปเธอจากเมมโมรีที่อยู่ในกล้อง'] ,
        'ผ่านตา' : ['แค่เธอทักทายฉันคงจะละลาย ฉันจึงผ่านไปให้เธอได้มองเห็นกัน เพียงแค่ครั้งเดียวขอแค่นิดเดียว ให้เธอรู้สึกคุ้น'] ,
        'วันเกิดฉันปีนี้' : ['ถ้าฉันอธิฐานด้วยหัวใจ เราจะได้พบกันไหม เพียงคำขอเดียวในวันเกิดฉัน จะเป็นจริงได้ไหม'],
        'ฝันถึงแฟนเก่า' : ['ได้แต่สงสัยว่าถ้าวันนั้น ฉันไม่ทำเธอเสียใจ เราจะยังคบกันอยู่ไหม เธอยังจะรักฉันใช่ไหม'] ,
        'ไม่อยากให้เธอไม่สบาย' : ['จนเธอเข้ามา เธอทำให้ฉัน ได้รู้ว่าชีวิตก็มีค่า แค่มองฟ้าดูพระอาทิตย์ตกด้วยกันทุกวัน'] ,
        'Please' : ['รู้ทุกครั้งที่เรามองตา ยังทำให้ใจของเธอสั่น ทุกอย่างที่ผ่านมานั้นมันคือเรื่องจริง'] ,
        'ฝนตกไหม' : ['อากาศชื้นนะคืนนี้ ระวังหนาวนะแบบนี้ ก่อนเข้านอนเป่าผมให้ดี ฉันกลัวเธอจะไม่สบาย'] ,
        'คิด(แต่)ไม่ถึง' : ['ยังนึกถึงวันนั้น วันที่เราหัวเราะกัน ไม่เคยลืมรอยยิ้มเธอสักครั้ง จำได้ไหม วันที่เราทะเลาะกัน']

    }
            songname = pick_random_key_from_dict(pop)
            #print(random_key)
            hint = pop[songname]
            message3 = Message(frame, text=hint, width=600,font='Garuda 30 bold' , 
            anchor=CENTER,bg="#00C5A7")
            message3.place(width=600, height=190,x=212, y=288)
            entry = Entry(poppart, width= 25,font=20)
            entry.place(x=352, y=553)
            Button(poppart, text= "Click to Check", command= checkans).place(x=700, y=553)
            poppart.mainloop()
        def rnbpart():
            choosetype.destroy()
            rnbpart=Tk()
            rnbpart.title("เกมทายเพลง")
            rnbpart.geometry("1024x768")
            #background
            frame = Frame(rnbpart)
            frame.config(background="cyan")
            frame.place(width=1024, height=768, x=0, y=0)
            photo2=PhotoImage(file="bg2.gif")
            label1 = Label(frame, image=photo2)
            label1.place(width=1024, height=768,x = 0, y = 0)
            def pick_random_key_from_dict(rnb: dict):
                keys = list(rnb.keys())
                random_key = random.choice(keys)
                return random_key
            def checkans():
                answer=entry.get()
                if answer==songname:
                    rnbpart.destroy()
                    correctans=Tk()
                    correctans.title("เกมทายเพลง")
                    correctans.geometry("1024x768")
                    #background
                    frame = Frame(correctans)
                    frame.config(background="cyan")
                    frame.place(width=1024, height=768, x=0, y=0)
                    photocor=PhotoImage(file="correctans.gif")
                    label1 = Label(frame, image=photocor)
                    label1.place(width=1024, height=768,x = 0, y = 0)
                    #command
                    def exit():
                        correctans.destroy()
                    def playagain():
                        correctans.destroy()
                        maindata()
                    #button
                    bpa= Button(frame, text="เล่นอีกครั้ง",font='Garuda 30 bold' ,command=playagain,bg="#00C5A7")
                    bpa.place(width=230, height=120,x=77, y=591)
                    bexit = Button(frame, text="ออก",font='Garuda 30 bold' ,command=exit,bg="#00C5A7")
                    bexit.place(width=230, height=120,x=717, y=591)
                    correctans.mainloop()
                else:
                    rnbpart.destroy()
                    wrongans=Tk()
                    wrongans.title("เกมทายเพลง")
                    wrongans.geometry("1024x768")
                    #background
                    frame = Frame(wrongans)
                    frame.config(background="cyan")
                    frame.place(width=1024, height=768, x=0, y=0)
                    photowro=PhotoImage(file="wrongans.gif")
                    label1 = Label(frame, image=photowro)
                    label1.place(width=1024, height=768,x = 0, y = 0)
                    #command
                    def exit():
                        wrongans.destroy()
                    def showans():
                        showans = Message(frame, text=songname, width=600,font='Garuda 30 bold' , 
                    anchor=CENTER,bg="white")
                        showans.place(width=600, height=190,x=212, y=288)
                    def playagain():
                        wrongans.destroy()
                        maindata()
                    #button
                    bpa= Button(frame, text="เล่นอีกครั้ง",font='Garuda 30 bold' ,command=playagain,bg="#00C5A7")
                    bpa.place(width=230, height=120,x=77, y=591)
                    bexit = Button(frame, text="ออก",font='Garuda 30 bold' ,command=exit,bg="#00C5A7")
                    bexit.place(width=230, height=120,x=717, y=591)
                    bans= Button(frame, text="เฉลย",font='Garuda 30 bold' ,command=showans,bg="#00C5A7")
                    bans.place(width=230, height=120,x=397, y=591)
                    wrongans.mainloop()
            rnb={'เอาไรว่ามา' : ['อย่ามายิ้มได้ไหมถ้าเธอไม่ได้จริงจัง เลิกน่ารักเพราะฉันกำลังจะไหวหวั่น'] ,
        'เป็นเพราะฝน' : ['จากฟ้าหยดลงบนพื้น จากตาอาบหน้าให้ชื้น เมื่อไหร่เธอจะย้อนคืนมาหา'] ,
        'รักแรกพบ' : ['แต่วันนึงฉันผ่านมาพบเธอตรงนั้น ดวงใจ เป็นเดือดเป็นร้อนช่างทรมาน'] ,
        'ไกล' : ['ฉันยังเหมือนเดิมสิ่งเหล่านั้นยังเหมือนเดิม ยังเฝ้ารอเธอคนเดียวทั้งหัวใจ'] ,
        'กีดกัน' : ['ยามที่เราทั้งสองได้พานพบ ลบเรื่องราวอดีตที่ร้าวราน เธอคือความรักแท้'] ,
        'กอดความเจ็บช้ำ' : ['ในสิ่งที่ฉันต้องเจอทรมาณ ยังบอกตัวเองว่ามันแค่เมื่อวาน มองไปก็เหมือนว่าคงไม่มีทาง'] ,
        'ลบไม่ได้ช่วยให้ลืม' : ['และลบทุกรูปที่มีเธอ ภาพความทรงจำในวันนั้น ลบมันไปทุกข้อความ'] ,
        'รักแรก' : ['รักแรกมันลืมยาก ฉันคงลืมยาก แม้จะนานเท่าไร ไม่มีวันที่จะจางหาย'] ,
        'ภาวิณี' : ['ยังเหมือนเดิม และฉันคงเดิม ทุกข์ทนไปกับวันที่เธอได้ ร่ำลาในวันนั้น'] ,
        'เพื่อนรัก'  : ['เปลี่ยนไปเป็นรัก รักจนหมดหัวใจ รักเพียงแต่เธอ ขอเพียงให้เธอได้รู้'] 
    }
            songname = pick_random_key_from_dict(rnb)
            #print(random_key)
            hint = rnb[songname]
            message3 = Message(frame, text=hint, width=600,font='Garuda 30 bold' , 
            anchor=CENTER,bg="#00C5A7")
            message3.place(width=600, height=190,x=212, y=288)
            entry = Entry(rnbpart, width= 25,font=20)
            entry.place(x=352, y=553)
            Button(rnbpart, text= "Click to Check", command= checkans).place(x=700, y=553)
            rnbpart.mainloop()
        def rockpart():
            choosetype.destroy()
            rockpart=Tk()
            rockpart.title("เกมทายเพลง")
            rockpart.geometry("1024x768")
            #background
            frame = Frame(rockpart)
            frame.config(background="cyan")
            frame.place(width=1024, height=768, x=0, y=0)
            photo2=PhotoImage(file="bg2.gif")
            label1 = Label(frame, image=photo2)
            label1.place(width=1024, height=768,x = 0, y = 0)
            def pick_random_key_from_dict(rock: dict):
                keys = list(rock.keys())
                random_key = random.choice(keys)
                return random_key
            def checkans():
                answer=entry.get()
                if answer==songname:
                    rockpart.destroy()
                    correctans=Tk()
                    correctans.title("เกมทายเพลง")
                    correctans.geometry("1024x768")
                    #background
                    frame = Frame(correctans)
                    frame.config(background="cyan")
                    frame.place(width=1024, height=768, x=0, y=0)
                    photocor=PhotoImage(file="correctans.gif")
                    label1 = Label(frame, image=photocor)
                    label1.place(width=1024, height=768,x = 0, y = 0)
                    #command
                    def exit():
                        correctans.destroy()
                    def playagain():
                        correctans.destroy()
                        maindata()
                    #button
                    bpa= Button(frame, text="เล่นอีกครั้ง",font='Garuda 30 bold' ,command=playagain,bg="#00C5A7")
                    bpa.place(width=230, height=120,x=77, y=591)
                    bexit = Button(frame, text="ออก",font='Garuda 30 bold' ,command=exit,bg="#00C5A7")
                    bexit.place(width=230, height=120,x=717, y=591)
                    correctans.mainloop()
                else:
                    rockpart.destroy()
                    wrongans=Tk()
                    wrongans.title("เกมทายเพลง")
                    wrongans.geometry("1024x768")
                    #background
                    frame = Frame(wrongans)
                    frame.config(background="cyan")
                    frame.place(width=1024, height=768, x=0, y=0)
                    photowro=PhotoImage(file="wrongans.gif")
                    label1 = Label(frame, image=photowro)
                    label1.place(width=1024, height=768,x = 0, y = 0)
                    #command
                    def exit():
                        wrongans.destroy()
                    def showans():
                        showans = Message(frame, text=songname, width=600,font='Garuda 30 bold' , 
                    anchor=CENTER,bg="white")
                        showans.place(width=600, height=190,x=212, y=288)
                    def playagain():
                        wrongans.destroy()
                        maindata()
                    #button
                    bpa= Button(frame, text="เล่นอีกครั้ง",font='Garuda 30 bold' ,command=playagain,bg="#00C5A7")
                    bpa.place(width=230, height=120,x=77, y=591)
                    bexit = Button(frame, text="ออก",font='Garuda 30 bold' ,command=exit,bg="#00C5A7")
                    bexit.place(width=230, height=120,x=717, y=591)
                    bans= Button(frame, text="เฉลย",font='Garuda 30 bold' ,command=showans,bg="#00C5A7")
                    bans.place(width=230, height=120,x=397, y=591)
                    wrongans.mainloop()
            rock={'เล่นของสูง' : ['แม้ต้อยต่ำแต่ยังมีหัวใจ แม้ต้องเจ็บแต่มันก็คุ้มก็สุขใจ ไม่ผิดใช่ไหมที่ฉันไม่เจียมตัว'],
        'คุกเข่า' : ['แต่ถ้าตัวเธอยังรัก ยังห่วงใย และถ้าอดีตของเรา ยังพอมีความหมาย ได้โปรดอย่าจากฉันไป'],
        'สองรัก' : ['ยิ่งฟังไม่เข้าใจ ยิ่งฟังยิ่งทรมานฉัน เธอบอกเหตุผล ที่หยุดความรักระหว่างฉัน'],
        'จันทร์เจ้า' : ['ร้องบรรเลง เสียงเพลงเทาเทา ท่ามกลางหมู่ดาว ร้อยเรื่องราวนับพัน'],
        'ขี้หึง' : ['อยากให้เธอได้รู้ เฝ้าดูแล้วเข้าใจก่อน หากใครทำใจฉันสั่นคลอน เธอจะรู้สึกหึงและห่วงไหม'],
        'ฤดูร้อน' : ['หยุดทั้งหัวใจ เดินต่อไปไม่มีแสงดาว โอบกอดน้ำตาโอบกอดหัวใจกับความเศร้า'],
        'น้ำลาย' : ['บ้างก็ว่าฉันเป็นคนอย่างนั้น บ้างก็ว่าฉันเคยทำอย่างนี้ ว่ากันว่าฉันเป็นคนไม่ดี ว่าแต่ว่าไม่เคยพูดกับฉันซักที'],
        'โปรดส่งใครมารักฉันที' : ['จะต้องเหงากัน อีกนานไหม ต้องนั่งถอนใจ อีกกี่ครั้ง'],
        'อย่างน้อย' : ['อาจจะเหนื่อยบางครั้ง อาจจะเจ็บบางที แต่ก็ยิ้มได้เรื่อยมา อาจจะต้องผิดหวัง ก็ไม่เป็นไร'],
        'เธอยัง' : ['ได้แต่คิดแล้วก็สงสัย อยู่ตรงนั้นเธอเป็นอย่างไรก็ไม่รู้ ฝากเพลงนี้ให้ไปถามเธอดู อยากจะรู้ในความเป็นไป']
    }
            songname = pick_random_key_from_dict(rock)
            #print(random_key)
            hint = rock[songname]
            message3 = Message(frame, text=hint, width=600,font='Garuda 30 bold' , 
            anchor=CENTER,bg="#00C5A7")
            message3.place(width=600, height=190,x=212, y=288)
            entry = Entry(rockpart, width= 25,font=20)
            entry.place(x=352, y=553)
            Button(rockpart, text= "Click to Check", command= checkans).place(x=700, y=553)
            rockpart.mainloop()
        def tpoppart():
            choosetype.destroy()
            tpoppart=Tk()
            tpoppart.title("เกมทายเพลง")
            tpoppart.geometry("1024x768")
            #background
            frame = Frame(tpoppart)
            frame.config(background="cyan")
            frame.place(width=1024, height=768, x=0, y=0)
            photo2=PhotoImage(file="bg2.gif")
            label1 = Label(frame, image=photo2)
            label1.place(width=1024, height=768,x = 0, y = 0)
            def pick_random_key_from_dict(rock: dict):
                keys = list(rock.keys())
                random_key = random.choice(keys)
                return random_key
            def checkans():
                answer=entry.get()
                if answer==songname:
                    tpoppart.destroy()
                    correctans=Tk()
                    correctans.title("เกมทายเพลง")
                    correctans.geometry("1024x768")
                    #background
                    frame = Frame(correctans)
                    frame.config(background="cyan")
                    frame.place(width=1024, height=768, x=0, y=0)
                    photocor=PhotoImage(file="correctans.gif")
                    label1 = Label(frame, image=photocor)
                    label1.place(width=1024, height=768,x = 0, y = 0)
                    #command
                    def exit():
                        correctans.destroy()
                    def playagain():
                        correctans.destroy()
                        maindata()
                    #button
                    bpa= Button(frame, text="เล่นอีกครั้ง",font='Garuda 30 bold' ,command=playagain,bg="#00C5A7")
                    bpa.place(width=230, height=120,x=77, y=591)
                    bexit = Button(frame, text="ออก",font='Garuda 30 bold' ,command=exit,bg="#00C5A7")
                    bexit.place(width=230, height=120,x=717, y=591)
                    correctans.mainloop()
                else:
                    tpoppart.destroy()
                    wrongans=Tk()
                    wrongans.title("เกมทายเพลง")
                    wrongans.geometry("1024x768")
                    #background
                    frame = Frame(wrongans)
                    frame.config(background="cyan")
                    frame.place(width=1024, height=768, x=0, y=0)
                    photowro=PhotoImage(file="wrongans.gif")
                    label1 = Label(frame, image=photowro)
                    label1.place(width=1024, height=768,x = 0, y = 0)
                    #command
                    def exit():
                        wrongans.destroy()
                    def showans():
                        showans = Message(frame, text=songname, width=600,font='Garuda 30 bold' , 
                    anchor=CENTER,bg="white")
                        showans.place(width=600, height=190,x=212, y=288)
                    def playagain():
                        wrongans.destroy()
                        maindata()
                    #button
                    bpa= Button(frame, text="เล่นอีกครั้ง",font='Garuda 30 bold' ,command=playagain,bg="#00C5A7")
                    bpa.place(width=230, height=120,x=77, y=591)
                    bexit = Button(frame, text="ออก",font='Garuda 30 bold' ,command=exit,bg="#00C5A7")
                    bexit.place(width=230, height=120,x=717, y=591)
                    bans= Button(frame, text="เฉลย",font='Garuda 30 bold' ,command=showans,bg="#00C5A7")
                    bans.place(width=230, height=120,x=397, y=591)
                    wrongans.mainloop()
            tpop={'มูเตลู' : ['จงหยุด อยู่ตรงนั้น เจ้าพรหมลิขิตของฉัน ส่งรักเธอให้ฉันมา อย่าให้ต้องเสียเวลา'] ,
        'ฉันจะฉาปเธอ' : ['ถ้าทำกันขนาดนี้ คงต้องปล่อยเธอวันนี้ ไม่ได้โกรธเลย baby'] ,
        'PLAY WITH ME' : ['ถ้าเธอชนะได้ฉันเป็นแฟน แต่ถ้าแพ้ฉันเป็นแฟนเธอ นะ'] ,
        'เกินต้าน' : ['ห้ามใจเอาไว้ก่อนอดทนเอาไว้ก่อน ควบคุมอาการตัวเองให้ไหว'] ,
        'โดนเทแต่เท่อยู่'  : ['ใครก็ถามว่าฉันนั้นเจ็บไหม โดนเค้าเทแล้วเจ็บไหม ลองมาโดนดูเอง..จะรู้เลย แต่ฟูมฟายก็ไม่ช่วยอะไร'] ,
        'DEJAYOU'  : ['เธอก่อกวนใจของฉันเสมอ ไม่ให้พักเลย ไม่มีตอนไหนไม่คิดถึงเธอ'] ,
        'Booty Bomb'  : ['ให้เป็นแบบใครก็คงไม่ไหว ได้โปรดเถอะช่วยเข้าใจได้ไหม You know you know you know'] ,
        '17 นาที'  : ['มันยังไม่ถึงเวลาตอบ 10 นาที ร้องเพลงจนหอบ 11 นาที เฮ้อ อยากคุยด้วยแล้วโว้ย 13 นาที โอเค อีก 4 นาทีโอเค'] ,
        'เกินปุยมั้ย' : ['ทำให้เธอไปขนาดนั้น หากว่านานกว่านี้ไม่ไหว ก็ใจของฉันมัน calling you'] ,
        'เฮอร์ไมโอน้อง' : ['อยากมีเวทมนตร์คาถาจะเสกพี่มาให้เป็น my boo Accio Confundo นะโมนะโม เลิฟยูเลิฟยู'] 
    }
            songname = pick_random_key_from_dict(tpop)
            #print(random_key)
            hint = tpop[songname]
            message3 = Message(frame, text=hint, width=600,font='Garuda 30 bold' , 
            anchor=CENTER,bg="#00C5A7")
            message3.place(width=600, height=190,x=212, y=288)
            entry = Entry(tpoppart, width= 25,font=20)
            entry.place(x=352, y=553)
            Button(tpoppart, text= "Click to Check", command= checkans).place(x=700, y=553)
            tpoppart.mainloop()
        #button part
        bfolksong = Button(frame, text="Folksong",font='Garuda 30 bold' ,command=folksongpart,bg="#00C5A7")
        bfolksong.place(width=200, height=75,x=150, y=275)
        bforlife = Button(frame, text="เพื่อชีวิต",font='Garuda 35 bold' ,command=forlifepart,bg="#00C5A7")
        bforlife.place(width=200, height=75,x=404, y=275)
        bhiphop = Button(frame, text="HipHop",font='Garuda 35 bold' ,command=hiphoppart,bg="#00C5A7")
        bhiphop.place(width=200, height=75,x=660, y=275)
        bluktung = Button(frame, text="ลูกทุ่ง",font='Garuda 35 bold' ,command=lukthungpart,bg="#00C5A7")
        bluktung.place(width=200, height=75,x=150, y=420)
        bpop = Button(frame, text="Pop",font='Garuda 35 bold' ,command=poppart,bg="#00C5A7")
        bpop.place(width=200, height=75,x=404, y=420)
        brnb = Button(frame, text="R&B",font='Garuda 35 bold' ,command=rnbpart,bg="#00C5A7")
        brnb.place(width=200, height=75,x=660, y=420)
        brock = Button(frame, text="Rock",font='Garuda 35 bold' ,command=rockpart,bg="#00C5A7")
        brock.place(width=200, height=75,x=277, y=553)
        btpop = Button(frame, text="T-Pop",font='Garuda 35 bold' ,command=tpoppart,bg="#00C5A7")
        btpop.place(width=200, height=75,x=532, y=553)
        choosetype.mainloop()
    #command?
    def explain():
        explain = Tk()
        explain.title("คำอธิบายเกม")
        w = Label(explain, text="กดPLAYเพื่อเล่น จากนั้นจะมีหมวดหมู่เพลงให้คุณเลือกเล่น \nคลิกเลือกหมวดหมู่เพลงจากนั้นท่อนพลงจะขึ้นมาให้คุณทาย \nพิมพ์คำตอบของคุณลงในช่องใส่คำตอบ แล้วคลิก check the answer") # Create a label with words
        w.pack() # Put the label into the window
        def buttonPushed():
            explain.destroy()
        myButton = Button(explain, text="Exit",command=buttonPushed)
        myButton.pack()
        explain.mainloop()
    def checkProfile():
        root.destroy()
        root2 = Tk()
        root2.title('ค้นหาข้อมูลเพลง')
        root2.geometry('1024x768')
        app2 = Frame(root2)
        app2.grid()
        blanklabel1 = Label(app2, width=5)
        blanklabel2 = Label(app2, width=30)
        class Node():
            def __init__(self,key,type,songname,songname1,songname2,songname3,songname4,songname5,songname6,songname7,songname8,songname9):
                self.key = key
                self.type = type
                self.songname = songname
                self.songname1 = songname1
                self.songname2 = songname2
                self.songname3 = songname3
                self.songname4 = songname4
                self.songname5 = songname5
                self.songname6 = songname6
                self.songname7 = songname7
                self.songname8 = songname8
                self.songname9 = songname9
                self.left = None
                self.right = None
        class BST():
            def __init__(self):
                self.root = None

            def put(self,key,type,songname,songname1,songname2,songname3,songname4,songname5,songname6,songname7,songname8,songname9):
                self.root = self.insert(self.root,key,type,songname,songname1,songname2,songname3,songname4,songname5,songname6,songname7,songname8,songname9)

            def insert(self,node,key,type,songname,songname1,songname2,songname3,songname4,songname5,songname6,songname7,songname8,songname9):
                if node is None:
                    return Node(key,type,songname,songname1,songname2,songname3,songname4,songname5,songname6,songname7,songname8,songname9)
                if key < node.key:
                    node.left = self.insert(node.left,key,type,songname,songname1,songname2,songname3,songname4,songname5,songname6,songname7,songname8,songname9)
                else:
                    node.right = self.insert(node.right,key,type,songname,songname1,songname2,songname3,songname4,songname5,songname6,songname7,songname8,songname9)
                return node
            
            def run_inorder(self):
                self.inorder(self.root)

            def inorder(self,parent):
                if parent is not None:
                    self.inorder(parent.left)
                    print(str(parent.key) + "->",end=" ")
                    self.inorder(parent.right)
            
            def search(self,key):
                curr = self.root
                while curr is not None:
                    if curr is None or curr.key == key:
                        return curr
                    if key < curr.key:
                        curr = curr.left
                    else:
                        curr = curr.right
        
        searchlabel = Label(app2,text='เลขเพลง', font=('tahoma','11','bold'),width=15,anchor=W)
        searchtext = StringVar()
        searchentry = Entry(app2, textvariable=searchtext, font=('tahoma','11','bold'),width=14)

        namelabel = Label(app2,text='หมวดหมู่', font=('tahoma','11','bold'),width=15,anchor=W)
        nameentry = Label(app2, fg="#000", bg="cyan", font=('tahoma', '11', 'bold'), width=15, anchor=W)
        snamelabel = Label(app2,text='ชื่อเพลง', font=('tahoma','11','bold'),width=15,anchor=W)
        snameentry = Label(app2, fg="#000", bg="grey", font=('tahoma', '11', 'bold'), width=15, anchor=W)
        snamelabel1 = Label(app2,text='         ', font=('tahoma','11','bold'),width=15,anchor=W)
        snameentry1 = Label(app2, fg="#000", bg="grey", font=('tahoma', '11', 'bold'), width=15, anchor=W)
        snamelabel2 = Label(app2,text=' ', font=('tahoma','11','bold'),width=15,anchor=W)
        snameentry2 = Label(app2, fg="#000", bg="grey", font=('tahoma', '11', 'bold'), width=15, anchor=W)
        snamelabel3 = Label(app2,text=' ', font=('tahoma','11','bold'),width=15,anchor=W)
        snameentry3 = Label(app2, fg="#000", bg="grey", font=('tahoma', '11', 'bold'), width=15, anchor=W)
        snamelabel4 = Label(app2,text=' ', font=('tahoma','11','bold'),width=15,anchor=W)
        snameentry4 = Label(app2, fg="#000", bg="grey", font=('tahoma', '11', 'bold'), width=15, anchor=W)
        snamelabel5 = Label(app2,text=' ', font=('tahoma','11','bold'),width=15,anchor=W)
        snameentry5 = Label(app2, fg="#000", bg="grey", font=('tahoma', '11', 'bold'), width=15, anchor=W)
        snamelabel6 = Label(app2,text=' ', font=('tahoma','11','bold'),width=15,anchor=W)
        snameentry6 = Label(app2, fg="#000", bg="grey", font=('tahoma', '11', 'bold'), width=15, anchor=W)
        snamelabel7 = Label(app2,text=' ', font=('tahoma','11','bold'),width=15,anchor=W)
        snameentry7 = Label(app2, fg="#000", bg="grey", font=('tahoma', '11', 'bold'), width=15, anchor=W)
        snamelabel8 = Label(app2,text=' ', font=('tahoma','11','bold'),width=15,anchor=W)
        snameentry8 = Label(app2, fg="#000", bg="grey", font=('tahoma', '11', 'bold'), width=15, anchor=W)
        snamelabel9 = Label(app2,text=' ', font=('tahoma','11','bold'),width=15,anchor=W)
        snameentry9 = Label(app2, fg="#000", bg="grey", font=('tahoma', '11', 'bold'), width=15, anchor=W)

        enterbutton = Button(app2, text='ยืนยัน', font=('tahoma', '11', 'bold'), width=10,
                            command=lambda: enterfind())
        backbutton = Button(app2, text='กลับ', font=('tahoma', '11', 'bold'), width=10,
                            command=lambda: root2exit())
        blanklabel1.grid(column=0, row=0, rowspan=4)
        blanklabel2.grid(column=1 ,row=0,columnspan=3)
        searchlabel.grid(column=1, row=1)
        searchentry.grid(column=3, row=1)
        snamelabel.grid(column=1, row=3)
        snameentry.grid(column=3, row=3)
        snamelabel1.grid(column=1, row=4)
        snameentry1.grid(column=3, row=4)
        snamelabel2.grid(column=1, row=5)
        snameentry2.grid(column=3, row=5)
        snamelabel3.grid(column=1, row=6)
        snameentry3.grid(column=3, row=6)
        snamelabel4.grid(column=1, row=7)
        snameentry4.grid(column=3, row=7)
        snamelabel5.grid(column=1, row=8)
        snameentry5.grid(column=3, row=8)
        snamelabel6.grid(column=1, row=9)
        snameentry6.grid(column=3, row=9)
        snamelabel7.grid(column=1, row=10)
        snameentry7.grid(column=3, row=10)
        snamelabel8.grid(column=1, row=11)
        snameentry8.grid(column=3, row=11)
        snamelabel9.grid(column=1, row=12)
        snameentry9.grid(column=3, row=12)
        namelabel.grid(column=1, row=2)
        nameentry.grid(column=3, row=2)
        enterbutton.grid(column=3, row=15)
        backbutton.grid(column=3, row=16)
        def enterfind():
            b = BST()
            b.put(1,'FolkSong','แก้มน้องนางนั้นแดงกว่าใคร','จ่าหน้าซองถึงน้องพี่','อ้ายยังกอยอยู่','อะไรเอ่ยสวยกว่า..ทะเล','ภาษารักไม่บอกรัก','ฉันเป็นแมลง','หนีห่าง','ภาพฝันในจักรวาล','ใจรัก','ใครงามเลิศในปฐพี')
            b.put(2,'HipHop','มีแค่เรา','เป็นไรไหม','ครั้งสุดท้าย','MORNING','เสือสิ้นลาย','เป็นได้ทุกอย่า','วายร้าย','Very Very Small','ธาตุทองซาวด์','Microphone')
            b.put(3,'R&B','เอาไรว่ามา','เป็นเพราะฝน','รักแรกพบ','ไกล','กีดกัน','กอดความเจ็บช้ำ','ลบไม่ได้ช่วยให้ลืม','รักแรก','ภาวิณี','เพื่อนรัก')
            b.put(4,'เพื่อชีวิต','ขอนไม้กับเรือ','หนอนผีเสื้อ','ขวัญใจพี่หลวง','11 ร.ด.','กลับกลาย','เสมอ','ลมเพลมพัด','วณิพก','เวลคัมทูไทยแลนด์','ยายสา')
            b.put(5,'ลูกทุ่ง','ผู้สาวขาเลาะ','คำแพง','ไม่มีข้อแม้ตั้งแต่เริ่มต้น','มหาลัยวัวชน','ให้เคอรี่มาส่งได้บ่','ขอใจเธอแลกเบอร์โทร','กอดเสาเถียง','ปี้จนป่น','ความคิดถึงกำลังเดินทาง','โนบรา-โนราห์')
            b.put(6,'Rock','เล่นของสูง','คุกเข่า','สองรัก','จันทร์เจ้า','ขี้หึง','ฤดูร้อน','น้ำลาย','โปรดส่งใครมารักฉันที','อย่างน้อย','เธอยัง')
            b.put(7,'Pop','เจ็บจนพอ','ภาพจำ','พูดไม่คิด','ผ่านตา','วันเกิดฉันปีนี้','ฝันถึงแฟนเก่า','ไม่อยากให้เธอไม่สบาย','Please','ฝนตกไหม','คิด(แต่)ไม่ถึง')
            b.put(8,'T-Pop','มูเตลู','ฉันจะฉาปเธอ','Play with me','เกินต้าน','โดนเทแต่เท่อยู่','Dejayou','Booty Bomb','17 นาที','เกินปุยมุ้ย','เฮอร์ไมโอน้อง')
            
            while True:
                uid = int(searchentry.get())
                n = b.search(uid)
                if n is not None:
                    b.run_inorder()
                    print("Found : ",n.key,n.type,n.songname,n.songname1,n.songname2,n.songname3,n.songname4,n.songname5,n.songname6,n.songname7,n.songname8,n.songname9)
                    snameentry.config(text = n.songname)
                    snameentry1.config(text = n.songname1)
                    snameentry2.config(text = n.songname2)
                    snameentry3.config(text = n.songname3)
                    snameentry4.config(text = n.songname4)
                    snameentry5.config(text = n.songname5)
                    snameentry6.config(text = n.songname6)
                    snameentry7.config(text = n.songname7)
                    snameentry8.config(text = n.songname8)
                    snameentry9.config(text = n.songname9)
                    nameentry.config(text = n.type)
                    break
                else:
                    b.run_inorder()
                    messagebox.showinfo('แจ้งเตือน','NOT FOUND')
                    break
        def root2exit():
            root2.destroy()
            maindata()

        root2.mainloop()

    #buttonchecklyric
    bt = Button(frame, text="เช็คเนื้อเพลง",font='Garuda 40 bold' ,command=checkProfile,bg="#00C5A7")
    bt.place(width=320, height=115,x=352, y=599)
    #buttonplay
    btn = Button(frame, text="PLAY",font='Garuda 60 bold' ,command=choosetype,bg="#00C5A7")
    btn.place(width=320, height=115,x=352, y=384)
    #button?
    btnhint= Button(frame, text="?",font='Garuda 10 bold' ,command=explain,bg="white")
    btnhint.place(width=20, height=20,x=1004, y=0)
    root.mainloop()
maindata()