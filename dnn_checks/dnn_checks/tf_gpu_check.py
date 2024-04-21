import tensorflow as tf
import time

def simple_dnn_compute():
    # Create a simple DNN model
    random_image_cpu = tf.random.normal((2, 5, 5, 3))
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(2, 3, activation='relu', input_shape=(5, 5, 3)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(2, activation='relu'),
    ])
    result = model(random_image_cpu)
    return result



cpu_devices = [cpu.name for cpu in tf.config.list_logical_devices('CPU')]
gpu_devices = [gpu.name for gpu in tf.config.list_logical_devices('GPU')]
all_devices = cpu_devices + gpu_devices
print(f"All devices found: {all_devices}")
for device in all_devices:
    print(f"Testing device: {device}")
    with tf.device(device):
        _ = simple_dnn_compute()
    print(f"Success dnn computation, device: {device}")
