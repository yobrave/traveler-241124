"""One sentence on the internet for a traveler from 1800 (200 chars max)."""
import json
import os

CONFIG = {"name": "entry.txt", "folder": os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"}
SENTENCE = ("It is a library that copies whatever any reader scribbles onto "
            "every doorstep on Earth the same instant "
            "— and every doorstep scribbles back.")


def save(spec, text):
    os.makedirs(spec["folder"], exist_ok=True)
    path = os.path.join(spec["folder"], spec["name"])
    stream = open(path, "w", encoding="utf-8", newline="\n")
    stream.write(text + "\n")
    stream.close()
    return path


saved = save(CONFIG, SENTENCE.strip())
print(json.dumps({"saved": saved, "size": len(SENTENCE.strip())}))
