import pynvml

pynvml.nvmlInit()
deviceCount = pynvml.nvmlDeviceGetCount()
for i in range(deviceCount):
    print i
    handle = pynvml.nvmlDeviceGetHandleByIndex(i)
    procs = pynvml.nvmlDeviceGetComputeRunningProcesses(handle)
    for p in procs:
        pid = str(p.pid)
        with open("/host/proc/" + pid + "cmdline") as name:
            if 'mapd_server' in name:
                print name

pynvml.nvmlShutdown()