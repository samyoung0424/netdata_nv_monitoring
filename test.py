import pynvml

pynvml.nvmlInit()
deviceCount = pynvml.nvmlDeviceGetCount()
for i in range(deviceCount):
    print i
    handle = pynvml.nvmlDeviceGetHandleByIndex(i)
    procs = pynvml.nvmlDeviceGetComputeRunningProcesses(handle)

    for p in procs:
        print p.pid, type(p.pid)
        #name = pynvml.nvmlSystemGetProcessName(p.pid)
        #print name

pynvml.nvmlShutdown()