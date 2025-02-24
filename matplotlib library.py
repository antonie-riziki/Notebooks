#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize = (5,3))#Container that contains all objects(data, axes, labels etc.)
plt.xkcd()#Print a sketch like graphical presentation
plt.style.use('ggplot')
x = np.linspace(0, 10, 1000) #generating range of numbers 0 - 10, with a spacing of 1000
plt.rcParams.update({'font.size': 12})
plt.plot(x, np.sin(x), color = 'black', label = 'sin(x)') #plot axis (x,y)
plt.axis([0, 10, -1, 1])#Removes whitespace on the graph. Fits graph to the plot area
plt.title ('Graphical Presentation of Sin(x)')
plt.legend(loc = "lower left")#Positions the legend, accompanied with the label
ax = plt.axes()
ax.set(xlabel = "x", ylabel = "sin(x)")
plt.grid(False)
plt.tight_layout()
plt.savefig("Sin(x).png")
plt.show()


fig = plt.figure()
ax = plt.axes()
x = np.linspace(0, 10, 1000)
y = np.linspace(0, 10, 1000)
z = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x), color = "black", linestyle = "solid", label = "sin(x)");
plt.plot(y, np.sin(y - 1), color = "blue", linestyle = "dotted", label = "sin(y)")
plt.plot(z, np.sin(z - 2), color = "red", linestyle = "dashdot", label = "sin(z)")
plt.axis([0, 10, -1, 1])
plt.title("Graphical Presentation of Sin(x,y,z)")
plt.legend(loc = "best")
#plt.axes(projection = "3d")
ax.set(xlabel = "data 1", ylabel = "data 2")
plt.show()


# Change default font size
plt.rcParams.update({'font.size': 15})

fig = plt.figure()
#ax = plt.axes(projection = "3d")

# Solid line, color specified by its name
plt.plot(x, np.sin(x - 0), color='blue', linestyle='solid', label='bleu')
# Short name for color, dashed line
plt.plot(x, np.sin(x - 1), color='g', linestyle='dashed', label='vert')
# Grayscale between 0 and 1, dashes and dots
plt.plot(x, np.sin(x - 2), color='0.75', linestyle='dashdot', label='gris')
# RGB color, dotted line
plt.plot(x, np.sin(x - 3), color='#FF0000', linestyle='dotted', label='rouge')
# Axis limits. Try also 'tight' and 'equal' to see their effect
plt.axis([-1, 11, -1.5, 1.5])
# Labels
plt.title("Example of a graph")
# The legend is generated from the argument 'label' of 'plot'
# 'loc' specified the placement of the legend.
plt.legend(loc='best');
# Axis titles
ax = ax.set(xlabel='x', ylabel='sin(x)')
plt.show()

print(plt.style.available[:6])
#d = plt.axes(projection = "3d")
# Change the size of the figure
fig = plt.figure(figsize=(12,8))
for i in range(6):    
    # This is how you add subplots
    fig.add_subplot(3,2,i+1)    
    plt.style.use(plt.style.available[i])    
    plt.plot(x, y)        
    # This is how you write on a plot
    plt.text(s=plt.style.available[i], x=5, y=2, color='red')
plt.show()
