import random
from random import shuffle

#function to get everyone going for lunch
def read_lunchlist(mylist):
	with open(mylist, 'r') as document:
		answer = {}
		for line in document:
			line = line.split()
			if not line:
				continue
			answer[line[0]] = line[1:]
	return answer

#NewEmployeeList is a dynamic file where records for new employees will get added, this file should not have records for existing employees
#EmplyeeLunchList file will have all the employees going for lunch and this will include the new employees as well

f = open('NewEmployeeList.txt')
f1 = open('EmployeeLunchList.txt', 'a')
for line in f.readlines():
        f1.write(line)

f1.close()
f.close()

lunchlist='EmployeeLunchList.txt'
lunchlist=read_lunchlist(lunchlist)

#defining the group sizes to be of 3,4 OR 5

groups=[]
appropriate_group_size=[3,4,5]
n=random.choice(appropriate_group_size)
print 'the group size is'
print n

#create random groups of size n(3,4,or 5)
def random_group(d, size=n):
        keys = list(d.keys())
        random.shuffle(keys)
        for i in range(0, len(keys), size):
                yield [(key, d[key]) for key in keys[i:i + size]]

#applying the random function to the list of people going for lunch
for group in random_group(lunchlist):
	groups.append(group)
#print groups

#generate the groups and identify anyone left alone and assign them to one of the groups
def generate_groups(groups):
	group_of_1=[]
	group_of_3=[]
	for i in groups:
		if len(i) == 1:
			#group_of_1.append(i)
			for x in i:
				group_of_1.append(x)# x is the tuple
		else:
			group_of_3.append(i)
	print 'printing group_of_1 :'
	print group_of_1

	print 'printing other groups :'
	print group_of_3	
	
	print 'the randomly chosen group from other groups to accomodate anyone left behind is'
	z=random.choice(group_of_3)
	print z
	
	print 'the dont be sad group is'
	print z+group_of_1

y=generate_groups(groups)
print y	

