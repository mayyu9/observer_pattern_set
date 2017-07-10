"""
knows its observers.
notifies the observers when there is state change.
"""

class Subject:
    def __init__(self):
        self._observers = set();
        self._subject_state = None;

    def attach(self, observer):
        observer._subject = self;
        self._observers.add(observer);

    def detach(self,observer):
        observer._subject = None;
        self._observers.remove(observer);

    def _notify(self):
        print("notify");
        for observer in self._observers:
            observer.update(self._subject_state);

    @property
    def subject_state(self):
        return self._subject_state;

    @subject_state.setter
    def subject_state(self,arg):
        print("state setter",arg);
        #set the data to the state
        self._subject_state = arg;
        #notify the observers with updated state value.
        self._notify();
