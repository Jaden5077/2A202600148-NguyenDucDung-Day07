# Báo Cáo Lab 7: Embedding & Vector Store

**Họ tên:** Nguyễn Đức Dũng
**Nhóm:** Nhóm 1
**Ngày:** 10/4/2026

---

## 1. Warm-up (5 điểm)

### Cosine Similarity (Ex 1.1)

**High cosine similarity nghĩa là gì?**

- Khi 2 vector có high cosine similarity, chúng tương đồng về hướng, và có nghĩa gần giống nhau.

**Ví dụ HIGH similarity:**

- Sentence A: "hôm nay trời nắng"
- Sentence B: "hôm nay trời quang"
- Tại sao tương đồng: Cả 2 câu đều nói về thời tiết đẹp, nắng, không mây.

**Ví dụ LOW similarity:**

- Sentence A: "hôm nay trời nắng"
- Sentence B: "hôm nay trời mưa"
- Tại sao khác: Cả 2 câu đều nói về thời tiết, nhưng một câu nói về trời nắng, một câu nói về trời mưa.

**Tại sao cosine similarity được ưu tiên hơn Euclidean distance cho text embeddings?**

- Cosine similarity phản ánh sự tương đồng về hướng của các vector, và hướng hướng của embedding phản ánh nghĩa của nó; còn Euclidean distance liên quan đến độ dài vector.

### Chunking Math (Ex 1.2)

**Document 10,000 ký tự, chunk_size=500, overlap=50. Bao nhiêu chunks?**

- Số chunk: (10000 - 50) / (500 - 50) = 22.11 => 23 chunks

**Nếu overlap tăng lên 100, chunk count thay đổi thế nào? Tại sao muốn overlap nhiều hơn?**

- Nếu overlap tăng lên 100, số chunk: (10000 - 100) / (500 - 100) = 24.75 => 25 chunks
- Tăng overlap làm tăng số chunk, nhưng mỗi chunk dài ra giúp kéo dài ngữ cảnh.

---

## 2. Document Selection — Nhóm (10 điểm)

### Domain & Lý Do Chọn

**Domain:** Các paper khoa học

**Tại sao nhóm chọn domain này?**

- Vì đây là domain có nhiều thuật ngữ chuyên ngành.
- Đồng thời cũng dễ kiếm, nhiều paper công khai miễn phí.

### Data Inventory

| #   | Tên tài liệu              | Nguồn                                   | Số ký tự (ước tính từ nguồn) | Metadata đã gán                                                                          |
| :-- | :------------------------ | :-------------------------------------- | :--------------------------- | :--------------------------------------------------------------------------------------- |
| 1   | Battiston et al. - 2020   | Bài đánh giá (Review) khoa học tổng hợp | ~110.000                     | `category`: Khoa học mạng (Network Science); `date`: 03/06/2020; `difficulty`: Khó       |
| 2   | Cai et al. - 2021         | Nature Communications                   | ~30.000                      | `category`: Thần kinh học (Neuroscience); `date`: 2021; `difficulty`: Trung bình - Khó   |
| 3   | Deng et al. - 2025        | IEEE Xplore                             | ~15.000                      | `category`: Học sâu (Deep Learning); `date`: 2025; `difficulty`: Trung bình - Khó        |
| 4   | Ji et al. - 2022          | Information Sciences                    | ~25.000                      | `category`: Đồ thị thông tin (Informatics); `date`: 2022; `difficulty`: Trung bình - Khó |
| 5   | Rubinov and Sporns - 2010 | NeuroImage                              | ~35.000                      | `category`: Kết nối não bộ (Brain connectivity); `date`: 2010; `difficulty`: Trung bình  |

### Metadata Schema

- Các field đã chọn: _Category_, _Date_, _Difficulty_

| Trường metadata | Kiểu   | Ví dụ giá trị                   | Tại sao hữu ích cho retrieval? |
| --------------- | ------ | ------------------------------- | ------------------------------ |
| Category        | String | Khoa học mạng (Network Science) | Giúp lọc theo lĩnh vực         |
| Date            | Number | 2020                            | Giúp lọc theo thời gian        |
| Difficulty      | String | Khó                             | Giúp lọc theo độ khó           |

---

## 3. Chunking Strategy — Cá nhân chọn, nhóm so sánh (15 điểm)

### Baseline Analysis

Chạy `ChunkingStrategyComparator().compare()` trên 2-3 tài liệu:

| Tài liệu | Strategy                         | Chunk Count | Avg Length | Preserves Context? |
| -------- | -------------------------------- | ----------- | ---------- | ------------------ |
|          | FixedSizeChunker (`fixed_size`)  |             |            |                    |
|          | SentenceChunker (`by_sentences`) |             |            |                    |
|          | RecursiveChunker (`recursive`)   |             |            |                    |

### Strategy Của Tôi

**Loại:** [FixedSizeChunker / SentenceChunker / RecursiveChunker / custom strategy]

