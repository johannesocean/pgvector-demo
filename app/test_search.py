from app.db.connect import create_db_connection

import os
from openai.embeddings_utils import get_embedding


if __name__ == '__main__':
    # This script is used to test the embedding model, and the
    # cosine similarity function within the database.

    text = "Did anyone adopt a cat this weekend?"
    embedding = get_embedding(text, os.getenv('EMBEDDING_MODEL'))

    connection = create_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(f"""
            SELECT 
                text, 
                1 - (embedding <=> '{embedding}') AS cosine_similarity
            FROM embeddings
            ORDER BY cosine_similarity desc
            LIMIT 3
        """)
        for r in cursor.fetchall():
            print(f"Text: {r[0]}; Similarity: {r[1]}")
    except Exception as error:
        print("Error..", error)
    finally:
        cursor.close()
        connection.close()
