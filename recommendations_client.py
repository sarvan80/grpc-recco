from recommendations_pb2 import BookCategory, RecommendationRequest
# from __future__ import print_function
import grpc
from concurrent import futures
import time
import recommendations_pb2_grpc as pb2_grpc
import recommendations_pb2 as pb2
import random

def Recommend(stub):
    if stub.category not in pb2.books_by_category:
        # context.abort(grpc.StatusCode.NOT_FOUND, "Category not found")
        print(grpc.StatusCode.NOT_FOUND, "Category not found")

    books_for_category = pb2.books_by_category[stub.category]
    num_results = min(stub.max_results, len(books_for_category))
    books_to_recommend = random.sample(
        books_for_category, num_results
    )


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pb2_grpc.RecommendationsStub(channel)
        Recommend(stub)


if __name__ == '__main__':
    run()