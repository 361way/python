import datetime
import sys,os
from peewee  import *
from collections import OrderedDict
from random import choice
from sqlite3.dbapi2 import Timestamp


db = SqliteDatabase('notes.db')

class Note(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    
    
    class Meta:
        database = db

def initialize():
    """ create database and table if they exist"""
    db.connect()
    db.create_tables([Note],safe=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    

def menu_loop():
    """ show menu loop"""
    choice = None
    while choice !='q':
        print '*'*20
        print 'Enter q to quit'
        for k,v in menu.items():
            print k,v.__doc__
        
        print '*'*20
        choice = raw_input('Action:').lower().strip()
        print '\n'
        if choice in menu:
            clear()
            menu[choice]() 
            #print '\n'
    
def add_note():
     """ add a note"""
     print 'Enter your note and press ctrl+d when finished'
     data = sys.stdin.read().strip()
     if data and raw_input('Save: Y/N ').lower() !='n':
         print '\n'
         Note.create(content=data)
         print 'Saved successfully'

def view_notes(search_query=None):
     """ view notes"""
     notes = Note.select().order_by(Note.timestamp.desc())
     if search_query:
         notes = notes.where(Note.content.contains(search_query))
     
     for note in notes:
         timestamp = note.timestamp.strftime('%A %B %d,%Y %I:%M%p')
         clear()
         print timestamp
         print '='*len(timestamp)
         print note.content
         print '='*len(timestamp)
         print '\n'
         print '\n\n' + '='*len(timestamp)
         print 'n) next note'
         print 'd) delete note'
         print 'q) return to main menu'
         print '*'*20
         next_note = raw_input('Action: N/Q: ').lower().strip()
         print '\n'

         if next_note == 'q':
             break
         elif next_note == 'd':
             delete_note(note)
def search_note():
     """ search a note"""
     view_notes(raw_input('search: '))

def delete_note(note):
     """ delete a note"""
     if raw_input('are you sure ? N/Y: ').lower() == 'y':
         print '\n'
         Note.delete_instance(note)
         print 'note deleted'
     
menu = OrderedDict([('a',add_note),('v',view_notes),('s',search_note)])
     
             
if __name__ == '__main__':
    initialize()
    menu_loop()
  
           
