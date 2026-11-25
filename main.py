import os
from pathlib import Path

LINE = "Quick update: nothing has changed since the invite, the reminder, and the pre-meeting we held to prepare for this meeting."


def main() -> None:
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    text = output_path.read_text(encoding="utf-8")
    assert 1 <= len(text) <= 200
    assert "\n" not in text
    assert "\r" not in text
    assert text.strip()


if __name__ == "__main__":
    main()
