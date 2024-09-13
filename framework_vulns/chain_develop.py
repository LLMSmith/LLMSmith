import os
import sys
import types
import time
import argparse
from treelib import Tree, Node

MAP = {
    "exec": "<builtin>.exec",
    "eval": "<builtin>.eval"
}

CGCACHE = {}
IMPLICIT = 0

def parse_class_func(caller):
    caller_class = ""
    caller_func = ""
    caller_split = caller.split(".") + ["<PAD>"]
    for i in range(1, len(caller_split)):
        module = ".".join(caller_split[:-i])
        try:
            if isinstance(eval(module), types.FunctionType):
                caller_func = caller_split[-i-1]
            if isinstance(eval(module), type):
                caller_class = caller_split[-i-1]
                break
        except Exception as e:
            caller_func = caller_split[-i-1]
            break
    if caller_class == "":
        whole = caller_func
    else:
        whole = caller_class + "." + caller_func
    return [caller_class, caller_func, whole, caller]

def insert_node(tree, data, parent, file, ccc):
    MAX_RETRY = 10
    cnt = 0
    for child in tree.children(parent):
        if child.data[0] == data:
            return
    for node in tree.rsearch(parent):
        tag = tree.get_node(node).tag[:-2]
        d = tree.get_node(node).data
        # if tag == file+'/'+data and :
        if d == ccc:
            return
    while True:
        # print(data + "_" + str(cnt))
        try:
            id = data + "_" + str(cnt)
            tag = file + "/" + id
            tree.create_node(tag=tag, identifier=id, parent=parent, data=[data, ccc])
            # if ccc.endswith('.TreeofThought.solve'):
            #     tree.show()
            #     exit()
            return
        except Exception as e:
            cnt += 1
            if cnt >= MAX_RETRY:
                # if ccc.endswith('DFSSolver.solve'):
                    # print(222)
                    # exit()
                return

def find_files_with_string(root_dir, search_string):
    matching_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if not file.endswith(".py"):
                continue
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if search_string in content:
                        matching_files.append(file_path)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

    return matching_files

def classof(node):
    # return the class of node (if exists)
    return node.data[0].split(".")[0]

def funcof(node):
    # return the function of node
    return node.data[0]

def extend_tree_cg(tree, cg, file, leaves=None, is_root=False):
    # single file extend: sink -> xx -> xx -> xx
    cnt = 0
    while True:
        last_tree_size = tree.size()
        if cnt == 0:
            # if it is the first iteration,
            # use the original tree leaves!!!
            leaves = leaves
        else:
            # add from new leaves
            leaves = tree.leaves()
        for leaf in leaves:
            if not is_root:
                if is_implicit(leaf, cg):
                    print("[INFO] implicit function: ", leaf.tag)
                    global IMPLICIT
                    IMPLICIT += 1
                    sink = classof(leaf)
                    tree.update_node(leaf.identifier, data=[classof(leaf), classof(leaf)])
                else:
                    # sink = funcof(leaf)
                    sink = leaf.data[1]
            else:
                # sink = funcof(leaf)
                sink = leaf.data[1]
            if sink in MAP.keys():
                sink = MAP[sink]
            for caller, callees in cg.items():
                for callee in callees:
                    if callee.endswith(sink):
                        # if callee.endswith('TreeofThought.solve'):
                            # print(cg)
                        #     print(leaf)
                        #     print(leaf.data)
                        #     print(caller)
                        #     print(parse_class_func(callee))
                            # exit()
                        class_, func_, whole, ccc = parse_class_func(caller)
                        # if callee.endswith('DFSSolver.solve'):
                            # print(whole, ccc)
                            # exit()
                        insert_node(tree, whole, leaf.identifier, file, ccc)
        if last_tree_size == tree.size():
            return
        cnt += 1

def is_implicit(node, current_cg):
    # print(classof(node), funcof(node))
    if classof(node) == funcof(node):
        return False
    res = True
    # step 1: if current file does not contain the funcof(node)
    for caller, callees in current_cg.items():
        for callee in callees:
            # sink = funcof(node)
            sink = node.data[1]
            if sink in MAP.keys():
                sink = MAP[sink]
            if callee.endswith(sink):
                res = False
                return res
    # step 2: search all the file contains the classof(node)
    matching_files = find_files_with_string(package, classof(node))
    for suspect_file in matching_files:
        if suspect_file in CGCACHE.keys():
            cg = CGCACHE[suspect_file]
        else:
            cg = eval(os.popen(f"pycg --max-iter 10 {suspect_file}").read())
            CGCACHE[suspect_file] = cg
        for caller, callees in cg.items():
            for callee in callees:
                # sink = funcof(node)
                sink = node.data[1]
                if sink in MAP.keys():
                    sink = MAP[sink]
                if callee.endswith(sink):
                    # print("[DEBUG] ------> ", suspect_file)
                    res = False
                    return res
    # step 3: if all these file does not contains the caller of funcof(node)
    # then, it is an implicit call
    return res

