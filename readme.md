
<p align="center">

  <h3 align="center">PolyU ENG1003 AAE Freshman Project_Group7</h3>


<!-- Overview -->
<details open="open">
  <summary><h2 style="display: inline-block">Overview</h2></summary>
  <ol>
    <li><a href="#Background-of-Path-Planning-to-aviation-engineering"> Background of Path Planning to aviation engineering</a></li>
    <li><a href="#Theory-of-the-Path-planning-Algorithm">Theory of the Path planning Algorithm</a></li>
    <li><a href="#Introduction-of-the-engineering-tools">Introduction of the engineering tools</a></li>
    <li><a href="#Task1">Task1</a></li>
    <li><a href="#Task2_1">Task2_1</a></li>
    <li><a href="#Task2_2">Task2_2</a></li>
    <li><a href="#Task3">Task3</a></li>
    <li><a href="#Task4">Task4</a></li>
    <li><a href="#Reflective-essay">Reflective essay</a></li>
    <li><a href="#Refernces">References</a></li>
  </ol>
</details>



<!-- Background of Path Planning to aviation engineering -->
## Background of Path Planning to aviation engineering
Path planning is a computational problem for a flight to travel from an origin airport to the destinated airport with a minimum cost and safest journey. It is a must for pilots to complete as crowded airspace needs a collaborative path planning in order to fully utilize the sky and provides a safe journey for passengers. Apart from the best use of airspace, path planning is also important for commercial airlines to reduce flight cost. Based on the cost index, a shortest flight cruising in less fuel consumed altitude can be planned, thus minimizing the flight cost. 


<!-- Theory of the Path planning Algorithm -->
## Theory of the Path planning Algorithm
Path planning algorithms generate a geometric path, from an initial to a final point, passing through pre-defined via-points, either in the joint space or in the operating space of the robot, while trajectory planning algorithms take a given geometric path and endow it with the time information

<!-- Introduction of the engineering tools -->
## Introduction of the engineering tools
**Python**

Python is an interpreted, interactive, object-oriented programming language.
programming language, python is mainly used for web development, software development, mathematics and system scripting. Also, we can use python on the server to create web applications, connect to database systems for modifying files, handle big data and perform complex mathematics.



**Github**

GitHub is a web-based interface that uses Git, the open source version control software that lets multiple people make separate changes to web pages at the same time. As Carpenter notes, because it allows for real-time collaboration, GitHub encourages teams to work together to build and edit their site content.
<!-- Task1 -->


# Task1
**Click the link to view the original code: https://github.com/WxtTina/ENG1003_w1_7/blob/main/Task1**
## Methodology:
### To complete the assigned challenge for our group:
#### ---------------------------------------------------------------------Adding the program photo of group 7
#### Start and goal position:
```
# start and goal position
    sx = -5.0  # [m]
    sy = 30.0  # [m]
    gx = 50.0  # [m]
    gy = 15.0  # [m]
    grid_size = 1  # [m]
    robot_radius = 1.0  # [m]
```
#### Set border:
```
 # set obstacle positions for group 7
    ox, oy = [], []
    for i in range(-10, 60): # draw the button border 
        ox.append(i)
        oy.append(-10.0)
    for i in range(-10,60 ): # draw the right border
        ox.append(60.0)
        oy.append(i)
    for i in range(-10, 60): # draw the top border
        ox.append(i)
        oy.append(60.0)
    for i in range(-10, 60): # draw the left border
        ox.append(-10.0)
        oy.append(i)
#set free border
    for i in range(-10, 35):
        ox.append(i)
        oy.append(15+i)
    for i in range (25,60):
        ox.append(i)
        oy.append(-25+i)
 ```
#### Set fuel consuming area:
```
# set fuel consuming area
   fc_x, fc_y = [], []
    for i in range(10, 25):
        for j in range(30, 55):
            fc_x.append(i)
            fc_y.append(j)
```
#### Set time consuming area
```
# set time consuming area
    tc_x, tc_y = [], []
    for i in range(20, 38):
        for j in range(10, 25):
            tc_x.append(i)
            tc_y.append(j)
 ```
  
 ## The result: 
 
 
 ### ----------------------------------------------------------------------------------------------The .gif of Task1(Use the data from Polyu-A380)
 
 
|Aircraft Model   |C_F     | Del_F   | C_T     |Del_T    |C_C      |Del_F_A  |Del_T_A  |Cost     |
| :-----:          | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |  :-----:  |
| PolyU-A380   | 1 | 1   | 2 | 5 | 10 | 0.2 | 0.2 | 2941.417 |
| PolyU-A381   | 1 | 1.5 | 3 | 5 | 10 | 0.3 | 0.4 | 3714.716 |
| PolyU-A382   | 1 | 2.0 | 4 | 5 | 10 | 0.4 | 0.5 | 4486.516 | 
| PolyU-A383   | 1 | 2.5 | 5 | 5 | 10 | 0.5 | 0.1 | 5250.815 |


#### Among all 4 aircrafts, Polyu-A380 achieved the minimum cost



