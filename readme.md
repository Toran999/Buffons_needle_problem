<h1 align="center">Buffon's Needle Problem</h1>
I have created a program in python that simulates the famous Buffon Noodle method or 
Buffon needle method to approximate the value of PI, one of the most important Mathematical constant.
In this experiment, Pi shows up in seemingly unusal place.

Consider an experiment in which equally spaced parallel lines are drawn on grounds.
Now consider a needle or noodle or match or whatever object having very small width and length equal to the 
distance between the parallel lines drawn on  the ground. 

Now If you dropped the needle or match then what is the probability that the needle will cross the 
lines that you drew?

<img src="/imgs/final_project.jpg" width="100%" alt="experimental setup"/>
The matches you dropped will have random orientations and they can land anywhere on the grid.
So how do we calculate its probability??? Preety intense right?
Don't panic because luckily some old folks from 18th century came up with a whole field of 
mathematics known as geometric probability and 
                                                  
#### IT TURNS OUT THAT THE PROBABILITY OF NEEDLE LANDING ON LINE IS 2/PI !!! 

ISN'T IT INSANE??? HOW PI SHOWS UP IN UNIMAGINABLE PLACES???

There is another remarkable theorem in mathematics called CENTRAL LIMIT THEOREM 
that says if we repeat an probabilistic experiment infinite number (many) times we 
will get the total probability equal to the probability for each event to occur.

<p align="center">Or</p>
Simply put, if we toss a coin for n number of time and get m number of head or tail then 
m/n = 1/2 as n approaach to infinity. i.e. we will get almost equal no of head and tail on the long run.

or say, We rolled a dice for 600,000 times then we will get each number(1,2,3,4,5,6) for about 100,000
times.

that is, if we dropped our needle or matchsticks for many times, the ratio of needles that crossed  or touched the lines to the total number of needles dropped will be equal to 2/pi.

By using this to concept together we get the value of pi will be equal to 

                    PI = 2 / probability

But we have one problem left..................

Dropping needles or matches for a million times and observing how many needles crossed the lines is too tedious to do.
Last time it was 1901 when a guy named Mario Lazzarini performed it for 3408 times.

We aren't going to do that because we have a sophisticated machine and a powerful language to order it that together can
simulate this whole process of dropping needles on a grid line in only 15 lines of instructions!!!!!!!

So I just saved your 8 hours of manual tedious work under some few lines of codes.

<p align="center"><img src="/imgs/final_proj1.png" width="100%" alt="experimental setup"/></p>
So let's discuss how will we simulate this whole experiment in python.

1. So first of all,  dropping a needle from a height is completely random process as we don't know where will the needle land.
   So for working with this probabilistic event we will import a library called random in our program. We will be working with some math functions so we will import math library as well.
2. We define a variable named crossed whcih counts how many needles crossed the lines.
3. User provides input on how many needles should be tossed or how many times should a needle be tossed and store it in          
    variable named total.
4. As python stores user input variables as string we change it into integer with a pre built function int().
5. we create a for loop for total number of lines that tosses the needle for total number of times.
6. inside for loop we define a variable named head which is the position of the needle head when dropped on the grid from our     
    arbitary zero till one. zero and one are position where our two lines drawn on the ground are. so we take only two gridlines from the ground for simplification of the condition and allow our needle head to be between or on these lines.
7. we assign a random float to the position  (vertical distance from the zero line) of our head relative to the zero line. This 
    acts as dropping of needles as both.
    position of head of the needle after it is dropped and selecting a random number are both random process.
8. We use the uniform method of random library to get this point as our needle head can lie in anywhere. So we need to have     
    continuous values to select from.
9. Theta gives the orientation of the needle with respect to our zero line on the grid. The needle can make any angle from 0 to 
    360 degree (or 0 to 2π) with the grid lines. Since math library in python uses radian as unit of angle (and I don't want π to appear any where in my program ;) and luckily Sine function is continuous through all the value of theta ) We randomly choose through infinite values of theta (or very large value works as well) as angle to simulate the random orientation of needle after the drop.
10. The round function allows our values of head and theta to round off and I round of these values to nearest 3 decimal places 
    so that we will have fewer digits to work with.
11. we define a variable named y that defines the vertical distance of tip of needle from its head position. to do this, we use 
    sin() method from math library. As our length of needle is 1 unit (equal to the distance between two lines in the grid) and the hypotenuse(length of needle) times sin of the angle with horizontal gives the heigth of the triangle( or vertical distance between needle's head and tip in our case), the sin(theta) gives the vertical distance between tip and head of our needle. we store it in a variable named y.
12. As the value of sin() can be both negative and positive we can have both positive or negative value of y.
13. The sum of y and head gives the vertical position of tip relative to the zero line. the sum is stored in the variable named 
    tip.
14. if the tip is greater than or equal to one or the tip is less than or equal to zero our needle has crossed the line. This is 
    because the head of needle lies between the zero and one line and the tip lying above the one line or below the zero line means it crossed either zero or one line. This will increment the value of crossed by 1.
15. When the program has run for user defined (total) number of times our program calculates the probability as
            probability = (number of neeedles that crossed or touched the lines)/(total number of needles tossed) 
                        =crossed/total
    and stores it in p.
16. Then pi is given by
                                        pi = 2/p
17. Finally the program displays the value of pi approximated through this method.

####  Do not expect to get a very good approximation of pi through this method. The more number of times you toss the needle, the more LIKELY you are to get better approximation. And running a iteration for large number of times requires very high computational power or longer time so this is the limitation of this method and this program as well. 
#### But it is always thrillful to get to see your favorite number in such an unexpected place. So embrace the beauty of pi through this program. Besides, This program can be helpful to show how simple yet powerful device the computer is. Furthermore, You may also have realized how useful scientific tools can the programs be.

## Resource Materials And References
[1. Pi and Buffon's Matches - Numberphile](https://www.youtube.com/watch?v=sJVivjuMfWA) </br>
[2. Buffon's needle problem](https://en.wikipedia.org/wiki/Buffon%27s_needle_problem)