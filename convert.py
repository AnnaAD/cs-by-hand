import os
from pathlib import Path
import cairosvg

def convert_svgs_to_pdfs(root_dir="outputs"):
    root = Path(root_dir)

    if not root.exists():
        print(f"Directory not found: {root}")
        return

    count = 0

    # Walk through lec* subfolders
    for lec_dir in root.glob("lec*"):
        if lec_dir.is_dir():
            for svg_file in lec_dir.glob("*.svg"):
                pdf_file = svg_file.with_suffix(".pdf")

                try:
                    cairosvg.svg2pdf(
                        url=str(svg_file),
                        write_to=str(pdf_file)
                    )
                    print(f"Converted: {svg_file} -> {pdf_file}")
                    count += 1
                except Exception as e:
                    print(f"Failed: {svg_file} ({e})")

    print(f"\nDone. Converted {count} files.")


if __name__ == "__main__":
    convert_svgs_to_pdfs("outputs")