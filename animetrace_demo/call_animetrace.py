from pathlib import Path

import requests


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    base64_data = (base_dir / "image_base64.txt").read_text(encoding="utf-8")
    payload = {
        "is_multi": 1,
        "model": "animetrace_high_beta",
        "ai_detect": 1,
        "base64": base64_data,
    }
    response = requests.post(
        "https://api.animetrace.com/v1/search", json=payload, timeout=60
    )
    print("status:", response.status_code)
    (base_dir / "animetrace_response.json").write_text(response.text, encoding="utf-8")
    print("response saved to animetrace_response.json")


if __name__ == "__main__":
    main()
