#!/usr/bin/env python
# coding: utf-8

# # Welcome to Jupyter Notebooks
# 
# Notebooks are a handy way to combine code with text/explanations.  What's more, we can use notebooks to break up a program or analysis into several parts, running just one piece of code at a time.  For our purposes what this will do is allow us to look at a topic, execute some sample code to see how it works and then try writing something similar all in the same environment.
# 
# So for a quick background.  Notebooks are broken up into 'cells'.  Each cell can be interpretted by the browser in many different ways, but for our purposes each cell is either a documentation (Markdown) cell or a code (Python) cell.  Each cell is 'run' or 'executed' by either pressing a key combination or selecting one of the buttons at the top of the page.  For instance to run a cell, select the cell by clicking you mouse on in the box, then press CTRL+Enter.  
# <br>
# Try that with the cell below.

# In[ ]:


print('Welcome to Jupyter.  You have successfully run a code cell.')


# If you have done this correctly, you will see the results of running the cell immediately below the cell like such.
# ````{image} ../img/jupyter_welcome.png
# 
# ````

# The number on the left side of the cell just tells us the order in which the cell was run, so yours maybe different than the picture.
# 
# You can also run the cell by using the 'Cell' menu item at the top of screen.  This is useful if you want to run a series of cells, such as the entire notebook at once or all the cells up to a certain point.  For instance, say you are working your way through this notebook at get pulled away and decide to come back later.  You can scroll the browser down to the cell where you left off and simply select Cell-> Run All Above and this will ensure that all the prior cells are run before picking up where you left off.
# 
# ![image.png](../img/jupyter_run.png)

# ## In case something goes wrong
# Occassionally, this page will lose connection to the server or show an error message. You can simply refresh your webpage and most times the page will ask you if you want to restart the server.  Press yes.
# 
# In case things don't seem to be moving/running in your code, you can interrupt and restart your kernel.
# 
# Now, run the next cell.  This cell just makes sure that you see all the results of running the cells that follow in the notebook.

# In[ ]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

