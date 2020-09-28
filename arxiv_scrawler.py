import arxiv
import collections


def get_paper_id_from_url(url_string):
    if "http://arxiv.org/abs/" in url_string:
        return str(url_string).replace("http://arxiv.org/abs/", "")
    else:
        return ""


def collect_relevant_papers(query_string, node_count):

    papers = arxiv.query(query=query_string,
                         id_list=[],
                         max_results=50000,
                         start=0,
                         sort_by="relevance",
                         sort_order="descending",
                         prune=True,
                         iterative=False,
                         max_chunk_results=1000)

    auths = collections.defaultdict(lambda: [])

    for paper in papers:
        for auth in paper["authors"]:
            auths[auth].append(paper["id"])

    selected_papers = set()
    for key in sorted(auths.keys(), key=lambda x: len(auths[x]), reverse=True)[:min(len(auths), node_count)]:
        for id_url in auths[key]:
            selected_papers.add(get_paper_id_from_url(id_url))

    return selected_papers


def save_relevant_list_of_ids(queries, filename):

    all_papers = set()
    for query in queries:
        all_papers |= collect_relevant_papers(query, 70)

    with open(filename, "w") as file_w:

        file_w.write("\n".join(all_papers))


if __name__ == "__main__":

    queries = ["deep learning"]

    save_relevant_list_of_ids(queries, "relevant_paper_ids.txt")
