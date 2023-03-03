from src.openapi.openapi import count_tokens
import hashlib
import pandas as pd

from src.openapi.openapi import get_embedding
from src.openapi.openapi import vector_similarity


def split_file_into_chunks(file):
    with open(file, 'r', encoding='utf-8') as input_file:
        text_list = input_file.read().split('\n')
        res = []
        for text in text_list:
            if text == '':
                continue
            num_tokens = count_tokens(text)
            if num_tokens < 10:
                continue
            if num_tokens > 400:
                continue
            res.append(("Elections", hash(text), text, num_tokens))
        return res


def vectorize_file_to_csv(input, output):
    res = split_file_into_chunks(input)
    df = pd.DataFrame(res, columns=["title", "heading", "content", "tokens"])
    df.to_csv(output, index=False)
    return df


def embeddings_to_df(df: pd.DataFrame, file):
    embeddings = df["content"].apply(get_embedding).tolist()
    embedding_df = pd.DataFrame(embeddings, columns=[f"{i}" for i in range(len(embeddings[0]))])
    df = pd.concat([df, embedding_df], axis=1)
    del df['content']
    del df['tokens']
    df.to_csv(file, index=False)
    return df


if __name__ == '__main__':
    df = vectorize_file_to_csv("./data/elections/english/test.txt", "./data/embeddings/test.csv")
    query_vector = embeddings_to_df(df, "./data/embeddings/test-em.csv")
    print(query_vector.head(2))
