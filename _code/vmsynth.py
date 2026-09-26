"""Small, dependency-light helpers for the illustrative figures in
*Acoustic Measures of Voice Quality*.

Every signal produced here is SYNTHETIC. The generators exist to show
what a concept looks like (sampling, windowing, signal types), not to
model any particular voice or disorder. Licence: MIT (see LICENSE-CODE).

The source-filter recipe is deliberately simple:
    Rosenberg-type glottal pulses, one per cycle, with per-cycle period
    and amplitude  ->  first difference (lip radiation)  ->  cascade of
    second-order formant resonators  ->  optional additive aspiration noise.
"""

from __future__ import annotations

import numpy as np
from scipy.signal import lfilter

# Book palette (matches theme.scss). Ink for signals, one accent per role.
INK = "#23282c"
MUTED = "#8a8f94"
GRID = "#e3e5e7"
BLUE = "#1a6fb0"
ORANGE = "#c2571a"
GREEN = "#3a8a5c"

# Formant frequencies and bandwidths (Hz) for a generic adult /a/-like vowel.
VOWEL_A = ((700, 80), (1220, 90), (2600, 120), (3500, 150))


def style_axes(ax, grid: bool = True) -> None:
    """Recessive axes: no top/right spines, light grid, muted ticks."""
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(MUTED)
    ax.tick_params(colors=INK, labelsize=8.5, length=3)
    ax.xaxis.label.set_color(INK)
    ax.yaxis.label.set_color(INK)
    if grid:
        ax.grid(True, color=GRID, linewidth=0.6)
        ax.set_axisbelow(True)


def rosenberg_pulse(n: int, open_frac: float = 0.6, close_frac: float = 0.25) -> np.ndarray:
    """One glottal-flow cycle of length n samples (Rosenberg-type shape)."""
    n = max(int(n), 4)
    n_open = max(int(round(open_frac * n)), 1)
    n_close = max(int(round(close_frac * n)), 1)
    g = np.zeros(n)
    t1 = np.arange(n_open)
    g[:n_open] = 0.5 * (1 - np.cos(np.pi * t1 / n_open))
    t2 = np.arange(min(n_close, n - n_open))
    g[n_open:n_open + len(t2)] = np.cos(0.5 * np.pi * t2 / n_close)
    return g


def pulse_train(periods_s, amps, fs: float) -> np.ndarray:
    """Concatenate one pulse per cycle with the given periods (s) and amplitudes."""
    cycles = [a * rosenberg_pulse(round(T * fs)) for T, a in zip(periods_s, amps)]
    return np.concatenate(cycles)


def formant_filter(x: np.ndarray, fs: float, formants=VOWEL_A) -> np.ndarray:
    """Cascade of two-pole resonators, each normalised to unit gain at DC."""
    y = x
    for f, bw in formants:
        r = np.exp(-np.pi * bw / fs)
        theta = 2 * np.pi * f / fs
        a = [1.0, -2 * r * np.cos(theta), r * r]
        y = lfilter([sum(a)], a, y)
    return y


def synth_vowel(periods_s, amps, fs: float = 16000, noise_rel_db: float | None = None,
                seed: int = 0, warmup: int = 4) -> np.ndarray:
    """Synthetic vowel from per-cycle periods and amplitudes.

    noise_rel_db: level of added aspiration noise relative to the RMS of the
    voiced component (e.g. -30 for a little noise, +6 for noise-dominated).
    The noise is shaped by the same formant filter. Output is peak-normalised.
    warmup: number of extra cycles (copies of the first one) synthesised before
    the signal and then discarded, so the filters start in steady state.
    """
    rng = np.random.default_rng(seed)
    periods_s = np.concatenate([np.full(warmup, periods_s[0]), periods_s])
    amps = np.concatenate([np.full(warmup, amps[0]), amps])
    n_skip = int(sum(round(T * fs) for T in periods_s[:warmup]))
    src = np.diff(pulse_train(periods_s, amps, fs), prepend=0.0)  # radiation
    voiced = formant_filter(src, fs)
    y = voiced
    if noise_rel_db is not None:
        noise = formant_filter(np.diff(rng.standard_normal(len(src)), prepend=0.0), fs)
        noise *= np.sqrt(np.mean(voiced ** 2) / np.mean(noise ** 2)) * 10 ** (noise_rel_db / 20)
        y = voiced + noise
    y = y[n_skip:]
    return y / np.max(np.abs(y))


def n_cycles(f0: float, dur: float) -> int:
    return int(np.ceil(dur * f0)) + 2


