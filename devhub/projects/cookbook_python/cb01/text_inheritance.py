from abc import ABC, abstractmethod

class Animal(ABC):
  def __init__(self, name, age):
    self.name = name
    self.age = age

  @abstractmethod
  def speak(self):
    pass

  def info(self):
    return f"{self.name} is {self.age} years old."

class Dog(Animal):
  def __init__(self, name, age, breed):
    super().__init__(name, age)
    self.breed = breed

  def speak(self):
    return "Woof!"
  
  def info(self):
    return f"{self.name} is a {self.age} years old {self.breed}."

class Cat(Animal):
  def __init__(self, name, age, color):
    super().__init__(name, age)
    self.color = color

  def speak(self):
    return "Meow!"

  def info(self):
    return f"{self.name} is a {self.age} years old {self.color} cat."


# 创建对象并调用方法
dog = Dog("Buddy", 3, "Golden Retriever")
cat = Cat("Whiskers", 2, "black")

print(dog.info())   # 输出: Buddy is a 3 years old Golden Retriever.
print(dog.speak())  # 输出: Woof!

print(cat.info())   # 输出: Whiskers is a 2 years old black cat.
print(cat.speak())  # 输出: Meow!
