from pathlib import Path

# Who am I?
MY_NAME = "alice"  # or "bob"

# Key paths
KEYS_DIR = Path("keys")
PUBLIC_KEYS = {
    "F": KEYS_DIR / "Fpublic.pem",
    "L": KEYS_DIR / "Lpublic.pem",
}
PRIVATE_KEY = KEYS_DIR / "Fprivate.pem"

# Messages directory
MESSAGES_DIR = Path("messages")
