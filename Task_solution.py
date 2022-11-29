from urllib.request import urlopen
import json
url = "https://zorang-recrutment.s3.ap-south-1.amazonaws.com/addresses.json"
response = urlopen(url)
nums = json.loads(response.read())

# given values from the desc
store_latit= 28.9428
store_longit=77.2276

# for custom user input
# store_latit=float(input())
# store_longit=float(input())

def comp(ele):
    value1=ele['latitude']-store_latit
    value1*=value1
    value2=ele['longitude']-store_longit
    value2*=value2
    return value1+value2

# sorting the nums using comparator sorting
nums.sort(key=comp)

# initially total_dist as zero
tot_dist=0

for i in range(99):
    value1=nums[i]['latitude']-nums[i+1]['latitude']
    value1*=value1
    value2=nums[i]['longitude']-nums[i+1]['longitude']
    value2*=value2
    tot_dist+=(value1+value2)

each_dist=(tot_dist)/10

res=[]
ind =0

for i in range(9):
    temp=[ind]
    temp_dist=0
    while True:
        value1=nums[ind+1]['latitude']-nums[ind]['latitude']
        value1*=value1
        value2=nums[ind+1]['longitude']-nums[ind]['longitude']
        value2*=value2
        next_dist=value1+value2


#       checking for the minimum available distance.
        if temp_dist+next_dist<each_dist and ind+1<=100-i:
            # print(temp_dist, i, ind)
            temp_dist+=next_dist
            ind+=1
            temp.append(ind)
        else:
            break
    

    res.append(temp)
    ind+=1

temp=[]
while ind <100:
    temp.append(ind)
    ind+=1
res.append(temp)

def comp1(ele):
    return ele[1]

for i in res:
    temp=[]
    for j in i:
        temp2=[j]
        value1=nums[j]['latitude']-nums[i[0]]['latitude']
        value1*=value1
        value2=nums[j]['longitude']-nums[i[0]]['longitude']
        value2*=value2
        temp2.append(value1+value2)
        temp.append(temp2)


    temp.sort(key=comp1)

    for j in range(len(i)):
        i[j]=nums[temp[j][0]]['_id']

    
print(res)

