import json
import re
from pathlib import Path


def extract_strings(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(r'"([^"\\n]{4,})"')
    return [match.group(1) for match in pattern.finditer(text)]


def filter_strings(strings: list[str]) -> list[str]:
    keywords = [
        "api",
        "anime",
        "post",
        "token",
        "https",
        "识别",
        "模型",
        "key",
        "请求",
        "响应",
        "header",
        "body",
        "参数",
        "接口",
        "调用",
        "上传",
    ]
    filtered = []
    for s in strings:
        lower = s.lower()
        if any(keyword in lower for keyword in keywords):
            filtered.append(s)
    return filtered


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    path = base_dir / "api_docs_chunk.js"
    strings = extract_strings(path)
    filtered = filter_strings(strings)
    (base_dir / "api_docs_strings.json").write_text(
        json.dumps(filtered, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
