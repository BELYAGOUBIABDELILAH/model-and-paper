import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent

BASE_REPO_URL = "https://github.com/BELYAGOUBIABDELILAH/model-and-paper"
PAPERS_URL = f"{BASE_REPO_URL}/blob/main/papers/README.md"
MODELS_URL = f"{BASE_REPO_URL}/blob/main/models/README.md"
LICENSE_URL = f"{BASE_REPO_URL}/blob/main/LICENSE"
NEWSLETTER_URL = "https://axiomrepo.substack.com/"

def parse_markdown_brief(filepath: pathlib.Path, rel_prefix: str) -> str:
    content = filepath.read_text(encoding="utf-8")
    
    title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    link_match = re.search(r"\*\*Link:\*\*\s+\[.*?\]\((https?://[^\s)]+)\)", content)
    
    desc_match = re.search(
        r"\*\*Description:\*\*\s*(.+?)(?=\n\s*\*\*Curated by:\*\*|\Z)",
        content,
        flags=re.DOTALL
    )

    title = title_match.group(1).strip() if title_match else filepath.stem
    link = link_match.group(1).strip() if link_match else "#"
    
    if desc_match:
        desc_raw = desc_match.group(1).strip()
        desc = " ".join(desc_raw.split())
    else:
        desc = ""

    rel_path = f"{rel_prefix}/{filepath.name}"
    return f"* **[{title}]({rel_path})** ([Source]({link}))  \n  {desc}"

def get_directory_files(folder_name: str) -> list[pathlib.Path]:
    folder = ROOT / folder_name
    if not folder.exists():
        return []
    return sorted(
        [f for f in folder.glob("*.md") if f.name.lower() != "readme.md"],
        key=lambda f: f.name,
        reverse=True
    )

def format_entries(files: list[pathlib.Path], rel_prefix: str, limit: int = None) -> str:
    target_files = files[:limit] if limit else files
    return "\n\n".join(parse_markdown_brief(f, rel_prefix) for f in target_files)

def replace_marker_block(source: str, marker_tag: str, replacement_body: str) -> str:
    pattern = rf"(<!-- {marker_tag}:START -->).*?(<!-- {marker_tag}:END -->)"
    return re.sub(pattern, rf"\1\n{replacement_body}\n\2", source, flags=re.DOTALL)

def build_counters_block(paper_count: int, model_count: int) -> str:
    return (
        f'<p align="center">\n'
        f'  <a href="{PAPERS_URL}"><img src="https://img.shields.io/badge/Papers-{paper_count}%20Indexed-2563eb?style=flat-square" alt="Papers Count"></a>\n'
        f'  <a href="{MODELS_URL}"><img src="https://img.shields.io/badge/Models-{model_count}%20Indexed-16a34a?style=flat-square" alt="Models Count"></a>\n'
        f'  <a href="{NEWSLETTER_URL}"><img src="https://img.shields.io/badge/Newsletter-Axiom%20Repo-ff6719?style=flat-square&logo=substack" alt="Axiom Repo Newsletter"></a>\n'
        f'  <a href="{LICENSE_URL}"><img src="https://img.shields.io/badge/License-MIT-gray?style=flat-square" alt="License"></a>\n'
        f'</p>'
    )

def main():
    paper_files = get_directory_files("papers")
    model_files = get_directory_files("models")
    
    paper_count = len(paper_files)
    model_count = len(model_files)

    # 1. Update main repository README
    root_readme_path = ROOT / "README.md"
    if root_readme_path.exists():
        root_readme = root_readme_path.read_text(encoding="utf-8")
        
        # Update badge counters
        root_readme = replace_marker_block(root_readme, "COUNTERS", build_counters_block(paper_count, model_count))
        
        # Update dynamic count text if present
        root_readme = re.sub(
            r"<!-- PAPERS_COUNT -->\d+<!-- /PAPERS_COUNT -->",
            f"<!-- PAPERS_COUNT -->{paper_count}<!-- /PAPERS_COUNT -->",
            root_readme
        )
        root_readme = re.sub(
            r"<!-- MODELS_COUNT -->\d+<!-- /MODELS_COUNT -->",
            f"<!-- MODELS_COUNT -->{model_count}<!-- /MODELS_COUNT -->",
            root_readme
        )

        # Update top 5 entries
        root_readme = replace_marker_block(root_readme, "PAPERS", format_entries(paper_files, "./papers", limit=5))
        root_readme = replace_marker_block(root_readme, "MODELS", format_entries(model_files, "./models", limit=5))
        
        root_readme_path.write_text(root_readme, encoding="utf-8")

    # 2. Update Papers Archive README
    papers_readme_path = ROOT / "papers" / "README.md"
    papers_entries = format_entries(paper_files, ".")
    papers_content = (
        f"# Research Papers Archive\n\n"
        f"Total indexed: **{paper_count}** papers.\n\n"
        f"[← Back to Model & Paper]({BASE_REPO_URL})\n\n"
        f"---\n\n"
        f"{papers_entries}\n\n"
        f"---\n\n"
        f"Curated by [Belyagoubi Mohammed Abdelilah](https://github.com/BELYAGOUBIABDELILAH) · "
        f"[Contact](mailto:belyagoubiabdillah@gmail.com) · "
        f"[Newsletter]({NEWSLETTER_URL})\n"
    )
    papers_readme_path.write_text(papers_content, encoding="utf-8")

    # 3. Update Models Archive README
    models_readme_path = ROOT / "models" / "README.md"
    models_entries = format_entries(model_files, ".")
    models_content = (
        f"# Open-Source Models Archive\n\n"
        f"Total indexed: **{model_count}** models.\n\n"
        f"[← Back to Model & Paper]({BASE_REPO_URL})\n\n"
        f"---\n\n"
        f"{models_entries}\n\n"
        f"---\n\n"
        f"Curated by [Belyagoubi Mohammed Abdelilah](https://github.com/BELYAGOUBIABDELILAH) · "
        f"[Contact](mailto:belyagoubiabdillah@gmail.com) · "
        f"[Newsletter]({NEWSLETTER_URL})\n"
    )
    models_readme_path.write_text(models_content, encoding="utf-8")

if __name__ == "__main__":
    main()
