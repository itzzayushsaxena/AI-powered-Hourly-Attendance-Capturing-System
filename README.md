# AI-powered-Hourly-Attendance-Capturing-System(AI_PHACS)
#### This is prototype of our project for [Design Engineering Subject](http://www.de.gtu.ac.in/Account/AboutUS).
#### University : [GTU](https://www.gtu.ac.in/) 

#### AI_PHACS is a software based attendance capturing system which will recognize the Faces And Accordingly will Store the data (Attendance) Present or Absent, then data can be used as per requirements.

## Table of contents
1. [Requirements](#-requirements)
2. [Technology Used](#-technology-used)
3. [Found Solution For Loop-Hole In Technology](#-found-best-solution-for-loop-hole-in-technology)
4. [Want To Contribute ??](#-want-to-contribute-)
5. [Known Bugs](#-known-bugs)
6. [Work Done Timeline](#-work-timeline)
7. [Future Development]()
8. [License](#license)
9. [FAQ](#faq)
10. [Reference](#-reference)
11. [Meet Team](#-team--role)


## **->Requirements**
#### python version >= 3
#### pip version==20.0.2    

## Setting up and running the Software on your machine.
#### 1. Make sure you have downloaded & installed python version >= 3, pip version == 20.0.2

#### 2. To download & intall the required python packages run following command in cmd.
 ```
pip install -r requirements.txt
```
#### 3. Now to run the Software, After changing directory to ../AI_PHACS in cmd run following command
```
main.py
```
#### 4. If you don't want to authenticate & authorize yourself again & again to access the admin page or user page you can run following command
### Note : cmd directory ../AI_PHACS
```
admin_page.py
```
```
user_page.py
```
 



## **->Technology Used**

#### Language - python 3.8
#### GUI Toolkit - tkinter, ttk
#### Database - mysql

## **->Found Best Solution For Loop Hole In Technology**
### **->Tkinter**
#### 1.When a PhotoImage or other Image object are added to a Tkinter widget, the image won’t always show up.
#### The problem is that the Tkinter/Tk interface doesn’t handle references to Image objects properly; the Tk widget will hold a reference to the internal object, but Tkinter does not. When Python’s garbage collector discards the Tkinter object, Tkinter tells Tk to release the image. But since the image is in use by a widget, Tk doesn’t destroy it. Not completely. It just blanks the image, making it completely transparent…    
#### Solution : Just describe the Master Window in which you want image.
#### example :  
```
self.object = PhotoImage(file="image.png", master=self.window_obj_name)
```

## **->Want To Contribute ??**
#### Feel free to contribute to this project. To learn how you could help, read the ["Contributing"](/contributing.md) page.


## **->Known Bugs**

#### ...

## **->Work Timeline**
#### ->Pending Work
#### 1. Fully  Database Connection
#### 2. User Page  
#### 3. How backend will Work??
#### 4. Python File to Recognize Faces
#### 5. Organizing files by:
if file is in same directory
```
os.system('.py_file_name')
```
if file is in different directory
```
os.system('python .py_file_name')
```

#### ->Completed Work

#### 1. Main Page Design
#### 2. User & Admin Login Page Design
#### 3. Admin Page Design
#### 4. Admin Page -> Add_User Page Design
#### 5. Add_User Page Backend & Database
#### 6. User_login & Admin_login Validation 
#### 7. Connect Admin & Add_User Page with BackButton
#### 8. edited all pngs
#### 9. Admin Page -> Add_Student Page Design
#### 10. Admin Page -> check_Detail Page Design
#### 11. Admin Page -> check_Attendance Page Design
#### 12. redesigned the UI
#### 13. validation of add_student Section
#### 14. Database Created
#### 15. Add_Student page & Detail page Database Connected & functionality added

## **->Future Development Plan**
#### 1. Custom Modification Feature for Admin(can add department, Stream...)
#### 2. Student Page where student can see their data

## **->License**

## **->FAQ**

## **->Reference**

#### 1. https://docs.python.org/3/
#### 2. https://docs.python.org/3/library/tkinter.html
#### 3. https://stackoverflow.com/
#### 4. https://icons8.com/icons/


## **->Team & Role**

#### Karmakar Sudip S. -> Leader, Project Organiser, Technical Skill Person   
#### Bherwani Bhavyesh J. -> Concept Generator, Technical Skill Person
#### Ayush Saxena ->  Project Organiser, Technical Skill Person
#### Masrani Jay H. -> An Analyser, Quality Checker 
#### Donda Preet T. -> sheets Maker
