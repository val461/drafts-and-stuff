#!/usr/bin/env python3
"""
https://claude.ai/chat/75f05d7c-edbd-4244-9700-9e9324c9ebca
Digits -> MIDI melody.
Option -h for help.

Random digits are statistically similar to pi's, so they will sound the same: pi is "random-sounding". √2, e and φ behave like pi, so they only give you different melodies, not a different character.
For more musical results, try the Markov or logistic-map sources, or rationals and Thue–Morse for audible repetition and structure.

Since you like the chromatic scale, you may be enjoying the dissonance and the lack of a tonal center. Octatonic and whole tone are good in-between options, as they are structured but not "simplistic".

Examples:

python3 pi_melody.py --source pi --base 12 --scale chromatic
python3 pi_melody.py --source sqrt2 --base 7 --scale harmonic_minor --walk
python3 pi_melody.py --source markov --base 8 --scale octatonic --seed 3

# Markov: small steps, so it sounds the most "melodic"
python3 pi_melody.py --source markov --scale octatonic

# Logistic map: chaotic but deterministic, in a scale with no resolution
python3 pi_melody.py --source logistic --scale whole_tone

# Thue–Morse: fractal repetition; digits also set rhythm
python3 pi_melody.py --source thue_morse --scale octatonic --rhythm digits

# 1/7: a repeating pattern in base 6, so you hear the loop
python3 pi_melody.py --source one_seventh --scale whole_tone --rhythm digits

# Markov in Messiaen mode 3, slower and impressionist
python3 pi_melody.py --source markov --scale messiaen3 --rhythm digits --tempo 90

# Pi itself, as a random walk through the octatonic scale
python3 pi_melody.py --source pi --scale octatonic --walk
"""
import argparse, math, random, struct

# ---------- digit sources ----------
def frac_digits(x_scaled, bits, n, base):
    one = 1 << bits
    frac = x_scaled & (one - 1)
    out = []
    for _ in range(n):
        frac *= base
        out.append(frac >> bits)
        frac &= one - 1
    return out

