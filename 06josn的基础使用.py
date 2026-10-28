import json

d = {
    "name": "张三",
    "age": 30,
    "gender": "男"
}

# 将字典转换为 JSON 字符串
json_str = json.dumps(d, ensure_ascii=False)

# 使用 print 函数打印 JSON 字符串
print(json_str)

l = [
    {
        "name": "张三",
        "age": 30,
        "gender": "男"
    },
    {
        "name": "张三",
        "age": 30,
        "gender": "男"
    },
    {
        "name": "张三",
        "age": 30,
        "gender": "男"
    }

]
print(json.dumps(l, ensure_ascii=False))

json_str = '{"name": "张三", "age": 30, "gender": "男"}'
json_array_str = '[{"name": "张三", "age": 30, "gender": "男"}, {"name": "张三", "age": 30, "gender": "男"}, {"name": "张三", "age": 30, "gender": "男"}]'

res_dict = json.loads(json_str)
print(res_dict, type(res_dict))

res_list = json.loads(json_array_str)
print(res_list, type(res_list))
