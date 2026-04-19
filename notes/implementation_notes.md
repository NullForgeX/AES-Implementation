# Implementation Notes

For this project, I chose to represent the AES state as a 4x4 matrix of bytes. I used that structure because it matches the way AES is usually explained in class and in most reference material, so it made the round operations easier to follow.

I split the implementation into separate files so the code would be easier to manage and test. The main AES transformations are grouped in one file, the key expansion logic is separate, and the full encryption/decryption process is handled in the core file. This made it easier to debug individual parts instead of trying to fix everything in one large script.

One part that took extra attention was `MixColumns`, since it uses arithmetic in `GF(2^8)` instead of normal multiplication. To handle that, I wrote a helper function for Galois field multiplication and used it inside both the forward and inverse column-mixing steps.

Another important part was key expansion. Since AES-128 uses round keys throughout the algorithm, I separated the key schedule logic so I could test it independently from the rest of the encryption flow.

To check correctness, I used a standard AES-128 test vector and also tested that decrypting an encrypted block returns the original plaintext. That helped confirm that both directions of the algorithm were working correctly.

Overall, the goal of this implementation was not to build a full cryptography library, but to understand the internal steps of AES and implement them clearly in Python.