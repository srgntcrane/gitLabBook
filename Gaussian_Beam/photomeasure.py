import nidaqmx
import matplotlib.pyplot as plt

with nidaqmx.Task() as task:
    task.allchannels.add_ai_voltage_chan('cDAQ1Mod1/aio:1')
    data = task.read(number_of_samples_per_channel=1)
    print(data)
