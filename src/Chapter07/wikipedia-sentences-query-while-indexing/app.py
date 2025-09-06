__copyright__ = "Copyright (c) 2021 Jina AI Limited. All rights reserved."
__license__ = "Apache-2.0"

import os
import time
import warnings

import click
from jina import Document, DocumentArray, Client, Flow
from jina.logging.logger import JinaLogger

warnings.filterwarnings("ignore", category=DeprecationWarning)
os.environ['JINA_LOG_LEVEL'] = 'DEBUG'

DATA_FILE = 'data/toy.txt'  # change this if you get the full data
DOCS_PER_ROUND = 5  # nr of documents to index in each round
QUERY_REST_PORT = 9000  # REST port of Flow, defined in flow.yml

logger = JinaLogger('app')


def docarray_from_file(filename):
    docs = []
    with open(filename) as f:
        for line in f:
            docs.append(Document(text=line))
    return DocumentArray(docs)


def query_restful():
    while True:
        text = input('please type a sentence: ')
        if not text:
            break

        query_doc = Document()
        query_doc.text = text
        response = query_docs(query_doc)
        matches = response[0].matches
        len_matches = len(matches)
        logger.info(f'Ta-Dah🔮, {len_matches} matches we found for: "{text}" :')

        for idx, match in enumerate(matches):
            score = match.scores['cosine'].value
            if score < 0.0:
                continue
            logger.info(f'> {idx:>2d}({score:.2f}). {match.text}')


def query_docs(docs: Document):
    logger.info(f'Searching document {docs}...')
    return Client(host='localhost', port=QUERY_REST_PORT, protocol='http').search(
        inputs=docs, return_results=True)


def start_flow_loop() -> None:
    docs = docarray_from_file(DATA_FILE)
    f = Flow.load_config('flow.yml')
    logger.info(f'starting Flow')
    f.plot('flow.png')
    with f:
        for round, docs_batch in enumerate(docs.batch(DOCS_PER_ROUND)):
            logger.info(f'Round {round} of indexing...')
            logger.info(f'Indexing {len(docs_batch)} docs')
            f.index(docs_batch)
            logger.info(f'Waiting 10 seconds before next round.')
            time.sleep(10)
        logger.info(f'No more docs to index. Serving Flow until Ctrl+C...')
        f.block()

@click.command()
@click.option(
    '--task',
    '-t',
    type=click.Choice(['flow', 'client'], case_sensitive=False),
)
def main(task: str):
    """main entrypoint for this example"""
    if task == 'flow':
        try:
            start_flow_loop()
        except Exception as e:
            logger.info(f'Caught {e}. Shutting down...')

    elif task == 'client':
        query_restful()


if __name__ == '__main__':
    main()
