import sys
from chunking import compute_similarity


def get_scores():
    # Fix lỗi hiển thị ký tự đặc biệt trên terminal
    if sys.stdout.encoding != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")

    # Khởi tạo Real Embedder bằng sentence-transformers
    try:
        from sentence_transformers import SentenceTransformer

        # Model này hỗ trợ đa ngôn ngữ (bao gồm tiếng Việt) rất tốt
        model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    except ImportError:
        print("Vui lòng cài đặt thư viện: pip install sentence-transformers")
        return

    pairs = [
        ("Hôm nay trời rất đẹp", "Thời tiết hôm nay thật tuyệt"),
        ("Tôi thích học lập trình Python", "Con mèo đang ngủ trên ghế"),
        (
            "Deep learning là một lĩnh vực của AI",
            "Học sâu là một nhánh của trí tuệ nhân tạo",
        ),
        ("Trái đất quay quanh mặt trời", "Mặt trăng là vệ tinh của Trái đất"),
        ("Cơm tấm rất ngon", "Phở bò là món ăn truyền thống"),
    ]

    print(f"{'Câu A':<40} | {'Câu B':<40} | {'Similarity'}")
    print("-" * 100)

    for a, b in pairs:
        # Encode câu thành vector (thực tế)
        # normalize_embeddings=True để tối ưu cho việc tính cosine similarity
        vec_a = model.encode(a, normalize_embeddings=True).tolist()
        vec_b = model.encode(b, normalize_embeddings=True).tolist()

        # Sử dụng hàm compute_similarity từ file chunking của bạn
        score = compute_similarity(vec_a, vec_b)

        print(f"'{a[:38]}...': '{b[:38]}...': {score:.4f}")


if __name__ == "__main__":
    get_scores()
