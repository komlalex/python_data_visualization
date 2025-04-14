"""DATA VISUALIZATION USING PYTHON, MATPLOTLIB AND SEABORN 
Data visualization is the graphic representation of data. It involves producing 
images that can communicate relationaships among the represented data to viewers. 
Visualizing data is an essential part of data analysis and machine learning. In this 
tutorial, we'll use Python libraries Matplotlib and Seaborn to learn and apply 
some popular data visualiztion techniques."""  
import matplotlib.pyplot as plt 
import seaborn as sns 

"""Line Chart 

Line charts are one of the simplest and most midely used data visualization 
techniques. A line chart displays information as a series of data points 
or markers, connected by straight lines. You can customize the shape, size , color 
and other aesthetic elements of the markers and lines for better visual clarity. 

Here's a Python list showing the yield of apples (tons per hectare) over six years 
in an imaginary country called Kanto
"""

yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931] 

"""We can visualize how the yield of apples changes over time using the line 
chart. To draw a line chart, we can use the plt.plot function"""
#plt.figure() 
#plt.plot(yield_apples)  

"""Let's enhance this plot step-by-step to make it more informative and 
beautiful.""" 

"""Customizing the X-axis 
The X-axis of the plot currently shows list elements indexed 0 to 5. The 
plot would be more informative if we could show the year for which the data 
is being plotted. We can do this by two arguments plt.plot"""
years = [2010, 2011, 2012, 2013, 2014, 2015]
yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]   
#plt.figure()
#plt.plot(years, yield_apples) 

"""Axis Labels 
We can add labels to the axes to show what each axis represents using the 
plt.xlabel and plt.ylabel methods. 
"""
#plt.xlabel("Year") 
#plt.ylabel("Yield (tons per hectare)") 

"""Plotting Multiple Lines
It's really easy to plot multiple lines in the same graph. Just invoke the 
plt.plot multiple times. Let's compare the yields of apples vs oranges in Kanto.

"""
years = range(2000, 2012) 
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9372, 0.939, 0.9342] 
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, 0.893] 

#plt.figure()
#plt.plot(years, apples) 
#plt.plot(years, oranges) 
#plt.ylabel("Yield (tons per hectare)")
#plt.xlabel("Year")

"""Chart Title and Legend 
To differentiate between multiple lines, we can include a legend 
within the graph using the plt.legend function. We also give the entire 
chart a title using the plt.title function. 
""" 
#plt.title("Crop Yields in Kanto")
#plt.legend(["Apples", "Oranges"]) 


"""Line Markers 
We can also show markers for data points on each line using the marker 
argument of plt.plot. Matplotlib supports many different types of markers like 
circles, squares, cross, diamond etc.  

Styling Lines and Markers  
The plt.plot function supports many arguments for styling lines and markers: 
* color or c: set the color of the line 
* linestyle or ls: choose between a solid or dashed line 
* linewidth or lw: set the width of a line 
* markersize or ms: set the size of the markers 
* markeredgecolor or mec: set the edge color for markers 
* markerfacecolor or mfc: set the fill color for markers 
* alpha: opacity of the plot
"""
plt.figure()
plt.plot(years, apples, marker="o", c="b", ls="-", lw=2, ms=8, mew=2, mec= "navy") 
plt.plot(years, oranges, marker="x", c="r", ls="--", lw=3, ms=10, alpha=0.5) 
plt.ylabel("Yield (tons per hectare)")
plt.xlabel("Year") 
plt.title("Crop Yields in Kanto")
plt.legend(["Apples", "Oranges"]) 

"""The fmt argument provies a shorthand for specifying the line style, 
marker and line color. It can be provided as the third argument

fmt = '[marker][line][color]'
"""
plt.figure()
plt.plot(years, apples, "s-b") 
plt.plot(years, oranges, "o--r") 
plt.ylabel("Yield (tons per hectare)")
plt.xlabel("Year") 
plt.title("Crop Yields in Kanto")
plt.legend(["Apples", "Oranges"]) 

plt.show()