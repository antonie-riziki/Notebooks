import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)

plt.style.use('classic')
fig=plt.figure(figsize=(5,3))
ax = plt.axes(facecolor='#E6E6E6')
# Display ticks underneath the axis
ax.set_axisbelow(True)
# White frame
plt.grid(color='w', linestyle='solid')

# Hide the frame
for spine in ax.spines.values():    
    spine.set_visible(False)
    
# Hide the markers at the top and the right
ax.xaxis.tick_bottom()
ax.yaxis.tick_left()

# We can personalise the markers, and rotate them
marqueurs = [-3, -2, -1, 0, 1, 2, 3]
xtick_labels = ['A', 'B', 'C', 'D', 'E', 'F']
plt.xticks(marqueurs, xtick_labels, rotation=30)

# Change the color of markers
ax.tick_params(colors='gray', direction='out')
for tick in ax.get_xticklabels():    
    tick.set_color('gray')
for tick in ax.get_yticklabels():    
    tick.set_color('gray')    
    
# Change the color of the edges
ax.hist(x, edgecolor='#E6E6E6', color='#EE6666');
plt.axes(projection = "3d")
plt.show()
