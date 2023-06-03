import matplotlib.pyplot as plt
import pandas as pd

#Line Plot
# importing  the data
x= pd.read_csv("C:\\Users\\Welcome\\Desktop\\pyt_21\\Book1.csv")
y= pd.read_csv("C:\\Users\\Welcome\\Desktop\\pyt_21\\Book2.csv")

#creating figure 
fig = plt.figure(figsize = (8, 4),dpi=100)

ax = fig.add_axes([.4,.4,.4,.4])
ax1 = ax.plot(x,y)
ax2= ax.plot(y,x)
# Adding title to the plot
plt.title("Line Plot", fontsize=15, color="green")
# Adding label on the y-axis
plt.ylabel(' mark2',color='k',alpha=0.7)
# Adding label on the x-axis
plt.xlabel('mark1',color='k')
plt.legend(['mark1','mark2'])
plt.savefig("op_line.jpg")

#------------------------------------------------------------------
#Bar Plot


data = pd.read_csv("C:\\Users\\Welcome\\Desktop\\pyt_21\\exam1.csv")

x= data['race']
y= data['writing score']
fig = plt.figure(figsize = (8, 4))

ax = fig.add_axes([.4,.4,.4,.4])
plt.bar(x,y,color='b',alpha=.7)
plt.title("Bar Plot",color='red',alpha=.4)
 
# Adding label on the y-axis
plt.ylabel('score')
# Adding label on the x-axis
plt.xlabel('group')
plt.show()
plt.savefig("op_bar.jpg")

#--------------------------------------------------------------
# Histogram


data = pd.read_csv("C:\\Users\\Welcome\\Desktop\\pyt_21\\exam1.csv")
fig = plt.figure(figsize = (8, 4))

ax = fig.add_axes([.4,.4,.4,.4])
x = data['math score']
plt.hist(x,color='grey', edgecolor='red',alpha=0.7)
plt.title("Histogram",color='purple')
plt.xlabel('score')
plt.ylabel('count')
plt.show()
plt.savefig("op_hist.jpg")

#------------------------------------------------------------------
# Scatter Plot


data = pd.read_csv("C:\\Users\\Welcome\\Desktop\\pyt_21\\exam1.csv")
fig = plt.figure(figsize = (8, 4))

ax = fig.add_axes([.4,.4,.4,.4])
x = data['math score']
plt.scatter(x,y,color='g', edgecolor='b',alpha=0.7)
plt.title("Scatter Plot",color='k')
plt.xlabel('maths mark')
plt.ylabel('count')
plt.show()
plt.savefig("op_scat.jpg")

#---------------------------------------------------------------
# Pie  Chart

race = ['GROUP-A', 'GROUP-B', 'GROUP-C',
        'GROUP-D', 'GROUP-E']
data = [23, 10, 35, 15, 12]
explode = [0.001, 0.01, 0.1, 0.01, 0.01]
colors = ( "orange", "cyan", "yellow",
          "grey", "green",)
# plotting the data
plt.pie(data, labels=race,explode=explode,autopct='%1.2f%%',
        colors=colors, shadow=True) 
# Adding title to the plot
plt.title("Pie  Chart") 
plt.show()
plt.savefig("op_pie.jpg")

