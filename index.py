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
plt.figure()
plt.plot(years, yield_apples) 

"""Axis Labels 
We can add labels to the axes to show what each axis represents using the 
plt.xlabel and plt.ylabel methods. 
"""
plt.xlabel("Year") 
plt.ylabel("Apple Yield")
plt.show()