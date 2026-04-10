import os
import sys
import logging
from datetime import datetime
from chunking import ChunkingStrategyComparator

# Đường dẫn folder chứa data
folder_path = r"../data/pdf_parsed"
# Đường dẫn folder chứa log (tự động tạo nếu chưa có)
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

def setup_logging():
    """Thiết lập logging để vừa in ra console, vừa ghi ra file riêng theo thời gian."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = os.path.join(log_dir, f"analysis_{timestamp}.log")
    
    # Cấu hình logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(message)s',
        handlers=[
            logging.FileHandler(log_filename, encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return log_filename

def run_baseline_analysis():
    # Fix lỗi hiển thị ký tự đặc biệt trên terminal Windows
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
    
    log_file = setup_logging()
    logging.info(f"--- Analysis started at {datetime.now()} ---")
    logging.info(f"--- Log saved to: {log_file} ---\n")
    
    comparator = ChunkingStrategyComparator()
    
    if not os.path.exists(folder_path):
        logging.error(f"Error: Folder {folder_path} does not exist.")
        return

    documents = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    if not documents:
        logging.warning("No files found in the directory.")
        return

    logging.info("# Baseline Analysis: Chunking Strategy Comparison\n")
    
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
        
        results = comparator.compare(text, chunk_size=300)
        
        for strategy, data in results.items():
            logging.info(f"### Strategy: {strategy}")
            logging.info(f"- Number of chunks: {data['count']}")
            logging.info(f"- Average chunk length: {data['avg_length']:.2f}")
            logging.info("- Sample chunks (first 2):")
            for i, chunk in enumerate(data['chunks'][:2]):
                preview = chunk.replace('\n', ' ')[:100] + "..." if len(chunk) > 100 else chunk.replace('\n', ' ')
                logging.info(f"   {i+1}. {preview}")
            logging.info("") # Dòng trống
            
        logging.info("-" * 50 + "\n")

if __name__ == "__main__":
    run_baseline_analysis()