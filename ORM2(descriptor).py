class Field:
	
	def __init__(self, *, type_, default=None, nullable=False):
		self.type=type_
		self.default=default
		self.nullable=nullable
		
	def __set_name__(self, owner, name):
		self.name=name
	
	def __get__(self, instance, owner):
		if instance is None:
			return self
		return instance.__dict__.get(self.name, self.default)
	def __set__(self, instance, value):
		if value is None:
			if not self.nullable:
				print("no")
			instance.__dict__[self.name]= None
			return
		if not isinstance(value, self.type):
			print("not type")
			return
		instance.__dict__[self.name] = value
class user:
	name=Field(type_ = str, nullable = False)
	age = Field(type_ = int, default = 0)
u=user()
u.name="Ali"
print(u.name)
u.name=None
u.age="g"
u.age=56
print(u.age)
	
		
