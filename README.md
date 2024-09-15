## LLMSmith

> Prototype of LLMSmith and the collection of LLM4Shell PoCs (keep updating)

This repository contains the official code used in paper "Demystifying RCE Vulnerabilities in LLM-Integrated Apps".

Official Website (Containing Demos, Ethics, etc.): https://sites.google.com/view/llmsmith

Please feel free to contact lyutoon@gmail.com if you have any questions.

### Repo Structure
- **framework_vulns**: Call chain extraction prototype used in our paper.
- **app_search**: whitebox app search utils.
- **app_tests**: real-world demos and the exploit prompts used by LLMSmith (`prompt.py`, keep updating)
- **chains_pocs**: PoCs, call chains of frameworks and the corresponding responsible disclosure. (PoCs keeps updating when I found other vulnerable frameworks)

### Clarification
LLMSmith now is still a research prototype and **can only be used for educational purpose**, it may exist some unexcepted behaviors or bugs;

Meanwhile, LLMSmith is under active updating (e.g., new vulnerable frameworks, new PoCs, new demos...)

### Cite
```
@article{liu2023demystifying,
  title={Demystifying rce vulnerabilities in llm-integrated apps},
  author={Liu, Tong and Deng, Zizhuang and Meng, Guozhu and Li, Yuekang and Chen, Kai},
  journal={arXiv preprint arXiv:2309.02926},
  year={2023}
}
```
