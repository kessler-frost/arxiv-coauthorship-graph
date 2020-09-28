import arxiv


def get_arxiv_couthor_connect_edges(filename="relevant_paper_ids.txt"):

    paper_ids = open(filename, "r").read().split()
    papers = []
    batch = 0
    batch_interval = 500
    while batch < len(paper_ids):
        papers += arxiv.query(id_list=paper_ids[batch:min(batch + batch_interval, len(paper_ids))])
        batch += batch_interval

    edges = []
    for paper in papers:
        auths = paper["authors"]
        for i, auth1 in enumerate(auths):
            for j, auth2 in enumerate(auths[i + 1:]):
                edges.append([auth1, auth2])

    return edges
