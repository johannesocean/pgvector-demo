from openai import OpenAI
from decouple import config

client = OpenAI(api_key=config("OPENAI_API_KEY"))


def get_embedding(text: str) -> list[float]:
    """Return embedding of text.

    Ref: https://platform.openai.com/docs/guides/embeddings
    """
    text = text.replace("\n", " ")
    response = client.embeddings.create(input=[text], model=config("EMBEDDING_MODEL"))
    return response.data[0].embedding


def get_embeddings(texts: list[str]) -> list[list[float]]:
    """Return embeddings of multiple texts.

    Ref: https://platform.openai.com/docs/guides/embeddings
    """
    texts = [text.replace("\n", " ") for text in texts]
    response = client.embeddings.create(input=texts, model=config("EMBEDDING_MODEL"))
    return [item.embedding for item in response.data]


if __name__ == '__main__':
    embedding_text = "Test text for embedding"
    embedding = get_embedding(embedding_text)
    print("single embedding")
    print(embedding)

    # test multiple texts
    embedding_texts = [
        "I like to eat broccoli and bananas.",
        "I ate a banana and spinach smoothie for breakfast.",
    ]
    embeddings = get_embeddings(embedding_texts)
    print("multiple embeddings")
    print(embeddings)
