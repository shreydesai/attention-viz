# attention-viz

`attention-viz` is a lightweight visualization for attention mechanisms in deep neural networks. It supports one score per token, producing HTML code that can be run in the browser (with no additional dependencies). Note that the scores don't necessarily need to form a valid probability distribution, so this tool can also be used to visualize other types of magnitude-based scores (e.g., gradient saliency).

<center><img width="45%" src="https://i.imgur.com/lzfJwBu.png"></center>

## Requirements

- Python 3.6+
- matplotlib (3.1.1)

## Usage

If `matplotlib` is not installed globally, set up a virtual environment and activate it:
```bash
$ virtualenv python3.6 venv
$ source venv/bin/activate
$ pip install matplotlib
```
The script `viz.py` takes in two arguments: `--text_path` (path to file of tokens, delimited by new lines) and `--score_path` (path to file of scores, also delimited by new lines). By default, the `BuGn` colormap is used, but this can be easily configured by setting the `--cmap` flag. Different colormap options are enumerated [here]([https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html](https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html)).

For convenience, `viz.py`'s output can be piped to an `index.html` file. Open this file in your browser to see the text overlaid with the attention heatmap:

```bash
$ python3 viz.py --text_path text --score_path score > index.html
$ open index.html  # opens file with default browser
```
 
If the attention distribution is highly concentrated, it may be difficult to read text with extremely dark backgrounds. You can use the `--alpha` flag to adjust the visualization. Generally, lower values of `--alpha` will result in more color concentration while higher values of `--alpha` will result in lesser color concentration:

 `--alpha 0.0`
 
 <center><img width="45%" src="https://i.imgur.com/NH4IOxl.png"></center>
 
 `--alpha 0.5`
 
<center><img width="45%" src="https://i.imgur.com/lzfJwBu.png"></center>

`--alpha 5.0`

<center><img width="45%" src="https://i.imgur.com/oSkvGii.png"></center>

## Citation

If you found this tool useful, please consider putting a link to this repository in your work.
