# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 20:06:48 2020

@author: user
"""
  
from pulp import *;

#This block of statement creates the linear programming model
prob = LpProblem("Giapetto",LpMaximize); #Create a LP maximization problem
x1 = LpVariable("x1",lowBound=0); #create a variable x1>-=0
x2 = LpVariable("x2",lowBound=0); #create another variable x2>=0
#objective function
prob += 20*x1+30*x2;

#Finishing hours
prob += 1*x1+2*x2 <= 100;
#Carpentary hours
prob+=2*x1+1*x2 <= 100;

#display the LP problem
prob;


#solving the LPP
status = prob.solve(); #solve with the default solver
print(LpStatus[status]); #print the solution status

print(value(x1));
print(value(x2));
print(value(prob.objective));


  #Plot the graph
  %matplotlib notebook
  %run giapetto_colormap.py