def type_examples(fs: float = 16000, dur: float = 0.6, f0: float = 125.0, seed: int = 1):
    """Four synthetic signals illustrating the signal types.

    Returns a dict {label: signal}. Construction:
      Type 1 - nearly periodic: 0.3 % random period jitter, 3 % amplitude variation.
      Type 2 - organised but non-stationary: period-1 for the first 40 % of the
               segment, then a bifurcation to a period-2 pattern (alternating long/
               short, strong/weak cycles), which adds a subharmonic at F0/2.
      Type 3 - no apparent periodicity but deterministic: cycle lengths and
               amplitudes driven by a chaotic logistic map (r = 3.9).
      Type 4 - noise-dominated: weak, irregular pulses buried in aspiration noise.
    """
    rng = np.random.default_rng(seed)
    T0 = 1.0 / f0
    n = n_cycles(f0, dur) + 40
    out = {}

    per = T0 * (1 + 0.003 * rng.standard_normal(n))
    amp = 1 + 0.03 * rng.standard_normal(n)
    out["Type 1"] = synth_vowel(per, amp, fs, noise_rel_db=-35, seed=seed)

    k = np.arange(n)
    split = int(0.4 * dur * f0)
    alt = np.where(k % 2 == 0, 1.0, -1.0) * (k >= split)
    per = T0 * (1 + 0.10 * alt + 0.003 * rng.standard_normal(n))
    amp = 1 + 0.35 * alt
    out["Type 2"] = synth_vowel(per, amp, fs, noise_rel_db=-35, seed=seed + 1)

    x = np.empty(n)
    x[0] = 0.37
    for i in range(1, n):
        x[i] = 3.9 * x[i - 1] * (1 - x[i - 1])
    per = T0 * (0.65 + 0.7 * x)
    amp = 0.45 + 0.9 * np.roll(x, 3)
    out["Type 3"] = synth_vowel(per, amp, fs, noise_rel_db=-25, seed=seed + 2)

    per = T0 * (1 + 0.25 * rng.standard_normal(n)).clip(0.5, 1.8)
    amp = 0.3 + 0.3 * rng.random(n)
    out["Type 4"] = synth_vowel(per, amp, fs, noise_rel_db=12, seed=seed + 3)

    m = int(dur * fs)
    return {key: sig[:m] for key, sig in out.items()}


def ac_f0_track(x: np.ndarray, fs: float, fmin: float = 60, fmax: float = 400,
                win_s: float = 0.04, hop_s: float = 0.01):
    """Naive short-time autocorrelation F0 estimate with NO voicing decision.

    Every frame returns the lag of the highest normalised autocorrelation peak
    in [1/fmax, 1/fmin]. Used only to show that an algorithm always produces a
    number, whether or not the signal has an F0.
    """
    L, H = int(win_s * fs), int(hop_s * fs)
    w = np.hanning(L)
    lo, hi = int(fs / fmax), int(fs / fmin)
    times, f0s = [], []
    for start in range(0, len(x) - L, H):
        fr = (x[start:start + L] - np.mean(x[start:start + L])) * w
        r = np.correlate(fr, fr, mode="full")[L - 1:L + hi + 1]
        r = r / (r[0] + 1e-12)  # biased estimate: mild preference for short lags
        lag = lo + int(np.argmax(r[lo:hi]))
        if 1 <= lag < hi - 1:  # parabolic refinement
            a, b, c = r[lag - 1], r[lag], r[lag + 1]
            den = a - 2 * b + c
            lag = lag + (0.5 * (a - c) / den if den != 0 else 0.0)
        times.append((start + L / 2) / fs)
        f0s.append(fs / lag)
    return np.array(times), np.array(f0s)


def plot_spectrogram(ax, x: np.ndarray, fs: float, win_s: float, fmax: float,
                     hop_s: float = 0.001, dyn_db: float = 60.0, nfft: int = 2048) -> None:
    """Gray-scale spectrogram (Hamming window) drawn with smooth interpolation."""
    from scipy.signal import spectrogram
    L = int(win_s * fs)
    H = max(1, int(hop_s * fs))
    ff, tt, S = spectrogram(x, fs, window="hamming", nperseg=L, noverlap=L - H,
                            nfft=max(nfft, L), mode="magnitude")
    keep = ff <= fmax
    SdB = 20 * np.log10(S[keep] + 1e-12)
    ax.imshow(SdB, origin="lower", aspect="auto", cmap="Greys",
              vmin=SdB.max() - dyn_db, vmax=SdB.max(), interpolation="bilinear",
              extent=[tt[0], tt[-1], 0, ff[keep][-1] / 1e3])
