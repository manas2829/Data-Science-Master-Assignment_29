#!/usr/bin/env python
# coding: utf-8

# # Assignment_05.03.2023 (BOKEH Visualization)

# ## Q1.How can you Create a Bokeh plot using python code?
# 
# ### Ans:-
# 

# In[1]:


import bokeh.io


# In[2]:


import bokeh.plotting


# In[3]:


bokeh.io.output_notebook()


# In[4]:


from bokeh.plotting import figure,output_file,show


# In[5]:


x_values = [1,2,3,4,5]
y_values = [6,7,2,4,5]

# Create a bokeh figure
fig = figure(title="Sample Plot",x_axis_label='X-Axis',y_axis_label='Y-Axis')

fig.circle(x_values,y_values,size=10,color='red')
show(fig)


# In[6]:


figure(title="Sample Plot",x_axis_label='X-Axis',y_axis_label='Y-Axis')

fig.line(x_values,y_values)
show(fig)


# ## Q2. What is glyphs in Bokeh and how can you add them to Bokeh Plot? Explain with Example.
# 
# ### Ans:-
#         Glyphs are the visual building blocks of Bokeh plots. They represent the shapes or markers that are plotted on the 
#         plot canvas to visually represent the data. Bokeh provides a wide range of glyphs such as lines, circles,rectangles,
#         patches, and more, that can be used to create different types of visualizations.
#         
#         

# In[7]:


from bokeh.plotting import figure,output_file,show
X=[1,2,3,4,5,6,7,8,9]
Y=[3,4,2,5,7,1,9,11,6]

# Create a Bokeh figure
fig= figure(title="Sample Plot",x_axis_label='Manas',y_axis_label='Priyanka')

#add a cicle glyphs to the figure
fig.circle(X,Y,size=10,color='navy',alpha=0.5)
#add a line Glyphs to the figure
fig.line(X,Y,line_width=2,color='red')
#output the plot to a file
output_file('Sample Plot.html')
#Show the plot in a new browser tab
show(fig)


# ## Q3. How can i custmized the appearance of a Bokhe plot, including the axes,title and legend?
# 
# ### Ans:-

# In[8]:


X=[1,2,3,4,5,6,7,8,9]
Y=[3,4,2,5,7,1,9,11,6]

# Create a Bokeh figure
fig= figure(title="Sample Plot",x_axis_label='Manas',y_axis_label='Pandey')

#add a cicle glyphs to the figure
fig.circle(X,Y,size=10,color='brown',legend_label='circel Glyph')
#add a line Glyphs to the figure
fig.line(X,Y,line_width=2,color='blue',legend_label='Line Glyph')

# Customize the appearance of the figure
fig.title.text_font_size = '20pt'
fig.title.text_color = 'green'
fig.xaxis.axis_label_text_font_style = 'bold'
fig.yaxis.axis_label_text_font_style = 'bold'
fig.legend.location = "top_left"
#output the plot to a file
output_file('Sample Plot.html')
#Show the plot in a new browser tab
show(fig)


# In[9]:


X=[1,2,3,4,5,6,7,8,9]
Y=[3,4,2,5,7,1,9,11,6]

# Create a Bokeh figure
fig= figure(title="Sample Plot",x_axis_label='Manas',y_axis_label='Pandey')

#add a cicle glyphs to the figure
fig.circle(X,Y,size=10,color='brown',legend_label='circel Glyph')
#add a line Glyphs to the figure
fig.line(X,Y,line_width=2,color='blue',legend_label='Line Glyph')

# Customize the appearance of the figure
fig.title.text_font_size = '20pt'
fig.title.text_color = 'green'
fig.xaxis.axis_label_text_font_style = 'bold'
fig.yaxis.axis_label_text_font_style = 'bold'
fig.legend.location = "bottom_right"
#Show the plot 
show(fig)


# ## Q4. What is a Bokeh server and how can you use it to create interactive plots that can be updated in real-time?
# 
# ### Ans:-
# 
#         Bokeh is a Python library for creating interactive visualizations for the web. Bokeh server is a Bokeh feature that enables real-time, two-way communication between a Bokeh plot in a web browser and a running Python process on a server.
#         
#         With Bokeh server, you can create interactive plots that can be updated in real-time based on user interactions or changes in data. To use Bokeh server, you need to create a Python script that defines the Bokeh plot you want to display in the browser, and then launch the Bokeh server to serve the plot to the web.
#         
#          The basic steps to create an interactive plot using Bokeh server:-
#          
#          1.Define your data and create a Bokeh plot using the Bokeh Python library.
# 
#          2.Create a Python function that will update the data used in the plot. This function can be triggered by user 
#         interactions, external data sources, or timers.
# 
#          3.Create a Bokeh server application that will serve the plot to a web page and handle incoming events and updates 
#          from the browser.
# 
#          4.Launch the Bokeh server application with the "bokeh serve" command.
# 
#          5.View the interactive plot in a web browser by navigating to the URL provided by the Bokeh server.
#          
#          
#          As an example, let's say you have a scatter plot of some data points, and you want to allow users to select a 
#          subset of the data points by clicking on the plot. Here's how you could use Bokeh server to implement this:-
#          
#         1. Create a scatter plot using Bokeh that displays your data.
# 
#         2.Define a Python function that updates the data used in the plot based on user interactions.
# 
#         3.Create a Bokeh server application that sets up the scatter plot and connects it to the update function.
# 
#         4.Launch the Bokeh server application with the "bokeh serve" command.
# 
#         5.Users can now interact with the plot in their web browser, and any changes they make will be sent to the server
#         and reflected in the plot.
# 
# 

# ## Q5. How can you embed a Bokhe plot into a webpage or deshboard using flak or Django?
# 
# ### Ans:-

# In[10]:


from flask import Flask,render_template
from bokeh.plotting import figure,output_file,show
from bokeh.embed import components
 
app = Flask(__name__)

@app.route('/')
def index():
    plot = figure()
    plot.circle([1,2,3,4,5,6,7,8,9],[10,9,6,5,3,8,2,1,7])
    
    script,div = components(plot)
    
    return render_template('index.html',script=script, div=div)

