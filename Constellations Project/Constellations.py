
# coding: utf-8

# # Constellations Codecademy Project

# In[1]:


get_ipython().run_line_magic('matplotlib', 'notebook')
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[2]:


# Orion
x = [-0.41, 0.57, 0.07, 0.00, -0.29, -0.32,-0.50,-0.23, -0.23]
y = [4.12, 7.71, 2.36, 9.10, 13.35, 8.13, 7.19, 13.25,13.43]
z = [2.06, 0.84, 1.56, 2.07, 2.36, 1.72, 0.66, 1.25,1.38]


# In[15]:

#Create a 2D visualization 
fig = plt.figure()
fig.add_subplot(1,1,1)
plt.scatter(x,y,color='red', marker='*')
plt.title('Orion 2D Constellations')
plt.show()


# In[17]:

#Create a 3D visualization
fig_3d = plt.figure()
constellation3d = fig_3d.add_subplot(1,1,1,projection="3d")
constellation3d.scatter(x,y,z, marker='*', color='orange')
plt.title('Orion 3D Constellation')
plt.show()

