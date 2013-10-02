from rodents import Rodent

#rodents_dict = {}

'''rodentfile = open('rodents.csv')
for line in rodentfile:
    contents = line.split(',')
    next_id = contents[0]
    if next_id in rodents_dict:
        rodents_dict[next_id].add_weight(contents[1])
    else:
        rodents_dict[next_id] = Rodent(contents[0])
        rodents_dict[next_id].add_weight(contents[1])
print rodents_dict'''


rodents = {}
for line in open('rodents.csv'):
    tag_id, weight = line.split(',')
    if tag_id not in rodents:
        rodents[tag_id] = Rodent(tag_id)
        rodents[tag_id].add_weight(weight)
    else:
        rodents[tag_id].add_weight(weight)

print rodents
for key in rodents:
    print rodents[key].tag_id, rodents[key].weight
    print 'What a nice rodent'
    print 'It looks like a water rat'
