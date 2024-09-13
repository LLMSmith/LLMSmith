import os
import json
import argparse
import requests
from base64 import b64decode
from urlextract import URLExtract

log_red = lambda x: print(f"\033[31m{x}\33[0m")
log_yellow = lambda x: print(f"\033[33m{x}\33[0m")
log_blue = lambda x: print(f"\033[34m{x}\33[0m")
extractor = URLExtract()
# simple filter, filted the github page
url_extract = lambda x: [i for i in list(set(extractor.find_urls(x, check_dns=True))) if not i.startswith("https://github.com/")]

def search(query, per_page=100):
    log_yellow(f"[+] Start scanning code: {query}")
    url = f"https://api.github.com/search/code?q={query}&per_page={per_page}"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "xxxx", 
    }
    cnt = 0
    res = []
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])
            cnt += len(items)
            res = res + items
            # Check for the "next" link in the response headers
            if 'Link' in response.headers:
                next_link = response.links.get('next', {}).get('url')
                url = next_link
            else:
                url = None  # No more pages, exit the loop
        else:
            print(f"Error: {response.status_code} - {response.text}")
            break
    log_red(f"[*] Total number of suspects: {cnt}")
    assert len(res) == cnt
    return res

def fetch_readme(full_name):
    url = f"https://api.github.com/repos/{full_name}/readme"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "xxxx", 
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        readme_content = data.get('content', '')
        readme_text = b64decode(readme_content).decode('utf-8')
        return readme_text
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def extract(items):
    res = {}
    cnt = 0
    fork_cnt = 0
    log_yellow(f"[+] Start extracting repo")
    for item in items:
        inner_res = {}
        # extract file name
        code_file = item['name']
        inner_res['code_file'] = [code_file]
        # extract repo
        repo = item['repository']
        # if it is a forked repo, continue
        if repo['fork']:
            fork_cnt += 1
            continue
        cnt += 1
        # extract the repo name
        repo_name = repo['full_name']
        if repo_name in res.keys():
            res[repo_name]['code_file'].append(code_file)
            continue
        log_blue('-' * 10 + '> ' + repo_name)
        inner_res['repo_name'] = repo_name
        # extract readme content
        try:
            readme_content = fetch_readme(repo_name)
        except:
            readme_content = ""
        if readme_content == None: readme_content = ""
        inner_res['readme_content'] = readme_content
        # extract urls in readme
        urls = url_extract(readme_content)
        inner_res['readme_urls'] = urls # + url_extract()
        # extract the description
        description = repo['description']
        inner_res['description'] = description
        # collect the author's info
        owner = repo['owner']
        owner_id = owner['login']
        inner_res['owner'] = owner_id

        res[repo_name] = inner_res
    log_red(f"[*] Total number of repos: {cnt}")
    return res, cnt

def main(args):
    """
    details contains: 
        code_file: file name
        repo_name: name of repo
        readme_content: readme
        readme_urls: readme urls
        description: description of the repo
        owner: owner of the repo
    """
    if not os.path.exists('result'):
        os.mkdir("result")
    query = args.query
    search_res = search(query)
    extract_res, cnt = extract(search_res)
    res = {
        "code": query,
        "suspect_num": cnt,
        "details": extract_res     
    }
    with open(f"./result/github_data/{query}.json", 'w') as f:
        json.dump(res, f, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-q', '--query',
        help='the target code',
        type=str
    )
    args = parser.parse_args()
    main(args)
