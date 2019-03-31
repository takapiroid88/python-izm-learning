# オブジェクトからJSON文字列
import json
json_data = {
  'Python': 'python-izm.com',
  'SearchEngine': ('google', 'yahoo')
}

print(type(json_data))
encode_data = json.dumps(json_data)
print(encode_data)
print(type(encode_data))

# 見やすい形に変換
print(json.dumps(json_data, indent=4))

# JSON文字列からオブエジェクト
decode_data = json.loads(encode_data)
print(decode_data)
print(type(decode_data))