# 🔐 AES Encryption / Decryption Project

A simple, clean, and educational implementation of **AES-128-CBC** encryption and decryption using Python.

This project contains two scripts:

* `encrypt.py` → Enter plaintext, and the script outputs:

  * Ciphertext (Base64)
  * Key (Base64)
  * IV (Base64)

* `decrypt.py` → Enter:

  * Ciphertext (Base64)
  * Key (Base64)
  * IV (Base64)

  And the script returns the **original plaintext**.

Both files use the **PyCryptodome** library.

---

## 📁 Project Structure

```
project/
│── encrypt.py
│── decrypt.py
│── README.md
```

---

## ⚙️ Requirements

Install PyCryptodome:

```bash
pip install pycryptodome
```

---

# 📌 How Encryption Works (encrypt.py)

When you run the encryption file:

```bash
python encrypt.py
```

You enter a normal text (plaintext), and the script will:

1. Generate a **random AES key** (16 bytes)
2. Generate a **random IV** (16 bytes)
3. Encrypt the text using **AES-128-CBC**
4. Output all values in **Base64** format, ready to copy/paste

### 🔄 Example Output:

```
Ciphertext (Base64): wKg3unQm9yH2BBQ9QVjNyg==
Key        (Base64): jHd92shTZNVrLWNFeX0eYw==
IV         (Base64): L0W0xU1P7AevB66xk9H5ng==
```

---

# 🔓 How Decryption Works (decrypt.py)

Run the decryption script:

```bash
python decrypt.py
```

You will be asked to input:

* Ciphertext (Base64)
* Key (Base64)
* IV (Base64)

The script will:

1. Decode the Base64 values into bytes
2. Use AES-128-CBC to decrypt
3. Remove padding
4. Return the original message

### ✔ Example:

Input:

```
Ciphertext: wKg3unQm9yH2BBQ9QVjNyg==
Key: jHd92shTZNVrLWNFeX0eYw==
IV: L0W0xU1P7AevB66xk9H5ng==
```

Output:

```
Original Text: Hello AES!
```

---

## 🧠 Why Base64?

AES produces **raw bytes**, not readable text.
Base64 allows us to:

* Represent bytes as readable text
* Copy/paste safely
* Store values in files, JSON, or databases

Important: **Base64 is not encryption** — it is only encoding.

---

## 🔐 Why IV?

The IV (Initialization Vector) adds randomness.
It ensures:

* Same plaintext encrypted twice → different ciphertext
* No patterns
* Stronger security

IV does **not need to be secret**, but it must:

* Be random
* Never repeat with the same key

---

## 📘 Notes

* This project is simplified for educational/university use.
* AES-128-CBC is easy to understand and implement.
* For real-world security, AES-GCM is recommended.

---

## ✨ Future Improvements

* Add GUI version (Tkinter)
* Add file encryption/decryption
* Convert scripts into .exe files using PyInstaller
* Add support for AES-256


