from __future__ import annotations

import copy
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(r"C:\Users\28100\Desktop\夏祭")
DOCX_PATH = ROOT / "边缘(疝气必看）_删18X统一清稿.docx"
CHARACTER_MD_PATH = ROOT / "人物梳理_替换用.md"
NAME_REPORT_PATH = ROOT / "角色名替换说明.txt"

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML_NS = "http://www.w3.org/XML/1998/namespace"
NS = {"w": W_NS}
W = f"{{{W_NS}}}"

ET.register_namespace("w", W_NS)


ROUND2_REPLACEMENTS = [
    ("杨文明", "__TMP_YANGWENMING__"),
    ("肥皂", "__TMP_FEIZAO__"),
    ("止水", "__TMP_ZHISHUI__"),
    ("大如", "__TMP_DARU__"),
    ("阿表", "__TMP_ABIAO__"),
    ("__TMP_ZHISHUI__", "肥皂"),
    ("__TMP_DARU__", "杨文明"),
    ("__TMP_YANGWENMING__", "阿表"),
    ("__TMP_FEIZAO__", "止水"),
    ("__TMP_ABIAO__", "余晖"),
]


def replace_text(text: str) -> tuple[str, bool]:
    new_text = text
    for old, new in ROUND2_REPLACEMENTS:
        new_text = new_text.replace(old, new)
    return new_text, new_text != text


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


def update_docx(path: Path) -> int:
    with zipfile.ZipFile(path, "r") as zin:
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

        temp_path = path.with_suffix(".tmp")
        with zipfile.ZipFile(temp_path, "w", compression=zipfile.ZIP_DEFLATED) as zout:
            for info in zin.infolist():
                data = new_document_xml if info.filename == "word/document.xml" else zin.read(info.filename)
                zout.writestr(info, data)

    temp_path.replace(path)
    return changed


def update_text_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    new_text, _ = replace_text(text)
    path.write_text(new_text, encoding="utf-8")


def rewrite_report() -> None:
    lines = [
        "角色名替换已执行：",
        "",
        "第一轮：",
        "- 5H -> 小葵",
        "- 多力多滋 -> 别凑",
        "- 雪兔 / 晴天下雪兔 -> 杨文明",
        "- 原止水 -> 肥皂",
        "- 原肥皂 -> 止水",
        "- Elkie -> 阿表",
        "- 原别凑 / 别凑过来 -> 大如",
        "",
        "第二轮（按角色槽位重排）：",
        "- 帅气队长 -> 肥皂",
        "- 甜脸会长 -> 杨文明",
        "- 气氛组 -> 阿表",
        "- 配角 -> 止水",
        "- 原阿表角色 -> 余晖",
        "",
        "当前正文对应：",
        "- 小葵：原 5H 角色",
        "- 别凑：原 多力多滋 角色",
        "- 肥皂：队长位",
        "- 杨文明：会长位",
        "- 阿表：室友 / 气氛组位",
        "- 止水：学姐圈观察者 / 配角位",
        "- 余晖：原游戏好友位",
    ]
    NAME_REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    changed = update_docx(DOCX_PATH)
    update_text_file(CHARACTER_MD_PATH)
    rewrite_report()
    print(changed)


if __name__ == "__main__":
    main()
