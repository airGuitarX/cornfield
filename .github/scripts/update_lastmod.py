#!/usr/bin/env python3
"""
Update last_modified in front matter of content/post/*/index.md from the file's
last git commit date. Run from repo root.
"""
import re
import subprocess
import sys
from pathlib import Path


def get_last_commit_iso(path: Path) -> str | None:
    """Return last commit date in ISO 8601 format for path, or None."""
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cI", "--", str(path)],
            capture_output=True,
            text=True,
            check=True,
        )
        return out.stdout.strip() or None
    except subprocess.CalledProcessError:
        return None


def update_front_matter_lastmod(content: str, new_lastmod: str) -> str:
    """Add or replace last_modified in YAML front matter (first --- ... --- block)."""
    # Match first front matter block
    pattern = re.compile(
        r"^(---\r?\n)(.*?)(\r?\n---\r?\n)",
        re.DOTALL,
    )
    match = pattern.match(content)
    if not match:
        return content

    preamble, fm, end_delim = match.groups()
    new_fm: str
    field = "last_modified"

    if re.search(rf"^{re.escape(field)}\s*:", fm, re.MULTILINE):
        # Replace existing last_modified value (allow various formats)
        new_fm = re.sub(
            rf"^{re.escape(field)}\s*:.*$",
            f'{field}: "{new_lastmod}"',
            fm,
            count=1,
            flags=re.MULTILINE,
        )
    else:
        # Insert last_modified after first `date:` line for consistency
        if re.search(r"^date\s*:", fm, re.MULTILINE):
            new_fm = re.sub(
                r"^(date\s*:.*)$",
                rf'\1\n{field}: "{new_lastmod}"',
                fm,
                count=1,
                flags=re.MULTILINE,
            )
        else:
            # No date line; append at end of front matter
            new_fm = fm.rstrip() + f'\n{field}: "{new_lastmod}"\n'

    return preamble + new_fm + end_delim + content[match.end() :]


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent.parent
    posts_dir = repo_root / "content" / "post"
    if not posts_dir.is_dir():
        print("No content/post directory", file=sys.stderr)
        return 0

    updated = 0
    for path in sorted(posts_dir.glob("*/index.md")):
        iso = get_last_commit_iso(path)
        if not iso:
            continue
        text = path.read_text(encoding="utf-8")
        new_text = update_front_matter_lastmod(text, iso)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            updated += 1
            print(path.relative_to(repo_root))

    print(f"Updated last_modified in {updated} post(s).", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
