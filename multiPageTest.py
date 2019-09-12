import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
axindex = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
sindex = Slider(axindex, 'Index', 1, 10, valinit=2, valstep=1)
def update(val):
    index = int(sindex.val)
    ax.clear()
    ax.set_xlabel('index={}'.format(index))
    x = np.arange(0, 2*np.pi, 0.01)
    y = np.sin(x * (2 ** index))
    ax.plot(x, y)
    fig.canvas.draw_idle()
sindex.on_changed(update)

update(None)
plt.show()