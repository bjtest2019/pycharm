#_author:test
#date:2019/4/14
import pickle
l = [1,2,3]
print(pickle.dumps(l))

b = pickle.dumps(l)

print(pickle.loads(b))

d = {"id":1,"name":"test","phone_number":"13245678901"}
b = pickle.dumps(d)
print(b)
print(pickle.loads(b))
