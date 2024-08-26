#!/usr/bin/env python
# coding: utf-8

# # Programming HW1 (25 points total)
# 
import numpy as np


# In[2]:


#This will go through your input matrix and manipulate each row and turn it into echelon form we discussed in class.
# If you are not able to make it into echelon form, then it is a singular matrix i.e., determinant is 0.
#hence we will return true, if it is successful then return True. 
#Do not make any changes here

def isSingular(A) :
    B = np.array(A,dtype=np.float_) # Lets make a copy as we are going to change this matrix
    try:
        alterRowZero(B)
        print(B)
        alterRowOne(B)
        print(B)
        alterRowTwo(B)
        print(B)
        alterRowThree(B)
        print(B)
        
    except ItIsSingular:
        return True
    return False

#this is our error class. no need to make any changes here
class ItIsSingular(Exception): pass


# In[3]:


#Remember that for the first row, all we need is the first element to be 1. 
#We can do it by dividing the whole row by the value of the element i.e., A[0,0]
#However if A[0,0] is zero, then we are in trouble.. so need to test for that.
#if that is the case we can add the lower row one by one to make sure we have a non zero first element.

# Do not edit this.
def alterRowZero(A) :
    if A[0,0] == 0 :
        A[0] = A[0] + A[1]
    if A[0,0] == 0 :
        A[0] = A[0] + A[2]
    if A[0,0] == 0 :
        A[0] = A[0] + A[3]
    if A[0,0] == 0 :
        raise ItIsSingular()
    A[0] = A[0] / A[0,0]
    return A

#We need to make the element below the diagonal element zero i.e. A[1,0]
# Next make A[1,1] = 1
# We'll divide the row by the value of A[1, 1].
# Do the zero test again

# There is no need to edit this function.
def alterRowOne(A) :
    A[1] = A[1] - A[1,0] * A[0]
    if A[1,1] == 0 :
        A[1] = A[1] + A[2]
        A[1] = A[1] - A[1,0] * A[0]
    if A[1,1] == 0 :
        A[1] = A[1] + A[3]
        A[1] = A[1] - A[1,0] * A[0]
    if A[1,1] == 0 :
        raise ItIsSingular()
    A[1] = A[1] / A[1,1]
    return A


# In[4]:


# Complete this function
def alterRowTwo(A) :
    # Make the required elements in row two to zero (hint: there are 2 of them).
    A[2] = A[2] - A[2,0] * A[0]
    A[2] =A[2] -A [2,1] * A[1]
    # zero test
    if A[2,2] == 0:
        A[2] = A[2] + A[3]
        A[2] = A[2] - A[2, 0] * A[0]
        A[2] = A[2] - A[2, 1] * A[1]
    
    if A[2,2] == 0:
        raise ItIsSingular()
    # Finally set the diagonal element to one by dividing the whole row by that element.
    A[2] = A[2] / A[2,2]
    return A


# In[5]:


# You should also complete this function
# Follow the instructions inside the function at each comment.
def alterRowThree(A) :
    #Insert code below to set the sub-diagonal elements of row three to zero.
    A[3] = A[3] - A[3,0] * A[0]
    A[3] = A[3] - A[3,1] * A[1]
    A[3] = A[3] - A[3,2] * A[2]
    # zero test
    if A[3,3] == 0:
        raise ItIsSingular()
    # Finally set the diagonal element to one by dividing the whole row by that element.
    A[3] = A[3] / A[3,3]
    return A


# In[6]:


#Sanity check. You should get the following solution when you run this.
A = np.array([
        [2, 0, 0, 0],
        [0, 3, 0, 0],
        [0, 0, 4, 4],
        [0, 0, 5, 5]
    ], dtype=np.float_)

isSingular(A)


# In[7]:


#Sanity check. You should get the following solution when you run this.
A = np.array([
        [0, 7, -5, 3],
        [2, 8, 0, 4],
        [3, 12, 0, 5],
        [1, 3, 1, 3]
    ], dtype=np.float_)

alterRowZero(A)
isSingular(A)


# In[8]:


alterRowOne(A)


# In[9]:


alterRowTwo(A)


# In[10]:


alterRowThree(A)


# ## General case (10 points)
# 
# Generalize your code for any dimenstion of square matrix.

# In[11]:


def isSingular(A):
    B = np.array(A, dtype=np.float_)
    try:
        for i in range(len(B)):
            alterRows(B, i)
            print(B)
    except ItIsSingular:
        return True
    return False

def alterRows(B, row):
    # Make the required elements in row two to zero
    if B[row, row] == 0:
        for i in range(row + 1, len(B)):
            B[row] += B[i]
            if B[row, row] != 0:
                break
    # zero test
    if B[row, row] == 0:
        raise ItIsSingular()
    
    # Set the diagonal element to one by dividing the whole row by that element.
    B[row] = B[row] / B[row,row]
    
    # set elements to zero
    for i in range(row + 1, len(B)):
        B[i] -= B[i, row] * B[row]

# Test with first example
A = np.array([
        [2, 0, 0, 0],
        [0, 3, 0, 0],
        [0, 0, 4, 4],
        [0, 0, 5, 5]
    ], dtype=np.float_)

#Test with second example
C = np.array([
        [0, 7, -5, 3],
        [2, 8, 0, 4],
        [3, 12, 0, 5],
        [1, 3, 1, 3]
    ], dtype=np.float_)

print(isSingular(A))
print(isSingular(C))

