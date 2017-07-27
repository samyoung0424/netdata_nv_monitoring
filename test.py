import pynvml

pynvml.nvmlInit()
deviceCount = pynvml.nvmlDeviceGetCount()
for i in range(deviceCount):
    print i
    handle = pynvml.nvmlDeviceGetHandleByIndex(i)
    procs = pynvml.nvmlDeviceGetComputeRunningProcesses(handle)
    for p in procs:
        pid = str(p.pid)
        with open("/host/proc/" + pid + "/cmdline") as pid_file:
            for line in pid_file:
                if line.find("mapd_server") != -1:
                    print "found"

pynvml.nvmlShutdown()