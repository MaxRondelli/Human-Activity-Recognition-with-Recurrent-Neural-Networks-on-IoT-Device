# This is the config file which holds the configuration values for different architectures

# Baseline LSTM Architecture:
LSTM1 = {
	'name' : 'LSTM1',
	'bidir' : False,
	'clip_val' : 10,
	'drop_prob' : 0.5,
	'n_epochs_hold' : 200,
	'n_layers' : 2,
	'learning_rate' : [0.0015],
	'weight_decay' : 0.001,
	'n_residual_layers' : 0,
	'n_highway_layers' : 0,
	'diag' : 'Architecure chosen is baseline LSTM with 1 layer',
	'save_file' : 'results_lstm1.txt'
}

# Baseline LSTM with 2 layers Architecture:
LSTM2 = {
	'name' : 'LSTM2',
	'bidir' : False,
	'clip_val' : 10,
	'drop_prob' : 0.5,
	'n_epochs_hold' : 200,
	'n_layers' : 2,
	'learning_rate' : [0.0015],
	'weight_decay' : 0.001,
	'n_residual_layers' : 0,
	'n_highway_layers' : 1,
	'diag' : 'Architecure chosen is baseline LSTM with 2 layers',
	'save_file' : 'results_lstm2.txt'
}

Architecture = {
	'LSTM1' : LSTM1,
	'LSTM2' : LSTM2
}


# Choose what architecure you want here:
arch = Architecture['LSTM2']

# This will set the values according to that architecture
bidir = arch['bidir']
clip_val = arch['clip_val']
drop_prob = arch['drop_prob']
n_epochs_hold = arch['n_epochs_hold']
n_layers = arch['n_layers']
learning_rate = arch['learning_rate']
weight_decay = arch['weight_decay']
n_highway_layers = arch['n_highway_layers']
n_residual_layers = arch['n_residual_layers']

# These are for diagnostics
diag = arch['diag']
save_file = arch['save_file']

# This will stay common for all architectures:
n_classes = 6
n_input = 9	
n_hidden = 32
batch_size = 64
n_epochs = 650
