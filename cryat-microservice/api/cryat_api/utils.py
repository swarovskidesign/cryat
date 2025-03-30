from urllib.parse import urlparse

def get_uri_for_proxy(url: str) -> str:
    """
    Extracts the last segment of the path from the URL.
    """

    parsed_url = urlparse(url)
    return parsed_url.path.rstrip("/").split("/")[-1]
