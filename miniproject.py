# VIHAAN KHURANA

# Mini Project 2021-22 Sem 1

# 








import turtle
t = turtle.Turtle()

print("\nGreetings! Thanks for taking out time ! \n\nCode Written by Vihaan Khurana \n")
method = input("\nWhich Method do you want to print output \na) Coordinate \nb) Read from file \nc) Perform Functions by Clicking Mouse"
               "(a/b/c) Please Choose : ")
screen = turtle.Screen()
screen.title('Vihaan Khurana MINI PROJECT 2022')
screen.bgcolor('#ccffcc')





def intersect(p1, p2, p3,p4):

    error = False

    x1 = p1[0]*10
    y1 = p1[1]*10
    x2 = p2[0]*10
    y2 = p2[1]*10
    a1 = p3[0]
    b1 = p3[1]
    a2 = p4[0]
    b2 = p4[1]
    


    try:
        u = 0
        t1 = (((x1-a2)*(b1-b2)-(y1-b2)*(a1-a2))/((y2-y1)*(a1-a2)-(x2-x1)*(b1-b2)))
        t2 = (((b2-y1)*(x2-x1)+(x1-a2)*(y2-y1))/((a1-a2)*(y2-y1)-(b1-b2)*(x2-x1)))
        if t2<=1 and t2>=0:
            u+=1
        if t1<=1 and t1>=0:
            u+=1
        if u==2 :                 
            error = True
        
    except ZeroDivisionError:
        pass
    return error

def point_in_polygon(points,p):
    max_point = [p[0]+500,p[1]]
    total_intersect= 0
    try:
        for i in range(len(points)+1):
            z = intersect(points[i],points[i+1],p,max_point)
            if z == True:
                total_intersect += 1
            
        
        
            
        
    except IndexError:
        pass
    return (total_intersect%2 == 1)










def button(x,y):
    p=[x,y]
    r = point_in_polygon(points,p)
    if r == True:
        print("The point is within the polygon")
    else:
        print("The point is outside the polygon")
    
turtle.onscreenclick(button)

def perimeter(points):
    distances = get_distances(points)
    length = 0

    for distance in distances:
        length = length + distance
        
    return length

def get_distances(points):
    i = 0
    distances = []
    while True:
        try: 
            for i in range(len(points)):
                point = points[i]
                next_point = points[i+1]
                x0 = point[0]
                y0 = point[1]
                x1 = next_point[0]
                y1 = next_point[1]

                point_distance = get_distance(x0, y0, x1, y1)
                distances.append(point_distance)

        except IndexError:
            
            break
    return distances
def get_distance(x0, y0, x1, y1):
    a = x1-x0
    b = y1- y0
    c_2 = a*a + b*b

    return c_2 ** (1/2)

def crossproduct(x0, y0, x1, y1):
    a = x0*y1
    b = y0*x1
    return(a-b)

def area (points):
    sum = 0.0
    N = len(points) - 1
    i = 0
    while True:
        try:
            for i in range(len(points)):
                point = points[i]
                next_point = points[i+1]
                x0 = point[0]
                y0 = point[1]
                x1 = next_point[0]
                y1 = next_point[1]
                sum += crossproduct(x0,y0,x1,y1)
        except IndexError:
            break
    return abs(sum)/2.0

def translate(x,y,points):
    updated = []
    for i in range(len(points)):
        x0 = points[i][0] + (x)
        y0 = points[i][1] + (y)
        updated.append([x0,y0])
    return updated
   
        
        
def make_polygon(points):
    
    turtle.pensize(5)
    
    
    turtle.penup()
    turtle.goto(points[0][0]*10,points[0][1]*10)
    turtle.pendown()
    for c in points:
        turtle.goto(c[0]*10,c[1]*10)
    turtle.penup()
    
    
def save_polygon(points):
    filename = input("Please keep the name of the file where you want to save data?:  ")
    outfile = open(filename, "w")
    for i in points:
        print(i[0],",",i[1],file=outfile)
    
         

    
import math  
def rotate(points,angle,p,q):
    updated = []
    for i in range(len(points)):
        x = points[i][0]
        y = points[i][1]
        x0 = (x-p)*math.cos(angle) + (y-q)*math.sin(angle)+p
        y0 = -(x-p)*math.sin(angle) + (y-q)*math.sin(angle)+q
        updated.append([x0,y0])
    return updated
