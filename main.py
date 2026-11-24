import os

LINE = "My agent reviewed my code, found 63 issues, and assigned them all to me — I'm now the junior developer on my own project."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "./output")
    os.makedirs(out_dir, exist_ok=True)
    os.chmod(out_dir, 0o755)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8", newline="") as f:
        assert f.read() == LINE
    assert 1 <= len(LINE) <= 199

if __name__ == "__main__":
    main()
