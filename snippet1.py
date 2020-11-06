import speclite.filters as filters
import matplotlib.pyplot as plt

sdss = filters.load_filters('sdss2010-*')
filters.plot_filters(sdss, wavelength_limits=(3000, 11000))
plt.savefig("mygraph.png")