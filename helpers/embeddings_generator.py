import openai

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.redis import Redis


def similarity_search(query: str, rds: Redis) -> list[str]:
    results = rds.similarity_search_limit_score(query=query, k=4, score_threshold=0.2)
    if results:
        text_content = [result.page_content for result in results]
        return text_content


def generate_response(message: str = "", rds: Redis = None) -> str:
    if not message:
        return "Hello, I am NiftyBridge AI assistant. How can I help you?"

    text_chunks = similarity_search(message, rds)

    if text_chunks:
        chunks_set = set(text_chunks)

        response_message = (
                f"Answer on this message: `{message}`" + "\n\n"
                                                         "using only this info:" + "`" + "\n\n".join(chunks_set) + "`"
        )
        if len(response_message) <= 4096:
            prompt = response_message
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant which talks only about info related in user content."
                    },
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300,
                n=1,
                stop=None,
                temperature=0.7,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            if response.choices:
                return response.choices[0].message.content.strip()

        else:
            return (
                f"Your message with similar pieces is too long: {len(response_message)} symbols. "
                "Try to make your message shorter"
            )
    return (
        "I'm sorry, I don't have an answer to that. "
        "Please contact support at support@nifty-bridge.com."
    )


def generate_embeddings_from_chunks(
        text_chunks: list[str],
) -> tuple[Redis, list[str]]:
    embeddings = OpenAIEmbeddings()
    rds = Redis.from_texts_return_keys(
        texts=text_chunks,
        embedding=embeddings,
        redis_url="redis://localhost:6379",
        index_name="link"
    )

    return rds
