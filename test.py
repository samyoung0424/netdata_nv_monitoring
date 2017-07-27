import pynvml

pynvml.nvmlInit()
deviceCount = pynvml.nvmlDeviceGetCount()
for i in range(deviceCount):
    handle = pynvml.nvmlDeviceGetHandleByIndex(i)
    procs = pynvml.nvmlDeviceGetComputeRunningProcesses(handle)
    for p in procs:
        print p
        #name = pynvml.nvmlSystemGetProcessName(p.pid)
        #print name

pynvml.nvmlShutdown()