import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os
import yaml
import brewer2mpl
import imageio

plt.ion()

model_list = list_of_models = [f for f in os.listdir("/Users/nathan/Code/OOHabstraction/comparisonTST/test_performance/models") if f.endswith(".cti")]

models = []
error_functions = []
standard_deviations = []
deviation_functions = []

for model in model_list:
    results_file = os.path.splitext(model)[0] + '-results.yaml'

    if os.path.exists(results_file):
        with open(results_file, 'r') as f:
            results = yaml.load(f)

        models.append(results['model'])
        error_functions.append(results['average error function'])
        standard_deviations.append(results['average deviation function'])
        deviation_functions.append(results['error function standard deviation'])

fig, ax = plt.subplots()

box_colors = brewer2mpl.get_map('Set3', 'qualitative', 10).mpl_colors
box_colors += brewer2mpl.get_map('Set3', 'qualitative', len(models)-10).mpl_colors

#for idx, model in enumerate(models):
ax.bar(list(range(len(models))), error_functions,
       yerr=[[0]*len(models), standard_deviations],
       color=box_colors, linewidth=0
       )

ax.grid(axis = 'y', color ='white', linestyle='-')
plt.xticks(list(range(len(models))), models, rotation='vertical')
# Pad margins so that markers don't get clipped by the axes
#plt.margins(0.2)
# Tweak spacing to prevent clipping of tick-labels
plt.subplots_adjust(bottom=0.4)

pp = PdfPages('overall-errors.pdf')
pp.savefig()
pp.close()

fig, ax = plt.subplots()

for model in model_list:
    results_file = os.path.splitext(model)[0] + '-results.yaml'

    if os.path.exists(results_file):
        with open(results_file, 'r') as f:
            results = yaml.load(f)

    temps = []
    sim_delay = []
    exp_delay = []
    for dataset in results['datasets']:
        for point in dataset['datapoints']:
            temps.append(point['temperature'])
            sim_delay.append(point['simulated ignition delay'])
            exp_delay.append(point['experimental ignition delay'])

    plt.clf()

    plt.plot(1000. / np.array(temps), sim_delay, 'o', label='Simulated')
    plt.plot(1000. / np.array(temps), exp_delay, 'x', label='Experimental')

    plt.ylabel('Ignition delay (s)')
    plt.xlabel('1000/T (1/K)')
    plt.semilogy()
    plt.legend()
    plt.show()
    plt.axis([0.55, 1.45, 4e-5, 2.6e-2])
    plt.savefig(model + '-ignition.png')
    #pp = PdfPages(model + '-ignition.pdf')
    #pp.savefig()
    #pp.close()

filenames = [m + '-ignition.png' for m in models]
images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('movie.gif', images)
