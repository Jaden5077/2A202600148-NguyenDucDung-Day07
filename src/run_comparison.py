import os
import sys
import logging
from datetime import datetime
from chunking import ChunkingStrategyComparator

# Đường dẫn folder chứa data
folder_path = r"./data/pdf_parsed"
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)


def setup_files():
    """Thiết lập logging vào file và khởi tạo file Markdown."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 1. Thiết lập Log file (.log) - Chỉ dùng FileHandler
    log_filename = os.path.join(log_dir, f"analysis_{timestamp}.log")

    # Reset logging manager để tránh trùng lặp handler nếu chạy nhiều lần
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        handlers=[logging.FileHandler(log_filename, encoding="utf-8")],
    )

    # 2. Thiết lập Markdown file (.md)
    md_filename = os.path.join(log_dir, f"report_{timestamp}.md")
    with open(md_filename, "w", encoding="utf-8") as f:
        f.write("# Chunking Strategy Analysis Report\n\n")
        f.write(
            "| Tài liệu | Strategy | Chunk Count | Avg Length | Preserves Context? |\n"
        )
        f.write("| :--- | :--- | :--- | :--- | :--- |\n")

    return log_filename, md_filename


def run_baseline_analysis():
    log_file, md_file = setup_files()

    # Ghi nhận thời gian bắt đầu vào file log
    logging.info(f"--- Analysis started at {datetime.now()} ---")

    comparator = ChunkingStrategyComparator()

    if not os.path.exists(folder_path):
        logging.error(f"Error: Folder {folder_path} does not exist.")
        return

    documents = [
        f
        for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]

    if not documents:
        logging.warning("No files found in the directory.")
        return

    for doc_name in documents:
        file_path = os.path.join(folder_path, doc_name)

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
        except Exception as e:
            logging.error(f"Error reading {doc_name}: {e}")
            continue

        logging.info(f"## Document: {doc_name}")
        logging.info(f"Total length: {len(text)} characters\n")

        # Giả sử comparator.compare trả về một dict các strategy
        results = comparator.compare(text, chunk_size=300)

        for strategy, data in results.items():
            # 1. Ghi chi tiết vào file Log
            logging.info(f"### Strategy: {strategy}")
            logging.info(f"- Number of chunks: {data['count']}")
            logging.info(f"- Average chunk length: {data['avg_length']:.2f}")
            logging.info("- Sample chunks (10th and 11th):")
            for i, chunk in enumerate(data["chunks"][10:12]):
                preview = (
                    chunk.replace("\n", " ")[:100] + "..."
                    if len(chunk) > 100
                    else chunk.replace("\n", " ")
                )
                logging.info(f"   {i+1}. {preview}")
            logging.info("")

            # 2. Ghi dòng dữ liệu vào file Markdown
            # Logic xác định Preserves Context (có thể thay đổi tùy logic của bạn)
            preserves_context = (
                "Yes"
                if any(x in strategy.lower() for x in ["semantic", "recursive"])
                else "No"
            )

            with open(md_file, "a", encoding="utf-8") as f:
                f.write(
                    f"| {doc_name} | {strategy} | {data['count']} | {data['avg_length']:.2f} | {preserves_context} |\n"
                )

        logging.info("-" * 50 + "\n")

    # Thông báo hoàn tất duy nhất ra terminal (tùy chọn)
    print(f"Done! Log: {log_file}")
    print(f"Done! Report: {md_file}")


if __name__ == "__main__":
    run_baseline_analysis()
