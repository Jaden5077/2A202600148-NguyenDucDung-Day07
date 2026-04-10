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
- Dữ liệu parse từ pdf, có vẻ khó chunking, nên có thể dùng để so sánh các strategy khác nhau.

### Data Inventory

| #   | Tên tài liệu              | Nguồn                    | Số ký tự (ước tính từ nguồn) | Metadata đã gán                                                                          |
| :-- | :------------------------ | :----------------------- | :--------------------------- | :--------------------------------------------------------------------------------------- |
| 1   | Battiston et al. - 2020   | Review khoa học tổng hợp | 537.821                      | `category`: Khoa học mạng (Network Science); `date`: 03/06/2020; `difficulty`: Khó       |
| 2   | Cai et al. - 2021         | Nature Communications    | 105.297                      | `category`: Thần kinh học (Neuroscience); `date`: 2021; `difficulty`: Trung bình - Khó   |
| 3   | Deng et al. - 2025        | IEEE Xplore              | 32.770                       | `category`: Học sâu (Deep Learning); `date`: 2025; `difficulty`: Trung bình - Khó        |
| 4   | Ji et al. - 2022          | Information Sciences     | 70.524                       | `category`: Đồ thị thông tin (Informatics); `date`: 2022; `difficulty`: Trung bình - Khó |
| 5   | Rubinov and Sporns - 2010 | NeuroImage               | 51.559                       | `category`: Kết nối não bộ (Brain connectivity); `date`: 2010; `difficulty`: Trung bình  |

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

**chunk_size=300**
Các file log:

- logs\report_20260410_224907.md
- logs\analysis_20260410_224907.log

| Tài liệu                    | Strategy     | Chunk Count | Avg Length | Preserves Context?                             |
| :-------------------------- | :----------- | :---------- | :--------- | :--------------------------------------------- |
| **Battiston et al. (2020)** | fixed_size   | 1921        | 299.96     | Thường cắt ngang từ/câu                        |
|                             | by_sentences | 1800        | 297.10     | Mất ngữ cảnh đoạn.                             |
|                             | recursive    | 2572        | 209.11     | Ổn hơn, giữ được cấu trúc đoạn văn và tiêu đề. |
| **Cai et al. (2021)**       | fixed_size   | 376         | 299.99     | Như trên                                       |
|                             | by_sentences | 470         | 222.74     | Như trên                                       |
|                             | recursive    | 466         | 225.96     | Như trên                                       |

### Strategy Của Tôi

**Loại:** recursive

**Mô tả cách hoạt động:**

- Chia nhỏ văn bản một cách đệ quy dựa trên một danh sách các dấu phân tách ưu tiên: `["\n\n", "\n", ". ", " ", ""]`.
- Đầu tiên,cố chia theo đoạn văn (`\n\n`), sau đó là xuống dòng (`\n`), rồi đến câu (`. `).
- Nếu vượt quá `chunk_size`, nó sẽ tìm dấu phân tách tiếp theo trong danh sách để chia nhỏ, cho đến khi đạt kích thước mục tiêu.

**Tại sao tôi chọn strategy này cho domain nhóm?**

- Vì các paper có cấu trúc phân tầng.
- Recursive có logic chunking ổn hơn so với 2 strategy còn lại.

**Code snippet (nếu custom):**

```python
# Paste implementation here
```

**chunk_size=500**
Các file log:

- analysis_20260410_230553.log
- report_20260410_230553.md

| Tài liệu                | Strategy     | Chunk Count | Avg Length |
| :---------------------- | :----------- | :---------- | :--------- |
| Battiston et al. - 2020 | fixed_size   | 1121        | 499.75     |
| Battiston et al. - 2020 | by_sentences | 1800        | 297.10     |
| Battiston et al. - 2020 | recursive    | 1448        | 371.42     |
| Cai et al. - 2021       | fixed_size   | 220         | 498.53     |
| Cai et al. - 2021       | by_sentences | 470         | 222.74     |
| Cai et al. - 2021       | recursive    | 280         | 376.06     |

### So Sánh: Strategy của tôi vs Baseline

