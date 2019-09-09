# %%
import json
coco = json.load(open("../person_keypoints_train2017.json"))
output = json.load(open("../output_.json"))
foot = json.load(open("../person_keypoints_train2017_foot_v1.json"))

# %%
image_dict = {}
for name, dataset in zip(["coco", "output", "foot"], [coco, output, foot]):
    l = {}
    for i in dataset["annotations"]:
        image_id = i["image_id"]
        if image_id not in l:
            l[image_id] = i
    image_dict[name] = l
print(image_dict.keys())
# %%
for name in ["coco", "output", "foot"]:
    print(name, "have", len(image_dict[name]), "annotationed images.")


# %%
new_categories = coco["categories"]
new_categories[0]["keypoints"] = ["鼻子", "左眼", "右眼", "左耳", "右耳", "左肩", "右肩", "左肘", "右肘", "左手腕",\
                               "右手腕", "左臀", "右臀", "左膝盖", "右膝盖", "左踝", "右踝", "左脚跟", "左鞋尖", "右脚跟", "右鞋尖", "左手端", "右手端", "脖子", "头顶"]

# %%
new_info = coco["info"]
new_licenses = coco["licenses"]

# %%
new_images = [i for i in foot["images"] if i["id"] in image_dict['foot']]

# %%
for i in range(len(new_images)):
    new_images[i]["coco_url"] = "http://121.48.164.95:65432/" + \
        new_images[i]["file_name"]
    new_images[i]["flickr_url"] = "http://121.48.164.95:65432/" + \
        new_images[i]["file_name"]

# %%
annotations_dict = {}
for name, dataset in zip(["coco", "output", "foot"], [coco, output, foot]):
    l = {}
    for i in dataset["annotations"]:
        anno_id = i["id"]
        if anno_id not in l:
            l[anno_id] = i
    annotations_dict[name] = l

for k in annotations_dict.keys():
    print(len(annotations_dict[k]))

# %%
ab = []
for i in annotations_dict["coco"]:
    if (len(annotations_dict["coco"][i]["keypoints"]) != 17*3):
        ab.append(i['id'])
print(len(ab), ab)
# %%
print(len(foot["annotations"][0]["keypoints"]))
print(len(annotations_dict["coco"][183062]["keypoints"]))


# %%
# coco左右耳--3,4
# output 左右鞋尖--0,2; 左右脚跟1,3; 头顶脖子左右手端 19,20,21,22
# new 17-左脚后跟、18-左鞋尖、19-右脚后跟、20-右鞋尖
#     21-左手端、22-右手端、23-胸骨/脖子(?)、24-头顶(?)
# foot  17. Left big toe.
#       18. Left small toe.
#       19. Left heel.
#       20. Right big toe.
#       21. Right small toe.
#       22. Right heel.

new_annotations = foot["annotations"]

for i, anno in enumerate(foot["annotations"]):
    if anno["id"] not in annotations_dict["coco"]:
        print(id)
    else:
        new_annotations[i]["keypoints"] = annotations_dict["coco"][anno["id"]]["keypoints"]

    assert  (len(annotations_dict["coco"][anno["id"]]["keypoints"]) == 17*3)

    if anno["id"] in annotations_dict["output"]:
        tail_17_24 = \
            annotations_dict["output"][anno["id"]]["keypoints"][1*3  : 1*3+3] + \
            annotations_dict["output"][anno["id"]]["keypoints"][0*3  : 0*3+3] +\
            annotations_dict["output"][anno["id"]]["keypoints"][3*3  : 3*3+3] +\
            annotations_dict["output"][anno["id"]]["keypoints"][2*3  : 2*3+3] +\
            annotations_dict["output"][anno["id"]]["keypoints"][21*3 : 21*3+3] +\
            annotations_dict["output"][anno["id"]]["keypoints"][22*3 : 22*3+3] +\
            annotations_dict["output"][anno["id"]]["keypoints"][20*3 : 20*3+3] +\
            annotations_dict["output"][anno["id"]]["keypoints"][19*3 : 19*3+3]
        assert (len(tail_17_24) == 8*3)
        new_annotations[i]["keypoints"] += tail_17_24
    else:
        tail_17_24 = \
            annotations_dict["foot"][anno["id"]]["keypoints"][19*3 : 19*3+3] + \
            annotations_dict["foot"][anno["id"]]["keypoints"][17*3 : 17*3+3] + \
            annotations_dict["foot"][anno["id"]]["keypoints"][22*3 : 22*3+3] + \
            annotations_dict["foot"][anno["id"]]["keypoints"][20*3 : 20*3+3] + \
            [0, 0, 0] + \
            [0, 0, 0] + \
            [0, 0, 0] + \
            [0, 0, 0]
        print(anno["id"])
        print(len(annotations_dict["foot"][anno["id"]]["keypoints"][19*3 : 19*3+3]))
        print(len(annotations_dict["foot"][anno["id"]]["keypoints"][17*3 : 17*3+3]))
        print(len(annotations_dict["foot"][anno["id"]]["keypoints"][22*3 : 22*3+3]))
        print(len(annotations_dict["foot"][anno["id"]]["keypoints"][20*3 : 20*3+3]))
        assert (len(tail_17_24) == 8*3)
        new_annotations[i]["keypoints"] += tail_17_24

    # if len(new_annotations[i]["keypoints"]) != 25*3:
    #     print(len(new_annotations[i]["keypoints"]))

# %%
for i in new_annotations:
    if len(i["keypoints"]) != 75:
        print(type(i["id"]))
# %%
new_json = {'info': new_info,
            'licenses': new_licenses,
            'images': new_images,
            'annotations': new_annotations,
            'categories': new_categories}

json.dump(new_json, open("new.json", 'w'))


# %%
