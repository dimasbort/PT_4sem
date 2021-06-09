# class MyDict:
#     def __init__(self):
#         self.d = {}
#         self.context = []
#         # self.last_key = []
#
#     def getContext(self, arr, value):
#         if not arr:
#             return {}
#         obj = {arr[len(arr) - 1]: value}
#         print(arr, 'arr', value)
#         for ind in range(len(arr) - 2, -1, -1):
#             obj = {str(arr[ind]): obj}
#         print(obj, 'cont')
#         return obj
#
#     def __setitem__(self, key, value):
#         print('set', key, value, self.context)
#         self.context = self.getContext(self.context, value)
#         self.d[key] = self.context
#         print('d', self.d)
#         self.context = []
#         return self.d
#
#     def __getitem__(self, item):
#         print('item', item)
#         self.context.append(item)
#         return self
#
#     def __str__(self):
#         return str(self.d)
#
#
# if __name__ == '__main__':
#     d = MyDict()
#     d["a"] = 1
#     d["a"]["b"] = 1
#     # print(d)
#     # d["a"]["b"] = 2

class MyDict:
    def __init__(self):
        self.d = dict()

    def __set
