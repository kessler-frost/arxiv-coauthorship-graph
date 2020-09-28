# Arxiv Co-authorship Graph

## Requirements
Packages used in this project:

`arxiv 0.5.3` - Courtesy of lukasschwab [here](https://github.com/lukasschwab/arxiv.py).

`networkx 2.5` - Website can be found [here](https://networkx.github.io/).

`matplotlib 3.3.2` - Website can be found [here](https://matplotlib.org/).

Python 3.7 onwards is supported.

## Extract Relevant Papers
To retrieve paper IDs from arxiv of topics which are relevant to us, in this case "deep learning", "computer vision", and "machine learning" to a file `relevant_paper_ids.txt`, just run,

`python arxiv_crawler.py`

## Pickle obtained Graph
After that we create a pickle of the co-authorship graph so that we do not have to do the time consuming process of crawling the arxiv again. This can be done by calling the `pickle_graph()` function in `graph_and_histogram.py` file.

## Visualize Graph and Distributions
Now, to visualize the graph and to obtain different measures used in the project including Degree Distribution, Closeness, and Betweenness, just run,

`python graph_and_histogram.py`
