import argparse

import matplotlib.cm as cm
import matplotlib.colors as colors
import matplotlib.pyplot as plt


def read_file(path, cast=False):
    res = [
        line.strip()
        for line in open(path).read().split('\n')
        if len(line.strip()) > 0
    ]
    if cast:
        res = [float(line) for line in res]
    return res


parser = argparse.ArgumentParser()
parser.add_argument('--text_path', type=str, default='text')
parser.add_argument('--score_path', type=str, default='score')
parser.add_argument('--cmap', type=str, default='BuGn')
parser.add_argument('--alpha', type=float, default=1.0)
args = parser.parse_args()

tokens = read_file(args.text_path)
scores = read_file(args.score_path, True)
cmap = cm.get_cmap(args.cmap)

off = (sum(scores) / len(scores)) * args.alpha
normer = colors.Normalize(vmin=min(scores)-off, vmax=max(scores)+off)
colors = [colors.to_hex(cmap(normer(x))) for x in scores]

if len(tokens) != len(colors):
    raise ValueError("number of tokens and colors don't match")

style_elems = []
span_elems= []
for i in range(len(tokens)):
    style_elems.append(f'.c{i} {{ background-color: {colors[i]}; }}')
    span_elems.append(f'<span class="c{i}">{tokens[i]} </span>')

print(
    f"""<!DOCTYPE html><html><head><link href="https://fonts.googleapis.com/css?family=Roboto+Mono&display=swap" rel="stylesheet"><style>span {{ font-family: "Roboto Mono", monospace; font-size: 12px; }} {' '.join(style_elems)}</style></head><body>{' '.join(span_elems)}</body></html>"""
)