# Task2_1
**Click the link to view the original code: https://github.com/WxtTina/ENG1003_w1_7/blob/main/Task2**
## Methodology & Result:
### The 2 variables should meet the following condition:
#### self.C_T - self.C_F <=30
#### -0.5*self.C_T + self.C_F <=-30
#### 2*self.C_T + self.C_F >=20
#### -4*self.C_T + self.C_F >=-220
#### We solved this problem by drawing a graf on symbolab
#### x represents C_F; y represents C_T in the following graf
#### ![This is an image](https://github.com/WxtTina/ENG1003_w1_7/blob/main/%E8%9E%A2%E5%B9%95%E6%88%AA%E5%9C%96%202021-10-21%20%E4%B8%8B%E5%8D%8810.03.03.png)
#### We tried the set of values of the four corners, and get the following results: 
|C_F     | C_T     |Cost     |
| :-----: | :-----: | :-----: |
| 20 | 20 | 29504.16664 | 
| 40 | 60 | 71438.69042 | 
| 40 | 10 | 36493.25394 |
| 50 | 20 | 50471.42853 |
#### Eventually, we figured out the set of variables that would lead to the minimum final cost, which is (20,20)



# Task2_2
**Click the link to view the original code: https://github.com/WxtTina/ENG1003_w1_7/blob/main/Task2**
## Methodology & Result:
### The 4 variables should meet the following condition:
#### self.C_F * self.Delta_F +  self.C_T * self.Delta_T >=25
#### self.C_F + self.C_T >=10
#### self.Delta_F + self.Delta_T >=10
#### self.Delta_F_A + self.Delta_T_A >=10

#### To simplify to code:
```
        self.C_F #a
        self.Delta_F = #b
        self.C_T = #c
        self.Delta_T = #d
```
#### First we add the following code:
```
        list1=[1000]
        for a in range(20):
            for b in range(20):
                for c in range(20):
                    for d in range(20):
                        if b*c+a*d>=25 and a+b>=10 and c+d>=10:
                            result=b*c+a*d+10
                            list1.append(result)
                                       
        x=10000000
        for i in range(len(list1)):
            if x>list1[i]:
                x=list1[i]
        print (x)
```
#### and get the result of x=35
![This is an image](https://github.com/WxtTina/ENG1003_w1_7/blob/main/Task2_2__1.png)
#### then we change the code into:
```
        list1=[1000]
        for a in range(20):
            for b in range(20):
                for c in range(20):
                    for d in range(20):
                        if b*c+a*d>=25 and a+b>=10 and c+d>=10:
                            result=b*c+a*d+10
                            list1.append(result)
                            if(result==35):
                                print(a,b,c,d)
```
#### and then we get the following output:
![This is an image](https://github.com/WxtTina/ENG1003_w1_7/blob/main/Task2_2__2.png)
#### when modify these sets of numbers, the final cost remains the same, which is 5042.361107568211
#### ------------------------------------------------------------------------------------------------------add pictures]

## Discussion
#### The final cost is calculated based on the following line:
```
self.costPerGrid = self.C_F * self.Delta_F + self.C_T * self.Delta_T + self.C_C
```
#### Since the result  self.costPerGrid  remains the same when  self.C_F  and  self.Delta_F  exchange their value, so there are multipule results towards this issue. 




# Task3
**Click the link to view the original code: https://github.com/WxtTina/ENG1003_w1_7/blob/main/Task3**
## Methodology:
### The minus cost area(takes 16 grid points):
#### We noticed that there are straight line in our result, and since the minus cost area doesn't have a regulated shape, we decided to base the minus cost area base on the original result, which means that we would let the minus cost area and the original path coincide.
## Result:
### ----------------------------------------------------------------------------------------------The .gif of Task3
 


# Reflective Essay
## 1 WU Xiaotao
####  I have been learning C++ before this program started, so I have some basic knowledge of computer programming. For the tasks assigned to our group, I can understand what our final target should be. Based on the python code with comments clearly instructing what they are used for, I can briefly understand the structure as well as the ideal purpose of the code, thus, task 1 and task2.1 is of little difficulty to me. For task2.2 and task3, I worked with our teammates, sought help from the tutor and our classmates and finally figured out the solution. It’s of great satisfaction in actually dealing with a practical problem, I really enjoyed the process.
#### Since I have been the group leader, I have gained a unique experience about how to collaborate with our teammates, separate our tasks and distribute them to the more suitable person in the team. I also get to know some classmeates who are really talented in coding and solving problems. I learnt a lot from them, and I look up to them. It is of great pleasure studying with them. 
#### Although we have faced many problems during the process, we managed to solve them through multiple attempts. After joining this program, I got a deeper understanding of the idea lying under the codes, and of the applicable thinking methods towards a certain practical problem. Besides, I get to know Github, and have learnt how to write a readme page, I think I would get a chance to use them in the future. GIthub is a perfect online community from which I have learnt and can learn various skills.

## 2 Chan Hoi To
####  Before this program, computer programming is totally new for me, and I have nearly no idea about how it works. But after communicating with our group leader and groupmates for task 1 to find the minimum cost for flight, I have a simple understanding of the principle of python code. This allows me to contribute to the following tasks. For the remaining tasks, my groupmates and I communicate to assign tasks for different members according to our talents, also collaborate on some challenging parts to achieve it like designing the area to reduce flight cost. To conclude, this experience is unique and beneficial for me as it allows me to gain computing knowledge as well as the ways to collaborate with classmates which is useful for my near future.


## 3 Wang Li
####  After take the class,i learned what the python is and the fundamental way to use the python.Besides,i know what is the github is designed for.what’s more,although i faced many difficulty like download python and the way to use python, but the class i take raised my interest on AAE and programming,making me want to learn what is the meaning of every symbol in the code which is given by the teacher.Most importantly,i learned the importance of the teamwork ,it is impossible to finish the hole work by myself,but with everyone’s great effort,we make it.In this special experience,i also learned that all the participants should participate in activities actively,to make the team stronger and have ability to finish the task.

## 4
## 5






