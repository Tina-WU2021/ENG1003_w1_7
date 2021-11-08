
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
 <img width="570" height="450" src="https://github.com/WxtTina/ENG1003_w1_7/blob/main/task%201_.gif"/> 
 
 
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
        self.Delta_F_A =  #e
        self.Delta_T_A =  #f
```


#### At first we write the following code:
```
 list1=[1000]
        for a in range(1,20):
            for b in range(1,20):
                for c in range(1,20):
                    for d in range(1,20):
                                if a*b+c*d>=25 and a+c>=10 and b+d>=10:
                                    result=a*b+c*d+10
                                    list1.append(result)
                                    if(result==53):
                                      print(a,b,c,d)
        
        x=10000000
        for i in range(len(list1)):
            if x>list1[i]:
                x=list1[i]
        print (x)

```
#### And get the result of x=35 and the corresponding sets of a, b, c and d
![This is an image](https://github.com/WxtTina/ENG1003_w1_7/blob/main/Task2_2__2.png)

#### The final cost is calculated based on the following line:
```
self.costPerGrid = self.C_F * self.Delta_F + self.C_T * self.Delta_T + self.C_C
```
#### We conlcude that the result  self.costPerGrid  remains the same when  self.C_F  and  self.Delta_F  exchange their value, so there are multipule results towards this issue.

#### But then we discovered:
```
        self.Delta_F_A =  #e
        self.Delta_T_A =  #f
 ```
#### These two variables would also effect the final cost.
#### So we modified the code to:
```
        
        list1=[1000]
        for a in range(1,20):
            for b in range(1,20):
                for c in range(1,20):
                    for d in range(1,20):
                        for e in range(1,20): 
                            for f in range(1,20):
                                if a*b+c*d>=25 and a+c>=10 and b+d>=10 and e+f>=10:
                                    result=a*(b+e)+c*(d+f)+10
                                    list1.append(result)
                                   
        
        x=10000000
        for i in range(len(list1)):
            if x>list1[i]:
                x=list1[i]
        print (x)
