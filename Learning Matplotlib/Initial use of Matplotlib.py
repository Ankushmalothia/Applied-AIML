import numpy as np
import matplotlib.pyplot as plt

product_catagory = np.array(['furniture', 'technology', 'office supplies'])
sales = np.array([4110451.90, 4744557.50, 3787492.52])

graph = plt.bar(product_catagory, sales)

plt.show()