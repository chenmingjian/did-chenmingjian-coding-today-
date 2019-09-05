#%%
import json

#%%
new = json.load(open("../new.json"))
#%%
new["annotations"][0]["keypoints"]
#%%
for i in range(len(new["annotations"])):
    new["annotations"][i]["keypoints"] = new["annotations"][i]["keypoints"][-24:]
#%%
new["categories"][0]["keypoints"] = new["categories"][0]["keypoints"][17:]

#%%
json.dump(new, open("9_point.json", "w"))


#%%
print(len(new["categories"][0]["keypoints"]), new["categories"][0]["keypoints"])
#%%
new["annotations"][0]["keypoints"]

#%%
for i in (new["annotations"]):
    if i["image_id"] == 101189:
        print(i["keypoints"])
    

#%%