def pi_digits(n, base):
    bits = 4*n + 64
    one = 1 << bits
    def arccot(x):
        total = term = one // x
        x2, k, sign = x*x, 1, -1
        while term:
            term //= x2; k += 2
            total += sign*(term//k); sign = -sign
        return total
    return frac_digits(4*(4*arccot(5) - arccot(239)), bits, n, base)

def sqrt_digits(k, n, base):
    bits = 4*n + 64
    return frac_digits(math.isqrt(k << (2*bits)), bits, n, base)

def phi_digits(n, base):
    bits = 4*n + 64
    return frac_digits(((1 << bits) + math.isqrt(5 << (2*bits))) >> 1, bits, n, base)

def e_digits(n, base):
    bits = 4*n + 64
    total = term = 1 << bits
    k = 1
    while term:
        term //= k; total += term; k += 1
    return frac_digits(total, bits, n, base)

def random_digits(n, base, seed):
    rng = random.Random(seed)
    return [rng.randrange(base) for _ in range(n)]

def rational_digits(p, q, n, base):
    out, r = [], p % q
    for _ in range(n):
        r *= base; out.append(r // q); r %= q
    return out

def thue_morse(n, base):
    return [bin(i).count("1") % base for i in range(n)]

def logistic_map(n, base, r=3.9, x=0.4):
    out = []
    for _ in range(n):
        x = r*x*(1-x); out.append(min(base-1, int(x*base)))
    return out

def markov(n, base, seed):
    rng = random.Random(seed); d = base//2; out = []
    for _ in range(n):
        d = min(base-1, max(0, d + rng.choice([-2,-1,-1,0,1,1,2])))
        out.append(d)
    return out

SOURCES = {
    "pi": lambda a: pi_digits(a.n, a.base),
    "e": lambda a: e_digits(a.n, a.base),
    "phi": lambda a: phi_digits(a.n, a.base),
    "sqrt2": lambda a: sqrt_digits(2, a.n, a.base),
    "sqrt3": lambda a: sqrt_digits(3, a.n, a.base),
    "random": lambda a: random_digits(a.n, a.base, a.seed),
    "one_seventh": lambda a: rational_digits(1, 7, a.n, a.base),
    "thue_morse": lambda a: thue_morse(a.n, a.base),
    "logistic": lambda a: logistic_map(a.n, a.base),
    "markov": lambda a: markov(a.n, a.base, a.seed),
}

# ---------- scales (semitone offsets) ----------
SCALES = {
    "chromatic": list(range(12)), # atonal
    "major": [0,2,4,5,7,9,11],
    "natural_minor": [0,2,3,5,7,8,10],
    "harmonic_minor": [0,2,3,5,7,8,11], # classical, dramatic
    "phrygian_dominant": [0,1,4,5,7,8,10], # Spanish/Middle Eastern
    "hungarian_minor": [0,2,3,6,7,8,11], # gypsy, tense
    "double_harmonic": [0,1,4,5,7,8,11], # Byzantine
    "whole_tone": [0,2,4,6,8,10], # dreamy, no resolution
    "blues": [0,3,5,6,7,10],
    "hirajoshi": [0,2,3,7,8], # Japanese, melancholic
    "in": [0,1,5,7,8], # darker Japanese
    "minor_pentatonic": [0,3,5,7,10],
    "major_pentatonic": [0,2,4,7,9],
    "octatonic": [0,2,3,5,6,8,9,11], # jazzy, symmetrical
    "messiaen3": [0,2,3,4,6,7,8,10,11], # impressionist
}

def build_scale(offsets, base, root):
    # extend over octaves if the base is larger than the scale
    return [root + 12*(i // len(offsets)) + offsets[i % len(offsets)] for i in range(base)]

# ---------- MIDI ----------
def vlq(v):
    o = [v & 0x7F]; v >>= 7
    while v: o.append((v & 0x7F) | 0x80); v >>= 7
    return bytes(reversed(o))

def write_midi(path, notes, durs, tempo_bpm, tpq=480):
    ev = b""
    for n, d in zip(notes, durs):
        ev += b"\x00" + bytes([0x90, n, 90]) + vlq(d) + bytes([0x80, n, 0])
    ev += b"\x00\xff\x2f\x00"
    track = (b"\x00\xff\x51\x03" + (60_000_000 // tempo_bpm).to_bytes(3, "big")
             + b"\x00\xc0\x00" + ev)
    with open(path, "wb") as f:
        f.write(b"MThd" + struct.pack(">IHHH", 6, 0, 1, tpq)
                + b"MTrk" + struct.pack(">I", len(track)) + track)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--source", choices=SOURCES, default="pi")
    p.add_argument("--base", type=int, default=None,
                   help="number base (default: number of notes in the scale)")
    p.add_argument("-n", "--n", type=int, default=128, help="number of notes")
    p.add_argument("--scale", choices=SCALES, default="natural_minor")
    p.add_argument("--root", type=int, default=57, help="MIDI root note (57 = A3)")
    p.add_argument("--walk", action="store_true",
                   help="digits are steps in a random walk instead of pitches")
    p.add_argument("--rhythm", choices=["parity", "digits"], default="parity",
                   help="parity: even=quarter, odd=eighth; digits: next digit sets duration")
    p.add_argument("--tempo", type=int, default=120)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("-o", "--out")
    a = p.parse_args()
    if a.base is None:
        a.base = len(SCALES[a.scale])

    digits = SOURCES[a.source](argparse.Namespace(**{**vars(a), "n": a.n * 2}))
    pitch_digits, rhythm_digits = digits[:a.n], digits[a.n:a.n*2]
    print(f"{a.source} in base {a.base}: {''.join(map(str, digits[:a.n]))}")

    tpq = 480
    scale = build_scale(SCALES[a.scale], a.base, a.root)
    notes, pos = [], len(scale)//2
    for d in pitch_digits:
        if a.walk:
            pos = max(0, min(len(scale)-1, pos + d - a.base//2))
            notes.append(scale[pos])
        else:
            notes.append(scale[d])
    if a.rhythm == "parity":
        durs = [tpq if d % 2 == 0 else tpq//2 for d in pitch_digits]
    else:
        choices = [tpq//2, tpq, tpq*2]
        durs = [choices[d % 3] for d in rhythm_digits]

    out = a.out or f"{a.source}_b{a.base}_{a.scale}{'_walk' if a.walk else ''}.mid"
    write_midi(out, notes, durs, a.tempo)
    print("wrote", out)

if __name__ == "__main__":
    main()
