import json
from collections import OrderedDict
from pathlib import Path

import yaml

if __name__ == "__main__":
    yaml.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        lambda loader, node: OrderedDict(loader.construct_pairs(node)),
    )

    with open("../apis/overrides.json") as f:
        content = json.load(f)
        for api in content:
            office = api["office"]
            parts = api["githubURL"].split("/")
            file = Path(
                "/home/raphael/development/apis/bundesAPI", parts[-1], "openapi.yaml"
            )
            print(parts[-1], "\t \t", f'x-office: "{office}"')
            print()
            # with open(file,"r") as f2:
            #     res = yaml.load(f2,yaml.SafeLoader)
            #     curent_info = res["info"]
            #     res["info"]["x-office"] = office
            #
            #
            #     with open(file, 'w') as yamlfile:
            #         yaml.safe_dump(res, yamlfile,sort_keys=False, allow_unicode=True)
