# References: 
# https://www.youtube.com/watch?v=DsYm4Tlr1rw
# https://medium.com/machine-learning-researcher/self-organizing-map-som-c296561e2117
# Question 2 : Happiness    
import numpy as np
import math 
import random
import matplotlib.pyplot as plt
import turtle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import geopandas

class SelfOrganizingMaps: 
    def __init__(self, input_vectors, no_cl):

        self.data_world_color = [] 

        turtle.register_shape("square", ((-10,-10), (-10,10), (10,10), (10,-10), (-10,-10)))
        self.t = turtle.Turtle(shape="square")
        self.t.penup() 
        self.t.speed(5)
        self.t.hideturtle()
        self.input_vectors = input_vectors
        self.no_clusters = no_cl
        self.clust_pos = [] # Stores the position of each cluster 
        self.no_of_attributes = len(input_vectors[0]) # Assuming that atleast one data point is provided 

        # Stores weight of each cluster 
        self.weights = [[np.random.rand() for j in range(self.no_of_attributes)] for i in range(self.no_clusters)]
        
        u = 0 
        for y in range(int(math.sqrt(self.no_clusters))):
            for x in range(int(math.sqrt(self.no_clusters))):
                
                screen_x, screen_y = -288 + (x*24), 88 - (y*24)
                self.clust_pos.append((screen_x, screen_y))
                color = self.color_code(u)
                self.t.color(color[0], color[1], color[2]) #Change 
                self.t.goto(screen_x, screen_y)     
                self.t.stamp()
                u+=1 

        self.learning_rate_0, self.lattice_width_0, self.time_constant = 0.5, 20, 3 
        
    def dist_each_cls(self, vec): 
        d = [] 
        for i in range(self.no_clusters): 
            distance = 0 
            for j in range(self.no_of_attributes):
                distance += (self.weights[i][j] - vec[j])**2
            d.append(math.sqrt(distance)) 
        return d

    def lattice_width(self, t): 
        return self.lattice_width_0 * math.exp(- t / self.time_constant)

    def influence_rate_of_all(self, d, lattice_width_t): 
        return [math.exp((-i**2) / (2 * (lattice_width_t ** 2))) for i in d] 
       
    def learning_rate(self, t):
        return self.learning_rate_0 * math.exp(-t/self.time_constant) 
        
    def color_code(self, clust_num):
        col = [[], [], []]
        for k in range(self.no_of_attributes): 
            col[k%3].append(self.weights[clust_num][k]) 
            
        return [sum(i) / len(i) for i in col] 

    def update_weights(self, learning_rate_t, vec, o_t):
        for i in range(self.no_clusters):
            ot = o_t[i]
            for j in range(self.no_of_attributes): 
                w_t, v_t = self.weights[i][j], vec[j]
                self.weights[i][j] = w_t + (ot * learning_rate_t * (v_t - w_t))
            color = self.color_code(i)
            self.t.color(color[0], color[1], color[2]) # Change when needed 
            self.t.goto(self.clust_pos[i])    
            self.t.stamp()
           

    def d_w(self, win): 
        return [math.sqrt((self.clust_pos[i][0] - self.clust_pos[win][0]) ** 2 + (self.clust_pos[i][1] - self.clust_pos[win][1]) ** 2) for i in range(self.no_clusters)] 

    def return_weight(self): 
        return self.weights
    
    def main(self, t): 
        lattice_width, learning_rate_t = self.lattice_width(t), self.learning_rate(t)
        
        for i in range(len(self.input_vectors)):
            print(i)
            vec = random.choice(self.input_vectors)
            d = self.dist_each_cls(vec)
            winning_cluster = d.index(min(d))  
            o_t = self.influence_rate_of_all(self.d_w(winning_cluster), lattice_width) # BMW, lattic_width 
            self.update_weights(learning_rate_t, vec, o_t)

    def put_names(self, id): 
      
        for i in range(len(self.input_vectors)):
            
            vec = self.input_vectors[i]
            d = self.dist_each_cls(vec)
            winning_cluster = d.index(min(d))
            pos_of_bmu = self.clust_pos[winning_cluster]
            self.t.goto(pos_of_bmu)
            self.t.pencolor("black")
            self.data_world_color.append(self.color_code(winning_cluster))
            
            self.t.write(str(id[i]), align="center", font=("Arial", 5, "normal"))
        return self.data_world_color
    
def clean_data(path): 
    # id_col = input("Enter the name of ID column: ")
    df = pd.read_csv(path)

    id = list(df["Country or region"]) 
    df = df.drop("Country or region", axis=1)
    df = df.drop("Overall rank", axis = 1)
    scaler = MinMaxScaler()
    return list(scaler.fit_transform(df)) , id 


no_of_cls = 100
epochs = 2
path = '2019.csv'
a, id = clean_data(path)
# print(b)
som = SelfOrganizingMaps(a, no_of_cls)
for t in range(epochs):
    som.main(t) 

colors = som.put_names(id)


world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
ax = world.plot()
for i in range(len(id)): 
    try: 
        world[world.name == id[i]].plot(color=tuple(colors[i]),ax=ax)
    except: 
        print(id[i], " not found on World Map...")
plt.show()

# som.return_weight()
turtle.update()
turtle.mainloop()