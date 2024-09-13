import re
import json
import argparse
from urllib.parse import urlparse
from urlextract import URLExtract
# from gensim.models import Word2Vec
# from gensim.utils import simple_preprocess
from sklearn.metrics.pairwise import cosine_similarity

template0 = "https://{}."
template1 = "https://www.{}."
url_black_list = [
    "https://colab.research.google.com/",
    "https://openai.com/",
    "https://img.",
    ".html",
    ".png",
    "/github.com",
    "/api/",
    "api.",
    "https://dcbadge.vercel.app/api/",
    template0.format("twitter"), template1.format("twitter"),
    template0.format("tiktok"), template1.format("tiktok"), 
    template0.format("youtube"), template1.format("youtube"),
    template0.format("kaggle"), template1.format("kaggle"),
    template0.format("instagram"), template1.format("instagram"),
    template0.format("github"), template1.format("github"),
    template0.format("reddit"), template1.format("reddit"),
    template0.format("quora"), template1.format("quora"),
    template0.format("pypi"), template1.format("pypi"),
    template0.format("discord"), template1.format("discord"),
    template0.format("docs"), template1.format("docs"),
]
extractor = URLExtract()
url_extract = lambda x: [i for i in list(set(extractor.find_urls(x, check_dns=True))) if not i.startswith("https://github.com/")]

repo_black_list = [
    "langchain",
    "pandasai",
    "pandas-ai",
    "llama_index",
    "langchain-serve",
    "langflow"
]

def check_in_url_blacklist(url):
    if url.endswith(".json") or \
       url.endswith(".py") or \
       url.endswith(".svg") or \
       url.endswith(".zip") or \
       url.endswith(".md"):
        return True 
    for u in url_black_list:
        if u in url:
            return True
    return False

def clean(text):
    pattern = r'[^a-zA-Z0-9\s]'
    cleaned_text = re.sub(pattern, ' ', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)

    return cleaned_text

def main(args):
    cnt = 0
    keywords = {}

    with open(f"./result/github_data/{args.query}.json", "r") as f:
        res = json.load(f)

    details = res['details']
    suspects = {}
    for repo, items in details.items():
        urls = items['readme_urls']
        des_urls = []
        # urls = url_extract(items['readme_content'])
        if items['description']:
            des_urls = url_extract(items['description'])
        repo_name = repo.split("/")[-1]
        if repo_name.lower() in repo_black_list: #or "awesome" in repo_name.lower():
            continue
        repo_name = clean(repo_name)
        suspects[repo] = []
        for url in urls+des_urls:
            if check_in_url_blacklist(url):
                continue
            url_ = clean(url)
            # repo_name in url, app!
            if "streamlit.app" in url:
                suspects[repo].append(url)
            elif ".app" in url or ".ai" in url:
                suspects[repo].append(url)
            elif repo_name in url_ or repo_name.replace(" ", "") in url_.replace(" ", ""):
                suspects[repo].append(url)
            # elif word2vec_cos_sim(repo_name, url_) > 0.7:
            #     suspects[repo].append(url)

    with open(f"./result/extracted_url/url_{args.query}.json", 'w') as f:
        json.dump(suspects, f, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-q', '--query',
        help='the target code',
        type=str
    )
    args = parser.parse_args()
    main(args)

