from __future__ import annotations

import copy
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(r"C:\Users\28100\Desktop\夏祭")
DOCX_PATH = ROOT / "边缘(疝气必看）_删18X统一清稿.docx"

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML_NS = "http://www.w3.org/XML/1998/namespace"
NS = {"w": W_NS}
W = f"{{{W_NS}}}"

ET.register_namespace("w", W_NS)


PARAGRAPH_REPLACEMENTS = [
    ("别凑过来", "大如"),
    ("晴天下雪兔", "杨文明"),
    ("雪兔", "杨文明"),
    ("5H同学", "小葵同学"),
    ("5H学姐", "小葵学姐"),
    ("5H", "小葵"),
    ("多力多滋", "别凑"),
    ("多多", "别凑"),
    ("Elkie", "阿表"),
]


def paragraph_text(paragraph: ET.Element) -> str:
    return "".join(node.text or "" for node in paragraph.findall(".//w:t", NS)).strip()


def rebuild_paragraph_text(paragraph: ET.Element, text: str) -> None:
    ppr = paragraph.find("w:pPr", NS)
    keep = copy.deepcopy(ppr) if ppr is not None else None
    paragraph.clear()
    if keep is not None:
        paragraph.append(keep)
    run = ET.SubElement(paragraph, f"{W}r")
    t = ET.SubElement(run, f"{W}t")
    t.set(f"{{{XML_NS}}}space", "preserve")
    t.text = text


def replace_text(text: str) -> tuple[str, bool]:
    new_text = text
    for old, new in PARAGRAPH_REPLACEMENTS:
        new_text = new_text.replace(old, new)
    return new_text, new_text != text


def main() -> None:
    with zipfile.ZipFile(DOCX_PATH, "r") as zin:
        root = ET.fromstring(zin.read("word/document.xml"))
        changed = 0
        for paragraph in root.findall(".//w:p", NS):
            text = paragraph_text(paragraph)
            if not text:
                continue
            new_text, did_change = replace_text(text)
            if did_change:
                rebuild_paragraph_text(paragraph, new_text)
                changed += 1
        new_document_xml = ET.tostring(root, encoding="utf-8", xml_declaration=True)

        temp_path = DOCX_PATH.with_suffix(".tmp")
        with zipfile.ZipFile(temp_path, "w", compression=zipfile.ZIP_DEFLATED) as zout:
            for info in zin.infolist():
                data = new_document_xml if info.filename == "word/document.xml" else zin.read(info.filename)
                zout.writestr(info, data)

    temp_path.replace(DOCX_PATH)
    print(changed)


if __name__ == "__main__":
    main()
