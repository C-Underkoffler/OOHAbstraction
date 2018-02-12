
import sys
from pyteck.eval_model import evaluate_model
import os
from os import listdir
from os.path import isfile, join


# List of models to be tested

model_list = list_of_models = [f for f in listdir("/home/ubuntu/Code/OOHabstraction/comparisonTST/reference_files/cantera_sub_models/wang/") if f.endswith(".cti")]

#evaluated_models
sub_list = [int(f.split('.')[1]) for f in os.listdir("/home/ubuntu/Code/OOHabstraction/comparisonTST/reference_files/cantera_sub_models/wang/") 
              if f.endswith(".cti")]

results_list = [int(f.split('.')[1]) for f in os.listdir("/home/ubuntu/Code/OOHabstraction/comparisonTST/test_performance/methylheptane_pyteck_results/") 
                if f.endswith(".yaml")]

evaluated_subs = list(set(sub_list) & set(results_list))

evaluated_models = []
for subs in evaluated_subs:
    evaluated_models.append('master.' + str(subs) +'.' + '1' +'.cti')
    
need_to_evaluate = []
for model in model_list:
    if model not in evaluated_models:
        need_to_evaluate.append(model)


species_key = '/home/ubuntu/Code/OOHabstraction/comparisonTST/reference_files/wang_species_keys.yaml'
data_path = 'data'
data_list = 'nbutanol-datalist.txt'
model_path = 'models'



if len(sys.argv)>1:
    "Command line arguments should be integers saying which models to run, in order"
    models_to_run = [need_to_evaluate[int(i)] for i in sys.argv[1:]]
else:
    models_to_run = need_to_evaluate

for model in models_to_run:

    output = evaluate_model(model, spec_keys_file='/home/ubuntu/Code/OOHabstraction/comparisonTST/reference_files/wang_species_keys.yaml',
                            dataset_file=data_list, data_path=data_path,
                            model_path=model_path,
			    results_path = '/pyteck/cache',
                            skip_validation=True
                            )
