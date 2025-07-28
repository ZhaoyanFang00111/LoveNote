from pathlib import Path

# Who am I?
MY_NAME = "F"  # or "bob"

# Key paths 
KEYS_DIR = Path("keys")
PUBLIC_KEYS = {
    "F": KEYS_DIR / "Fpublic.pem",
    "L": KEYS_DIR / "Lpublic.pem",
}
PRIVATE_KEY = KEYS_DIR / "Fprivate.pem"
PRIVATE_KEY1 = KEYS_DIR/ "Lprivate.pem"

# Messages directory
MESSAGES_DIR = Path("messages")
