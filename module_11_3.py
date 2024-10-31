class Introspection:
    def __init__(self, obj):
        self.obj = obj

    def __repr__(self):
        return f"<Introspection object at {hex(id(self))}>"

    def introspection_info(self):
        info = {}

        info['type'] = type(self.obj).__name__

        attributes = [attr for attr in dir(self.obj) if not callable(getattr(self.obj, attr)) and not attr.startswith('__')]
        info['attributes'] = attributes

        methods = [method for method in dir(self.obj) if callable(getattr(self.obj, method)) and not method.startswith('__')]
        info['methods'] = methods

        info['module'] = getattr(self.obj, '__module__', 'N/A')

        return info


number_info = Introspection(42)
print(number_info.introspection_info())
