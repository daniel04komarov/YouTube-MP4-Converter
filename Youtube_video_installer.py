from pytube import YouTube
import pygame as pg
import iab
import sqlite3
import random

#create database
connection = sqlite3.connect("addresses.db")

cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS
addresstbl(address TEXT PRIMARY KEY)"""

cursor.execute(command1)

pg.init()

#create display window
main_width = 1280    
main_height = 720

screen = pg.display.set_mode((main_width,main_height))
pg.display.set_caption("YouTube MP4 Video Downloader")

main_textcol = (255, 255, 255)
main_bgcolour = (54, 53, 52)
main_inpboxcolinactive = (0, 0, 0)
main_inpboxcolactive = (255, 255, 255)
main_buttontextcol = (255, 255, 255)
main_buttoncol = (28, 26, 26)

main_font = iab.define_font(("fonts/Poppins-Light.ttf"), 60)
label_font = iab.define_font(("fonts/Poppins-Light.ttf"), 40)
label_font2 = iab.define_font(("fonts/Poppins-Light.ttf"), 20)

icon = pg.image.load('images/icon.png')
pg.display.set_icon(icon)


def main_mn():
    clock = pg.time.Clock()

    submit_btn = iab.buttontext("Submit", main_buttontextcol, main_buttoncol, 200, 50, label_font, screen, (540, 300))
    update_btn = iab.buttontext("Update path", main_buttontextcol, main_buttoncol, 300, 50, label_font, screen, (490, 600))
    input_box1 = iab.InputBox(main_width/5, 200, 800, 50, label_font, main_inpboxcolinactive, main_inpboxcolactive)
    input_boxes = [input_box1]

    run = True
    while run == True:
        #background colour
        screen.fill(main_bgcolour)

        #Title
        iab.draw_text("YouTube MP4 Downloader", main_font, main_textcol, screen, main_width/5.1, 20)

        #buttons
        if submit_btn.draw() == True:
            if getaddress() == False:
                nodir_mn()

            else:
                if main(input_box1.handle_event(event), getaddress()) == False:
                    nolink_mn()

                elif main(input_box1.handle_event(event), getaddress()) == True:
                    downloaded_mn()

        if update_btn.draw() == True:
            updatepath_mn()

        #event manager
        for event in pg.event.get():
            
            if event.type == pg.QUIT:
                pg.quit()
                
            for box in input_boxes:
                box.handle_event(event)
                    
        for box in input_boxes:
            box.update()
                
        for box in input_boxes:
            box.draw(screen)
                
        pg.display.flip()
        clock.tick(30)
        
def nodir_mn():
    confirm_btn = iab.buttontext("Confirm", main_buttontextcol, main_buttoncol, 200, 50, label_font, screen, (540, 550))

    run = True
    while run == True:
        #background colour
        screen.fill(main_bgcolour)

        #Title
        iab.draw_text("No directory entered", main_font, main_textcol, screen, main_width/4, 20)

        #buttons
        if confirm_btn.draw() == True:
            main_mn()

        #event manager
        for event in pg.event.get():
                 
            if event.type == pg.QUIT:
                run = False
                
            pg.display.update()
            
    pg.quit()

def nolink_mn():
    confirm_btn = iab.buttontext("Confirm", main_buttontextcol, main_buttoncol, 200, 50, label_font, screen, (540, 550))

    run = True
    while run == True:
        #background colour
        screen.fill(main_bgcolour)

        #Title
        iab.draw_text("Incorrect link", main_font, main_textcol, screen, main_width/2.9, 20)

        #buttons
        if confirm_btn.draw() == True:
            main_mn()

        #event manager
        for event in pg.event.get():
                 
            if event.type == pg.QUIT:
                run = False
                
            pg.display.update()
            
    pg.quit()

def wrongdir_mn():
    confirm_btn = iab.buttontext("Confirm", main_buttontextcol, main_buttoncol, 200, 50, label_font, screen, (540, 550))

    run = True
    while run == True:
        #background colour
        screen.fill(main_bgcolour)

        #Title
        iab.draw_text("Incorrect directory entered", main_font, main_textcol, screen, main_width/4.6, 20)

        #buttons
        if confirm_btn.draw() == True:
            main_mn()

        #event manager
        for event in pg.event.get():
                 
            if event.type == pg.QUIT:
                run = False
                
            pg.display.update()
            
    pg.quit()

def downloaded_mn():
    confirm_btn = iab.buttontext("Confirm", main_buttontextcol, main_buttoncol, 200, 50, label_font, screen, (540, 550))

    run = True
    while run == True:
        #background colour
        screen.fill(main_bgcolour)

        #Title
        iab.draw_text("Success", main_font, main_textcol, screen, main_width/2.5, 20)
        iab.draw_text("Video downloaded to", label_font, main_textcol, screen, main_width/2.9, 100)
        iab.draw_text(getaddress(), label_font, main_textcol, screen, main_width/5, 150)

        #buttons
        if confirm_btn.draw() == True:
            main_mn()

        #event manager
        for event in pg.event.get():
                 
            if event.type == pg.QUIT:
                run = False
                
            pg.display.update()
            
    pg.quit()

def updatepath_mn():
    clock = pg.time.Clock()

    update_btn = iab.buttontext("Update", main_buttontextcol, main_buttoncol, 250, 50, label_font, screen, (515, 300))
    exit_btn = iab.buttontext("Exit", main_buttontextcol, main_buttoncol, 250, 50, label_font, screen, (515, 500))
    checkdir_btn = iab.buttontext("Check path", main_buttontextcol, main_buttoncol, 250, 50, label_font, screen, (515, 400))
    input_box1 = iab.InputBox(main_width/5, 200, 800, 50, label_font, main_inpboxcolinactive, main_inpboxcolactive)
    input_boxes = [input_box1]

    run = True
    while run == True:
        #background colour
        screen.fill(main_bgcolour)

        #Title
        iab.draw_text("Update directory path", main_font, main_textcol, screen, main_width/4.1, 20)

        #buttons
        if update_btn.draw() == True:
            if input_box1.handle_event(event) == "":
                wrongdir_mn()

            else:
                updateaddress(input_box1.handle_event(event))
                dirupdated_mn()
            
        elif exit_btn.draw() == True:
            main_mn()

        elif checkdir_btn.draw() == True:
            if getaddress() == True:
                nodir_mn()

            else:
                dir_mn()

        #event manager
        for event in pg.event.get():
            
            if event.type == pg.QUIT:
                pg.quit()
                
            for box in input_boxes:
                box.handle_event(event)
                    
        for box in input_boxes:
            box.update()
                
        for box in input_boxes:
            box.draw(screen)
                
        pg.display.flip()
        clock.tick(30)
    pg.quit()

def dirupdated_mn():
    confirm_btn = iab.buttontext("Confirm", main_buttontextcol, main_buttoncol, 200, 50, label_font, screen, (540, 550))

    run = True
    while run == True:
        #background colour
        screen.fill(main_bgcolour)

        #Title
        iab.draw_text("Directory updated", main_font, main_textcol, screen, main_width/3.9, 20)

        #buttons
        if confirm_btn.draw() == True:
            main_mn()

        #event manager
        for event in pg.event.get():
                 
            if event.type == pg.QUIT:
                run = False
                
            pg.display.update()
            
    pg.quit()

def prompt():
    miniscreen = pg.display.set_mode((640, 480))
    pg.display.set_caption("Downloading")

    confirm_btn = iab.buttontext("Confirm", main_buttontextcol, main_buttoncol, 200, 50, label_font, miniscreen, (210, 300))

    run = True
    while run == True:
        #background colour
        miniscreen.fill(main_bgcolour)

        #Title
        iab.draw_text("Video downloading", main_font, main_textcol, miniscreen, 20, 20)
        iab.draw_text("Do not exit program", main_font, main_textcol, miniscreen, 20, 100)

        if confirm_btn.draw() == True:
            run = False


        #event manager
        for event in pg.event.get():
                 
            if event.type == pg.QUIT:
                run = False
                
            pg.display.update()

    pg.quit()

def dir_mn():
    confirm_btn = iab.buttontext("Confirm", main_buttontextcol, main_buttoncol, 200, 50, label_font, screen, (540, 550))

    run = True
    while run == True:
        #background colour
        screen.fill(main_bgcolour)

        #Title
        iab.draw_text("Directory", main_font, main_textcol, screen, main_width/2.5, 20)
        iab.draw_text("Your Directory is:", label_font, main_textcol, screen, main_width/2.9, 100)
        iab.draw_text(getaddress(), label_font, main_textcol, screen, main_width/5, 150)

        #buttons
        if confirm_btn.draw() == True:
            main_mn()

        #event manager
        for event in pg.event.get():
                 
            if event.type == pg.QUIT:
                run = False
                
            pg.display.update()
            
    pg.quit()

def main(link, address):
    try:
        yt = YouTube(link)
        
        try:
            yd = yt.streams.get_highest_resolution()
            yd.download(address)
            return True
        except:
            wrongdir_mn()
    except:
        return False

def updateaddress(address):
    if getaddress() == False:
        cursor.execute("INSERT INTO addresstbl VALUES (?)", [address])
        connection.commit()

    else:

        cursor.execute("DELETE FROM addresstbl")
        connection.commit()
        updateaddress(address)

def getaddress():
    cursor.execute("SELECT address FROM addresstbl")

    if cursor.fetchone() == None:
        return False

    else:
        cursor.execute("SELECT address FROM addresstbl")
        results = cursor.fetchall()
        for result in results:
             if (str(result[0])) == "":
                 return False
             else:
                 return (str(result[0]))

main_mn()
