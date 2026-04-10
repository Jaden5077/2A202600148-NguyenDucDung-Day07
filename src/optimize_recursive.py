import os
import logging
from datetime import datetime
from chunking import RecursiveChunker

# Cấu hình đường dẫn
data_path = r"./data/pdf_parsed"
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Danh sách các chunk_size cần test
CHUNK_SIZES_TO_TEST = [200, 300, 400, 500, 600, 800, 1000]


def setup_output_files():
    """Thiết lập file log và file markdown cho quá trình tối ưu."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Setup Log
    log_file = os.path.join(log_dir, f"optimization_{timestamp}.log")
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        handlers=[logging.FileHandler(log_file, encoding="utf-8")],
    )

    # Setup Markdown
    md_file = os.path.join(log_dir, f"optimization_report_{timestamp}.md")
    with open(md_file, "w", encoding="utf-8") as f:
        f.write("# Recursive Chunker Optimization Report\n\n")
        f.write("| Tài liệu | Chunk Size | Chunk Count | Avg Length | Efficiency |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- |\n")

    return log_file, md_file


def run_optimization():
    log_file, md_file = setup_output_files()
    logging.info(f"--- Optimization started at {datetime.now()} ---")

    if not os.path.exists(data_path):
        print(f"Error: Folder {data_path} not found.")
        return

    files = [
        f for f in os.listdir(data_path) if os.path.isfile(os.path.join(data_path, f))
    ]

    if not files:
        print("No data files found to test.")
        return

    for filename in files:
        file_full_path = os.path.join(data_path, filename)
        try:
            with open(file_full_path, "r", encoding="utf-8") as f:
                text = f.read()
        except Exception as e:
            logging.error(f"Failed to read {filename}: {e}")
            continue

        logging.info(f"Analyzing Document: {filename} (Total length: {len(text)})")

        for size in CHUNK_SIZES_TO_TEST:
            chunker = RecursiveChunker(chunk_size=size)
            chunks = chunker.chunk(text)

            count = len(chunks)
            avg_len = sum(len(c) for c in chunks) / count if count > 0 else 0

            # Tính toán độ hiệu quả (tỷ lệ giữa avg_length so với chunk_size mục tiêu)
            efficiency = (avg_len / size) * 100 if size > 0 else 0

            # Ghi Log chi tiết
            logging.info(
                f"  - Size {size}: {count} chunks, Avg: {avg_len:.2f}, Efficiency: {efficiency:.1f}%"
            )

            # Ghi vào bảng Markdown
            with open(md_file, "a", encoding="utf-8") as f:
                f.write(
                    f"| {filename} | {size} | {count} | {avg_len:.2f} | {efficiency:.1f}% |\n"
                )

        logging.info("-" * 30)

    print(f"Optimization complete!")
    print(f"Results saved to:\n- {log_file}\n- {md_file}")


if __name__ == "__main__":
    run_optimization()
