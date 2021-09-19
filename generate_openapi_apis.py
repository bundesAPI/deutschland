import distutils.dir_util
import os
import requests
import subprocess


tmp_path = "./genarated"
if not os.path.exists(tmp_path):
    os.mkdir(tmp_path)

output_languages = ["python"]



# Construct apis which need to be generated with openapi from the github repos in bundesAPI
# Example: apis = [{"name": "smard","open_api_file":"https://raw.githubusercontent.com/bundesAPI/smard-api/main/openapi.yaml"}]

apis = []
all_repos = requests.get("https://api.github.com/users/bundesapi/repos").json()
print(f"Found {len(all_repos)} repos in the bundesAPI account.")
for repo in all_repos:
    repo_name = repo["name"]
    if repo["name"].endswith(("-api")):
        api_name = repo_name[:-4]
        # Construct url to openapi file.
        # Assumes always the same structure.
        # Probably better ways to do this by using git client or so
        open_api_file = f"https://raw.githubusercontent.com/bundesAPI/{repo_name}/main/openapi.yaml"
        apis.append({"name": api_name,"open_api_file":open_api_file})
        print(f"Found api with name {api_name} and openapi file {open_api_file}")
    else:
        print(f"Repo name {repo['name']} does not end with -api, skip it")



print("Start generation of apis.")
for api in apis:
    for language in output_languages:
        generation_path = f"{tmp_path}/{language}/{api['name']}"



output_languages = ["python"]
#apis = [{"name": "smard","open_api_file":"https://raw.githubusercontent.com/bundesAPI/smard-api/main/openapi.yaml"}]
#apis = []


for api in apis:
    try:
        for language in output_languages:

            generation_path = f"{tmp_path}/{language}/{api['name']}"

            # Generate the api using docker over subprocess. Improvment could be interact with docker over the python lib.
            # Example call:
            # docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate
            # -i https://raw.githubusercontent.com/bundesAPI/smard-api/main/openapi.yaml
            # --additional-properties=packageName=smard
            # -g python  -o /local/deutschland/smard
            subprocess.call(["docker",
                             "run","-v",
                             f"{os.getcwd()}:/local",
                             "--user",
                             f"{os.geteuid()}:{os.getegid()}",
                             "openapitools/openapi-generator-cli",
                             "generate",
                             "-i",f"{api['open_api_file']}",
                             f"--additional-properties=packageName={api['name']}",
                             "-g","python",
                             "-o",f"/local/{generation_path}"])

            # Copy it to the deutschland folder
            #distutils.dir_util.copy_tree(os.path.join(generation_path,api['name']), os.path.join("./deutschland/",api['name']))

    except Exception as e:
        print(f"Exception occured while trying to generate API for {api['name']} and language {language}")
