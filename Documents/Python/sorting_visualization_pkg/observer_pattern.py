from abc import ABC, abstractmethod

class Observer:

    _subject = None
    _observer_state = None

    def _init__(self):
        self._subject = None
        self._observer_state = None

    @abstractmethod
    def update(self, list):
        pass


class Subject:

    _observers = None
    _subject_state = None

    def __init__(self):
        self._observers = set()
        self._subject_state = None

    def attach(self, observer):
        observer._subject = self
        self._observers.add(observer)

    def detach(self, observer):
        observer._subject = None
        self._observers.discard(observer)

    @abstractmethod
    def _notify(self):
        pass
        """for observer in self._observers:
            observer.update(self._subject_state)"""
