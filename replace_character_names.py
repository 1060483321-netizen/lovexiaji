from __future__ import annotations

import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(r"C:\Users\28100\Desktop\夏祭")
DOCX_PATH = ROOT / "边缘(疝气必看）_删18X统一清稿.docx"
REPORT_PATH = ROOT / "边缘(疝气必看）_删18X统一清稿_修改说明.txt"
CHARACTER_MD_PATH = ROOT / "人物梳理_替换用.md"
NAME_REPORT_PATH = ROOT / "角色名替换说明.txt"

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W_NS}


REPLACEMENTS = [
    ("别凑过来", "__TMP_NAYEON_FULL__"),
    ("别凑", "__TMP_NAYEON_SHORT__"),
    ("晴天下雪兔", "__TMP_SNOW_FULL__"),
    ("雪兔", "__TMP_SNOW_SHORT__"),
    ("5H", "__TMP_FIVEH__"),
    ("多力多滋", "__TMP_CHAEYOUNG__"),
    ("止水", "__TMP_STOPWATER__"),
    ("肥皂", "__TMP_SOAP__"),
    ("Elkie", "__TMP_ELKIE__"),
    ("__TMP_FIVEH__", "小葵"),
    ("__TMP_CHAEYOUNG__", "别凑"),
    ("__TMP_SNOW_FULL__", "杨文明"),
    ("__TMP_SNOW_SHORT__", "杨文明"),
    ("__TMP_STOPWATER__", "肥皂"),
    ("__TMP_SOAP__", "止水"),
    ("__TMP_ELKIE__", "阿表"),
    ("__TMP_NAYEON_FULL__", "大如"),
    ("__TMP_NAYEON_SHORT__", "大如"),
]


def replace_in_text(text: str) -> str:
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    return text


def update_docx(path: Path) -> None:
    with zipfile.ZipFile(path, "r") as zin:
        document_xml = zin.read("word/document.xml")
        root = ET.fromstring(document_xml)
        for node in root.findall(".//w:t", NS):
            if node.text:
                node.text = replace_in_text(node.text)
        new_document_xml = ET.tostring(root, encoding="utf-8", xml_declaration=True)

        temp_path = path.with_suffix(".tmp")
        with zipfile.ZipFile(temp_path, "w", compression=zipfile.ZIP_DEFLATED) as zout:
            for info in zin.infolist():
                data = new_document_xml if info.filename == "word/document.xml" else zin.read(info.filename)
                zout.writestr(info, data)

    temp_path.replace(path)


def update_text_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    path.write_text(replace_in_text(text), encoding="utf-8")


def write_report() -> None:
    lines = [
        "角色名替换已执行：",
        "",
        "- 5H -> 小葵",
        "- 多力多滋 -> 别凑",
        "- 雪兔 / 晴天下雪兔 -> 杨文明",
        "- 原止水 -> 肥皂",
        "- 原肥皂 -> 止水",
        "- Elkie -> 阿表",
        "- 原别凑 / 别凑过来 -> 大如",
        "",
        "说明：",
        "- 本次采用临时占位替换，已避免“止水/肥皂”与“别凑/大如”互相覆盖。",
        "- 已同步更新清稿版 docx、人物梳理文件、修改说明文件中的角色名。",
    ]
    NAME_REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    update_docx(DOCX_PATH)
    update_text_file(REPORT_PATH)
    update_text_file(CHARACTER_MD_PATH)
    write_report()


if __name__ == "__main__":
    main()
