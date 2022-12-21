from progress.bar import Bar
import time

bar = Bar('Loading...', max=20)
for i in range(20):
    time.sleep(0.1)
    bar.next()
bar.finish()