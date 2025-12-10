import re
from collections import Counter
# Регулярний вираз для пошуку слів українськими літерами
WORD_RE = re.compile(r"[а-яіїєґ]+", re.IGNORECASE)
def pair_counter_generator(path):
    with open(path, "r", encoding="utf-8") as f:
        for lineno, raw in enumerate(f, start=1):
            line = raw.strip().lower()
            # витягаємо лише слова — пари між словами не будуть створені
            words = WORD_RE.findall(line)
            counter = Counter()
            # рахуємо пари *всередині* кожного слова
            for word in words:
                for i in range(len(word) - 1):
                    pair = word[i:i+2]
                    counter[pair] += 1
            # беремо топ-3
            top3 = counter.most_common(3)
            # оформлюємо текстовий рядок
            if top3:
                top3_text = ", ".join(f"{p} – {c}" for p, c in top3)
            else:
                top3_text = "(немає пар)"

            yield f"Рядок {lineno}: {top3_text}"

if __name__ == "__main__":
    FILE_PATH = "text.txt"
    for line in pair_counter_generator(FILE_PATH):
        print(line)