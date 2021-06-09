import sys
import re
sys.path.append('../..')

from factory import Factory

class UniqueObjectStorage():
    def __init__(self):
        self.objects_set = set()

    def add(self, key):
        if not key in self.objects_set:
            self.objects_set.add(key)

    def remove(self, key):
        if key in self.objects_set:
            self.objects_set.remove(key)

    def find(self, key):
        if key in self.objects_set:
            print(key)

    def print(self):
            for elem in self.objects_set:
                print(elem)

    def save(self):
        s = Factory.create_serializer("json")
        s.serialize(self.objects_set, "save_set.json")
        
    def load(self):
        s = Factory.create_serializer("json")
        self.objects_set = s.deserialize("", "save_set.json")


storage = UniqueObjectStorage()
print("adding world, 5, 269, 5:\n")
storage.add("world")
storage.add(5)
storage.add(269)
storage.add(5)
storage.print()


storage.remove(5)
print("after removing 5:\n")

storage.print()

print("find:\n ")
storage.find(269)

storage.save()
storage.print()