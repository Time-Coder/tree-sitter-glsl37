import subprocess
import sys

subprocess.call([sys.executable, "-m", "twine", "upload", "dist/tree-sitter-glsl37-*.tar.gz", "dist/tree_sitter_glsl37-*.whl", "--verbose"])