def check_intersect(points):
    error = False
    try:
        for i in range(3,(len(points)-1)):
            point = points[i]
            previous_point = points[i-1]
            x1 = point[0]
            y1= point[1]
            x2 = previous_point[0]
            y2 = previous_point[1]
    
            for z in range(i-2):
                check_point = points[z]
                nextcheck_point = points[z+1]
                a1 = check_point[0]
                b1 = check_point[1]
                a2 = nextcheck_point[0]
                b2 = nextcheck_point[1]
                try:
                    u = 0
                    t1 = (((x1-a2)*(b1-b2)-(y1-b2)*(a1-a2))/((y2-y1)*(a1-a2)-(x2-x1)*(b1-b2)))
                    t2 = (((b2-y1)*(x2-x1)+(x1-a2)*(y2-y1))/((a1-a2)*(y2-y1)-(b1-b2)*(x2-x1)))
                    
                    if t2<=1 and t2>=0:
                        u+=1
                    if t1<=1 and t1>=0:
                        u+=1
                    if u == 2 :                 
                        error = True
                        print("Try Again,The Line segement joining points ", x1,",",y1," and ", x2, ",",y2," are intersecting with Line segement joining points ", a1,",",b1," and ", a2, ",",b2,"  of polygon ")
                        break
                    else:
                        continue
                        
                except ZeroDivisionError:
                    continue

    except IndexError:
        pass
    return error
    
    
def omit(point, points):
    points.pop(point)
    return make_polygon(points)

def add(x,y,index,points):
    points.insert(index,[x,y])
    if check_intersect(points)is True:
        print("Can't add this point because the line segment inetersect")
    else:
        return make_polygon(points)









def all_funct(points):
    user = True
    while True:
        ask_anything= input("\n\n"
                        "This python-based programme does couple of functions to make you feel easy with polygons. so let's try it out \n\n"
                            "Please type in the name to perform these functions \n\n"
                        "To end the programme, type in (close)!\n\n"
                        "(P) - Perimeter\n(A) - Area\n(T) - Translate\n(R) - Rotate\n(O)- Omit any coordinate"
                        "\n(add) - Add any coordinate\n(S)- Scale the polygon\n(C) - Make Copies of polygon\n(save) - Save the Polygon"
                            "\n\n Please Type in here!: ")



    
    
        if ask_anything == "P":
            print("The perimeter of shape: ")
            print (perimeter(points))


        elif ask_anything== "A":
            print ("The area of shape: ")
            print(area(points))





        elif ask_anything == "T":
            ask_x = int(input("Enter the x coordinate by how much? "))
            ask_y = int(input("Enter the y coordinate by how much? "))
            ask_copy= input("Do you want to make (a) copy or (b) delete previous one? a/b")

            if ask_copy == "a":

            
                update_points = translate(ask_x, ask_y, points)
                make_polygon(update_points)
                
                
                
            else:
                turtle.clear()
            
                update_points = translate(ask_x, ask_y, points)
                make_polygon(update_points)
                
                ask_save = input("Do you want to save the file? ")
                if ask_save == "Y":
                    save_polygon(update_points)
                    print("\nYour datafile is saved successfully. Thank You! \nIt is saved in the folder which contains this programme\n")




        elif ask_anything== "R":
            ask_x = int(input("Enter the x coordinate for Center of rotation: "))
            ask_y = int(input("Enter the y coordinate for Center of rotation: "))
            ask_theta = int(input("Enter the angle(in degrees): "))
            ask_copy= input("Do you want to make (a) copy or (b) delete previous one? a/b")
            theta = math.radians(ask_theta)

            if ask_copy == "a":

            
                update_points = rotate(points, theta, ask_x, ask_y)
                make_polygon(update_points)
                
                
                
            else:
                turtle.clear()
            
                update_points = rotate(points, theta, ask_x, ask_y)
                make_polygon(update_points)
                
                ask_save = input("Do you want to save the file? ")
                if ask_save == "Y":
                    save_polygon(update_points)
                    print("\nYour datafile is saved successfully. Thank You! \nIt is saved in the folder which contains this programme\n")
            



        elif ask_anything == "O":
            print(points)
            if len(points)>=3:
                o = int(input("Which coordinate do you want to omit (0,1,2,3... ) from the above list"))
                turtle.clear()
                print(omit(o,points))
            else:
                print("\nSorry you cann't omit, otherwise your polygon won't be formed with two coordinates left! \n")



        elif ask_anything == "add":

            print(points)
            x = int(input("Enter the x coordinate of point you want to add: "))
            y = int(input("Enter the y coordinate of point you want to add: "))
            z = int(input("At which place you wnat to add this point into: (0,1,2,3...)"))
            
            
            turtle.clear()
            print(add(x,y,z,points))




        elif ask_anything == "S":
            s = float(input("What value do you want to scale: "))
            updated = []
            for i in range(len(points)):
                x = points[i][0]
                y = points[i][1]
                x0 = x*s
                y0 = y*s
                updated.append([x0,y0])
            print(make_polygon(updated))



        elif ask_anything == "C":
            c = input("Do you want to make copies by (a) Horizontally (b) Vertically (c) Roationally (d) Scaling:  ")
            n = int(input("How many copies do you want to make? "))
            if c == "a":
                l = int(input ("At what value do you want to make copies linearly: "))
                updated = []
                for z in range(1,n+1):
                    for i in range(len(points)):
                        x = points[i][0]
                        y = points[i][1]
                        x0 = x+(l*z)
                        y0 = y
                        updated.append([x0,y0])
                    
                    print(make_polygon(updated))
                    updated = []
                turtle.penup()
                        

            if c == "b":
                h = int(input ("At what value do you want to make copies horizontally: "))
                updated=[]
                for z in range(1,n+1):
                
                    
                    for i in range(len(points)):
                        x = points[i][0]
                        y = points[i][1]
                        x0 = x
                        y0 = y+(h*z)
                        updated.append([x0,y0])
                    
                    print(make_polygon(updated))
                    updated =[]

            if c == "c":
                a = int(input ("At what angle do you want to make copies rotate: "))
                p = int(input("Enter x coordinate of center of rotation: "))
                q = int(input("Enter y coordinate of center of rotation: "))
                updated = []
                theta = math.radians(a)
                for z in range(1,n+1):
                    for i in range(len(points)):
                        angle = a*z
                        updated= rotate(points,theta,p,q)
                    print(make_polygon(updated))
                    updated =[]

            if c == "d":
                s = float(input ("At what value do you want to make copies by scaling : "))
                updated=[]
                for z in range(1,n+1):
                
                    
                    for i in range(len(points)):
                        x = points[i][0]
                        y = points[i][1]
                        x0 = x*(s**z)
                        y0 = y*(s**z)
                        updated.append([x0,y0])
                    
                    print(make_polygon(updated))
                    updated =[]

            


                
                
            
                

                
            
            
                
            
            

        elif ask_anything == "save":
            save_polygon(points)
            print("\nYour datafile is saved successfully. Thank You! \nIt is saved in the folder which contains this programme\n")


        else:
            exit()


    
                    
