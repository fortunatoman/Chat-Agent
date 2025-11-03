import json

import agent

sep_str = "*" * 100
outfile = "demo_data.json"

queries = [
    "Summarize the metagpt paper.",
    "Summarize the autogen paper.",
    "What communication protocols are best for metagpt?",
    "What is conversation programming and how does autogen use it?",
    "Compare and contrast how metagpt and autogen handle roles.",
]

demo_data = {}
for query in queries:
    print(f"{sep_str}\nagent.runner(query={query})\n{sep_str}")
    demo_data[query] = agent.runner(query=query)

print(f"Writing to {outfile}")
json.dump(demo_data, open(outfile, "w"), indent=4)
