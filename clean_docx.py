from __future__ import annotations

import copy
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(r"C:\Users\28100\Desktop\夏祭")
SOURCE = ROOT / "边缘(疝气必看）_.docx"
DEST = ROOT / "边缘(疝气必看）_删18X统一清稿.docx"
REPORT = ROOT / "边缘(疝气必看）_删18X统一清稿_修改说明.txt"

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML_NS = "http://www.w3.org/XML/1998/namespace"
NS = {"w": W_NS}
W = f"{{{W_NS}}}"

ET.register_namespace("w", W_NS)


REPLACEMENTS = [
    {
        "start": 1323,
        "end": 1358,
        "summary": "【已删改：原文此处含成人描写。现保留为剧情结果：两人在醉酒和情绪推动下越界亲近，关系发生了实质变化。次日两人都因此产生了强烈而复杂的心理波动。请复核前后衔接。】",
    },
    {
        "start": 2085,
        "end": 2096,
        "summary": "【已删改：原文此处含成人描写。现保留为剧情结果：两人在办公室里短暂越界亲近，并因外部打断而仓促停下。请复核前后衔接。】",
    },
    {
        "start": 3620,
        "end": 3676,
        "summary": "【已删改：原文此处含成人描写。现保留为剧情结果：两人在重逢后的情绪决堤中确认了更深的亲密关系，并于当晚发生了实质性进展。后文人物态度与情感变化均承接此结果。请复核前后衔接。】",
    },
    {
        "start": 4658,
        "end": 4689,
        "summary": "【已删改：原文此处含成人描写。现保留为剧情结果：两人在独处时再次发生亲密接触，感情由此进一步加深。请复核前后衔接。】",
    },
    {
        "start": 5098,
        "end": 5105,
        "summary": "【已删改：原文此处含成人描写。现保留为剧情结果：两人在夜色与酒意中再度越界亲近，关系持续升温。请复核前后衔接。】",
    },
    {
        "start": 5967,
        "end": 5996,
        "summary": "【已删改：原文此处含成人描写。现保留为剧情结果：两人在私下独处时发生了较深的亲密接触。请复核前后衔接。】",
    },
    {
        "start": 8702,
        "end": 8750,
        "summary": "【存疑待审：原文此处含强迫性质的成人描写，已整体删除。现仅保留其作为重大冲突与创伤后果的剧情节点。建议重点复核相关人物动机、同意边界与后续因果。】",
    },
    {
        "start": 9539,
        "end": 9546,
        "summary": "【已删改：原文此处含成人描写。现保留为剧情结果：两人在情绪拉扯中再次发生亲密接触。请复核前后衔接。】",
    },
    {
        "start": 11497,
        "end": 11502,
        "summary": "【已删改：原文此处含成人描写。现保留为剧情结果：文中回溯了两人过去频繁而私密的亲密关系，具体细节已删除。请复核前后衔接。】",
    },
]


def paragraph_text(paragraph: ET.Element) -> str:
    return "".join(node.text or "" for node in paragraph.findall(".//w:t", NS)).strip()


def replace_text_nodes(root: ET.Element, old: str, new: str) -> int:
    count = 0
    for node in root.findall(".//w:t", NS):
        if node.text and old in node.text:
            node.text = node.text.replace(old, new)
            count += 1
    return count


def write_report() -> None:
    lines = [
        f"文件：{DEST}",
        "",
        "处理原则：",
        "1. 删除明显18X成人描写，不保留露骨细节。",
        "2. 用简短过渡说明保留剧情结果，避免情节断裂。",
        "3. 对强迫性质片段加入“存疑待审”标记，便于后续重点审核。",
        "4. 将文中出现的“419”统一替换为“越界”。",
        "",
        "已替换片段：",
    ]
    for item in REPLACEMENTS:
        lines.append(f"- 段落 {item['start']}-{item['end']}：{item['summary']}")
    lines.append("")
    lines.append(f"统计：共替换 {len(REPLACEMENTS)} 处连续片段。")
    REPORT.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    with zipfile.ZipFile(SOURCE, "r") as zin:
        document_xml = zin.read("word/document.xml")
        root = ET.fromstring(document_xml)
        body = root.find("w:body", NS)
        if body is None:
            raise RuntimeError("word/document.xml 缺少正文节点。")

        all_paragraphs = list(body.findall(".//w:p", NS))
        parent_map = {child: parent for parent in root.iter() for child in list(parent)}

        nonempty_map: dict[int, ET.Element] = {}
        nonempty_index = 0
        for paragraph in all_paragraphs:
            if paragraph_text(paragraph):
                nonempty_index += 1
                nonempty_map[nonempty_index] = paragraph

        for item in REPLACEMENTS:
            start_paragraph = nonempty_map[item["start"]]
            ppr = start_paragraph.find("w:pPr", NS)
            children_to_keep = [copy.deepcopy(ppr)] if ppr is not None else []
            start_paragraph.clear()
            for child in children_to_keep:
                start_paragraph.append(child)
            run = ET.SubElement(start_paragraph, f"{W}r")
            text_node = ET.SubElement(run, f"{W}t")
            text_node.set(f"{{{XML_NS}}}space", "preserve")
            text_node.text = item["summary"]

            for idx in range(item["start"] + 1, item["end"] + 1):
                paragraph = nonempty_map[idx]
                parent = parent_map.get(paragraph)
                if parent is not None:
                    parent.remove(paragraph)

        replace_text_nodes(root, "419", "越界")
        new_document_xml = ET.tostring(root, encoding="utf-8", xml_declaration=True)

        with zipfile.ZipFile(DEST, "w", compression=zipfile.ZIP_DEFLATED) as zout:
            for info in zin.infolist():
                data = new_document_xml if info.filename == "word/document.xml" else zin.read(info.filename)
                zout.writestr(info, data)

    write_report()


if __name__ == "__main__":
    main()
