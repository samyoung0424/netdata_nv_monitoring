import pynvml

deviceCount = pynvml.nvmlDeviceGetCount()
for i in range(deviceCount):
    handle = pynvml.nvmlDeviceGetHandleByIndex(i)
    procs = pynvml.nvmlDeviceGetComputeRunningProcesses(handle)
    print procs