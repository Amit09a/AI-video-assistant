from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

import os
import time
import httpx


def get_llm():
    return ChatMistralAI(
        model="mistral-small-latest",
        mistral_api_key=os.getenv("MISTRAL_AI_API_KEY"),
        temperature=0.3,
    )


def split_transcript(transcript: str) -> list:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=3000,
        chunk_overlap=200
    )
    return splitter.split_text(transcript)


def invoke_with_backoff(chain, input_data, max_attempts=6, base_delay=5, min_gap=1.2):
    """Invoke a chain with exponential backoff on 429s, plus a fixed
    minimum gap after every call (success or fail) to avoid tripping
    the rate limit again on the next call."""
    for attempt in range(max_attempts):
        try:
            result = chain.invoke(input_data)
            time.sleep(min_gap)  # breathing room before the next call
            return result
        except httpx.HTTPStatusError as e:
            print("Status:", e.response.status_code)
            print("Body:", e.response.text)
            print("Headers:", dict(e.response.headers))
        else:
            raise
        raise RuntimeError("Exceeded max retry attempts")


def summarize(transcript: str) -> str:
    llm = get_llm()

    map_prompt = ChatPromptTemplate.from_messages([
        ("system", "Summarize this portion of a meeting transcript concisely."),
        ("human", "{text}"),
    ])

    map_chain = map_prompt | llm | StrOutputParser()

    chunks = split_transcript(transcript)
    print(f"Summarizing {len(chunks)} chunk(s)...")

    chunk_summaries = [
        invoke_with_backoff(map_chain, {"text": chunk})
        for chunk in chunks
    ]

    combined = "\n\n".join(chunk_summaries)

    combined_prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are an expert meeting summarizer. Combine these partial summaries "
            "into one final professional meeting summary in bullet points.",
        ),
        ("human", "{text}"),
    ])

    combined_chain = (
        RunnablePassthrough() | RunnableLambda(lambda x: {"text": x}) | combined_prompt | llm | StrOutputParser()
    )

    return invoke_with_backoff(combined_chain, combined)


def generate_title(transcipt: str) -> str:
    llm = get_llm()

    title_chain = (
        RunnablePassthrough() | RunnableLambda(lambda x: {"text": x}) |
        ChatPromptTemplate.from_messages([
            (
                "system",
                "Based on the meeting transcript, generate a short professional meeting title "
                "(max 8 words). Only return the title, nothing else.",
            ),
            ("human", "{text}"),
        ])
        | llm
        | StrOutputParser()
    )

    return invoke_with_backoff(title_chain, transcipt[:500])