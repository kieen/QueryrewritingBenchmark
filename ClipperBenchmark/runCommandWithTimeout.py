import subprocess, os, signal, time
from builtins import float
# run commandString with timeout. After the timeout, kill all processes, including sub-processes
# return:  running time if success, "timeout" if timeout, and "error" if fail
def runCommandWithTimeout(commandString, timeout_in_second):
    try:
        timeoutInSecond = float(timeout_in_second)
        start_time = time.time()
        #p = subprocess.Popen(commandString,stderr=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
        p = subprocess.Popen(commandString, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
        # http://stackoverflow.com/questions/4789837/how-to-terminate-a-python-subprocess-launched-with-shell-true
        p.wait(timeoutInSecond)
        running_time = (time.time() - start_time) 
        #err = p.communicate()
        print("Command has finished, running p.communicate() ...")
        out, err = p.communicate()
        #print(out.decode('utf-8'))
        
        #print("running time: %.2f ms" % running_time)
        if p.returncode==0:
            #print("return code: %d " % p.returncode)
            print(out.decode('utf-8'))
            print(err.decode('utf-8'))
            return running_time
        else:
            return "error"
    except subprocess.TimeoutExpired as e:
        #print("Timeout after %s s" % timeoutInSecond)
        print(e)
        os.killpg(p.pid, signal.SIGTERM)
        return "timeout"
