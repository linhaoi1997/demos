import yaml

with open("taobao_caps.yaml", "r", encoding='utf-8') as fp:
    test = yaml.load(fp)
    print(test, type(test))