| Tài liệu             | Strategy (chunk size) | Chunk Count | Avg Length | Nhận xét chất lượng                                                              |
| :------------------- | :-------------------- | :---------- | :--------- | :------------------------------------------------------------------------------- |
| **Battiston et al.** | **Recursive (500)**   | 1448        | 371.42     | **Tối ưu nhất:** Giữ nguyên cấu trúc đoạn văn khoa học, đủ ngữ cảnh để LLM hiểu. |
|                      | Fixed Size (500)      | 1121        | 499.75     | Dễ cắt đôi công thức hoặc tên tác giả ở giữa câu.                                |
|                      | Recursive (300)       | 2572        | 209.11     | Khá vụn, nhưng vẫn giữ được tiêu đề và các mục liệt kê.                          |
|                      | Fixed Size (300)      | 1921        | 299.96     | Hiệu suất lấp đầy cao nhưng nội dung bị ngắt quãng vô tội vạ.                    |
| **Cai et al.**       | **Recursive (500)**   | 280         | 376.06     | **Tốt:** Cân bằng giữa số lượng mảnh và độ dài thông tin mỗi mảnh.               |
|                      | Fixed Size (500)      | 220         | 498.53     | Số mảnh ít nhất nhưng rủi ro mất ngữ cảnh tại điểm cắt là cao nhất.              |
|                      | Recursive (300)       | 466         | 225.96     | Chi tiết, phù hợp nếu bài báo có nhiều phân đoạn nhỏ.                            |
|                      | Fixed Size (300)      | 376         | 299.99     | Cắt cứng 300 ký tự, thường xuyên ngắt giữa câu.                                  |

### So Sánh Với Thành Viên Khác

| Thành viên           | Strategy                   | Retrieval Score (/10) | Điểm mạnh                       | Điểm yếu                    |
| :------------------- | :------------------------- | :-------------------- | :------------------------------ | :-------------------------- |
| Huỳnh Thái Bảo       | Baseline (Fixed + Overlap) | 5.0                   | Nhanh, phủ hết text             | Cắt ngang câu/từ, nhiễu cao |
| Trương Minh Tiền     | Sentence-based             | 8.5                   | Giữ câu trọn vẹn                | Độ dài không đồng đều       |
| Nguyễn Đức Dũng      | Recursive                  | 7.5                   | Giữ ngữ cảnh                    | Vẫn cắt ý                   |
| Phạm Đoàn Phương Anh | Semantic                   | 9.0                   | Ý nghĩa thống nhất              | Tốn tài nguyên tính toán    |
| Nguyễn Đức Trí       | Recursive                  | 8.0                   | Cân bằng ngữ cảnh và kích thước | Cần tinh chỉnh separators   |

**Strategy nào tốt nhất cho domain này? Tại sao?**

> _Viết 2-3 câu:_

- Có vẻ như là Semantic Chunking, vì nó giữ đúng cấu trúc paper.

---

## 4. My Approach — Cá nhân (10 điểm)

Giải thích cách tiếp cận của bạn khi implement các phần chính trong package `src`.

### Chunking Functions

**`SentenceChunker.chunk`** — approach:

Dùng regex `(?<=[.!?])\s+` để tách câu dựa trên các dấu kết thúc câu phổ biến. Sau khi tách, các câu được gom nhóm lại thành từng chunk sao cho số lượng câu không vượt quá `max_sentences_per_chunk`. Điều này giúp đảm bảo ngữ cảnh được giữ trọn vẹn trong các ranh giới câu tự nhiên.

**`RecursiveChunker.chunk` / `_split`** — approach:

Sử dụng thuật toán split đệ quy với danh sách separator ưu tiên `["\n\n", "\n", ". ", " ", ""]`. Nếu một đoạn văn vượt quá `chunk_size`, nó sẽ tìm separator cao nhất hiện có để chia nhỏ. Nếu không còn separator nào thì mới ép buộc cắt theo độ dài (force cut). Base case là khi độ dài văn bản nhỏ hơn hoặc bằng `chunk_size`.

### EmbeddingStore

**`add_documents` + `search`** — approach:

Sử dụng ChromaDB làm backend chính để lưu trữ và truy vấn vector. Trong trường hợp không có ChromaDB, hệ thống tự động fallback về in-memory store dùng danh sách Python. Việc tìm kiếm được thực hiện bằng cách tính `dot product` giữa vector truy vấn và toàn bộ vector trong store (đối với bản in-memory).

**`search_with_filter` + `delete_document`** — approach:

Hỗ trợ pre-filtering dựa trên metadata. Đối với in-memory store, hệ thống duyệt qua toàn bộ record để lọc theo metadata trước khi tính similarity. `delete_document` sẽ xóa toàn bộ các chunks có chứa `doc_id` tương ứng trong metadata của chúng.

