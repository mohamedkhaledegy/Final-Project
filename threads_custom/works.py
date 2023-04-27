
from PySide2.QtCore import Signal,QRunnable,QObject,Slot
import threading

class WorkerSignals(QObject):
    finished = Signal() # create a signal
    result = Signal(object) # create a signal that gets an object as argument

class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn # Get the function passed in
        self.args = args # Get the arguments passed in
        self.kwargs = kwargs # Get the keyward arguments passed in
        self.signals = WorkerSignals() # Create a signal class
    @Slot()
    def run(self): # our thread's worker function
        result = self.fn(*self.args, **self.kwargs) # execute the passed in function with its arguments
        self.signals.result.emit(result)  # return result
        self.signals.finished.emit()  # emit when thread ended
    def stop(self):
        self.threadactive = False
        self.wait()