def clean_tree(tree):
    f = lambda x: x[:-2]
    leaf_identifiers = set(map(f, [x.identifier for x in tree.leaves()]))
    record = dict.fromkeys(list(leaf_identifiers), 0)
    print(record)
    for leaf in tree.leaves():
        if record[f(leaf.identifier)] == 0:
            record[f(leaf.identifier)] = 1
        else:
            tree.remove_node(leaf.identifier)

def main(args):
    start = time.time()
    # prepare the analysis
    # package = "langchain"
    # package = "pandasai"
    # package = "langflow"
    # package = "pandas_llm"
    # package = "llama_index"
    # package = "autogpt"
    # package = 'metagpt'
    global package
    package = args.package

    # folder_path = "langchain/"
    # folder_path = "pandas-ai-0.8.1/" # old 0.8.1
    # folder_path = "langflow/src/backend/"
    # folder_path = "pandas-llm/"
    # folder_path = "llama_index/"
    # folder_path = "Auto-GPT/"
    # folder_path = "pandas-ai/" # new pandasai 1.0.3
    folder_path = args.dir
    os.chdir(folder_path)
    # find the suspected file
    init_sinks = ["exec", "eval"]#, "subprocess.run"]
    # init_sink = "exec"
    # init_sink = "eval"
    # init_sink = "subprocess.run"
    call_chain_cnt = 0
    cross_file_cnt = []
    cross_files = set()
    call_chain_len = []
    for init_sink in init_sinks:
        print(init_sink)
        search_string = init_sink + "("
        init_matching_files = find_files_with_string(package, search_string)
        # test tool.py as an example
        # suspect_file = "langchain/tools/python/tool.py"
        if init_sink == 'subprocess.run' and package == "langchain":
            init_matching_files = init_matching_files[1:]
        for init_suspect_file in init_matching_files:
            print(f"[+] Current initial file: {init_suspect_file}")
            if "experimental" in init_suspect_file or "example" in init_suspect_file:
                continue
            tree = Tree()
            tree.create_node(tag=init_sink, identifier=init_sink, data=[init_sink, init_sink])
            # generate cg
            cg = eval(os.popen(f"pycg {init_suspect_file}").read())
            CGCACHE[init_suspect_file] = cg
            extend_tree_cg(tree, cg, init_suspect_file, tree.leaves(), is_root=True)
            cross_files.add(init_suspect_file)
            # tree.show()
            if tree.depth() == 0:
                continue
            
            # tree, the tree's leaves
            # search the class of leaves, extend the tree with the new cg geneated from newly searched file
            # add to the leaf.
            while True:
                last_tree_size = tree.size()
                leaves = tree.leaves()
                for leaf in tree.leaves():
                    matching_files = find_files_with_string(package, classof(leaf))
                    for suspect_file in matching_files:
                        if "example.py" in suspect_file or "example-chatbot.py" in suspect_file:
                            continue
                        if suspect_file in CGCACHE.keys():
                            cg = CGCACHE[suspect_file]
                        else:
                            cg = eval(os.popen(f"pycg --max-iter 30 {suspect_file}").read())
                            CGCACHE[suspect_file] = cg
                        extend_tree_cg(tree, cg, suspect_file, leaves)
                        cross_files.add(suspect_file)
                        print("[DEBUG] ----> ", suspect_file)
                if last_tree_size == tree.size() or tree.size() >= 40:
                    break

            # clean_tree(tree)
            tree.show()
            # calculate the file number among one call chain and its length
            for leave in tree.leaves():
                file_set = set()
                tmp_cnt = 0
                tree_path = tree.rsearch(leave.identifier)
                for node_id in tree_path:
                    node = tree.get_node(node_id)
                    f_name = "/".join(node.tag.split("/")[:-1])
                    file_set.add(f_name)
                    tmp_cnt += 1
                cross_file_cnt.append(len(file_set)-1)
                call_chain_len.append(tmp_cnt)

            call_chain_cnt += len(tree.leaves())
    end = time.time()
    print(f"[RESULT]: --------> {package}")
    print('-' * 50)
    print(f"[TOTAL] Total time costs: {end-start}")
    print(f"[TOTAL] Total call chain: {call_chain_cnt}")
    # print(f"[+] Total number of cross file: {len(cross_files)}")
    print('-' * 50)
    print(f"[TOTAL] Total number of cross file: {sum(cross_file_cnt)}")
    print(f"[AVG] Average cross file number: {sum(cross_file_cnt) / call_chain_cnt}")
    print(f"[MAX] Max cross file number: {max(cross_file_cnt)}")
    print('-' * 50)
    print(f"[TOTAL] Total call chain length: {sum(call_chain_len)}")
    print(f"[AVG] Average call chain length: {sum(call_chain_len) / call_chain_cnt}")
    print(f"[MAX] Max call chain length: {max(call_chain_len)}")
    print('-' * 50)

    print(f'[*] Implicit call number: {IMPLICIT}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--package', help='package to be detected', type=str)
    parser.add_argument('--dir', help='package dir', type=str)
    args = parser.parse_args()
    if args.package != 'autogpt':
        exec(f'import {args.package}')
    import griptape.utils
    main(args)
