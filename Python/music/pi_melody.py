import struct, sys

BASE = int(sys.argv[1]) if len(sys.argv) > 1 else 7
N = int(sys.argv[2]) if len(sys.argv) > 2 else 128

def pi_digits(n, base):
    bits = 4*n + 64
    one = 1 << bits
    def arccot(x):
        total = term = one // x
        x2 = x*x; k = 1; sign = -1
        while term:
            term //= x2; k += 2
            total += sign*(term//k); sign = -sign
        return total
    pi = 4*(4*arccot(5) - arccot(239))
    frac = pi - 3*one
    out = []
    for _ in range(n):
        frac *= base
        out.append(frac >> bits)
        frac &= one - 1
    return out

digits = pi_digits(N, BASE)
print(f"pi = 3.{''.join(map(str, digits))} (base {BASE})")

# Scale expressed in half-tones
# A natural minor / C major diatonic scale; for base 7 each digit = one scale degree
scale = [57, 59, 60, 62, 64, 65, 67, 69, 71, 72][:BASE] if BASE <= 7 else None
if BASE == 7:
    scale = [57, 59, 60, 62, 64, 65, 67]   # A minor: A B C D E F G
    # scale = [60, 62, 64, 65, 67, 69, 71]  # C major: C D E F G A B
elif BASE == 5:
    scale = [57, 60, 62, 64, 67]  # A minor pentatonic: A C D E G
    # scale = [60, 62, 64, 67, 69]  # C major pentatonic: C D E G A
elif BASE == 8:
    scale = [60, 62, 64, 65, 67, 69, 71, 72]  # C major: C D E F G A B C

tpq = 480
ev = b""
for d in digits:
    # dur = tpq if d % 2 == 0 else tpq // 2
    dur = tpq
    n = scale[d]
    v = dur; o = [v & 0x7F]; v >>= 7
    while v: o.append((v & 0x7F) | 0x80); v >>= 7
    ev += b"\x00" + bytes([0x90, n, 90]) + bytes(reversed(o)) + bytes([0x80, n, 0])
ev += b"\x00\xff\x2f\x00"
track = b"\x00\xff\x51\x03" + (500000).to_bytes(3, "big") + b"\x00\xc0\x00" + ev
midi = b"MThd" + struct.pack(">IHHH", 6, 0, 1, tpq) + b"MTrk" + struct.pack(">I", len(track)) + track
open(f"pi_base{BASE}_melody.mid", "wb").write(midi)
