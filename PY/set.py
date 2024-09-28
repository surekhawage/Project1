time= {1,2,3,4,5,6}
clock= {6,7,8,9}


# num= ["m","o","h","i","t"]
# city="abcd"

# #deleting elements from set
# time.discard(1)
# time.remove(2)
# time.pop()
# # time.clear() #clear() removes all elements

# #update elements to set
# time.add(1)
# time.update(num)
# time.update(city)

#union
watch= time|clock
#intersection
c= time&clock
#difference
d=time-clock
e=clock-time

#symmetric difference
f=(time-clock)^(clock-time)

print(f)
print(e)
print(d)
print(c)
print(watch)
print(time)