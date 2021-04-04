import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import csv

breast = []
hip = []
image = []

IMAGE_FOLDER = "images/"

def getImage(path):
    return OffsetImage(plt.imread(IMAGE_FOLDER + path), zoom=0.15)

# Extract breast and hip info
with open("data.csv", mode="rt") as f:
    df = csv.DictReader(f)
    
    for row in df:
        breast.append(int(row["BREAST"]))
        hip.append(int(row["HIP"]))
        image.append(row["NAME"] + ".jpg")

# Plot
fig, ax = plt.subplots()
ax.scatter(hip, breast)

for x0, y0, path in zip(hip, breast, image):
    ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False)
    ax.add_artist(ab)

# Linear regression
lin = np.polyfit(hip, breast, 1)
lin_x = np.linspace(min(hip), max(hip), 10)
lin_y = lin[0]*lin_x + lin[1]
plt.plot(lin_x, lin_y, "-r", label="y={0}x + {1}".format(str(lin[0]), str(lin[1])))

# Change plot appearance
plt.title("Relationship between H and B size in Love Live!", fontdict={"size": 20})
plt.xlabel("Hip", fontdict={"size": 14})
plt.ylabel("Breast", fontdict={"size": 14})
plt.grid()
plt.legend(loc="upper left")
plt.xticks(np.arange(min(hip), max(hip)+1, 1.0))
plt.yticks(np.arange(min(breast), max(breast)+1, 1.0))


# Show plot
plt.show()