if method == "a":
    
    while True:
        points = []
        sides = int(input("\nPlease insert the number of side in a polygon: \n"))
        for i in range(1,sides+1):
            x = int(input(f"\nEnter X{i} coordinate: "))
            y = int(input(f"Enter Y{i} coordinate: "))
            points.append([x,y])
        points.append(points[0])
        if check_intersect(points)== False:
            break
        else:
            continue
    ask_shape = input("\nDo you want (a) With fill or (b) without fill? ")

    if ask_shape == "a":
        pen= input("Please input the pen colour (Suggestions- Black:): ")
        colour = input("Please input the fill colour (Suggestions- Pink:): ")
        turtle.pencolor(pen)
        turtle.pensize(7)
        turtle.fillcolor(colour)
        turtle.begin_fill()
        turtle.penup()        
        turtle.goto(points[0][0],points[0][1])
        turtle.pendown()
        for c in points:
            turtle.goto(c[0]*10,c[1]*10)
            turtle.write(str(c[0])+","+str(c[1]))
        turtle.end_fill()
        turtle.hideturtle()
    else:
        pen= input("Please input the pen colour: ")
        turtle.pencolor(pen)
        turtle.penup()
        turtle.pensize(5)
        turtle.goto(points[0][0],points[0][1])
        turtle.pendown()
        for c in points:
            turtle.goto(c[0]*10,c[1]*10)
            turtle.write(str(c[0])+","+str(c[1]))
        turtle.hideturtle()
        
        
            
        
    

    all_funct(points)
   
elif method == "b":
    List_points = []
    while True:
        filename = input("Enter the file name with desired coordinates: ")
        try:
            infile = open(filename,"r")
            break
        except FileNotFoundError:
            print("File Not Found Error. Please Try Again")

    try:
        for line in infile:
            x,y = line.split(",")
            x = int(x)
            y = int(y)
            List_points.append([x,y])
    except ValueError:
        pass
        
    


    print(make_polygon(List_points))
    all_funct(List_points)




