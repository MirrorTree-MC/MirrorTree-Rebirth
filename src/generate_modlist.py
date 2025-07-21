import json
from collections import defaultdict
from pathlib import Path


def load_modlist(json_path):
    with open(json_path, encoding="utf-8") as f:
        return json.load(f)


def build_table(mods):
    lines = ["| Mod | 相关链接 |", "| --- | --- |"]
    for mod in mods:
        link_str = " / ".join(
            f"[{link['type']}]({link['url']})" for link in mod["links"]
        )
        lines.append(f"| {mod['mod']} | {link_str} |")
    return "\n".join(lines)


def main():
    json_path = Path(__file__).parent / "modlist.json"
    modlist = load_modlist(str(json_path))
    sections = defaultdict(list)
    link_ref = dict()
    for item in modlist:
        sections[item["section"]].append(item)
        for link in item["links"]:
            ref_name = f"{item['id']}_{link['type']}"
            link_ref[ref_name] = link["url"]

    lines = []
    for section, mods in sections.items():
        lines.append(f"### **{section}**\n")
        table_lines = ["| Mod | 相关链接 |", "| --- | --- |"]
        for mod in mods:
            link_str = " / ".join(
                f"[{link['type']}][{mod['id']}_{link['type']}]" for link in mod["links"]
            )
            table_lines.append(f"| {mod['mod']} | {link_str} |")
        lines.extend(table_lines)
        lines.append("")

    # 链接统一管理
    lines.append("<!-- 链接统一管理 -->")
    for ref, url in link_ref.items():
        lines.append(f"[{ref}]: {url}")
    lines.append("")

    out_path = Path(__file__).parent / "modlist_output.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Mod list generated at {out_path}")


if __name__ == "__main__":
    main()
