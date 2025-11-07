import numpy as np
import matplotlib.pyplot as plt

product_catagory = np.array(['furniture', 'technology', 'office supplies'])
sales = np.array([4110451.90, 4744557.50, 3787492.52])

plt.bar(product_catagory, sales, color = "green", edgecolor = "red", width = 0.5)


plt.title("Sales graph", fontdict={"fontsize" : 20, "fontweight" : 3, "color" : "Gray"})
plt.xlabel("Product Catagory", fontdict={"fontsize" : 15, "fontweight" : 2, "color" : "Gray"})
plt.ylabel("Sales", fontdict={"fontsize" : 15, "fontweight" : 2, "color" : "Gray"})

tick_values = np.arange(0, 7000000, 1000000)
tick_labels = ["0L", "10L", "20L", "30L", "40L", "50L", "60L"]
plt.yticks(tick_values, tick_labels)

plt.show()