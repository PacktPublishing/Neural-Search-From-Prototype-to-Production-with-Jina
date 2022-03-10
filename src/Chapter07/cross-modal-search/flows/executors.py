""" Implementation of filters for images and texts"""
import numpy as np
from jina import Executor, DocumentArray, requests


class ImageReader(Executor):

    @requests(on='/index')
    def index_read(self, docs: 'DocumentArray', **kwargs):
        array = DocumentArray(list(filter(lambda doc: doc.modality=='image', docs)))
        for doc in array:
            doc.tensor = doc.tensor.astype(np.uint8)
        return array

    @requests(on='/search')
    def search_read(self, docs: 'DocumentArray', **kwargs):
        image_docs = DocumentArray(list(filter(lambda doc: doc.modality == 'image', docs)))
        if not image_docs:
            return DocumentArray([])
        for doc in image_docs:
            doc.load_uri_to_image_tensor()
            doc.tensor = doc.tensor.astype(np.uint8)
        print(f'search on ImageReader: {len(image_docs)} docs. {image_docs[0].mime_type}')
        return image_docs


class TextFilter(Executor):
    @requests
    def filter_text(self, docs: 'DocumentArray', **kwargs):
        docs = DocumentArray(list(filter(lambda doc: doc.modality == 'text', docs)))
        return docs