**Mô tả cách hoạt động:**

> _Viết 3-4 câu: strategy chunk thế nào? Dựa trên dấu hiệu gì?_

**Tại sao tôi chọn strategy này cho domain nhóm?**

> _Viết 2-3 câu: domain có pattern gì mà strategy khai thác?_

**Code snippet (nếu custom):**

```python
# Paste implementation here
```

### So Sánh: Strategy của tôi vs Baseline

| Tài liệu | Strategy      | Chunk Count | Avg Length | Retrieval Quality? |
| -------- | ------------- | ----------- | ---------- | ------------------ |
|          | best baseline |             |            |                    |
|          | **của tôi**   |             |            |                    |

### So Sánh Với Thành Viên Khác

| Thành viên | Strategy | Retrieval Score (/10) | Điểm mạnh | Điểm yếu |
| ---------- | -------- | --------------------- | --------- | -------- |
| Tôi        |          |                       |           |          |
| [Tên]      |          |                       |           |          |
| [Tên]      |          |                       |           |          |

**Strategy nào tốt nhất cho domain này? Tại sao?**

> _Viết 2-3 câu:_

---

## 4. My Approach — Cá nhân (10 điểm)

Giải thích cách tiếp cận của bạn khi implement các phần chính trong package `src`.

### Chunking Functions

**`SentenceChunker.chunk`** — approach:

> _Viết 2-3 câu: dùng regex gì để detect sentence? Xử lý edge case nào?_

**`RecursiveChunker.chunk` / `_split`** — approach:

> _Viết 2-3 câu: algorithm hoạt động thế nào? Base case là gì?_

### EmbeddingStore

**`add_documents` + `search`** — approach:

> _Viết 2-3 câu: lưu trữ thế nào? Tính similarity ra sao?_

**`search_with_filter` + `delete_document`** — approach:

> _Viết 2-3 câu: filter trước hay sau? Delete bằng cách nào?_

### KnowledgeBaseAgent

**`answer`** — approach:

> _Viết 2-3 câu: prompt structure? Cách inject context?_

### Test Results

```
# Paste output of: pytest tests/ -v
```

**Số tests pass:** ** / **

---

## 5. Similarity Predictions — Cá nhân (5 điểm)

| Pair | Sentence A | Sentence B | Dự đoán    | Actual Score | Đúng? |
| ---- | ---------- | ---------- | ---------- | ------------ | ----- |
| 1    |            |            | high / low |              |       |
| 2    |            |            | high / low |              |       |
| 3    |            |            | high / low |              |       |
| 4    |            |            | high / low |              |       |
| 5    |            |            | high / low |              |       |

**Kết quả nào bất ngờ nhất? Điều này nói gì về cách embeddings biểu diễn nghĩa?**

> _Viết 2-3 câu:_

---

## 6. Results — Cá nhân (10 điểm)

Chạy 5 benchmark queries của nhóm trên implementation cá nhân của bạn trong package `src`. **5 queries phải trùng với các thành viên cùng nhóm.**

### Benchmark Queries & Gold Answers (nhóm thống nhất)

| #   | Query | Gold Answer |
| --- | ----- | ----------- |
| 1   |       |             |
| 2   |       |             |
| 3   |       |             |
| 4   |       |             |
| 5   |       |             |

### Kết Quả Của Tôi

| #   | Query | Top-1 Retrieved Chunk (tóm tắt) | Score | Relevant? | Agent Answer (tóm tắt) |
| --- | ----- | ------------------------------- | ----- | --------- | ---------------------- |
| 1   |       |                                 |       |           |                        |
| 2   |       |                                 |       |           |                        |
| 3   |       |                                 |       |           |                        |
| 4   |       |                                 |       |           |                        |
| 5   |       |                                 |       |           |                        |

**Bao nhiêu queries trả về chunk relevant trong top-3?** \_\_ / 5

---

## 7. What I Learned (5 điểm — Demo)

**Điều hay nhất tôi học được từ thành viên khác trong nhóm:**

> _Viết 2-3 câu:_

**Điều hay nhất tôi học được từ nhóm khác (qua demo):**

> _Viết 2-3 câu:_

**Nếu làm lại, tôi sẽ thay đổi gì trong data strategy?**

> _Viết 2-3 câu:_

---

## Tự Đánh Giá

| Tiêu chí                    | Loại    | Điểm tự đánh giá |
| --------------------------- | ------- | ---------------- |
| Warm-up                     | Cá nhân | / 5              |
| Document selection          | Nhóm    | / 10             |
| Chunking strategy           | Nhóm    | / 15             |
| My approach                 | Cá nhân | / 10             |
| Similarity predictions      | Cá nhân | / 5              |
| Results                     | Cá nhân | / 10             |
| Core implementation (tests) | Cá nhân | / 30             |
| Demo                        | Nhóm    | / 5              |
| **Tổng**                    |         | **/ 100**        |
