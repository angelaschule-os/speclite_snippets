import speclite.filters as filters
import matplotlib

matplotlib.use('TkAgg')

sdss = filters.load_filters('sdss2010-*')
filters.plot_filters(sdss, wavelength_limits=(3000, 11000))

matplotlib.pyplot.show()
