import json, uuid, random
from datetime import datetime
from config import *
from encryptor import hybrid_encrypt, hybrid_decrypt

def add_note(sender, recipient, message):
    filename = f"{uuid.uuid4().hex}.json"
    encrypted = hybrid_encrypt(message, PUBLIC_KEYS['F'], PUBLIC_KEYS['L'])
    note = {
        "sender": sender,
        "recipient": recipient,
        "timestamp": datetime.utcnow().isoformat(),
        "ciphertext": encrypted
    }
    with open(MESSAGES_DIR / filename, 'w') as f:
        json.dump(note, f, indent=2)
    print(f"Added note: {filename}")

def draw_random_note():
    all_notes = list(MESSAGES_DIR.glob("*.json"))
    if not all_notes:
        print("No notes left!")
        return
    chosen = random.choice(all_notes)
    with open(chosen) as f:
        note = json.load(f)
    try:
        text = hybrid_decrypt(
            note["ciphertext"],
            PRIVATE_KEYS['F'],
            PRIVATE_KEYS['L']
        )
        print(f"🎉 Message from {note['sender']} at {note['timestamp']}:\n{text}")
        chosen.unlink()  # Delete after reading
    except Exception as e:
        print(f"⚠️ Failed to decrypt: {e}")
