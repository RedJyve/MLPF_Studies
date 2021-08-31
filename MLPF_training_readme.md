#Guide to Training and MLPF Model on Purdue Gilbreth

Build a singularity using the singularity_definition.sub definition file and the site https://cloud.sylabs.io/builder.  
You may have to create an account if you don't already have one.  
You can then upload the definition file using a button of the same name.  

If you have not already you should clone the MLPF repository.  
Once you have the singularity upload it to gilbreth along with the data you will be using.  
I suggest following the MLPF readme for figuring out how to correctly upload the data to the particleflow folder.  
One tip, if you are training the delhpes dataset, is to using the package zenodo-get to download the data for you.  
Once you gotten the data in the correct location make sure to run the data step of the launcher.py.  
Ex: For training on delphes singularity exec python3 mlpf/launcher.py --model-spec parameters/delphes-gnn-skipconn.yaml --action data. 
If your code is saying the it can't find the data, check the .yaml file for the path that it is looking for your data at (raw_path, validation_path) and make sure that your data is where it is pointing.  

Now you can start the training:
Make sure that you have the cuda and cudnn modules loaded on your gilberth instance.  
If you get error saying the it couldn't find certain libraries when training it likely means that you don't have the correct version of the cuda and cunn modules.  
Using the sinularity you created run the pipeline.py file with the correct argument for the training you would like to perform.  
Ex: For training on delphes singularity exec python3 mlpf/pipeline.py train -c parameters/delphes-gnn-skipconn.yaml -p delphes-  
If you are using GPU's for training add CUDA_VISIBLE_DEVICES=0,1 before the singularity exec portion of the command (use =0 for 1 gpu =0, 1 for 2 gpus, etc).  

If you are running the training in a slurm job (which is highly encouraged) follow the above steps in the slurm job script.  
A sample slurm job script is provided in this repository. 
