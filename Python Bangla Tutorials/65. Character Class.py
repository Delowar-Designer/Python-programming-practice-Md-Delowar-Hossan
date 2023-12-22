# Character Class
import re
pattern = r"[A-Z][a-z][0-9]"

if re.match(pattern, "Agoouo222jvn"):
    print("No characters")