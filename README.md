# AI-powered-Hourly-Attendance-Capturing-System

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
`self.object = PhotoImage(file="image.png", master=self.window_obj_name)`
## **->Requirements**

#### python version >= 3
#### pip version==20.0.2
#### PyMySQL==0.10.0


## **->Known Bugs**

#### ...

## **->Pending Work**

#### 1. Fully  Database Connection
#### 2. User Page  
#### 3. How backend will Work??
#### 4. Python File to Recognize Faces

## **->Completed Work**

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

## **->Reference**

#### 1. https://docs.python.org/3/
#### 2. https://docs.python.org/3/library/tkinter.html
#### 3. https://stackoverflow.com/
#### 4. https://icons8.com/icons/

## **->Team & Role**

#### Karmakar Sudip S. ->
#### Bherwani Bhavyesh J. ->
#### Ayush Saxena ->  
#### Masrani Jay H. ->  
#### Donda Preet T. ->
