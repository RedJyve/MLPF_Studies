import click
import tensorflow as tf

@click.command()
@click.option('-n', '--name', default='model', help='name for saved files', type=str)
@click.argument('saved_model_dir')
def tflite_convert(name, saved_model_dir):
    #saved_model_dir = "quantization_testing/model_full"
    converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
    converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS, tf.lite.OpsSet.SELECT_TF_OPS]
    tflite_quant_model = converter.convert()
    with open('{}_full.tflite'.format(name), 'wb') as f:
        f.write(tflite_quant_model)
    converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
    converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS, tf.lite.OpsSet.SELECT_TF_OPS]
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    converter.target_spec.supported_types = [tf.float16]
    tflite_quant_model = converter.convert()
    with open('{}_float16.tflite'.format(name), 'wb') as f:
        f.write(tflite_quant_model)
    converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
    converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS, tf.lite.OpsSet.SELECT_TF_OPS]
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    tflite_quant_model = converter.convert()
    with open('{}_dynamic.tflite'.format(name), 'wb') as f:
        f.write(tflite_quant_model)

if __name__ == '__main__':
    tflite_convert()
