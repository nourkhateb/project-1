#import sqlite module
import sqlite3

#create database and connect 
db=sqlite3.connect("nourapp.db")

#setting up the cursor 
cr=db.cursor()

#create the tables and field 
#cr.execute("create table if not exists skills (user_id integer,name text,progress integer)")

#commit and close method
def commit_close():
    db.commit()
    db.close()
    print("the conection with database is end ")

#user_id
user_id=input("enter your id please : ")

#input message
input_message= """How Can I Help You Sir ?
"s" ==> Show All Skills
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
Choose Option:
"""
#input option choose
user_input=input(input_message).strip().lower()

#command list
command_list=["s","a","d","u","q"]

#define the methods 
def show_skills():
    cr.execute(f"select * from skills where user_id='{user_id}'")
    result=cr.fetchall()
    print(f"You Have {len(result)} skills.")
    if len(result)>0:
        for name in result:
            print(f"skill ==> {name[1]} , ",end=" ")
            print(f"progress ==> {name[2]}%")
    commit_close()
    
def add_skills():
    name=input("please write your skill name : ").strip().capitalize()
    cr.execute(f"select name from skills where name='{name}'and user_id='{user_id}'")
    result= cr.fetchone()
    if result == None:
        prog=input("please write your skill progress : ").strip()
        cr.execute(f"insert into skills(user_id,name,progress)values('{user_id}','{name}','{prog}')")
    else:
        print("you cannot add it")
    commit_close()
    
def delete_skills():
    name=input(" please write your skill name : ").strip().capitalize()
    cr.execute(f"delete from skills where name ='{name}' and user_id='{user_id}'")
    commit_close()
    
def update_skills():
    name=input("please write your skill name : ").strip().capitalize()
    prog=input("please write your new skill progress : ").strip()
    cr.execute(f"update skills set progress ='{prog}'where name='{name}'and user_id='{user_id}'")
    commit_close()

#check if command is exists 
if user_input in command_list:
    if user_input == "s":
        show_skills()
    elif user_input == "a":
        add_skills()
    elif user_input == "d":
        delete_skills()
    elif user_input == "u":
        update_skills()
    else:
        print("App is closed")
        commit_close()
else:
    print(f" Sorry This Command \"{user_input}\" Not Found")
