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
flowers_df = sns.load_dataset("iris")  
#print(flowers_df.describe()) 

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
""" plt.figure(figsize=(12, 6))
plt.title("Distribution of Sepal Width") 
plt.hist(flowers_df.sepal_width, bins=np.arange(2, 5, 0.25))   """

# Bins of unequal size 
""" plt.figure(figsize=(12, 6))
plt.title("Distribution of Sepal Width") 
plt.hist(flowers_df.sepal_width, bins=[1, 3, 4, 4.5] ) """

"""Multiple Histograms
Similar to line charts, we can draw multiple histograms in a single 
chart. We can reduce the opacity of each histogram, so the bars of one histogram
don't hide the bars for others. 

Let's draw seperate histograms for each flower""" 
setosa_df = flowers_df[flowers_df.species == "setosa"] 
versicolor_df = flowers_df[flowers_df.species == "versicolor"]
virginica_df = flowers_df[flowers_df.species == "virginica"]  
sns.set_style("darkgrid")
""" plt.figure(figsize=(12, 6)) 
plt.title("Distribution of Sepal Width")
plt.hist(setosa_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25))
plt.hist(versicolor_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25)) 
plt.legend(["Setosa", "Versicolor"]) """
"""We can also stack multiple histograms on top of one another""" 
""" plt.figure(figsize=(12, 6)) 
plt.title("Distribution of Sepal Width")
plt.hist([setosa_df.sepal_width, versicolor_df.sepal_width, virginica_df.sepal_width] , alpha=0.4, bins=np.arange(2, 5, 0.25), stacked=True)
plt.legend(["Setosa", "Versicolor","Virginica"]) """ 


"""Bar Chart 
Bar charts are quite similar to line charts, i.e they show a sequence of values, 
however a bar is shown for each value rather, rather than points connected by lines.
We can use the plt.bar function to draw a bar chart. """ 
years = range(2000, 2006) 
apples = [0.35, 0.6, 0.9, 0.8, 0.65, 0.8]
oranges = [0.4, 0.8, 0.9, 0.7, 0.6, 0.8]  
""" plt.figure()
plt.bar(years, oranges)  
plt.plot(years, oranges, "o--r") """

"""Like histograms, bars can also be stacked on top of one another. We use 
the bottom argument to to plt.bar to achieve this.
"""
""" plt.figure()
plt.bar(years, apples) 
plt.bar(years, oranges, bottom=apples) 
plt.legend(["Apples", "Oranges"]) """ 

"""Bar Plots with Averages
Let's look at another sample dataset included with Seaborn, called "tips". 
The dataset contains information about the sex, time of day, and tip amount 
for customers visiting a restaurant over a week. 
""" 
tips_df = sns.load_dataset("tips") 

"""
We might want to draw a bar chart to visualize how the average bill amounts vary across
different days of the week. One way to do this would be to compute the day-wise 
averages and then use plt.bar. 
"""
bill_avg_df = tips_df.groupby("day", observed=True)[["total_bill"]].mean() 
""" print(bill_avg_df) 
plt.figure()
plt.bar(bill_avg_df.index, bill_avg_df.total_bill)
 """
"""
However, since this is a very common use case, the Seaborn library provides
a barplot function which can automatically compute averages
"""  
""" plt.figure(figsize=(12, 6))
sns.barplot(x="day", y="total_bill", data=tips_df)  """

"""The lines cutting each bar represents the amount of variation 
in the values. For instance, it seems like the variation in the total bill 
was quite high on Fridays, and lower on Saturday. 

We can also specify a hue argument to compare bar plots side-by-side based 
on a third feature, e.g. sex.
"""
""" plt.figure()
sns.barplot(x="day", y="total_bill", hue="sex", data=tips_df)   """

"""You can make the bars horizontal by simply switching the axes
"""
""" plt.figure()
sns.barplot(x="total_bill", y="day", hue="sex", data=tips_df) """ 


