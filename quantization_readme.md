#Guide to Quantizaing MLPF models

#YOU MUST BE USING TF_NIGHTLY FOR THIS STEP
Once you have your folder containing a saved_model.pb file you can use quatization_convert.py to convert the saved_model to tflite with a few levels of quantization.
(Ex: python3 quantization_convert.py --name model /path/to/saved_model/folder

You can then run tests on these tflite model.

For testing purposes a saved_model directory is in the github that works with the convertion process.
