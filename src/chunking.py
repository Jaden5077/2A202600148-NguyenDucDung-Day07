from __future__ import annotations

import math
import re


class FixedSizeChunker:
    """
    Split text into fixed-size chunks with optional overlap.

    Rules:
        - Each chunk is at most chunk_size characters long.
        - Consecutive chunks share overlap characters.
        - The last chunk contains whatever remains.
        - If text is shorter than chunk_size, return [text].
    """

    def __init__(self, chunk_size: int = 500, overlap: int = 50) -> None:
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, text: str) -> list[str]:
        if not text:
            return []
        if len(text) <= self.chunk_size:
            return [text]

        step = self.chunk_size - self.overlap
        chunks: list[str] = []
        for start in range(0, len(text), step):
            chunk = text[start : start + self.chunk_size]
            chunks.append(chunk)
            if start + self.chunk_size >= len(text):
                break
        return chunks


class SentenceChunker:
    """
    Split text into chunks of at most max_sentences_per_chunk sentences.

    Sentence detection: split on ". ", "! ", "? " or ".\n".
    Strip extra whitespace from each chunk.
    """

    def __init__(self, max_sentences_per_chunk: int = 3) -> None:
        self.max_sentences_per_chunk = max(1, max_sentences_per_chunk)

    def chunk(self, text: str) -> list[str]:
        if not text:
            return []
        
        # Split into sentences using markers: ". ", "! ", "? ", or ".\n"
        sentences = re.split(r'(?<=[.!?])\s+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        chunks: list[str] = []
        for i in range(0, len(sentences), self.max_sentences_per_chunk):
            chunk_sentences = sentences[i : i + self.max_sentences_per_chunk]
            chunks.append(" ".join(chunk_sentences))
        
        return chunks


class RecursiveChunker:
    """
    Recursively split text using separators in priority order.

    Default separator priority:
        ["\n\n", "\n", ". ", " ", ""]
    """

    DEFAULT_SEPARATORS = ["\n\n", "\n", ". ", " ", ""]

    def __init__(self, separators: list[str] | None = None, chunk_size: int = 500) -> None:
        self.separators = self.DEFAULT_SEPARATORS if separators is None else list(separators)
        self.chunk_size = chunk_size

    def chunk(self, text: str) -> list[str]:
        return self._split(text, self.separators)

    def _split(self, current_text: str, remaining_separators: list[str]) -> list[str]:
        if not current_text:
            return []
            
        if len(current_text) <= self.chunk_size:
            return [current_text]

        if not remaining_separators:
            # If no more separators, just force cut
            return [current_text[i : i + self.chunk_size] for i in range(0, len(current_text), self.chunk_size)]

        separator = remaining_separators[0]
        next_separators = remaining_separators[1:]

        # Split current text by the first separator
        if separator == "":
            # Character-level split
            parts = list(current_text)
        else:
            parts = current_text.split(separator)

        final_chunks = []
        current_buffer = []
        current_len = 0

        for i, part in enumerate(parts):
            # Re-add separator except for the last part
            if i < len(parts) - 1:
                part_with_sep = part + separator
            else:
                part_with_sep = part

            if len(part_with_sep) > self.chunk_size:
                # If a single part is too big, recurse on it
                if current_buffer:
                    final_chunks.append("".join(current_buffer))
                    current_buffer = []
                    current_len = 0
                
                res = self._split(part_with_sep, next_separators)
                final_chunks.extend(res)
            elif current_len + len(part_with_sep) <= self.chunk_size:
                current_buffer.append(part_with_sep)
                current_len += len(part_with_sep)
            else:
                if current_buffer:
                    final_chunks.append("".join(current_buffer))
                current_buffer = [part_with_sep]
                current_len = len(part_with_sep)

        if current_buffer:
            final_chunks.append("".join(current_buffer))

        return [c for c in final_chunks if c]


def _dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def compute_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    """
    Compute cosine similarity between two vectors.

    cosine_similarity = dot(a, b) / (||a|| * ||b||)

    Returns 0.0 if either vector has zero magnitude.
    """
    dot_prod = _dot(vec_a, vec_b)
    mag_a = math.sqrt(sum(x * x for x in vec_a))
    mag_b = math.sqrt(sum(x * x for x in vec_b))
    
    if mag_a == 0 or mag_b == 0:
        return 0.0
        
    return dot_prod / (mag_a * mag_b)


class ChunkingStrategyComparator:
    """Run all built-in chunking strategies and compare their results."""

    def compare(self, text: str, chunk_size: int = 200) -> dict:
        results = {}
        
        strategies = {
            "fixed_size": FixedSizeChunker(chunk_size=chunk_size, overlap=20),
            "by_sentences": SentenceChunker(max_sentences_per_chunk=3),
            "recursive": RecursiveChunker(chunk_size=chunk_size)
        }
        
        for name, chunker in strategies.items():
            chunks = chunker.chunk(text)
            num_chunks = len(chunks)
            avg_len = sum(len(c) for c in chunks) / num_chunks if num_chunks > 0 else 0
            results[name] = {
                "count": num_chunks,
                "avg_length": avg_len,
                "chunks": chunks
            }
            
        return results


