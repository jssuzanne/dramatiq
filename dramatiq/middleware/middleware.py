class Middleware:
    """Base class for broker middleware.  The default implementations
    for all hooks are no-ops and subclasses may implement whatever
    subset of hooks they like.
    """

    @property
    def actor_options(self):
        """The set of options that may be configured on each actor.
        """
        return set()

    def before_acknowledge(self, broker, queue_name):
        """Called before a message is acknowledged.
        """

    def after_acknowledge(self, broker, queue_name):
        """Called after a message has been acknowledged.
        """

    def before_declare_actor(self, broker, actor):
        """Called before an actor is declared.
        """

    def after_declare_actor(self, broker, actor):
        """Called after an actor has been declared.
        """

    def before_declare_queue(self, broker, queue_name):
        """Called before a queue is declared.
        """

    def after_declare_queue(self, broker, queue_name):
        """Called before a queue has been declared.
        """

    def before_enqueue(self, broker, message, delay):
        """Called before a message is enqueued.
        """

    def after_enqueue(self, broker, message, delay):
        """Called after a message has been enqueued.
        """

    def before_process_message(self, broker, message):
        """Called before a message is processed.
        """

    def after_process_message(self, broker, message, *, result=None, exception=None):
        """Called after a message has been processed.
        """