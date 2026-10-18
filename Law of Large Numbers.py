import random
import matplotlib.pyplot as plt

Heads = 0
Tails = 0
ranges = [10, 100, 1000, 10000]
for i in range (1,10001):
    result = random.randint(0,1)
    if result == 1:
        Heads = Heads + 1
    else:
        Tails = Tails + 1

    if i in ranges:

        print("---------------------")
        print("Heads and Tails for", i,":", Heads,Tails, "\n")
        print("Percentage of Heads for", i, ":", Heads/i*100,"%", "\n")
        print("Percentage of Tails for", i, ":", Tails/i*100,"%", "\n")
        print("---------------------")

        categories = ['Heads', 'Tails']
        values = [Heads, Tails]
        
        fig = plt.figure(figsize=(6, 6)) 
        fig.canvas.manager.set_window_title("LLN Simulation - Case " + str(i))
        
        plt.bar(categories, values, color=['blue', 'orange']) 
        
        
        plt.title("Results for " + str(i) + " Tosses")
        plt.ylabel("Number of Outcomes")
        
        
        plt.show() 


     