"""HEATMAP 
A heatmap is used to visualize 2-dimensional data like a matrix, or table 
using colors. The best way to understand it is by looking at an example. 
We'll use another sample dataset from Seaborn, called "flights" to 
visualize monthly passenger footfall at an airport over 12 years. 
"""
flights_df  = sns.load_dataset("flights").pivot(index="month", columns="year", values="passengers")
#print(flights_df) 

"""flights_df is a matrix with one row for each month and one column for 
each year. The values in the matrix show the number of passengers (in thousands) 
that visited the airport in a specific month of a spific month. We can use the 
sns.heatmap function to visualize the footfall at the airport.
"""
""" plt.figure(figsize=(12, 6)) 
plt.title("No. of Passengers (1000s)")  
sns.heatmap(flights_df)  """

"""The brighter colors indicate a higher footfall. By looking at the graph, 
we can infer two things: 
* The footfall at the airport in any given year tends to be highest around 
July & August. 
* The footfall at the airport in any given month tends to grow year by year. 

We can also display the actual values in each block by specifying 
annot= True, and use the cmpa argument to change the color palet
"""
""" plt.figure(figsize=(12, 6))
plt.title("No. of Passengers (1000s)")
sns.heatmap(flights_df, fmt="d", annot=True, cmap="Greens")  """

"""IMAGES 
Matplotlib can also be used to display images. Llet's download an image from 
the internet 
"""
from urllib.request import urlretrieve  
from PIL import Image 
#urlretrieve("https://i.imgur.com/SkPbg.jpg", "chart.jpg")

img = Image.open("charts.jpg")

"""An image loaded using PIL is simply a 3-dimensional numpy array 
containing pixel intensities for the red, green and blue (RGB) channels of the 
image. We can convert the image into an array using np.array""" 
img_array = np.array(img)  
""" plt.figure()
plt.imshow(img_array)
plt.axis(False) 
plt.grid(False)  """

"""
Plotting Multiple Charts in a Grid 
Matplotlib and Seaborn also support plotting multiple charts in a 
grid, using plt.subplots, which returns a set of axes that can be used for 
plotting.

Here's a single grid showing the different types of charts we've covered in 
this tutorial.
"""
fig, axes = plt.subplots(2, 3, figsize=(16, 8)) 
# Use the axes for for plotting 
axes[0, 0].plot(years, apples, "s-b")
axes[0, 0].plot(years, oranges, "o--r") 
axes[0, 0].set_xlabel("Year")
axes[0, 0].set_ylabel("Yield")
axes[0, 0].legend(["Apples", "Oranges"])
axes[0, 0].set_title("Crop  Yields in Kanto") 

# Pass the axes into seaborn 

axes[0, 1].set_title("Sepal Length vs. Sepal Width")
sns.scatterplot(x=flowers_df.sepal_length, 
                y=flowers_df.sepal_width, 
                hue=flowers_df.species, 
                s=100, 
                ax=axes[0, 1]) 

#  Use the axes for plotting 
axes[0, 2].set_title("Distribution for Sepal Width")
axes[0, 2].hist([setosa_df.sepal_width, versicolor_df.sepal_width, virginica_df.sepal_width], 
                bins=np.arange(2, 5, 0.25), 
                stacked=True) 
axes[0, 2].legend(["Setosa", "Versicolor", "Virginica"]) 

# Pass the axes into seaborn 
axes[0, 1].set_title("Restaurant Bills")
sns.barplot(x="day", 
                y="total_bill", 
                data=tips_df,
                hue="sex", 
                ax=axes[1, 0]
                )  
# Pass the axes into seaborn 
axes[1, 1].set_title("Flight traffic") 
sns.heatmap(flights_df, cmap="Blues", ax=axes[1, 1]) 

# Plot an image using the axes 
axes[1, 2].set_title("Data Science Meme") 
axes[1, 2].imshow(img)
axes[1, 2].grid(False)
axes[1, 2].set_xticks([])
axes[1, 2].set_yticks([]) 

plt.tight_layout(pad=2)
plt.show() 