else:
    while True:
        points = []
        sides = int(input("\nPlease insert the number of side in a polygon: \n"))
        for i in range(1,sides+1):
            x = int(input(f"\nEnter X{i} coordinate: "))
            y = int(input(f"Enter Y{i} coordinate: "))
            points.append([x,y])
        points.append(points[0])
        if check_intersect(points)== False:
            break
        else:
            continue
    ask_shape = input("\nDo you want (a) With fill or (b) without fill? ")

    if ask_shape == "a":
        pen= input("Please input the pen colour (Suggestions- Black:): ")
        colour = input("Please input the fill colour (Suggestions- Pink:): ")
        turtle.pencolor(pen)
        turtle.pensize(7)
        turtle.fillcolor(colour)
        turtle.begin_fill()
        turtle.penup()        
        turtle.goto(points[0][0],points[0][1])
        turtle.pendown()
        for c in points:
            turtle.goto(c[0]*10,c[1]*10)
            turtle.write(str(c[0])+","+str(c[1]))
        turtle.end_fill()
        turtle.hideturtle()
    else:
        pen= input("Please input the pen colour: ")
        turtle.pencolor(pen)
        turtle.penup()
        turtle.pensize(7)
        turtle.goto(points[0][0],points[0][1])
        turtle.pendown()
        for c in points:
            turtle.goto(c[0]*10,c[1]*10)
            turtle.write(str(c[0])+","+str(c[1]))
        turtle.hideturtle()
    def make_square(x,colour,text,y=15, pen = "white"):

        from turtle import Screen, Turtle

        FONT_SIZE = y
        FONT = ('Courier', FONT_SIZE, 'bold')

        screen = Screen()

        textbox = Turtle()
        textbox.hideturtle()
        textbox.color(colour)
        textbox.shape('square')
        textbox.shapesize(stretch_wid=2, stretch_len=5)
        textbox.penup()
        textbox.goto(x, 340)
        textbox.stamp()
        textbox.color(pen)
        textbox.goto(x, 340 - FONT_SIZE/2)  # center vertically based on font size
        textbox.write(text, align='center', font=FONT)

            
            
    make_square(-346,"pink","Area",15,"black")
    make_square(-240,"black","Perimeter",13)
    make_square(-134,"pink","Save",15,"black")
    make_square(-28,"black","Omit (x,y)",13)
    make_square(78,"pink","Translate",13,"black")
    make_square(184,"black","Rotate")
    make_square(290,"pink","Add (x,y)",13,"black")
    import turtle
    def button(x,y):
        
        if x<-296 and x>-396 and y < 360 and y> 320:
            print(area(points))
        elif x<-189 and x>-289 and y < 360 and y> 320:
            print(perimeter(points))
        elif x<-85 and x>-184 and y < 360 and y> 320:
            print(save_polygon(points))
        elif x<21 and x>-77 and y < 360 and y> 320:
            print(points)
            if len(points)>=3:
                o = int(input("Which coordinate do you want to omit (0,1,2,3... ) from the above list"))
                turtle.clear()
                print(omit(o,points))
            else:
                print("\nSorry you cann't omit, otherwise your polygon won't be formed with two coordinates left! \n")
        elif x<128 and x>27 and y < 360 and y> 320:
            ask_x = int(input("Enter the x coordinate by how much? "))
            ask_y = int(input("Enter the y coordinate by how much? "))
            ask_copy= input("Do you want to make (a) copy or (b) delete previous one? a/b")

            if ask_copy == "a":

            
                update_points = translate(ask_x, ask_y, points)
                make_polygon(update_points)
                
                
                
            else:
                turtle.clear()
            
                update_points = translate(ask_x, ask_y, points)
                make_polygon(update_points)
                
                ask_save = input("Do you want to save the file? ")
                if ask_save == "Y":
                    save_polygon(update_points)
                    print("\nYour datafile is saved successfully. Thank You! \nIt is saved in the folder which contains this programme\n")


            
        elif x<235 and x>134 and y < 360 and y> 320:
            ask_x = int(input("Enter the x coordinate for Center of rotation: "))
            ask_y = int(input("Enter the y coordinate for Center of rotation: "))
            ask_theta = int(input("Enter the angle(in degrees): "))
            ask_copy= input("Do you want to make (a) copy or (b) delete previous one? a/b")
            theta = math.radians(ask_theta)

            if ask_copy == "a":

            
                update_points = rotate(points, theta, ask_x, ask_y)
                make_polygon(update_points)
                
                
                
            else:
                turtle.clear()
            
                update_points = rotate(points, theta, ask_x, ask_y)
                make_polygon(update_points)
                
                ask_save = input("Do you want to save the file? ")
                if ask_save == "Y":
                    save_polygon(update_points)
                    print("\nYour datafile is saved successfully. Thank You! \nIt is saved in the folder which contains this programme\n")
        elif x<341 and x>240 and y < 360 and y> 320:
            print(points)
            x = int(input("Enter the x coordinate of point you want to add: "))
            y = int(input("Enter the y coordinate of point you want to add: "))
            z = int(input("At which place you wnat to add this point into: (0,1,2,3...)"))
            
            
            turtle.clear()
            print(add(x,y,z,points))
        else:
            pass
    
            
        
            
            

        

        
        
    turtle.onscreenclick(button)

    

    
