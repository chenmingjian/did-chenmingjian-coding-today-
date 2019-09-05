# %%
import json

# %%
coco = json.load(open("../person_keypoints_val2017.json"))
output = json.load(open("../output_.json"))
foot = json.load(open("../person_keypoints_train2017_foot_v1.json"))

# %%
for i in coco.keys():
    print(type(output[i]))

# %%
print(type(foot["categories"]))
print(type(output["categories"]))

# %%
output["categories"] = [output["categories"]]
output["categories"][0]['keypoints'] = ['left_tiptoe', 'left_heel', 'right_tiptoe', 'right_heel', 'nose', 'left_eye', 'right_eye', 'left_ear', 'right_ear', 'left_shoulder', 'right_shoulder',
                                        'left_elbow', 'right_elbow', 'left_wrist', 'right_wrist', 'left_hip', 'right_hip', 'left_knee', 'right_knee', 'left_ankle', 'right_ankle', 'headtop', 'neck', 'left_head_endpoint', 'right_head_endpoint']
json.dump(output, open("../output_.json", "w"))

# %%
print(output["categories"])
print(coco["categories"])
print(foot["categories"])
# %%
print(output["annotations"][0]["image_id"])


# %%
print(len(output["image_id"]))

# %%
l = []
for i in output["annotations"]:
    if i["image_id"] not in l:
        l.append(i["image_id"])

print(len(l))


# %%
print(foot["annotations"][0])
print(coco["annotations"][0])
print(output["annotations"][0])

# %%
print(foot["categories"])


# %%