### KnowledgeBaseAgent

**`answer`** — approach:

Agent triển khai pattern RAG chuẩn: nhận câu hỏi -> search `top_k` chunks liên quan từ `EmbeddingStore` -> xây dựng prompt bằng cách chèn các chunks này vào phần `Context` -> gọi LLM để tổng hợp câu trả lời dựa trên context đó.

### Test Results

```
# Paste output of: pytest tests/ -v
```

---> test_results.log

**Số tests pass:** 42 passed in 0.11s

---

## 5. Similarity Predictions — Cá nhân (5 điểm)

| Pair | Sentence A                           | Sentence B                                | Dự đoán              | Actual Score (MockEmbedder) | Đúng? |
| ---- | ------------------------------------ | ----------------------------------------- | -------------------- | --------------------------- | ----- |
| 1    | Hôm nay trời rất đẹp                 | Thời tiết hôm nay thật tuyệt              | High                 | -0.1177                     | Sai   |
| 2    | Tôi thích học lập trình Python       | Con mèo đang ngủ trên ghế                 | Low                  | 0.1352                      | Đúng  |
| 3    | Deep learning là một lĩnh vực của AI | Học sâu là một nhánh của trí tuệ nhân tạo | High (Dịch)          | 0.0455                      | Sai   |
| 4    | Trái đất quay quanh mặt trời         | Mặt trăng là vệ tinh của Trái đất         | Low (Cùng chủ đề)    | -0.0039                     | Đúng  |
| 5    | Cơm tấm rất ngon                     | Phở bò là món ăn truyền thống             | Medium (Cùng chủ đề) | -0.1810                     | Sai   |

**Kết quả nào bất ngờ nhất? Điều này nói gì về cách embeddings biểu diễn nghĩa?**

Kết quả pair 1 và 3 là bất ngờ nhất. Nguyên nhân hẳn là do sử dụng `MockEmbedder` tạo vector ngẫu nhiên cố định, nó không hiểu ngữ nghĩa. Vì vậy tốt hơn là ta cần một model llm thực sự.

Sau khi dùng _sentence_transformers_:

| Pair | Sentence A                           | Sentence B                                | Dự đoán              | Actual Score (Embedding) | Đúng? |
| :--- | :----------------------------------- | :---------------------------------------- | :------------------- | :----------------------- | ----- |
| 1    | Hôm nay trời rất đẹp                 | Thời tiết hôm nay thật tuyệt              | High                 | 0.8171                   | Đúng  |
| 2    | Tôi thích học lập trình Python       | Con mèo đang ngủ trên ghế                 | Low                  | 0.1020                   | Đúng  |
| 3    | Deep learning là một lĩnh vực của AI | Học sâu là một nhánh của trí tuệ nhân tạo | High (Dịch)          | 0.8452                   | Đúng  |
| 4    | Trái đất quay quanh mặt trời         | Mặt trăng là vệ tinh của Trái đất         | Low (Cùng chủ đề)    | 0.4737                   | Đúng  |
| 5    | Cơm tấm rất ngon                     | Phở bò là món ăn truyền thống             | Medium (Cùng chủ đề) | 0.5561                   | Đúng  |

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

- Chunking phụ thuộc vào tài liệu
- Chunking có thể rất phức tạp

**Điều hay nhất tôi học được từ nhóm khác (qua demo):**

- Có nhiều kỹ thuật Chunking tiên tiến (nhưng cũng phức tạp)

**Nếu làm lại, tôi sẽ thay đổi gì trong data strategy?**

- Tìm hiểu các kỹ thuật tinh vi hơn

---

## Tự Đánh Giá

| Tiêu chí                    | Loại    | Điểm tự đánh giá |
| --------------------------- | ------- | ---------------- |
| Warm-up                     | Cá nhân | 5/ 5             |
| Document selection          | Nhóm    | 10/ 10           |
| Chunking strategy           | Nhóm    | 10/ 15           |
| My approach                 | Cá nhân | 10/ 10           |
| Similarity predictions      | Cá nhân | 5/ 5             |
| Results                     | Cá nhân | 10/ 10           |
| Core implementation (tests) | Cá nhân | 30/ 30           |
| Demo                        | Nhóm    | / 5              |
| **Tổng**                    |         | 80/ 100          |
