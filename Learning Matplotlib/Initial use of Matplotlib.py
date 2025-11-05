import numpy as np
import matplotlib.pyplot as plt

product_catagory = np.array(['furniture', 'technology', 'office supplies'])
sales = np.array([4110451.90, 4744557.50, 3787492.52])

plt.bar(product_catagory, sales)
plt.title("Sales graph", fontdict={"fontsize" : 20, "fontweight" : 3, "color" : "Gray"})
plt.xlabel("Product Catagory", fontdict={"fontsize" : 15, "fontweight" : 2, "color" : "Gray"})
plt.ylabel("Sales", fontdict={"fontsize" : 15, "fontweight" : 2, "color" : "Gray"})

plt.show()