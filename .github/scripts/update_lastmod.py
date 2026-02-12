#!/usr/bin/env python3
"""
Update last_modified in front matter of content/post/*/index.md from the file's
last git commit date. Run from repo root.
"""
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable


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


def extract_front_matter(content: str) -> tuple[str, str, str, int] | None:
    """Return (preamble, front_matter, end_delim, end_index) for the first front matter block."""
    pattern = re.compile(
        r"^(---\r?\n)(.*?)(\r?\n---\r?\n)",
        re.DOTALL,
    )
    match = pattern.match(content)
    if not match:
        return None
    preamble, fm, end_delim = match.groups()
    return preamble, fm, end_delim, match.end()


def find_existing_last_modified(fm: str) -> str | None:
    match = re.search(r"^last_modified\s*:\s*(.+)\s*$", fm, re.MULTILINE)
    if not match:
        return None
    raw = match.group(1).strip()
    if raw.startswith('"') and raw.endswith('"') and len(raw) >= 2:
        return raw[1:-1]
    if raw.startswith("'") and raw.endswith("'") and len(raw) >= 2:
        return raw[1:-1]
    return raw


def update_front_matter_lastmod(content: str, new_lastmod: str) -> str:
    """Add or replace last_modified in YAML front matter (first --- ... --- block)."""
    # Match first front matter block
    parts = extract_front_matter(content)
    if not parts:
        return content
    preamble, fm, end_delim, end_index = parts
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

    return preamble + new_fm + end_delim + content[end_index:]


def parse_rfc3339(value: str) -> "datetime | None":
    from datetime import datetime

    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def to_pst_iso(value: str) -> str | None:
    from zoneinfo import ZoneInfo

    dt = parse_rfc3339(value)
    if not dt:
        return None
    la = ZoneInfo("America/Los_Angeles")
    return dt.astimezone(la).replace(microsecond=0).isoformat()


def is_la_offset(value: str) -> bool:
    from zoneinfo import ZoneInfo

    dt = parse_rfc3339(value)
    if not dt:
        return False
    la = ZoneInfo("America/Los_Angeles")
    return dt.utcoffset() == dt.astimezone(la).utcoffset()


def should_update(existing: str | None, new_value: str) -> bool:
    if not existing:
        return True
    if not is_la_offset(existing):
        return True
    existing_dt = parse_rfc3339(existing)
    new_dt = parse_rfc3339(new_value)
    if not existing_dt or not new_dt:
        return existing != new_value
    return existing_dt != new_dt


def iter_target_paths(repo_root: Path, posts_dir: Path, paths: Iterable[str]) -> Iterable[Path]:
    if not paths:
        yield from sorted(posts_dir.glob("*/index.md"))
        return
    for p in paths:
        if not p:
            continue
        candidate = Path(p)
        if not candidate.is_absolute():
            candidate = (repo_root / candidate).resolve()
        yield candidate


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent.parent
    posts_dir = repo_root / "content" / "post"
    if not posts_dir.is_dir():
        print("No content/post directory", file=sys.stderr)
        return 0

    updated = 0
    paths = [p for p in sys.argv[1:] if p.strip()]
    for path in iter_target_paths(repo_root, posts_dir, paths):
        if not path.is_file():
            continue
        iso = get_last_commit_iso(path)
        if not iso:
            continue
        pst_iso = to_pst_iso(iso) or iso
        text = path.read_text(encoding="utf-8")
        parts = extract_front_matter(text)
        existing = None
        if parts:
            _, fm, _, _ = parts
            existing = find_existing_last_modified(fm)
        if not should_update(existing, pst_iso):
            continue
        new_text = update_front_matter_lastmod(text, pst_iso)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            updated += 1
            print(path.relative_to(repo_root))

    print(f"Updated last_modified in {updated} post(s).", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
