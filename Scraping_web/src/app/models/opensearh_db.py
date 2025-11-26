# @ Author: naflashDev
# @ Create Time: 2025-04-22 12:17:59
# @ Project: Cebolla
# @ Description: Main entry point for running the application in a development
# environment.
#
# This script cointeins the methots to save de information in opensearch
from opensearchpy import OpenSearch
from loguru import logger

def store_in_opensearch(data,host,port,nom_index) -> None:
    """
    Stores the processed data in OpenSearch.

    This function connects to a local OpenSearch instance and stores the
    extracted and filtered content (such as text and keywords) in an index
    called "documents". The OpenSearch instance is configured to use basic
    authentication.

    Args:
        data (dict): The data to store in OpenSearch. Typically includes the
        URL, text, and keywords.
        host (str): The host of the OpenSearch server (e.g., "localhost").
        port (int): The port of the OpenSearch server (e.g., 9200).
        nom_index(str): Name of the Index to store the data.
    """
    try:

        logger.info(f"Connecting to OpenSearch instance at {host}:{port}.")

        client = OpenSearch(
            hosts=[{'host': host, 'port': port}]
        )

        response = client.index(index=nom_index, body=data)

        logger.info(
            f"Document indexed successfully. Response: {response['result']}"
        )

    except Exception as e:
        logger.error(f"Error while storing data in OpenSearch: {e}")