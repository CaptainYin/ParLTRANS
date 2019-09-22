import multiprocessing
import time

def func(msg):
    print(multiprocessing.current_process().name+'-'+msg)
def deadloop():
    while true:
        pass
def job(qk):
    q=qk[0]
    k=qk[1]
    res=0
    for i in range(1000000):
        res+=i+i**2+i**3+i**4
    #q.put(res)
pool=multiprocessing.Pool(processes=32)
q=multiprocessing.Queue()
#for i in xrange(100000):
#    pool.apply_async(job,(q,))
pool.map(job,[(1,i) for i in range(40)])
pool.close()
pool.join()
#print(q.get())
print("all done")
