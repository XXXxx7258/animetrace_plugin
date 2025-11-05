from html.parser import HTMLParser
from pathlib import Path


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.chunks: list[str] = []

    def handle_data(self, data: str) -> None:
        data = data.strip()
        if data:
            self.chunks.append(data)


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    html = (base_dir / "en_api_docs.html").read_text(encoding="utf-8")
    parser = TextExtractor()
    parser.feed(html)
    text = "\n".join(parser.chunks)
    (base_dir / "en_api_docs.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
