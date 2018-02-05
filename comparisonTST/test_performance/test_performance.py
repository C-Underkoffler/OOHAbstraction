
import sys
from pyteck.eval_model import evaluate_model
from os import listdir
from os.path import isfile, join


# List of models to be tested

model_list = list_of_models = [f for f in listdir("~/OOHabstraction/comparisonTST/reference_files/cantera_sub_models/wang") if f.endswith(".cti")]

species_key = '~/OOHabstraction/comparisonTST/reference_files/wang_species_keys.yaml'
data_path = 'data'
data_list = 'nbutanol-datalist.txt'
model_path = 'models'



if len(sys.argv)>1:
    "Command line arguments should be integers saying which models to run, in order"
    models_to_run = [model_list[int(i)] for i in sys.argv[1:]]
else:
    models_to_run = model_list

for model in models_to_run:

    output = evaluate_model(model, spec_keys_file='~/OOHabstraction/comparisonTST/reference_files/wang_species_keys.yaml',
                            dataset_file=data_list, data_path=data_path,
                            model_path=model_path,
                            skip_validation=True
                            )
