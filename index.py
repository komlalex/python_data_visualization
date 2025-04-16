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
""" plt.figure()
plt.plot(years, apples, marker="o", c="b", ls="-", lw=2, ms=8, mew=2, mec= "navy") 
plt.plot(years, oranges, marker="x", c="r", ls="--", lw=3, ms=10, alpha=0.5) 
plt.ylabel("Yield (tons per hectare)")
plt.xlabel("Year") 
plt.title("Crop Yields in Kanto")
plt.legend(["Apples", "Oranges"])  """

"""The fmt argument provies a shorthand for specifying the line style, 
marker and line color. It can be provided as the third argument

fmt = '[marker][line][color]'
"""
""" plt.figure()
plt.plot(years, apples, "s-b") 
plt.plot(years, oranges, "o--r") 
plt.ylabel("Yield (tons per hectare)")
plt.xlabel("Year") 
plt.title("Crop Yields in Kanto")
plt.legend(["Apples", "Oranges"])  """


"""If no line style is specified in the fmt, only markers are drawn""" 
""" plt.figure()
plt.plot(years, apples, "or") 
plt.ylabel("Yield (tons per hectare)")
plt.xlabel("Year") 
plt.title("Crop Yields in Kanto")
plt.legend(["Apples"])  """

"""Improving Default Styles using Seaborn 
An easy way to make your charts look beautiful is to use default 
styles provided in the Seaborn library. These can be applied using the 
sns.set_style function."""

""" sns.set_style("whitegrid") 
plt.figure(figsize=(12, 12))
plt.plot(years, apples, "s-b") 
plt.plot(years, oranges, "o--r") 
plt.ylabel("Yield (tons per hectare)")
plt.xlabel("Year") 
plt.title("Crop Yields in Kanto")
plt.legend(["Apples", "Oranges"]) 

sns.set_style("darkgrid") 
plt.figure(figsize=(12, 12))
plt.plot(years, apples, "s-b") 
plt.plot(years, oranges, "o--r") 
plt.ylabel("Yield (tons per hectare)")
plt.xlabel("Year") 
plt.title("Crop Yields in Kanto")
plt.legend(["Apples", "Oranges"])  """

"""You can also edit default styles directly by modifying the 
matplotlib.rcParams dictionary.""" 
""" import matplotlib 
matplotlib.rcParams["font.size"] = 14  
matplotlib.rcParams["figure.figsize"] = (9, 5)
matplotlib.rcParams["figure.facecolor"] = "#33000099" 
plt.figure()
plt.plot(years, apples, "s-b") 
plt.plot(years, oranges, "o--r") 
plt.ylabel("Yield (tons per hectare)")
plt.xlabel("Year") 
plt.title("Crop Yields in Kanto")
plt.legend(["Apples", "Oranges"]) 
 """  

"""SCATTER PLOT  
In scatter plot, the values of 2 variables are plotted as 
a point on a 2-dimensional grid. Additionally, you can also use a third 
varibable to determine the size or color of the points. Let's try out an 
example.

The iris flower dataset provides samples measurements of sepals and 
petals for 3 species of flowers. The Iris dataset is included with the 
Seaborn library, and can be loaded as a Pandas data frame
""" 
flowers_df = sns.load_dataset("iris") 
print(flowers_df.species.unique()) 

"""Let's visualoze the relationship between the sepal length and sepal 
width. Our first instinct might be to create a line chart using plt.plot. 
However, the output is not very informative as there are too many 
combinations of the two properties within the dataset, and there doesn't seem 
to be a simple relationship between them.
""" 
#plt.plot(flowers_df.sepal_length, flowers_df.sepal_width) 

"""We can use a scatter plot to visualize how sepal length and 
sepal width vary using the scatterplot function from seaborn (imported as sns)
"""
#sns.scatterplot(x=flowers_df.sepal_length, y=flowers_df.sepal_width) 

"""Adding Hues 
Notice how the points in the above plot seem to form distinct clusters 
with some outliers. We can color the dots using the flower species as a hue. 
We can also make the points larger using the s argument.""" 
#sns.scatterplot(x=flowers_df.sepal_length, y=flowers_df.sepal_width, hue=flowers_df.species, s=100) 

"""Ading hues make the plot more informative. We can immediately tell that 
the flowers of the Setosa species have a smaller sepal length but higher sepal
widths, while the opposite holds for the Virginica species
""" 

"""Customizing Seaborn Figures""" 
""" plt.figure(figsize=(12, 6))
plt.title("Sepal Dimensions")
sns.scatterplot(x=flowers_df.sepal_length, y=flowers_df.sepal_width, hue=flowers_df.species, s=100) 
 """
"""Plotting using Pandas Data Frames 
Seaborn has in-built support for Pandas data frames. Instead of passing each 
columns as a series, you can also pass column names and use the data
argument to pass the data frame.""" 
""" plt.title("Sepal Dimensions") 
sns.scatterplot(x="sepal_length", 
                y="sepal_width", 
                hue="species", 
                s=100, 
                data=flowers_df)  """ 

"""HISTOGRAM 
A histogram represents the distribution of data by forming the 
bins along the range of the data and then drawing bars to show the 
number of observations that fall in each bin.

As an example, let's visualize how the values of sepal width in the flowers 
dataset are distributed. We can use the plt.hist function to create a histogram.
"""
#flowers_df = sns.load_dataset("iris")  
print(flowers_df.describe()) 

""" plt.figure(figsize=(12, 6))
plt.title("Distribution of Sepal Width") 
plt.hist(flowers_df.sepal_width)  """

"""We can immediately see that the values of sepal width fall in 
the range 2.0-4.5, and around 35 values are in the range 2.9-3.1, which 
seems to be the largest bin."""  


"""
Controlling the size of bins 
We can control the number of bins, or the size of each bin using the bins 
argument.
""" 
""" plt.figure(figsize=(12, 6))
plt.title("Distribution of Sepal Width") 
plt.hist(flowers_df.sepal_width, bins=5)  
 """
import numpy as np 
# Specifying the boundaries of each bin 
plt.figure(figsize=(12, 6))
plt.title("Distribution of Sepal Width") 
plt.hist(flowers_df.sepal_width, bins=np.arange(2, 5, 0.25))  

# Bins of unequal size 
plt.figure(figsize=(12, 6))
plt.title("Distribution of Sepal Width") 
plt.hist(flowers_df.sepal_width, bins=[1, 3, 4, 4.5] )

plt.show()