```
#### and get the result of x=53

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
                            if(result==53):
                                print(a,b,c,d,e,f)
```
#### and then we get the following output:
![This is an image](https://github.com/WxtTina/ENG1003_w1_7/blob/main/Task2.2.png)
#### when modify these two sets of numbers, 
#### the set 1 16 9 1 9 1 will get the final cost of 5042.361107568212
#### the set 9 1 1 16 1 9 will get the final cost of 5023.340905032679
#### So the final result would be:
```
        self.C_F = 9 #a
        self.Delta_F = 1 #b
        self.C_T = 1 #c
        self.Delta_T = 16 #d
        self.C_C = 10
        
        self.Delta_F_A = 1 # additional fuel #e
        self.Delta_T_A = 9
```





# Task3
**Click the link to view the original code: https://github.com/WxtTina/ENG1003_w1_7/blob/main/Task3**
## Methodology:
### The minus cost area(takes 16 grid points):
#### We noticed that there are straight line in our result, and since the minus cost area doesn't have a regulated shape, we decided to base the minus cost area base on the original result, which means that we would let the minus cost area and the original path coincide.
#### To modify the code: The strategy for setting up minus time area are similar to the fule consuming area and the time consuming area, so we modified to code accordingly.
#### Some code we modified:
#### for initializing(around line 25):
```
def __init__(self, ox, oy, resolution, rr, fc_x, fc_y, tc_x, tc_y, mc_x, mc_y):
```
#### for calculating the final cost(around line 60):
```
        self.C_P = -2
        self.Delta_P = 2
        self.costPerGrid = self.C_F * self.Delta_F + self.C_T * self.Delta_T + self.C_C + self.C_P * self.Delta_P
```
#### add minus consuming area:
```
                # add minus consuming area
                if self.calc_grid_position(node.x, self.min_x) in self.mc_x:
                    if self.calc_grid_position(node.y, self.min_y) in self.mc_y:
                        # print("minus time consuming area!!")
                        node.cost = node.cost + self.C_P * self.Delta_P * self.motion [i][2]
```

## Result:

 <img width="570" height="450" src="https://github.com/WxtTina/ENG1003_w1_7/blob/main/task%203.gif"/> 

 


# Reflective Essay
## 1 WU Xiaotao
####  I have been learning C++ before this program started, so I have some basic knowledge of computer programming. For the tasks assigned to our group, I can understand what our final target should be. Based on the python code with comments clearly instructing what they are used for, I can briefly understand the structure as well as the ideal purpose of the code, thus, task 1 and task2.1 is of little difficulty to me. For task2.2 and task3, I worked with our teammates, sought help from the tutor and our classmates and finally figured out the solution. It’s of great satisfaction in actually dealing with a practical problem, I really enjoyed the process.
#### Since I have been the group leader, I have gained a unique experience about how to collaborate with our teammates, separate our tasks and distribute them to the more suitable person in the team. I also get to know some classmeates who are really talented in coding and solving problems. I learnt a lot from them, and I look up to them. It is of great pleasure studying with them. 
#### Although we have faced many problems during the process, we managed to solve them through multiple attempts. After joining this program, I got a deeper understanding of the idea lying under the codes, and of the applicable thinking methods towards a certain practical problem. Besides, I get to know Github, and have learnt how to write a readme page, I think I would get a chance to use them in the future. GIthub is a perfect online community from which I have learnt and can learn various skills.

## 2 Chan Hoi To
####  Before this program, computer programming is totally new for me, and I have nearly no idea about how it works. But after communicating with our group leader and groupmates for task 1 to find the minimum cost for flight, I have a simple understanding of the principle of python code. This allows me to contribute to the following tasks. For the remaining tasks, my groupmates and I communicate to assign tasks for different members according to our talents, also collaborate on some challenging parts to achieve it like designing the area to reduce flight cost. To conclude, this experience is unique and beneficial for me as it allows me to gain computing knowledge as well as the ways to collaborate with classmates which is useful for my near future.

## 3 Wang Li
####  I haven’t been exposed to computer programming before, so designing the path planning is pretty difficult for me. Fortunately, the teacher is patient and groupmates are enthusiastic. With the teacher’s help and groupmates’ cooperation, we finished task 1, find the minimum cost for flight and complete the remaining tasks as arranged by the group leader. Even though we encountered many difficulties, like downloading the python, we have overcome them one by one. After completing group tasks together, I have a new understanding of my abilities, I also understand the importance of teamwork and know that we should sometimes rely on the strength of the group, rather than relying on our own strength to complete certain problems. Most importantly, I learn that every person in the group needs to work hard to make the team stronger. 

## 4 Tsang Kai Lok
#### Before joining this freshman seminar project, I have never learned about computer programming. So, in the beginning, I think this path planning algorithm will be a challenging task for me. But after communicating with my groupmates and group leader, they taught me some basic concepts about python, we cooperate to finish task 1 for finding the minimum cost for flight. For the following tasks, the group leader assigned me to finish task 2.1. In this task, I need to use four equations to find two unknowns by using the graphical method. In addition, we also collaborate on some additional tasks which are challenging. To conclude, I feel grateful to cooperate with my groupmates and this project allows me to understand more about computer programming especially python which is useful for my future career path. 
## 5 HO Hin Yeung
####  Before taking this class, I didn’t learn any programming language. After attending this class, I have learned how to code in python and how to use GitHub. I found using GitHub to collaborate with others is convenient because we can finish jobs within our branches. After that, we can easily merge our changes into the main branch after checking. Although I faced some difficulties throughout the project, I got help from my groupmates and finally solved the problem. I felt glad to finish the project together with my groupmates.  I believe this experience will be helpful in the future when I have chances to cooperate with people.






