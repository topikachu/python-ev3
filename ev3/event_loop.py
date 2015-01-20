"""
A simple condition-based event loop.
"""
import time


class EventLoop(object):
    """The event loop.
    """
    def __init__(self):
        self._events = []
        self._closed = False

    def register_condition(self, condition, target, repeat=False, count=-1):
        """Register `target` to be called when ``condition()`` evaluates to
        true. 

        If `repeat` is false, `target` will only be called once for a serie
        of polls where `condition` evaluates to true, e.g. when a button is
        pressed. 

        If `count` is a positive number, the condition will be automatically
        unregistered after been called this many times.

        Returns an ID that can be used to unregister the condition. 
        """
        self._events.append(Event(condition, target, repeat, count))
        return len(self._events) - 1

    def register_value_change(self, getter, startvalue, target, count=-1):
        """Register `target` to be called when evaliating ``getter()`` 
        returns a new value. `startvalue` is the starting value to check 
        against.
    
        If `count` is a positive number, `target` will be called
        periodically this many times before it will be disabled.
    
        Returns an ID that can be used to unregister the timer.
        """
        self._events.append(ValueChangeEvent(
            getter, startvalue, target, count))
        return len(self._events) - 1

    def register_timer(self, seconds, target, count=1):
        """Register `target` to be called when the given number of seconds
        has passed. 

        If `count` is a positive number, `target` will be called
        periodically this many times before it will be disabled.

        Returns an ID that can be used to unregister the timer.
        """
        target_time = time.time() + seconds
        condition = lambda: time.time() >= target_time
        return self._add_condition(condition, target, False, count)

    def unregister(self, id):
        """Ungegister condition with the given id."""
        del self._events[id]

    def start(self):
        """Starts the event loop."""
        self._loop()

    def stop(self):
        """Stops event loop."""
        self._closed = True

    def _loop(self):
        """The event loop."""
        while not self._closed:
            for i in range(len(self._events) - 1, -1, -1):
                self._events[i].evaluate()
                if self._events[i]._count == 0:
                    self.unregister(i)
            time.sleep(0.1)





class Event(object):
    """The base Event class.
    """
    def __init__(self, condition, target, repeat=False, count=-1):
        self._condition = condition
        self._target = target
        self._repeat = repeat
        self._count = count
        self._previous_evaluation = False
        self._evaluation = False

    def poll(self):
        """Returns true if condition is satisfied, otherwise
        false. `evaluation` is the evaluated condition."""
        return self._evaluation and (
            self._repeat or not self._previous_evaluation)

    def evaluate(self):
        """Evaluate the condition. If it evaluates to true, `target` is
        called and the count number is decreased."""
        self._evaluation = self._condition()
        if self.poll():
            self._target(self)
            if self._count >= 0:
                self._count -= 1
        self._previous_evaluation = self._evaluation

    evaluation = property(
        lambda self: self._evaluation,
        doc='The value from the most resent evaluation of the condition.')

    previous_evaluation = property(
        lambda self: self._previous_evaluation,
        doc='The value from the previous evaluation of the condition.')

    repeat = property(
        lambda self: self._repeat,
        lambda self, value: setarrt(self, '_repeat', bool(value)),
        doc="Whether to call target every time `condition` is true, even "
        "if it haven't changed since last poll.")

    count = property(
        lambda self: self._count,
        lambda self, value: setarrt(self, '_count', int(value)),
        doc='Remaining number of times this event can be fired before it is '
        'automatically unregistered.')




class ValueChangeEvent(Event):
    def __init__(self, getter, startvalue, target, count=-1):
        Event.__init__(self, getter, target, count=count)
        self._previous_evaluation = startvalue

    def poll(self):
        return self._evaluation != self._previous_evaluation
            
