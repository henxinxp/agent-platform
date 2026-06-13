from ddgs import DDGS

def search_web(query: str):

    with DDGS() as ddgs:

        results = list(
            ddgs.text(
                query,
                max_results=3
            )
        )

    text = ""

    for r in results:

        text += (
            f"{r['title']}\n"
            f"{r['body']}\n\n"
        )

    return text