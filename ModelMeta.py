class ModelRegistery:
	models={}
	@classmethod
	def register(cls, model):
		cls.models[model.__name__]=model

class ModelMetaInfo:
	def __init__(self):
		self.fields={}
		
class ModelMeta(type):
	def __new__(mcs, name, bases, ns):
		if name== "Model":
			return super().__new__(mcs, name, bases, ns)
			
		meta=ModelMetaInfo()
		
		for attr_name, attr_value in list(ns.items()):
			if isinstance(attr_value, Field):
				attr_value.name=attr_name
				meta.fields[attr_name]=attr_value
				ns.pop(attr_name)
		cls=super().__new__(mcs, name, bases, ns)
		
		cls._meta=meta
		ModelRegistery.register(cls)
		
		return cls
		
class Model(metaclass=ModelMeta):
	def __init__(self, **k):
		for field_name, field in self._meta.fields:
			if field_name in k:
				setattr(self, field_name, k)
			else:
				setattr(self, field_name, field)
				
class User(Model): pass
